"""
Markdown Report Exporter
"""

def export_markdown(report):

    with open("reports/report.md", "w") as file:

        file.write("# Password Strength Report\n\n")

        file.write(report)

    print("Markdown report generated.")
