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
        subject="Outreach Pipeline Demo",
        html_content="""
        <h2>Hello!</h2>
        <p>This email was sent using Brevo API integration.
        </p>
        """
    )

    try:

        response = api_instance.send_transac_email(email)

        print("Email sent successfully")
        print(response)

    except ApiException as error:

        print("Brevo Error:", error)