# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class GetApplicationTemplateResponseBody(DaraModel):
    def __init__(
        self,
        application_template: main_models.GetApplicationTemplateResponseBodyApplicationTemplate = None,
        request_id: str = None,
    ):
        # The application template details.
        self.application_template = application_template
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.application_template:
            self.application_template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_template is not None:
            result['ApplicationTemplate'] = self.application_template.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationTemplate') is not None:
            temp_model = main_models.GetApplicationTemplateResponseBodyApplicationTemplate()
            self.application_template = temp_model.from_map(m.get('ApplicationTemplate'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetApplicationTemplateResponseBodyApplicationTemplate(DaraModel):
    def __init__(
        self,
        application_template_id: str = None,
        application_template_name: str = None,
        built_in_application_actions: List[main_models.GetApplicationTemplateResponseBodyApplicationTemplateBuiltInApplicationActions] = None,
        built_in_application_status: str = None,
        create_time: int = None,
        custom_rule_status: str = None,
        description: str = None,
        template_status: str = None,
        unknown_action: str = None,
        update_time: int = None,
    ):
        # The ID of the application template.
        self.application_template_id = application_template_id
        # The name of the application template.
        self.application_template_name = application_template_name
        # The list of built-in application actions.
        self.built_in_application_actions = built_in_application_actions
        # The switch status for built-in application control. Valid values:
        # - **Enable**: Enabled.
        # - **Disable**: Disabled.
        self.built_in_application_status = built_in_application_status
        # The creation time of the application template. The value is a UNIX timestamp in seconds.
        self.create_time = create_time
        # The switch status for custom application rules. Valid values:
        # - **Enable**: Enabled.
        # - **Disable**: Disabled.
        self.custom_rule_status = custom_rule_status
        # The description of the application template.
        self.description = description
        # The overall switch status of the application template. Valid values:
        # - **Enable**: Enabled.
        # - **Disable**: Disabled.
        self.template_status = template_status
        # The action for unidentified applications. Valid values:
        # - **Allow**: Allows the traffic.
        # - **Alert**: Monitors the traffic.
        # - **Deny**: Blocks the traffic.
        self.unknown_action = unknown_action
        # The last update time of the application template. The value is a UNIX timestamp in seconds.
        self.update_time = update_time

    def validate(self):
        if self.built_in_application_actions:
            for v1 in self.built_in_application_actions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_template_id is not None:
            result['ApplicationTemplateId'] = self.application_template_id

        if self.application_template_name is not None:
            result['ApplicationTemplateName'] = self.application_template_name

        result['BuiltInApplicationActions'] = []
        if self.built_in_application_actions is not None:
            for k1 in self.built_in_application_actions:
                result['BuiltInApplicationActions'].append(k1.to_map() if k1 else None)

        if self.built_in_application_status is not None:
            result['BuiltInApplicationStatus'] = self.built_in_application_status

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.custom_rule_status is not None:
            result['CustomRuleStatus'] = self.custom_rule_status

        if self.description is not None:
            result['Description'] = self.description

        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status

        if self.unknown_action is not None:
            result['UnknownAction'] = self.unknown_action

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationTemplateId') is not None:
            self.application_template_id = m.get('ApplicationTemplateId')

        if m.get('ApplicationTemplateName') is not None:
            self.application_template_name = m.get('ApplicationTemplateName')

        self.built_in_application_actions = []
        if m.get('BuiltInApplicationActions') is not None:
            for k1 in m.get('BuiltInApplicationActions'):
                temp_model = main_models.GetApplicationTemplateResponseBodyApplicationTemplateBuiltInApplicationActions()
                self.built_in_application_actions.append(temp_model.from_map(k1))

        if m.get('BuiltInApplicationStatus') is not None:
            self.built_in_application_status = m.get('BuiltInApplicationStatus')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CustomRuleStatus') is not None:
            self.custom_rule_status = m.get('CustomRuleStatus')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')

        if m.get('UnknownAction') is not None:
            self.unknown_action = m.get('UnknownAction')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetApplicationTemplateResponseBodyApplicationTemplateBuiltInApplicationActions(DaraModel):
    def __init__(
        self,
        action: str = None,
        application_id: int = None,
    ):
        # The action performed on the application. Valid values:
        # - **Allow**: Allows the traffic.
        # - **Alert**: Monitors the traffic.
        # - **Deny**: Blocks the traffic.
        self.action = action
        # The ID of the application in the built-in application signature library.
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

