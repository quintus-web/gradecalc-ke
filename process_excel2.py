import pandas as pd
import json

# Read the Excel file with 2024 cutoff data
df = pd.read_excel('Kenya_Degree_Cutoffs_2025_2026.xlsx', skiprows=2)

# Define cluster subject mappings based on KUCCPS clusters
cluster_subjects = {
    1: ["English", "Kiswahili", "History", "Geography"],  # Law
    2: ["Mathematics", "English", "Kiswahili", "History"],  # Business/Commerce
    3: ["English", "Kiswahili", "History", "Geography"],  # Arts/Humanities
    5: ["Mathematics", "Physics", "Chemistry", "Geography"],  # Civil Engineering
    6: ["Mathematics", "Physics", "Chemistry", "Biology"],  # Electrical/Mechanical Engineering
    7: ["Mathematics", "Physics", "Chemistry", "Biology"],  # Computing & IT
    8: ["English", "Kiswahili", "History", "Geography"],  # Education (Arts)
    9: ["Mathematics", "Physics", "Chemistry", "Biology"],  # Education (Science)
    10: ["Mathematics", "Physics", "Chemistry", "Biology"],  # Pure Sciences
    11: ["Mathematics", "Physics", "Geography", "Chemistry"],  # Architecture/Built Environment
    12: ["Mathematics", "Physics", "Chemistry", "Biology"],  # Engineering
    13: ["Biology", "Chemistry", "Physics", "Mathematics"],  # Medicine/Health Sciences
    14: ["Biology", "Chemistry", "Mathematics", "English"],  # Health (alternative)
    15: ["Biology", "Chemistry", "Mathematics", "Geography"],  # Agriculture
}

def get_cluster_code(degree_name):
    """Determine cluster code based on degree name"""
    degree_lower = degree_name.lower()
    
    # Medicine & Health
    if any(word in degree_lower for word in ["medicine", "surgery", "mbchb"]):
        return 13
    elif any(word in degree_lower for word in ["pharmacy", "pharmaceutical"]):
        return 13
    elif any(word in degree_lower for word in ["nursing", "midwifery"]):
        return 13
    elif any(word in degree_lower for word in ["dental", "dentistry"]):
        return 13
    elif any(word in degree_lower for word in ["clinical medicine", "clinical officer"]):
        return 13
    elif any(word in degree_lower for word in ["radiography", "radiology"]):
        return 13
    elif any(word in degree_lower for word in ["physiotherapy", "occupational therapy"]):
        return 13
    elif any(word in degree_lower for word in ["medical laboratory", "lab sciences"]):
        return 13
    elif any(word in degree_lower for word in ["public health", "health records", "nutrition", "dietetics"]):
        return 14
    
    # Law
    elif any(word in degree_lower for word in ["law", "laws", "ll.b"]):
        return 1
    
    # Business
    elif any(word in degree_lower for word in ["commerce", "business", "economics", "accounting", "finance", "human resource", "procurement", "supply chain", "entrepreneurship", "banking"]):
        return 2
    
    # Computing & IT
    elif any(word in degree_lower for word in ["computer science", "information technology", "software engineering", "cyber security", "data science", "artificial intelligence"]):
        return 7
    
    # Engineering
    elif "civil engineering" in degree_lower or "structural engineering" in degree_lower:
        return 5
    elif any(word in degree_lower for word in ["electrical", "electronic", "mechanical", "mechatronic", "aerospace", "aeronautical", "chemical engineering", "marine engineering", "petroleum engineering", "telecommunication engineering", "biomedical engineering"]):
        return 6
    elif any(word in degree_lower for word in ["engineering", "geospatial"]):
        return 12
    
    # Architecture & Built Environment
    elif any(word in degree_lower for word in ["architecture", "architectural", "quantity surveying", "construction management", "real estate", "landscape", "urban planning", "land economics", "surveying"]):
        return 11
    
    # Education
    elif "education (arts)" in degree_lower or ("education" in degree_lower and "arts" in degree_lower):
        return 8
    elif "education (science)" in degree_lower or ("education" in degree_lower and "science" in degree_lower):
        return 9
    elif any(word in degree_lower for word in ["education", "teaching"]):
        return 8
    
    # Agriculture
    elif any(word in degree_lower for word in ["agriculture", "veterinary", "horticulture", "animal science", "agribusiness", "forestry", "environmental science", "natural resource", "aquatic", "fisheries"]):
        return 15
    
    # Sciences
    elif any(word in degree_lower for word in ["actuarial", "mathematics", "statistics", "physics", "chemistry", "biochemistry", "microbiology", "biomedical science", "forensic science", "biology", "zoology", "botany", "geology", "meteorology"]):
        return 10
    
    # Arts & Social Sciences
    elif any(word in degree_lower for word in ["arts", "international relations", "criminology", "communication", "journalism", "psychology", "sociology", "political science", "linguistics", "gender", "social work", "counselling", "community development", "film", "theatre", "music", "public relations", "library", "hospitality", "tourism"]):
        return 3
    
    # Default to Arts
    else:
        return 3

# Process the data
courses_dict = {}

for _, row in df.iterrows():
    degree = str(row['PROGRAMME NAME']).strip()
    university = str(row['INSTITUTION NAME']).strip()
    
    # Skip if invalid
    if degree == 'nan' or university == 'nan':
        continue
    
    # Get cutoff - use 2024 cutoff
    cutoff_str = str(row['2024 CUTOFF'])
    
    # Parse cutoff value
    try:
        if cutoff_str == 'nan' or cutoff_str == '-' or not cutoff_str:
            continue
        cutoff = float(cutoff_str)
    except Exception as e:
        continue
    
    # Get cluster code
    cluster_code = get_cluster_code(degree)
    
    # Add to dictionary
    if degree not in courses_dict:
        courses_dict[degree] = {
            'name': degree,
            'cluster_code': cluster_code,
            'universities': []
        }
    
    courses_dict[degree]['universities'].append({
        'name': university,
        'cutoff': round(cutoff, 3)
    })

# Convert to list and add cluster subjects
courses_list = []
for course in courses_dict.values():
    cluster_code = course['cluster_code']
    course_data = {
        'name': course['name'],
        'cluster': cluster_subjects.get(cluster_code, cluster_subjects[3]),
        'universities': sorted(course['universities'], key=lambda x: x['cutoff'])
    }
    courses_list.append(course_data)

# Sort courses by name
courses_list.sort(key=lambda x: x['name'])

# Generate JavaScript file
js_content = """// KUCCPS Cluster Groups Reference:
// Group I:   English, Kiswahili, Mathematics
// Group II:  Biology, Physics, Chemistry
// Group III: History, Geography, CRE
// Group IV:  Agriculture, Computer Studies, Building Construction, etc.
// Group V:   Business Studies, French, Music, etc.

const coursesData = """

js_content += json.dumps(courses_list, indent=2)
js_content += ";\n"

# Write to file
with open('data.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Successfully processed {len(courses_list)} courses!")
print(f"Total university entries: {sum(len(c['universities']) for c in courses_list)}")
