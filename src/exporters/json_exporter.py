"""
JSON Report Exporter
"""

import json

def export_json(report):

    with open("reports/report.json", "w") as file:

        json.dump(report, file, indent=4)

    print("JSON report generated.")
