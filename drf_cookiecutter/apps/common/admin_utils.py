from django.contrib.admin.options import TO_FIELD_VAR
from django.contrib.admin.utils import unquote


class CustomToolbarActionsModelAdminMixin:
    change_form_template = "admin/custom_toolbar_actions_change_form.html"
    change_actions = []
    submit_buttons = []

    def get_instance(self, request, object_id):
        to_field = request.POST.get(
            TO_FIELD_VAR, request.GET.get(TO_FIELD_VAR)
        )
        obj = self.get_object(request, unquote(object_id), to_field)
        return obj

    def change_view(self, request, object_id, form_url="", extra_context=None):
        extra_context = extra_context or {}
        extra_context.update(
            {
                "change_actions": [
                    self._get_action_dict(action, request, object_id)
                    for action in self.get_change_actions(request, object_id)
                ],
                "submit_buttons": [
                    self._get_submit_button_dict(
                        button_tuple, request, object_id
                    )
                    for button_tuple in self.get_submit_buttons(
                        request, object_id
                    )
                ],
            }
        )
        return super().change_view(request, object_id, form_url, extra_context)

    def get_change_actions(self, request, object_id):
        return self.change_actions

    def _get_action_dict(self, action_name, request, object_id):
        action = getattr(self, action_name)
        return dict(
            title=getattr(
                action, "title", action_name.replace("_", " ").title()
            ),
            url=action(request, object_id),
        )

    def get_submit_buttons(self, request, object_id):
        return self.submit_buttons

    def _get_submit_button_dict(self, button_tuple, request, object_id):
        button_title, button_name = button_tuple
        return dict(
            title=button_title,
            name=button_name,
        )
