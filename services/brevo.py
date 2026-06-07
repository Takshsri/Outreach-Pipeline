import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException


def send_email(api_key, sender_email, receiver_email):

    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = api_key

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )

    sender = {
        "email": sender_email,
        "name": "Ramya Outreach"
    }

    to = [
        {
            "email": receiver_email
        }
    ]

    email = sib_api_v3_sdk.SendSmtpEmail(

        to=to,

        sender=sender,

        subject="Business Collaboration Opportunity",

        html_content=f"""
        <html>
        <body>

            <h2>Hello,</h2>

            <p>
            I hope you are doing well.
            </p>

            <p>
            I recently came across your company profile
            during our AI-powered outreach research workflow.
            </p>

            <p>
            We are currently exploring potential business
            collaboration and networking opportunities with
            innovative companies in your industry.
            </p>

            <p>
            Your organization stood out based on its
            industry presence and operational scale.
            </p>

            <p>
            I would love to connect and explore possible
            collaboration opportunities.
            </p>

            <p>
            Looking forward to hearing from you.
            </p>

            <br>

            <p>
            Best Regards,<br>
            Ramya Mannam<br>
            AI Outreach Pipeline
            </p>

        </body>
        </html>
        """
    )

    try:

        response = api_instance.send_transac_email(email)

        print("Email sent successfully")
        print(response)

    except ApiException as error:

        print("Brevo Error:", error)