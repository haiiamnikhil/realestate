from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string


class EmailNotifier:
    
    def __init__(self):
        self.template_name = {
            'enquiry' : 'common/email/prop_enquiry.html'
        }
        self.from_email = settings.EMAIL_HOST_USER
    
    def send_enquiry_email(self, enquiry):

        subject = enquiry['subject']
        recipient = [enquiry['receiver']]
        template = self.template_name[enquiry['type']]
        html_content = render_to_string(template, enquiry)
        email = EmailMultiAlternatives(subject=subject,from_email=self.from_email,to=recipient)
        email.attach_alternative(html_content,'text/html')
        email.send()