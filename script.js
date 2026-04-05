const gradesMap = {
  "A": 12, "A-": 11, "B+": 10, "B": 9, "B-": 8,
  "C+": 7, "C": 6, "C-": 5, "D+": 4, "D": 3, "D-": 2, "E": 1
};

const subjects = [
  "English", "Kiswahili", "Mathematics", "Biology",
  "Chemistry", "Physics", "History", "Geography"
];

function initSubjects() {
  const container = document.getElementById("subjects");
  subjects.forEach(subject => {
    container.innerHTML += `
      <div class="subject-item">
        <label>${subject}</label>
        <select data-subject="${subject}">
          <option value="">-- Grade --</option>
          ${Object.keys(gradesMap).map(g => `<option value="${g}">${g}</option>`).join("")}
        </select>
      </div>
    `;
  });
}

function getSubjectGrades() {
  let data = {}, total = 0, count = 0;
  document.querySelectorAll("select").forEach(select => {
    const subject = select.dataset.subject;
    const grade = select.value;
    if (grade) {
      const points = gradesMap[grade];
      data[subject] = points;
      total += points;
      count++;
    }
  });
  return { data, total, count };
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

function evaluateCourses(meanPoints) {
  return coursesData.map(course => {
    const qualifiedUnis = course.universities.filter(uni => meanPoints >= uni.cutoff);
    return {
      name: course.name,
      qualified: qualifiedUnis.length > 0,
      universities: qualifiedUnis,
      allUniversities: course.universities
    };
  });
}

function renderResults(mean, grade, courseResults) {
  const qualified = courseResults.filter(c => c.qualified);
  const notQualified = courseResults.filter(c => !c.qualified);

  let html = `
    <div class="results-header">
      <div style="font-size:0.85rem; color:#94a3b8;">Your Mean Grade</div>
      <div class="mean-badge">${grade}</div>
      <div class="mean-points">${mean.toFixed(2)} points</div>
    </div>
    <div class="courses-label">✅ Courses You Qualify For (${qualified.length})</div>
  `;

  if (qualified.length === 0) {
    html += `<p style="color:#94a3b8; font-size:0.85rem; text-align:center;">No courses matched your grades yet. Keep pushing! 💪</p>`;
  }

  qualified.forEach(course => {
    html += `
      <div class="course-card qualified">
        <div class="course-name">🎓 ${course.name}</div>
        <div class="uni-list">${course.universities.map(u => `• ${u.name} — cutoff ${u.cutoff}`).join("<br>")}</div>
      </div>
    `;
  });

  if (notQualified.length > 0) {
    html += `<div class="courses-label" style="margin-top:20px;">⚠️ Just Out of Reach (${notQualified.length})</div>`;
    notQualified.forEach(course => {
      const minCutoff = Math.min(...course.allUniversities.map(u => u.cutoff));
      html += `
        <div class="course-card not-qualified">
          <div class="course-name">${course.name}</div>
          <div class="uni-list">Minimum cutoff needed: ${minCutoff}</div>
        </div>
      `;
    });
  }

  document.getElementById("result").innerHTML = html;
}

function calculate() {
  const { data, total, count } = getSubjectGrades();

  if (count === 0) {
    document.getElementById("result").innerHTML = `<p class="error-msg">⚠️ Please select at least one grade!</p>`;
    return;
  }

  const mean = total / count;
  const grade = getMeanGrade(mean);
  const courseResults = evaluateCourses(mean);

  renderResults(mean, grade, courseResults);
}

initSubjects();
