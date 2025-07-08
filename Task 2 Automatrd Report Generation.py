import csv
from collections import defaultdict
from fpdf import FPDF

# Step 1: Read data from CSV
def read_data(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

# Step 2: Analyze data
def analyze_data(data):
    department_scores = defaultdict(list)
    for row in data:
        dept = row['Department']
        score = int(row['Score'])
        department_scores[dept].append(score)

    summary = {}
    for dept, scores in department_scores.items():
        avg = sum(scores) / len(scores)
        summary[dept] = {
            'count': len(scores),
            'average_score': round(avg, 2),
            'max_score': max(scores),
            'min_score': min(scores)
        }
    return summary

# Step 3: Generate PDF report
def generate_pdf(summary, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt="Department Score Summary Report", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    for dept, stats in summary.items():
        pdf.cell(200, 10, txt=f"Department: {dept}", ln=True)
        pdf.cell(200, 10, txt=f" - Total Employees: {stats['count']}", ln=True)
        pdf.cell(200, 10, txt=f" - Average Score: {stats['average_score']}", ln=True)
        pdf.cell(200, 10, txt=f" - Highest Score: {stats['max_score']}", ln=True)
        pdf.cell(200, 10, txt=f" - Lowest Score: {stats['min_score']}", ln=True)
        pdf.ln(5)

    pdf.output(output_path)
    print(f"Report generated: {output_path}")

# Main flow
if __name__ == "__main__":
    data = read_data("data.csv")
    summary = analyze_data(data)
    generate_pdf(summary, "sample_report.pdf")
