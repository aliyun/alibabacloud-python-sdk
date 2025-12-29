# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class CreateStateConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        state_configuration: main_models.CreateStateConfigurationResponseBodyStateConfiguration = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the desired-state configuration.
        self.state_configuration = state_configuration

    def validate(self):
        if self.state_configuration:
            self.state_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.state_configuration is not None:
            result['StateConfiguration'] = self.state_configuration.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StateConfiguration') is not None:
            temp_model = main_models.CreateStateConfigurationResponseBodyStateConfiguration()
            self.state_configuration = temp_model.from_map(m.get('StateConfiguration'))

        return self

class CreateStateConfigurationResponseBodyStateConfiguration(DaraModel):
    def __init__(
        self,
        configure_mode: str = None,
        create_time: str = None,
        description: str = None,
        parameters: Dict[str, Any] = None,
        resource_group_id: str = None,
        schedule_expression: str = None,
        schedule_type: str = None,
        state_configuration_id: str = None,
        tags: Dict[str, Any] = None,
        targets: str = None,
        template_id: str = None,
        template_name: str = None,
        template_version: str = None,
    ):
        # The configuration mode. Valid values:
        self.configure_mode = configure_mode
        # The time when the desired-state configuration was created.
        self.create_time = create_time
        # The description.
        self.description = description
        # The parameters.
        self.parameters = parameters
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The schedule expression.
        self.schedule_expression = schedule_expression
        # The schedule type.
        self.schedule_type = schedule_type
        # The ID of the desired-state configuration.
        self.state_configuration_id = state_configuration_id
        # The tags added to the configuration.
        self.tags = tags
        # The queried resources.
        self.targets = targets
        # The template ID.
        self.template_id = template_id
        # The name of the template.
        self.template_name = template_name
        # The name of the template version.
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configure_mode is not None:
            result['ConfigureMode'] = self.configure_mode

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.schedule_expression is not None:
            result['ScheduleExpression'] = self.schedule_expression

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.state_configuration_id is not None:
            result['StateConfigurationId'] = self.state_configuration_id

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.targets is not None:
            result['Targets'] = self.targets

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigureMode') is not None:
            self.configure_mode = m.get('ConfigureMode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ScheduleExpression') is not None:
            self.schedule_expression = m.get('ScheduleExpression')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('StateConfigurationId') is not None:
            self.state_configuration_id = m.get('StateConfigurationId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Targets') is not None:
            self.targets = m.get('Targets')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        return self

