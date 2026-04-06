import pandas as pd
import json

# Read the Excel file
df = pd.read_excel('FULL_Kenya_Universities_Degrees_Cutoffs.xlsx', sheet_name='Cutoff_Points')

# Define cluster subject mappings based on KUCCPS clusters
cluster_subjects = {
    1: ["English", "Kiswahili", "History", "Geography"],  # Law
    2: ["Mathematics", "English", "Kiswahili", "History"],  # Business
    3: ["English", "Kiswahili", "History", "Geography"],  # Humanities/Arts
    4: ["English", "Kiswahili", "Geography", "History"],  # Social Sciences
    5: ["Mathematics", "Physics", "Chemistry", "Geography"],  # Engineering (Civil/Construction)
    6: ["Mathematics", "Physics", "Chemistry", "Biology"],  # Engineering (Electrical/Mechanical)
    7: ["Mathematics", "Physics", "Chemistry", "Biology"],  # Computing & IT
    8: ["English", "Kiswahili", "History", "Geography"],  # Education (Arts)
    9: ["Mathematics", "Physics", "Chemistry", "Biology"],  # Computing
    10: ["Mathematics", "Physics", "Chemistry", "Biology"],  # Pure Sciences
    11: ["Mathematics", "Physics", "Geography", "Chemistry"],  # Built Environment (Architecture)
    12: ["Mathematics", "Physics", "Chemistry", "Biology"],  # Engineering
    13: ["Biology", "Chemistry", "Physics", "Mathematics"],  # Health Sciences/Medicine
    14: ["Biology", "Chemistry", "Mathematics", "Geography"],  # Agriculture
    15: ["Biology", "Chemistry", "Mathematics", "Geography"],  # Agriculture & Environmental
}

# Custom cluster assignments for specific courses
custom_clusters = {
    "Bachelor of Law": 1,
    "Bachelor of Laws": 1,
    "Bachelor of Commerce": 2,
    "Bachelor of Economics": 2,
    "Bachelor of Business": 2,
    "Bachelor of Arts": 3,
    "BSc Civil Engineering": 5,
    "Bachelor of Architecture": 11,
    "BSc Computer Science": 7,
    "BSc Information Technology": 7,
    "Bachelor of Medicine and Surgery": 13,
    "Bachelor of Pharmacy": 13,
    "Bachelor of Nursing": 13,
    "Bachelor of Education": 8,
    "BSc Electrical": 6,
    "BSc Mechanical": 6,
    "Bachelor of Agriculture": 15,
    "Bachelor of Veterinary": 13,
}

def get_cluster_code(degree_name, cluster_name):
    """Determine cluster code based on degree name and cluster"""
    degree_lower = degree_name.lower()
    
    # Check custom mappings first
    for key, code in custom_clusters.items():
        if key.lower() in degree_lower:
            return code
    
    # Map by cluster name
    cluster_mapping = {
        "Health Sciences": 13,
        "Medicine": 13,
        "Law": 1,
        "Business": 2,
        "Humanities": 3,
        "Arts": 3,
        "Engineering": 12,
        "Computing": 7,
        "Education": 8,
        "Sciences": 10,
        "Built Environment": 11,
        "Agriculture": 15,
    }
    
    for key, code in cluster_mapping.items():
        if key.lower() in str(cluster_name).lower():
            return code
    
    # Default mappings based on keywords
    if any(word in degree_lower for word in ["medicine", "surgery", "pharmacy", "nursing", "dental", "clinical"]):
        return 13
    elif any(word in degree_lower for word in ["law", "laws"]):
        return 1
    elif any(word in degree_lower for word in ["commerce", "business", "economics", "accounting"]):
        return 2
    elif any(word in degree_lower for word in ["computer", "information technology", "software", "cyber"]):
        return 7
    elif any(word in degree_lower for word in ["engineering", "mechanical", "electrical", "civil"]):
        return 12
    elif any(word in degree_lower for word in ["architecture", "quantity surveying", "construction"]):
        return 11
    elif any(word in degree_lower for word in ["education"]):
        return 8
    elif any(word in degree_lower for word in ["agriculture", "veterinary", "forestry"]):
        return 15
    else:
        return 3  # Default to Arts/Humanities

# Process the data
courses_dict = {}

for _, row in df.iterrows():
    degree = str(row['Degree Programme']).strip()
    university = str(row['University']).strip()
    cluster_name = str(row['Cluster']).strip()
    
    # Get cutoff - try 2026 estimate first, then 2024
    cutoff_str = str(row['Cutoff 2026 (Estimated)'])
    if cutoff_str == 'nan' or cutoff_str == '-':
        cutoff_str = str(row['Cutoff 2024 (Official)'])
    
    # Parse cutoff value (handle ranges like "42.044.9" which means 42.0-44.9)
    try:
        cutoff_str = cutoff_str.strip()
        if cutoff_str == 'nan' or cutoff_str == '-' or not cutoff_str:
            continue
        
        # Handle concatenated ranges like "42.044.9" (means 42.0 to 44.9)
        if len(cutoff_str) > 6 and '.' in cutoff_str:
            # Split at the second decimal point
            parts = cutoff_str.split('.')
            if len(parts) >= 3:
                # Take first number (e.g., "42.0" from "42.044.9")
                cutoff = float(f"{parts[0]}.{parts[1]}")
            else:
                cutoff = float(cutoff_str)
        else:
            cutoff = float(cutoff_str)
    except Exception as e:
        print(f"Skipping {degree} at {university}: Could not parse cutoff '{cutoff_str}'")
        continue
    
    # Get cluster code
    cluster_code = get_cluster_code(degree, cluster_name)
    
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
