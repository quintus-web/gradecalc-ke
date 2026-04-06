const gradesMap = {
  "A": 12, "A-": 11, "B+": 10, "B": 9, "B-": 8,
  "C+": 7, "C": 6, "C-": 5, "D+": 4, "D": 3, "D-": 2, "E": 1
};

const subjectGroups = [
  {
    group: "Group I — Languages & Maths",
    subjects: ["English", "Kiswahili", "Mathematics"]
  },
  {
    group: "Group II — Sciences",
    subjects: ["Biology", "Physics", "Chemistry"]
  },
  {
    group: "Group III — Humanities",
    subjects: ["History", "Geography", "CRE", "IRE", "HRE"]
  },
  {
    group: "Group IV — Technical & Applied",
    subjects: ["Agriculture", "Computer Studies", "Home Science", "Art & Design", "Building Construction", "Power Mechanics", "Woodwork", "Metalwork", "Drawing & Design", "Aviation Technology", "Electricity"]
  },
  {
    group: "Group V — Languages & Business",
    subjects: ["Business Studies", "French", "German", "Arabic", "Music", "Kenyan Sign Language"]
  }
];

const subjects = subjectGroups.flatMap(g => g.subjects);

const categoryMap = {
  "Medicine": ["Medicine", "Surgery", "Pharmacy", "Dental", "Nursing", "Clinical", "Radiography", "Physiotherapy", "Optometry", "Medical", "Health Records", "Oral Health", "Dental Technology", "Public Health", "Nutrition", "Occupational Therapy", "Veterinary", "Midwifery"],
  "Engineering": ["Engineering", "Architecture", "Quantity Surveying", "Construction", "Geospatial", "Marine", "Petroleum", "Landscape", "Surveying", "Urban", "Land Economics", "Real Estate"],
  "Computing": ["Computer Science", "Information Technology", "Software Engineering", "Data Science", "Cyber Security", "Artificial Intelligence", "Business Information Technology", "Computer Engineering"],
  "Law": ["Law", "Laws"],
  "Business": ["Commerce", "Economics", "Human Resource", "Accounting", "Business Administration", "Finance", "Procurement", "Supply Chain", "Banking", "Entrepreneurship", "Hospitality", "Tourism"],
  "Education": ["Education"],
  "Arts": ["Arts", "International Relations", "Criminology", "Communication", "Journalism", "Psychology", "Policy", "Sociology", "Political Science", "Counselling", "Social Work", "Community Development"],
  "Agriculture": ["Agriculture", "Food Science", "Environmental Health", "Horticulture", "Animal Science", "Agribusiness", "Forestry", "Environmental Science", "Natural Resource", "Aquatic", "Fisheries"],
  "Science": ["Actuarial", "Mathematics", "Statistics", "Physics", "Chemistry", "Biochemistry", "Industrial Chemistry", "Analytical Chemistry", "Microbiology", "Biomedical Science", "Forensic", "Biology", "Geology", "Meteorology", "Bachelor of Science"]
};

let allCourseResults = [];

function initSubjects() {
  const container = document.getElementById("subjects");
  subjectGroups.forEach(({ group, subjects: subs }) => {
    container.innerHTML += `<div class="subject-group-label">${group}</div>`;
    const grid = document.createElement("div");
    grid.className = "subjects-grid";
    subs.forEach(subject => {
      grid.innerHTML += `
        <div class="subject-item">
          <label>${subject}</label>
          <select data-subject="${subject}">
            <option value="">-- Grade --</option>
            ${Object.keys(gradesMap).map(g => `<option value="${g}">${g}</option>`).join("")}
          </select>
        </div>
      `;
    });
    container.appendChild(grid);
  });
}

function getSubjectGrades() {
  let data = {}, total = 0, count = 0;
  document.querySelectorAll("select[data-subject]").forEach(select => {
    const subject = select.dataset.subject;
    const grade = select.value;
    if (grade) {
      const points = gradesMap[grade];
      data[subject] = points;
      total += points;
      count++;
    }
  });
  const best7 = Object.values(data).sort((a, b) => b - a).slice(0, 7);
  const aggregate = best7.reduce((sum, p) => sum + p, 0);
  return { data, total, count, aggregate };
}

