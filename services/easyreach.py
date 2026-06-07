def prepare_eazyreach_leads(company_data):


    lead = {
        "company": company_data["name"],
        "industry": company_data["industry"],
        "linkedin": company_data["linkedin"],
        "location": company_data["location"],
        "email": company_data["email"]
    }

    return lead