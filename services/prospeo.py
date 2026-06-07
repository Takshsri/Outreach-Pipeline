import requests


# STEP 1 — Company Enrichment
def find_company_contacts(
    company_domain,
    prospeo_api_key
):

    print(
        f"\nFinding company details for {company_domain}...\n"
    )

    url = "https://api.prospeo.io/search-company"

    headers = {
        "X-KEY": prospeo_api_key,
        "Content-Type": "application/json"
    }

    payload = {

        "filters": {
            "company": {
                "websites": {
                    "include": [company_domain]
                }
            }
        },

        "page": 1
    }

    try:

        response = requests.post(
            url,
            headers=headers,
            json=payload
        )

        print(
            "Prospeo Status:",
            response.status_code
        )

        response.raise_for_status()

        data = response.json()

        contacts = []

        results = data.get(
            "results",
            []
        )

        for item in results:

            company = item.get(
                "company",
                {}
            )

            contacts.append({

                "name": company.get(
                    "name"
                ),

                "industry": company.get(
                    "industry"
                ),

                "employees": company.get(
                    "employee_count"
                ),

                "location": company.get(
                    "location",
                    {}
                ).get(
                    "country"
                ),

                "linkedin": company.get(
                    "linkedin_url"
                ),

                "website": company.get(
                    "website"
                )
            })

        return contacts

    except requests.exceptions.HTTPError as error:

        print("HTTP Error:", error)

        print(response.text)

    except requests.exceptions.RequestException as error:

        print("Request Error:", error)

    return []


# STEP 2 — Search People
def search_people(
    company_domain,
    prospeo_api_key
):

    print("\nSearching people...\n")

    url = "https://api.prospeo.io/search-person"

    headers = {
        "X-KEY": prospeo_api_key,
        "Content-Type": "application/json"
    }

    payload = {

        "filters": {
            "company": {
                "websites": {
                    "include": [company_domain]
                }
            }
        },

        "page": 1
    }

    try:

        response = requests.post(
            url,
            headers=headers,
            json=payload
        )

        print(
            "Search Person Status:",
            response.status_code
        )

        response.raise_for_status()

        data = response.json()

        

        results = data.get(
            "results",
            []
        )

        if not results:

            print("\nNo people found")

            return None

        first_result = results[0]

        person = first_result.get(
            "person",
            {}
        )

        email_data = person.get(
            "email",
            {}
        )

        return {

            "person_id": person.get(
                "person_id"
            ),

            "full_name": person.get(
                "full_name"
            ),

            "title": person.get(
                "current_job_title"
            ),

            "linkedin": person.get(
                "linkedin_url"
            ),

            "email": email_data.get(
                "email",
                "Not Found"
            )
        }

    except requests.exceptions.HTTPError as error:

        print("HTTP Error:", error)

        print(response.text)

    except requests.exceptions.RequestException as error:

        print("Request Error:", error)

    return None