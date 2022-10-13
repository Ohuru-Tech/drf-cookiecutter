from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings


class CustomAllauthAdapter(DefaultAccountAdapter):
    def _get_verification_url(self):
        set_url = getattr(settings, "EMAIL_VERIFICATION_URL")
        if not set_url:
            return None
        if set_url[-1] != "/":
            return set_url + "/"
        return set_url

    def send_mail(self, template_prefix, email, context):
        verification_url = self._get_verification_url()
        if verification_url:
            context[
                "activate_url"
            ] = f"{verification_url()}{context['key']}"
        else:
            return super(CustomAllauthAdapter, self).send_mail(
                template_prefix, email, context
            )
        msg = self.render_mail(template_prefix, email, context)
        msg.send()
