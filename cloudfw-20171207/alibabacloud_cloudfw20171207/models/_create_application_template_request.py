# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class CreateApplicationTemplateRequest(DaraModel):
    def __init__(
        self,
        add_built_in_application_custom_actions: List[main_models.CreateApplicationTemplateRequestAddBuiltInApplicationCustomActions] = None,
        application_template_name: str = None,
        built_in_application_status: str = None,
        custom_rule_status: str = None,
        description: str = None,
        template_status: str = None,
        unknown_action: str = None,
    ):
        # The list of custom actions to configure for built-in applications. The application IDs in the list must be unique.
        self.add_built_in_application_custom_actions = add_built_in_application_custom_actions
        # The name of the application template. The name must be 1 to 64 characters in length and can contain Chinese characters, letters, digits, hyphens (-), underscores (_), and periods (.). It cannot contain spaces or be empty.
        # 
        # This parameter is required.
        self.application_template_name = application_template_name
        # The switch status of built-in application control. Only **Enable** is supported, which indicates that built-in application control is enabled. If you pass Disable, an error is returned.
        # 
        # This parameter is required.
        self.built_in_application_status = built_in_application_status
        # The switch status of custom application rules. Valid values:
        # - **Enable**: Enables the feature.
        # - **Disable**: Disables the feature.
        # 
        # This parameter is required.
        self.custom_rule_status = custom_rule_status
        # The description of the application template. The description can be up to 128 characters in length and can be empty.
        self.description = description
        # The overall switch status of the application template. Valid values:
        # - **Enable**: Enables the template.
        # - **Disable**: Disables the template.
        # 
        # This parameter is required.
        self.template_status = template_status
        # The action to take on unidentified applications. Valid values:
        # - **Allow**: Allows the traffic.
        # - **Alert**: Monitors the traffic.
        # - **Deny**: Blocks the traffic.
        # 
        # This parameter is required.
        self.unknown_action = unknown_action

    def validate(self):
        if self.add_built_in_application_custom_actions:
            for v1 in self.add_built_in_application_custom_actions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddBuiltInApplicationCustomActions'] = []
        if self.add_built_in_application_custom_actions is not None:
            for k1 in self.add_built_in_application_custom_actions:
                result['AddBuiltInApplicationCustomActions'].append(k1.to_map() if k1 else None)

        if self.application_template_name is not None:
            result['ApplicationTemplateName'] = self.application_template_name

        if self.built_in_application_status is not None:
            result['BuiltInApplicationStatus'] = self.built_in_application_status

        if self.custom_rule_status is not None:
            result['CustomRuleStatus'] = self.custom_rule_status

        if self.description is not None:
            result['Description'] = self.description

        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status

        if self.unknown_action is not None:
            result['UnknownAction'] = self.unknown_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.add_built_in_application_custom_actions = []
        if m.get('AddBuiltInApplicationCustomActions') is not None:
            for k1 in m.get('AddBuiltInApplicationCustomActions'):
                temp_model = main_models.CreateApplicationTemplateRequestAddBuiltInApplicationCustomActions()
                self.add_built_in_application_custom_actions.append(temp_model.from_map(k1))

        if m.get('ApplicationTemplateName') is not None:
            self.application_template_name = m.get('ApplicationTemplateName')

        if m.get('BuiltInApplicationStatus') is not None:
            self.built_in_application_status = m.get('BuiltInApplicationStatus')

        if m.get('CustomRuleStatus') is not None:
            self.custom_rule_status = m.get('CustomRuleStatus')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')

        if m.get('UnknownAction') is not None:
            self.unknown_action = m.get('UnknownAction')

        return self

class CreateApplicationTemplateRequestAddBuiltInApplicationCustomActions(DaraModel):
    def __init__(
        self,
        action: str = None,
        application_id: int = None,
    ):
        # The action to perform on the application. Valid values:
        # - **Allow**: Allows the traffic.
        # - **Alert**: Monitors the traffic.
        # - **Deny**: Blocks the traffic.
        self.action = action
        # The ID of the application for which you want to configure a custom action. The application must exist in the built-in application signature library and the ID cannot be 0. You can call the ListApplications operation to query the ID.
        self.application_id = application_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        return self

