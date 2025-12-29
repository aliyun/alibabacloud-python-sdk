# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateStateConfigurationRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        configure_mode: str = None,
        description: str = None,
        parameters: Dict[str, Any] = None,
        region_id: str = None,
        resource_group_id: str = None,
        schedule_expression: str = None,
        schedule_type: str = None,
        state_configuration_id: str = None,
        tags: Dict[str, Any] = None,
        targets: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The configuration mode. Valid values: ApplyOnce: The configuration is applied only once. After a configuration is updated, the new configuration is applied. ApplyAndMonitor: The configuration is applied only once. After the configuration is applied, the system only checks whether the configuration is migrated in the future. ApplyAndAutoCorrect: The configuration is always applied.
        self.configure_mode = configure_mode
        # The description.
        self.description = description
        # The parameters.
        self.parameters = parameters
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The schedule expression.
        self.schedule_expression = schedule_expression
        # The schedule type.
        self.schedule_type = schedule_type
        # The ID of the desired-state configuration.
        # 
        # This parameter is required.
        self.state_configuration_id = state_configuration_id
        # The tags to be added to the configuration.
        self.tags = tags
        # The resources to be queried.
        self.targets = targets

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

        if self.state_configuration_id is not None:
            result['StateConfigurationId'] = self.state_configuration_id

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.targets is not None:
            result['Targets'] = self.targets

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

        if m.get('StateConfigurationId') is not None:
            self.state_configuration_id = m.get('StateConfigurationId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Targets') is not None:
            self.targets = m.get('Targets')

        return self

