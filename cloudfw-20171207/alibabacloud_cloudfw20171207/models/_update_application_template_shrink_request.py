# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateApplicationTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        add_built_in_application_custom_actions_shrink: str = None,
        application_template_id: str = None,
        application_template_name: str = None,
        built_in_application_status: str = None,
        custom_rule_status: str = None,
        description: str = None,
        remove_built_in_application_custom_actions_shrink: str = None,
        template_status: str = None,
        unknown_action: str = None,
    ):
        # The list of custom actions to be added or updated for built-in applications. This list is merged with RemoveBuiltInApplicationCustomActions by removing items first and then adding items. The same application ID cannot appear in both lists at the same time.
        self.add_built_in_application_custom_actions_shrink = add_built_in_application_custom_actions_shrink
        # The ID of the application template to be modified. The template must exist within the current Alibaba Cloud account.
        # 
        # This parameter is required.
        self.application_template_id = application_template_id
        # The name of the application template. The name must be 1 to 64 characters in length and can contain Chinese characters, letters, digits, hyphens (-), underscores (_), and periods (.). It cannot contain spaces. If this parameter is not specified or is left empty, the original value is retained.
        self.application_template_name = application_template_name
        # The switch status of built-in application control. Valid values: only **Enable** is supported. If you specify Disable, an error is returned. If this parameter is not specified or is left empty, the original value is retained.
        self.built_in_application_status = built_in_application_status
        # The switch status of custom rules for applications. Valid values:
        # - **Enable**: Enabled.
        # - **Disable**: Disabled.
        # If this parameter is not specified or is left empty, the original value is retained.
        self.custom_rule_status = custom_rule_status
        # The description of the application template. The description can be up to 128 characters in length. If this parameter is not specified, the original value is retained. If an empty string is specified, the description is cleared.
        self.description = description
        # The list of built-in applications from which to remove custom actions. After removal, these applications revert to the default actions of the template. The same application ID cannot appear in AddBuiltInApplicationCustomActions at the same time.
        self.remove_built_in_application_custom_actions_shrink = remove_built_in_application_custom_actions_shrink
        # The master switch status of the application template. Valid values:
        # - **Enable**: Enabled.
        # - **Disable**: Disabled.
        # If this parameter is not specified or is left empty, the original value is retained.
        self.template_status = template_status
        # The action for unidentified applications. Valid values:
        # - **Allow**: Allow.
        # - **Alert**: Monitor.
        # - **Deny**: Block.
        # If this parameter is not specified or is left empty, the original value is retained.
        self.unknown_action = unknown_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_built_in_application_custom_actions_shrink is not None:
            result['AddBuiltInApplicationCustomActions'] = self.add_built_in_application_custom_actions_shrink

        if self.application_template_id is not None:
            result['ApplicationTemplateId'] = self.application_template_id

        if self.application_template_name is not None:
            result['ApplicationTemplateName'] = self.application_template_name

        if self.built_in_application_status is not None:
            result['BuiltInApplicationStatus'] = self.built_in_application_status

        if self.custom_rule_status is not None:
            result['CustomRuleStatus'] = self.custom_rule_status

        if self.description is not None:
            result['Description'] = self.description

        if self.remove_built_in_application_custom_actions_shrink is not None:
            result['RemoveBuiltInApplicationCustomActions'] = self.remove_built_in_application_custom_actions_shrink

        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status

        if self.unknown_action is not None:
            result['UnknownAction'] = self.unknown_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddBuiltInApplicationCustomActions') is not None:
            self.add_built_in_application_custom_actions_shrink = m.get('AddBuiltInApplicationCustomActions')

        if m.get('ApplicationTemplateId') is not None:
            self.application_template_id = m.get('ApplicationTemplateId')

        if m.get('ApplicationTemplateName') is not None:
            self.application_template_name = m.get('ApplicationTemplateName')

        if m.get('BuiltInApplicationStatus') is not None:
            self.built_in_application_status = m.get('BuiltInApplicationStatus')

        if m.get('CustomRuleStatus') is not None:
            self.custom_rule_status = m.get('CustomRuleStatus')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RemoveBuiltInApplicationCustomActions') is not None:
            self.remove_built_in_application_custom_actions_shrink = m.get('RemoveBuiltInApplicationCustomActions')

        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')

        if m.get('UnknownAction') is not None:
            self.unknown_action = m.get('UnknownAction')

        return self

