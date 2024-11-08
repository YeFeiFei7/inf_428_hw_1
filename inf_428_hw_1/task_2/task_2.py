import pandas as pd
import numpy as np

# Define department and importance
departments = [
    ("Engineering", 5),
    ("Marketing", 3),
    ("Finance", 4),
    ("HR", 2),
    ("Science", 4)
]

# Define a function to generate random threat scores
def generate_random_data(mean, variance, num_samples):
    # scores 0-90
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)

# Generate sample data
data = {
    "Employee_Name": [],
    "Department": [],
    "Department_Importance": [],
    "Threat_Score": []
}

# Populate data for each department
for dept_name, importance in departments:
    num_employees = np.random.randint(10, 16)  # Number of employees per department
    mean_threat = np.random.randint(20, 70)    # Random mean threat score for department
    variance_threat = np.random.randint(5, 15) # Random variance for threat score

    threat_scores = generate_random_data(mean_threat, variance_threat, num_employees)

    # Fill data for each employee in the department
    for i in range(num_employees):
        data["Employee_Name"].append(f"{dept_name}_Emp_{i+1}")
        data["Department"].append(dept_name)
        data["Department_Importance"].append(importance)
        data["Threat_Score"].append(threat_scores[i])

# Create DataFrame
df = pd.DataFrame(data)


def calculate_aggregated_threat(df):
    # Group by department and calculate the average threat index for each department
    department_avg_threat = df.groupby('Department').apply(
        lambda x: x['Threat_Score'].mean()
    ).reset_index(name='Avg_Threat_Score')

    # Add importance and average threat index into calculation
    weighted_threats = []
    total_importance = 0

    for _, row in department_avg_threat.iterrows():
        dept_name = row['Department']
        avg_threat_score = row['Avg_Threat_Score']
        importance = df[df['Department'] == dept_name]['Department_Importance'].iloc[0]

        weighted_threats.append(avg_threat_score * importance)
        total_importance += importance

    # Added check to prevent division by 0
    if total_importance == 0:
        return 0  # If the importance of all departments is 0, return 0

    # calculate total threat score
    aggregated_threat_score = sum(weighted_threats) / total_importance
    return round(aggregated_threat_score, 2)


#Call the function and print the total threat index
aggregated_threat_score = calculate_aggregated_threat(df)
print("Aggregated Threat Score:", aggregated_threat_score)