function getMeanGrade(mean) {
  if (mean >= 11.5) return "A";
  if (mean >= 10.5) return "A-";
  if (mean >= 9.5)  return "B+";
  if (mean >= 8.5)  return "B";
  if (mean >= 7.5)  return "B-";
  if (mean >= 6.5)  return "C+";
  if (mean >= 5.5)  return "C";
  if (mean >= 4.5)  return "C-";
  if (mean >= 3.5)  return "D+";
  if (mean >= 2.5)  return "D";
  if (mean >= 1.5)  return "D-";
  return "E";
}

function getWeightedCluster(subjectGrades, clusterSubjects) {
  return clusterSubjects.reduce((sum, sub) => sum + (subjectGrades[sub] || 0), 0);
}

function getCourseCategory(courseName) {
  for (const [cat, keywords] of Object.entries(categoryMap)) {
    if (keywords.some(k => courseName.includes(k))) return cat;
  }
  return "Other";
}

function evaluateCourses(subjectGrades, aggregate) {
  return coursesData.map(course => {
    const weighted = getWeightedCluster(subjectGrades, course.cluster);
    const qualifiedUnis = course.universities.filter(uni => weighted >= uni.cutoff);
    const minCutoff = Math.min(...course.universities.map(u => u.cutoff));
    const gap = minCutoff - weighted;
    return {
      name: course.name,
      category: getCourseCategory(course.name),
      weightedCluster: weighted,
      qualified: qualifiedUnis.length > 0,
      universities: qualifiedUnis,
      allUniversities: course.universities,
      minCutoff,
      gap: gap > 0 ? gap : 0
    };
  });
}

function toggleCard(id) {
  const el = document.getElementById(id);
  const icon = document.getElementById("icon-" + id);
  el.classList.toggle("hidden");
  icon.textContent = el.classList.contains("hidden") ? "▼" : "▲";
}

function shareResults(grade, mean, qualifiedCount) {
  const text = `🎓 My KCSE Results on GradeCalc KE\nMean Grade: ${grade} (${mean} pts)\nI qualify for ${qualifiedCount} university courses!\n\nCheck yours → https://quintus-web.github.io/gradecalc-ke`;
  if (navigator.share) {
    navigator.share({ title: "GradeCalc KE Results", text });
  } else {
    navigator.clipboard.writeText(text).then(() => alert("Results copied! Paste and share 🚀"));
  }
}

