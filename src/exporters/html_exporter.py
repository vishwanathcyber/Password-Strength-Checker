"""
HTML Report Exporter
"""

def export_html(report):

    html = f"""
    <html>
    <head>
        <title>Password Strength Report</title>
    </head>
    <body>
        <h1>Password Strength Report</h1>
        <pre>{report}</pre>
    </body>
    </html>
    """

    with open("reports/report.html", "w") as file:
        file.write(html)

    print("HTML report generated.")
