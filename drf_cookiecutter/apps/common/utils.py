import logging

# import pickle
import smtplib
import socket

import dns.resolver

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)

COUNTRY_CHOICES = []
# with open(getattr(settings, "COUNTRIES_LIST_FILE_PATH"), "rb") as c_file:
#     COUNTRY_CHOICES = pickle.load(c_file)[5:]


class EmailVerification:
    @staticmethod
    def get_email_mx(domain: str) -> str:
        """
        Validates the MX record for the given email's domain
        @param domain: the domain extracted from the email
        @return: true if valid, false otherwise
        """
        try:
            records = dns.resolver.resolve(domain, "MX")
            return str(records[0].exchange)
        except dns.resolver.NoAnswer:
            return "None"

    @staticmethod
    def validate_email_mailbox(email: str) -> bool:
        """
        Validates if the mailbox actually exists
        @param email: the email to be checked
        @return: true if valid, false otherwise
        """
        host = socket.gethostname()
        server = smtplib.SMTP()
        server.set_debuglevel(0)

        mxRecord = EmailVerification.get_email_mx(email.split("@")[1])

        if mxRecord == "None":
            return False

        # SMTP Conversation
        server.connect(mxRecord)
        server.helo(host)
        server.mail("me@domain.com")
        code, message = server.rcpt(str(email))
        server.quit()

        # Assume 250 as Success
        if code == 250:
            return True
        return False