function resetForm() {
  document.querySelectorAll("select[data-subject]").forEach(s => s.value = "");
  document.getElementById("result").innerHTML = "";
  document.getElementById("filters").classList.add("hidden");
  allCourseResults = [];
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function applyFilters() {
  if (!allCourseResults.length) return;
  const cat = document.getElementById("filter-category").value;
  const status = document.getElementById("filter-status").value;
  const search = document.getElementById("search-box").value.toLowerCase();

  let filtered = allCourseResults;
  if (cat) filtered = filtered.filter(c => c.category === cat);
  if (status === "qualified") filtered = filtered.filter(c => c.qualified);
  if (status === "not-qualified") filtered = filtered.filter(c => !c.qualified);
  if (search) filtered = filtered.filter(c => c.name.toLowerCase().includes(search));

  renderCourseCards(filtered);
}

function renderCourseCards(results) {
  const qualified = results.filter(c => c.qualified);
  const notQualified = results.filter(c => !c.qualified);
  const container = document.getElementById("result");

  const header = container.querySelector(".results-header");
  const headerHTML = header ? header.outerHTML : "";

  let html = headerHTML;

  html += `<div class="courses-label">✅ Eligible Courses (${qualified.length})</div>`;

  if (qualified.length === 0) {
    html += `<p class="empty-msg">No eligible courses in this filter. Try changing the category.</p>`;
  }

  qualified.forEach(course => {
    const id = "q-" + Math.random().toString(36).slice(2);
    html += `
      <div class="course-card qualified fade-in">
        <div class="course-name" onclick="toggleCard('${id}')">
          🎓 ${course.name}
          <span class="toggle-icon" id="icon-${id}">▼</span>
        </div>
        <div class="course-meta">
          <span class="badge badge-green">Cluster: ${course.weightedCluster.toFixed(2)} pts</span>
          <span class="badge badge-blue">${course.category}</span>
        </div>
        <div class="uni-list" id="${id}">
          ${course.universities.map(u => `
            <div class="uni-row">
              <span>🏫 ${u.name}</span>
              <span class="cutoff-tag">Cutoff: ${u.cutoff}</span>
            </div>
          `).join("")}
        </div>
      </div>
    `;
  });

  if (notQualified.length > 0) {
    html += `<div class="courses-label" style="margin-top:24px;">❌ Not Yet Eligible (${notQualified.length})</div>`;
    notQualified.forEach(course => {
      const id = "n-" + Math.random().toString(36).slice(2);
      const pct = Math.min(100, Math.round((course.weightedCluster / course.minCutoff) * 100));
      html += `
        <div class="course-card not-qualified fade-in">
          <div class="course-name" onclick="toggleCard('${id}')">
            ${course.name}
            <span class="toggle-icon" id="icon-${id}">▼</span>
          </div>
          <div class="course-meta">
            <span class="badge badge-orange">Your pts: ${course.weightedCluster.toFixed(2)}</span>
            <span class="badge badge-red">Need +${course.gap.toFixed(2)} more</span>
          </div>
          <div class="progress-bar"><div class="progress-fill" style="width:${pct}%"></div></div>
          <div class="progress-label">${pct}% of minimum cutoff (${course.minCutoff})</div>
          <div class="uni-list hidden" id="${id}">
            ${course.allUniversities.map(u => `
              <div class="uni-row">
                <span>🏫 ${u.name}</span>
                <span class="cutoff-tag">Cutoff: ${u.cutoff}</span>
              </div>
            `).join("")}
          </div>
        </div>
      `;
    });
  }

  container.innerHTML = html;
}

function renderResults(mean, grade, aggregate, courseResults) {
  const qualified = courseResults.filter(c => c.qualified);
  const notQualified = courseResults.filter(c => !c.qualified);

  const headerHTML = `
    <div class="results-header">
      <div class="stats-row">
        <div class="stat-box">
          <div class="stat-label">Mean Grade</div>
          <div class="mean-badge">${grade}</div>
        </div>
        <div class="stat-box">
          <div class="stat-label">Mean Points</div>
          <div class="stat-value">${mean.toFixed(2)}</div>
        </div>
        <div class="stat-box">
          <div class="stat-label">Aggregate (best 7)</div>
          <div class="stat-value">${aggregate}</div>
        </div>
      </div>
      <div class="eligibility-summary">
        <span class="pill green">✅ ${qualified.length} Eligible</span>
        <span class="pill red">❌ ${notQualified.length} Not Eligible</span>
      </div>
      <button class="share-btn" onclick="shareResults('${grade}', ${mean.toFixed(2)}, ${qualified.length})">
        📤 Share My Results
      </button>
    </div>
  `;

  document.getElementById("result").innerHTML = headerHTML;
  renderCourseCards(courseResults);
  document.getElementById("result").scrollIntoView({ behavior: "smooth", block: "start" });
}

function calculate() {
  const { data, total, count, aggregate } = getSubjectGrades();

  if (count === 0) {
    document.getElementById("result").innerHTML = `<p class="error-msg">⚠️ Please select at least one grade!</p>`;
    return;
  }

  document.getElementById("loading").classList.remove("hidden");
  document.getElementById("result").innerHTML = "";
  document.getElementById("filters").classList.add("hidden");

  setTimeout(() => {
    const mean = total / count;
    const grade = getMeanGrade(mean);
    allCourseResults = evaluateCourses(data, aggregate);

    document.getElementById("loading").classList.add("hidden");
    document.getElementById("filters").classList.remove("hidden");

    renderResults(mean, grade, aggregate, allCourseResults);
  }, 600);
}

initSubjects();
