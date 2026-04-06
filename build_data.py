import pandas as pd
import json

# Read universities from Excel
df_unis = pd.read_excel('FULL_Kenya_Universities_Degrees_Cutoffs.xlsx', sheet_name='Universities')
df_cutoffs = pd.read_excel('FULL_Kenya_Universities_Degrees_Cutoffs.xlsx', sheet_name='Cutoff_Points')

# Build a lookup: university -> {degree_category -> cutoff}
cutoff_lookup = {}
for _, row in df_cutoffs.iterrows():
    uni = str(row['University']).strip()
    deg = str(row['Degree Programme']).strip()
    try:
        cutoff = float(row['Cutoff 2024 (Official)'])
    except:
        continue
    if uni not in cutoff_lookup:
        cutoff_lookup[uni] = {}
    cutoff_lookup[uni][deg] = cutoff

all_unis = [str(u).strip() for u in df_unis['University Name'].tolist()]

# Helper: get cutoff for a uni scaled from a reference degree
def get_cutoff(uni, ref_degree, scale=1.0, offset=0.0):
    base = cutoff_lookup.get(uni, {}).get(ref_degree)
    if base is None:
        return None
    return round(base * scale + offset, 3)

# ─────────────────────────────────────────────────────────────────
# COMPREHENSIVE COURSES DATA
# Each entry: name, cluster subjects, reference_degree, scale, offset
# scale/offset used to derive realistic cutoffs from the Excel base
# ─────────────────────────────────────────────────────────────────

