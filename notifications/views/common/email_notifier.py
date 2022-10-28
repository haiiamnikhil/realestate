from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string

from properties.models import Properties
from system_settings.models import EmailSettings


class EmailNotifier:

    def __init__(self):
        self.template_name = {
            'enquiry': 'common/email/prop_enquiry.html'
        }
        self.from_email = settings.EMAIL_HOST_USER

    def send_email_notification(self, data: dict, user=None, type=None):
        params = {}
        email_settings = EmailSettings.objects.get(user__user=user)
        if email_settings.is_enabled:
            params['subject'] = Properties.objects.get(
                uid=data['prop_uid']).heading
            params['receiver'] = email_settings.email
            params['type'] = type
            params['body'] = {
                'comment': data['comment'],
                'phone': data['phone'],
                'name': data['full_name'],
                'email': data['email']
            }
            self.send_email(params)
        else:
            pass

    def send_email(self, enquiry):

        subject = enquiry['subject']
        recipient = [enquiry['receiver']]
        template = self.template_name[enquiry['type']]
        html_content = render_to_string(template, enquiry)
        email = EmailMultiAlternatives(
            subject=subject, from_email=self.from_email, to=recipient)
        email.attach_alternative(html_content, 'text/html')
        email.send()
