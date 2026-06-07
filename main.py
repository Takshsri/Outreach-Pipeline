from services.ocean import find_similar_companies
from services.brevo import send_email
from services.easyreach import prepare_eazyreach_leads

from services.prospeo import (
    find_company_contacts,
    search_people
)

from config import (
    PROSPEO_API_KEY,
    BREVO_API_KEY
)


def main():

    print("=" * 50)
    print("AI OUTREACH PIPELINE")
    print("=" * 50)

    company_domain = input(
        "\nEnter company domain: "
    ).strip()

    # STEP 1 — Ocean.io
    similar_companies = find_similar_companies(
        company_domain
    )

    if not similar_companies:

        print("\nNo similar companies found")
        return

    print("\nSimilar Companies:\n")

    for index, company in enumerate(
        similar_companies,
        start=1
    ):

        print(f"{index}. {company}")

    # Select first valid company
    selected_company = None

    for company in similar_companies:

        if "." in company and len(company) > 5:

            selected_company = company
            break

    if not selected_company:

        print("\nNo valid company found")
        return

    print("\n" + "=" * 50)
    print("COMPANY ENRICHMENT")
    print("=" * 50)

    # STEP 2 — Prospeo Company Enrichment
    contacts = find_company_contacts(
        selected_company,
        PROSPEO_API_KEY
    )

    if not contacts:

        print("\nNo company details found")
        return

    contact = contacts[0]

    print("\nCompany Details:\n")

    print(f"Company Name : {contact['name']}")
    print(f"Industry     : {contact['industry']}")
    print(f"Employees    : {contact['employees']}")
    print(f"Location     : {contact['location']}")
    print(f"LinkedIn     : {contact['linkedin']}")
    print("-" * 40)

    print("\n" + "=" * 50)
    

    # STEP 3 — Search People + Emails
    person = search_people(
        selected_company,
        PROSPEO_API_KEY
    )

    if not person:

        print("\nNo people found")
        return

    print("\nVerified Contact:\n")

    print(f"Name      : {person['full_name']}")
    print(f"Title     : {person['title']}")
    print(f"LinkedIn  : {person['linkedin']}")
    print(f"Email     : {person['email']}")

    print("\n" + "=" * 50)
    print("=" * 50)

    # STEP 4 — EazyReach Lead Preparation
    lead = prepare_eazyreach_leads({

        "name": contact["name"],
        "industry": contact["industry"],
        "location": contact["location"],
        "linkedin": person["linkedin"],
        "email": person["email"]
    })


    print(f"Company   : {lead['company']}")
    print(f"Industry  : {lead['industry']}")
    print(f"Location  : {lead['location']}")
    print(f"LinkedIn  : {lead['linkedin']}")
    

    print("\n" + "=" * 50)
    print("EMAIL AUTOMATION")
    print("=" * 50)

    # STEP 5 — Confirmation
    confirm = input(
        "\nSend outreach email? (yes/no): "
    ).lower()

    if confirm != "yes":

        print("\nEmail sending cancelled")
        return

    receiver_email = person.get(
        "email"
    )

    if not receiver_email:

        print("\nNo receiver email found")
        return

    # STEP 6 — Brevo Automation
    send_email(
        BREVO_API_KEY,
        "ramyamannam7@gmail.com",
        receiver_email
    )

    print("\nOutreach email sent successfully")


if __name__ == "__main__":
    main()