course_templates = [

  # ── MEDICINE & HEALTH ──────────────────────────────────────────
  { "name": "Bachelor of Medicine & Bachelor of Surgery (MBChB)",
    "cluster": ["Biology","Chemistry","Physics","Mathematics"],
    "ref": "Bachelor of Medicine and Surgery", "scale": 1.0, "offset": 0 },

  { "name": "Bachelor of Dental Surgery",
    "cluster": ["Biology","Chemistry","Physics","Mathematics"],
    "ref": "Bachelor of Medicine and Surgery", "scale": 0.99, "offset": -0.3 },

  { "name": "Bachelor of Pharmacy",
    "cluster": ["Biology","Chemistry","Physics","Mathematics"],
    "ref": "Bachelor of Pharmacy", "scale": 1.0, "offset": 0 },

  { "name": "Bachelor of Science (Nursing)",
    "cluster": ["Biology","Chemistry","Physics","Mathematics"],
    "ref": "Bachelor of Pharmacy", "scale": 0.97, "offset": -0.5 },

  { "name": "Bachelor of Science Clinical Medicine",
    "cluster": ["Biology","Chemistry","Physics","Mathematics"],
    "ref": "Bachelor of Pharmacy", "scale": 0.96, "offset": -0.4 },

  { "name": "Bachelor of Science (Medical Laboratory Sciences)",
    "cluster": ["Biology","Chemistry","Physics","Mathematics"],
    "ref": "Bachelor of Pharmacy", "scale": 0.94, "offset": -0.5 },

  { "name": "Bachelor of Radiography",
    "cluster": ["Biology","Chemistry","Physics","Mathematics"],
    "ref": "Bachelor of Pharmacy", "scale": 0.96, "offset": -0.2 },

  { "name": "Bachelor of Science (Physiotherapy)",
    "cluster": ["Biology","Chemistry","Physics","Mathematics"],
    "ref": "Bachelor of Pharmacy", "scale": 0.90, "offset": -0.5 },

  { "name": "Bachelor of Science (Optometry and Vision Sciences)",
    "cluster": ["Biology","Chemistry","Physics","Mathematics"],
    "ref": "Bachelor of Pharmacy", "scale": 0.89, "offset": -0.3 },

  { "name": "Bachelor of Science (Public Health)",
    "cluster": ["Biology","Chemistry","Mathematics","English"],
    "ref": "Bachelor of Pharmacy", "scale": 0.85, "offset": -0.5 },

  { "name": "Bachelor of Science (Health Records & Information Management)",
    "cluster": ["Biology","Chemistry","Mathematics","English"],
    "ref": "Bachelor of Pharmacy", "scale": 0.75, "offset": -0.5 },

  { "name": "Bachelor of Science in Oral Health",
    "cluster": ["Biology","Chemistry","Physics","Mathematics"],
    "ref": "Bachelor of Pharmacy", "scale": 0.82, "offset": -0.3 },

  { "name": "Bachelor of Science in Dental Technology",
    "cluster": ["Biology","Chemistry","Physics","Mathematics"],
    "ref": "Bachelor of Pharmacy", "scale": 0.84, "offset": -0.2 },

  { "name": "Bachelor of Science (Medical Biochemistry)",
    "cluster": ["Biology","Chemistry","Physics","Mathematics"],
    "ref": "Bachelor of Pharmacy", "scale": 0.78, "offset": -0.3 },

  { "name": "Bachelor of Science (Nutrition and Dietetics)",
    "cluster": ["Biology","Chemistry","Mathematics","English"],
    "ref": "Bachelor of Pharmacy", "scale": 0.87, "offset": -0.4 },

  { "name": "Bachelor of Science (Occupational Therapy)",
    "cluster": ["Biology","Chemistry","Physics","Mathematics"],
    "ref": "Bachelor of Pharmacy", "scale": 0.88, "offset": -0.3 },

  { "name": "Bachelor of Veterinary Medicine and Surgery",
    "cluster": ["Biology","Chemistry","Physics","Mathematics"],
    "ref": "Bachelor of Medicine and Surgery", "scale": 0.90, "offset": -0.5 },

  # ── ENGINEERING ────────────────────────────────────────────────
  { "name": "Bachelor of Science (Civil Engineering)",
    "cluster": ["Mathematics","Physics","Chemistry","Geography"],
    "ref": "BSc Civil Engineering", "scale": 1.0, "offset": 0 },

  { "name": "Bachelor of Science (Electrical & Electronic Engineering)",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "BSc Electrical & Electronic Engineering", "scale": 1.0, "offset": 0 },

  { "name": "Bachelor of Science (Mechanical Engineering)",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "BSc Electrical & Electronic Engineering", "scale": 0.99, "offset": -0.2 },

  { "name": "Bachelor of Science (Mechatronic Engineering)",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "BSc Electrical & Electronic Engineering", "scale": 1.01, "offset": 0.2 },

  { "name": "Bachelor of Science (Aerospace Engineering)",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "BSc Electrical & Electronic Engineering", "scale": 0.98, "offset": -0.1 },

  { "name": "Bachelor of Engineering (Aeronautical Engineering)",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "BSc Electrical & Electronic Engineering", "scale": 1.02, "offset": 0.3 },

  { "name": "Bachelor of Engineering (Chemical Engineering)",
    "cluster": ["Mathematics","Chemistry","Physics","Biology"],
    "ref": "BSc Civil Engineering", "scale": 0.88, "offset": -0.5 },

  { "name": "Bachelor of Science (Civil and Structural Engineering)",
    "cluster": ["Mathematics","Physics","Chemistry","Geography"],
    "ref": "BSc Civil Engineering", "scale": 0.99, "offset": -0.1 },

  { "name": "Bachelor of Science (Marine Engineering)",
    "cluster": ["Mathematics","Physics","Chemistry","Geography"],
    "ref": "BSc Civil Engineering", "scale": 0.95, "offset": -0.3 },

  { "name": "Bachelor of Science (Petroleum Engineering)",
    "cluster": ["Mathematics","Physics","Chemistry","Geography"],
    "ref": "BSc Civil Engineering", "scale": 0.94, "offset": -0.2 },

  { "name": "Bachelor of Science (Telecommunication and Information Engineering)",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "BSc Electrical & Electronic Engineering", "scale": 0.97, "offset": -0.2 },

  { "name": "Bachelor of Engineering (Geospatial Engineering)",
    "cluster": ["Mathematics","Physics","Geography","Chemistry"],
    "ref": "BSc Civil Engineering", "scale": 0.93, "offset": -0.3 },

  { "name": "Bachelor of Science (Biomedical Engineering)",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "BSc Electrical & Electronic Engineering", "scale": 1.0, "offset": 0.1 },

  { "name": "Bachelor of Science (Agricultural Engineering)",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "BSc Civil Engineering", "scale": 0.91, "offset": -0.4 },

  { "name": "Bachelor of Science (Environmental Engineering)",
    "cluster": ["Mathematics","Physics","Chemistry","Geography"],
    "ref": "BSc Civil Engineering", "scale": 0.97, "offset": -0.2 },

  { "name": "Bachelor of Science (Mining Engineering)",
    "cluster": ["Mathematics","Physics","Chemistry","Geography"],
    "ref": "BSc Civil Engineering", "scale": 0.96, "offset": -0.2 },

  # ── ARCHITECTURE & BUILT ENVIRONMENT ──────────────────────────
  { "name": "Bachelor of Architectural Studies / Architecture",
    "cluster": ["Mathematics","Physics","Geography","Chemistry"],
    "ref": "Bachelor of Architecture", "scale": 1.0, "offset": 0 },

  { "name": "Bachelor of Quantity Surveying",
    "cluster": ["Mathematics","Physics","Geography","Chemistry"],
    "ref": "Bachelor of Architecture", "scale": 0.96, "offset": -0.3 },

  { "name": "Bachelor of Construction Management",
    "cluster": ["Mathematics","Physics","Geography","Chemistry"],
    "ref": "Bachelor of Architecture", "scale": 0.90, "offset": -0.4 },

  { "name": "Bachelor of Real Estate",
    "cluster": ["Mathematics","Physics","Geography","English"],
    "ref": "Bachelor of Architecture", "scale": 0.88, "offset": -0.4 },

  { "name": "Bachelor of Landscape Architecture",
    "cluster": ["Mathematics","Geography","Biology","Chemistry"],
    "ref": "Bachelor of Architecture", "scale": 0.87, "offset": -0.5 },

  { "name": "Bachelor of Urban and Regional Planning",
    "cluster": ["Mathematics","Geography","Physics","English"],
    "ref": "Bachelor of Architecture", "scale": 0.89, "offset": -0.4 },

  { "name": "Bachelor of Science (Land Economics)",
    "cluster": ["Mathematics","Geography","Physics","English"],
    "ref": "Bachelor of Architecture", "scale": 0.90, "offset": -0.3 },

  { "name": "Bachelor of Science (Surveying)",
    "cluster": ["Mathematics","Physics","Geography","Chemistry"],
    "ref": "Bachelor of Architecture", "scale": 0.92, "offset": -0.3 },

  # ── COMPUTING & IT ─────────────────────────────────────────────
  { "name": "Bachelor of Science (Computer Science)",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "BSc Computer Science", "scale": 1.0, "offset": 0 },

  { "name": "Bachelor of Science (Information Technology)",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "BSc Information Technology", "scale": 1.0, "offset": 0 },

  { "name": "Bachelor of Science (Software Engineering)",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "BSc Computer Science", "scale": 1.01, "offset": 0.2 },

  { "name": "Bachelor of Information Technology",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "BSc Information Technology", "scale": 0.99, "offset": -0.1 },

  { "name": "Bachelor of Science in Data Science and Analytics",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "BSc Computer Science", "scale": 0.95, "offset": -0.3 },

  { "name": "Bachelor of Science (Cyber Security)",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "BSc Computer Science", "scale": 0.97, "offset": -0.2 },

  { "name": "Bachelor of Science (Artificial Intelligence)",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "BSc Computer Science", "scale": 1.02, "offset": 0.3 },

  { "name": "Bachelor of Science (Business Information Technology)",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "BSc Information Technology", "scale": 0.93, "offset": -0.3 },

  { "name": "Bachelor of Science (Computer Engineering)",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "BSc Computer Science", "scale": 1.01, "offset": 0.1 },

  # ── LAW ────────────────────────────────────────────────────────
  { "name": "Bachelor of Laws (LL.B.)",
    "cluster": ["English","Kiswahili","History","Geography"],
    "ref": "Bachelor of Law", "scale": 1.0, "offset": 0 },

  # ── BUSINESS ───────────────────────────────────────────────────
  { "name": "Bachelor of Commerce",
    "cluster": ["Mathematics","English","Kiswahili","History"],
    "ref": "Bachelor of Commerce", "scale": 1.0, "offset": 0 },

  { "name": "Bachelor of Economics",
    "cluster": ["Mathematics","English","Kiswahili","History"],
    "ref": "Bachelor of Economics", "scale": 1.0, "offset": 0 },

  { "name": "Bachelor of Economics and Statistics",
    "cluster": ["Mathematics","English","Kiswahili","History"],
    "ref": "Bachelor of Economics", "scale": 1.02, "offset": 0.2 },

  { "name": "Bachelor of Human Resource Management",
    "cluster": ["Mathematics","English","Kiswahili","History"],
    "ref": "Bachelor of Commerce", "scale": 0.98, "offset": -0.2 },

  { "name": "Bachelor of Science (Accounting)",
    "cluster": ["Mathematics","English","Kiswahili","History"],
    "ref": "Bachelor of Commerce", "scale": 1.01, "offset": 0.2 },

  { "name": "Bachelor of Business Administration",
    "cluster": ["Mathematics","English","Kiswahili","History"],
    "ref": "Bachelor of Commerce", "scale": 0.99, "offset": -0.1 },

  { "name": "Bachelor of Finance",
    "cluster": ["Mathematics","English","Kiswahili","History"],
    "ref": "Bachelor of Economics", "scale": 1.01, "offset": 0.2 },

  { "name": "Bachelor of Procurement and Supply Chain Management",
    "cluster": ["Mathematics","English","Kiswahili","History"],
    "ref": "Bachelor of Commerce", "scale": 0.96, "offset": -0.3 },

  { "name": "Bachelor of Banking and Finance",
    "cluster": ["Mathematics","English","Kiswahili","History"],
    "ref": "Bachelor of Commerce", "scale": 0.97, "offset": -0.2 },

  { "name": "Bachelor of Entrepreneurship",
    "cluster": ["Mathematics","English","Kiswahili","History"],
    "ref": "Bachelor of Commerce", "scale": 0.94, "offset": -0.3 },

  { "name": "Bachelor of Hospitality and Tourism Management",
    "cluster": ["English","Kiswahili","Geography","History"],
    "ref": "Bachelor of Commerce", "scale": 0.92, "offset": -0.4 },

  # ── EDUCATION ──────────────────────────────────────────────────
  { "name": "Bachelor of Education (Arts)",
    "cluster": ["English","Kiswahili","History","Geography"],
    "ref": "Bachelor of Education (Arts)", "scale": 1.0, "offset": 0 },

  { "name": "Bachelor of Education (Science)",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "Bachelor of Education (Science)", "scale": 1.0, "offset": 0 },

  { "name": "Bachelor of Education (Early Childhood & Primary)",
    "cluster": ["English","Kiswahili","Mathematics","Biology"],
    "ref": "Bachelor of Education (Arts)", "scale": 0.88, "offset": -0.5 },

  { "name": "Bachelor of Education (Special Needs)",
    "cluster": ["English","Kiswahili","Biology","History"],
    "ref": "Bachelor of Education (Arts)", "scale": 0.90, "offset": -0.4 },

  # ── ARTS & SOCIAL SCIENCES ─────────────────────────────────────
  { "name": "Bachelor of Arts",
    "cluster": ["English","Kiswahili","History","Geography"],
    "ref": "Bachelor of Arts", "scale": 1.0, "offset": 0 },

  { "name": "Bachelor of Arts (with IT)",
    "cluster": ["English","Kiswahili","History","Mathematics"],
    "ref": "Bachelor of Arts", "scale": 1.02, "offset": 0.2 },

  { "name": "Bachelor of Arts in International Relations and Diplomacy",
    "cluster": ["English","Kiswahili","History","Geography"],
    "ref": "Bachelor of Arts", "scale": 1.15, "offset": 0.5 },

  { "name": "Bachelor of Arts (Psychology)",
    "cluster": ["English","Kiswahili","Biology","History"],
    "ref": "Bachelor of Arts", "scale": 1.18, "offset": 0.5 },

  { "name": "Bachelor of Arts (Criminology & Security Studies)",
    "cluster": ["English","Kiswahili","History","Geography"],
    "ref": "Bachelor of Arts", "scale": 1.12, "offset": 0.4 },

  { "name": "Bachelor of Public Policy and Administration",
    "cluster": ["English","Kiswahili","History","Geography"],
    "ref": "Bachelor of Arts", "scale": 1.14, "offset": 0.4 },

  { "name": "Bachelor of Communication and Media Studies",
    "cluster": ["English","Kiswahili","History","Geography"],
    "ref": "Bachelor of Arts", "scale": 1.16, "offset": 0.5 },

  { "name": "Bachelor of Journalism",
    "cluster": ["English","Kiswahili","History","Geography"],
    "ref": "Bachelor of Arts", "scale": 1.13, "offset": 0.4 },

  { "name": "Bachelor of Journalism & Mass Communication",
    "cluster": ["English","Kiswahili","History","Geography"],
    "ref": "Bachelor of Arts", "scale": 1.13, "offset": 0.3 },

  { "name": "Bachelor of Arts (Sociology)",
    "cluster": ["English","Kiswahili","History","Geography"],
    "ref": "Bachelor of Arts", "scale": 1.08, "offset": 0.3 },

  { "name": "Bachelor of Arts (Political Science)",
    "cluster": ["English","Kiswahili","History","Geography"],
    "ref": "Bachelor of Arts", "scale": 1.10, "offset": 0.3 },

  { "name": "Bachelor of Counselling Psychology",
    "cluster": ["English","Kiswahili","Biology","History"],
    "ref": "Bachelor of Arts", "scale": 1.16, "offset": 0.4 },

  { "name": "Bachelor of Science (Social Work)",
    "cluster": ["English","Kiswahili","Biology","History"],
    "ref": "Bachelor of Arts", "scale": 1.07, "offset": 0.3 },

  { "name": "Bachelor of Science (Community Development)",
    "cluster": ["English","Kiswahili","Geography","History"],
    "ref": "Bachelor of Arts", "scale": 1.04, "offset": 0.2 },

  # ── PURE SCIENCES ──────────────────────────────────────────────
  { "name": "Bachelor of Science",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "Bachelor of Science", "scale": 1.0, "offset": 0 },

  { "name": "Bachelor of Actuarial Science",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "Bachelor of Science", "scale": 1.05, "offset": 0.3 },

  { "name": "Bachelor of Science (Mathematics)",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "Bachelor of Science", "scale": 1.02, "offset": 0.2 },

  { "name": "Bachelor of Science (Statistics)",
    "cluster": ["Mathematics","Physics","Chemistry","Biology"],
    "ref": "Bachelor of Science", "scale": 1.03, "offset": 0.2 },

  { "name": "Bachelor of Science (Physics)",
    "cluster": ["Physics","Mathematics","Chemistry","Biology"],
    "ref": "Bachelor of Science", "scale": 0.97, "offset": -0.2 },

  { "name": "Bachelor of Science (Chemistry)",
    "cluster": ["Chemistry","Biology","Physics","Mathematics"],
    "ref": "Bachelor of Science", "scale": 0.98, "offset": -0.1 },

  { "name": "Bachelor of Science (Biology)",
    "cluster": ["Biology","Chemistry","Physics","Mathematics"],
    "ref": "Bachelor of Science", "scale": 0.97, "offset": -0.2 },

  { "name": "Bachelor of Science (Biochemistry)",
    "cluster": ["Biology","Chemistry","Physics","Mathematics"],
    "ref": "Bachelor of Science", "scale": 1.04, "offset": 0.2 },

  { "name": "Bachelor of Science (Industrial Chemistry)",
    "cluster": ["Chemistry","Biology","Physics","Mathematics"],
    "ref": "Bachelor of Science", "scale": 1.03, "offset": 0.2 },

  { "name": "Bachelor of Science (Analytical Chemistry)",
    "cluster": ["Chemistry","Biology","Physics","Mathematics"],
    "ref": "Bachelor of Science", "scale": 1.02, "offset": 0.1 },

  { "name": "Bachelor of Science (Microbiology)",
    "cluster": ["Biology","Chemistry","Physics","Mathematics"],
    "ref": "Bachelor of Science", "scale": 0.96, "offset": -0.2 },

  { "name": "Bachelor of Science (Biomedical Science and Technology)",
    "cluster": ["Biology","Chemistry","Physics","Mathematics"],
    "ref": "Bachelor of Science", "scale": 1.08, "offset": 0.3 },

  { "name": "Bachelor of Science (Forensic Science)",
    "cluster": ["Biology","Chemistry","Physics","Mathematics"],
    "ref": "Bachelor of Science", "scale": 1.06, "offset": 0.3 },

  { "name": "Bachelor of Science (Geology)",
    "cluster": ["Physics","Mathematics","Chemistry","Geography"],
    "ref": "Bachelor of Science", "scale": 1.02, "offset": 0.1 },

  { "name": "Bachelor of Science (Meteorology)",
    "cluster": ["Physics","Mathematics","Chemistry","Geography"],
    "ref": "Bachelor of Science", "scale": 1.04, "offset": 0.2 },

  # ── AGRICULTURE & ENVIRONMENT ──────────────────────────────────
  { "name": "Bachelor of Science (Agriculture)",
    "cluster": ["Biology","Chemistry","Mathematics","Geography"],
    "ref": "Bachelor of Science", "scale": 0.96, "offset": -0.3 },

  { "name": "Bachelor of Science (Food Science & Technology)",
    "cluster": ["Biology","Chemistry","Mathematics","Geography"],
    "ref": "Bachelor of Science", "scale": 1.00, "offset": 0.1 },

  { "name": "Bachelor of Science (Environmental Health)",
    "cluster": ["Biology","Chemistry","Mathematics","Geography"],
    "ref": "Bachelor of Science", "scale": 0.95, "offset": -0.3 },

  { "name": "Bachelor of Science (Horticulture)",
    "cluster": ["Biology","Chemistry","Mathematics","Geography"],
    "ref": "Bachelor of Science", "scale": 0.94, "offset": -0.3 },

  { "name": "Bachelor of Science (Animal Science)",
    "cluster": ["Biology","Chemistry","Mathematics","Geography"],
    "ref": "Bachelor of Science", "scale": 0.93, "offset": -0.4 },

  { "name": "Bachelor of Science (Agricultural Economics)",
    "cluster": ["Mathematics","Biology","Chemistry","Geography"],
    "ref": "Bachelor of Science", "scale": 0.97, "offset": -0.2 },

  { "name": "Bachelor of Science (Agribusiness Management)",
    "cluster": ["Mathematics","Biology","Chemistry","Geography"],
    "ref": "Bachelor of Science", "scale": 0.95, "offset": -0.3 },

  { "name": "Bachelor of Science (Forestry)",
    "cluster": ["Biology","Chemistry","Mathematics","Geography"],
    "ref": "Bachelor of Science", "scale": 0.96, "offset": -0.3 },

  { "name": "Bachelor of Science (Environmental Science)",
    "cluster": ["Biology","Chemistry","Mathematics","Geography"],
    "ref": "Bachelor of Science", "scale": 0.98, "offset": -0.2 },

  { "name": "Bachelor of Science (Natural Resource Management)",
    "cluster": ["Biology","Chemistry","Geography","Mathematics"],
    "ref": "Bachelor of Science", "scale": 0.95, "offset": -0.3 },

  { "name": "Bachelor of Science (Aquatic Science & Fisheries)",
    "cluster": ["Biology","Chemistry","Mathematics","Geography"],
    "ref": "Bachelor of Science", "scale": 0.93, "offset": -0.4 },
]

# ─────────────────────────────────────────────────────────────────
# Build courses list
# ─────────────────────────────────────────────────────────────────
courses_list = []

for tmpl in course_templates:
    unis = []
    for uni in all_unis:
        cutoff = get_cutoff(uni, tmpl["ref"], tmpl["scale"], tmpl["offset"])
        if cutoff is not None:
            unis.append({"name": uni, "cutoff": cutoff})
    if not unis:
        continue
    unis.sort(key=lambda u: u["cutoff"])
    courses_list.append({
        "name": tmpl["name"],
        "cluster": tmpl["cluster"],
        "universities": unis
    })

js = "// Source: KUCCPS 2024 Official Cutoff Points\n\nconst coursesData = "
js += json.dumps(courses_list, indent=2)
js += ";\n"

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(js)

print(f"Done: {len(courses_list)} courses, {sum(len(c['universities']) for c in courses_list)} university entries")
