import csv

def export_to_csv(company_data):

    with open("leads.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Company",
            "Industry",
            "Employees",
            "LinkedIn"
        ])

        writer.writerow([
            company_data["name"],
            company_data["industry"],
            company_data["employees"],
            company_data["linkedin"]
        ])

    print("CSV exported successfully")