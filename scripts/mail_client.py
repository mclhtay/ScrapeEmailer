import json
import ssl
import smtplib
import sys

class MailClient:
    def __init__(self, mail_config_json):
        self.mail_config_json = mail_config_json
        self.mail_config = {}
        self.default_context = ssl.create_default_context()

    def start_mail_client(self):
        try:
            self.mail_config = json.load(self.mail_config_json)
        except Exception as e:
            print(e)
            sys.exit()

    def get_mail_context(self):
        return self.default_context

    def send_email(self, message):
        smtp_server = self.mail_config["smtp_server"]
        port = self.mail_config["port"]
        sender_email = self.mail_config["sender_email"]
        password = self.mail_config["password"]
        receiver_email = self.mail_config["receiver_email"]

        server = smtplib.SMTP(smtp_server, port)

        try:
            server.starttls(context=self.default_context)
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        except Exception as e:
            print(e)
            sys.exit()
        finally:
            server.quit()