# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateStateConfigurationShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        configure_mode: str = None,
        description: str = None,
        parameters: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        schedule_expression: str = None,
        schedule_type: str = None,
        tags_shrink: str = None,
        targets: str = None,
        template_name: str = None,
        template_version: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The configuration mode. Valid values: ApplyOnce: The configuration is applied only once. After a configuration is updated, the new configuration is applied. ApplyAndMonitor: The configuration is applied only once. After the configuration is applied, the system only checks whether the configuration is migrated in the future. ApplyAndAutoCorrect: The configuration is always applied.
        self.configure_mode = configure_mode
        # The description of the desired-state configuration.
        self.description = description
        # The parameters.
        self.parameters = parameters
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The schedule expression. The interval between two schedules must be a minimum of 30 minutes.
        # 
        # This parameter is required.
        self.schedule_expression = schedule_expression
        # The schedule type. Set the value to rate.
        # 
        # This parameter is required.
        self.schedule_type = schedule_type
        # The tags to be added to the configuration.
        self.tags_shrink = tags_shrink
        # The resources to be queried.
        # 
        # This parameter is required.
        self.targets = targets
        # The name of the template. The name must be 1 to 200 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        # 
        # This parameter is required.
        self.template_name = template_name
        # The version number of the template. If you do not specify this parameter, the latest version of the template is used.
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.configure_mode is not None:
            result['ConfigureMode'] = self.configure_mode

        if self.description is not None:
            result['Description'] = self.description

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.schedule_expression is not None:
            result['ScheduleExpression'] = self.schedule_expression

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        if self.targets is not None:
            result['Targets'] = self.targets

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConfigureMode') is not None:
            self.configure_mode = m.get('ConfigureMode')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ScheduleExpression') is not None:
            self.schedule_expression = m.get('ScheduleExpression')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        if m.get('Targets') is not None:
            self.targets = m.get('Targets')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        return self

