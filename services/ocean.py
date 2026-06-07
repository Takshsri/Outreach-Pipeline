import requests

from config import OCEAN_API_KEY


def find_similar_companies(company_domain):

    print(f"\nFinding companies similar to {company_domain}...\n")

    url = "https://api.ocean.io/v3/search/companies"

    headers = {
        "x-api-token": OCEAN_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
    "size": 5,
    "companiesFilters": {
        "lookalikeDomains": [company_domain]
    },
    "fields": [
        "domain",
        "name"
    ]
}

    try:

        response = requests.post(
            url,
            headers=headers,
            json=payload
        )

        print("Status Code:", response.status_code)

        response.raise_for_status()

        data = response.json()

        companies = []

        results = data.get("companies", [])

        for item in results:

            company_info = item.get("company", {})

            domain = company_info.get("domain")

            if domain:
                companies.append(domain)

        return companies

    except requests.exceptions.HTTPError as error:

        print("HTTP Error:", error)

        print(response.text)

    except requests.exceptions.RequestException as error:

        print("Request Error:", error)

    return []