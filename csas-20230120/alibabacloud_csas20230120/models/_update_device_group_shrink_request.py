# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDeviceGroupShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        device_group_id: str = None,
        dynamic_operator: str = None,
        dynamic_rule_shrink: str = None,
        name: str = None,
    ):
        # The description of the device label. Set this parameter to an empty string to clear the description. The description can contain letters, digits, Chinese characters, spaces, periods (.), underscores (_), and hyphens (-).
        self.description = description
        # The ID of the device label.
        self.device_group_id = device_group_id
        # The operator of the dynamic device group rule.
        self.dynamic_operator = dynamic_operator
        # The matching rule of the dynamic device label.
        self.dynamic_rule_shrink = dynamic_rule_shrink
        # The name of the device label. The name must be 1 to 128 characters in length and can contain letters, digits, Chinese characters, periods (.), underscores (_), and hyphens (-). Spaces are not supported.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id

        if self.dynamic_operator is not None:
            result['DynamicOperator'] = self.dynamic_operator

        if self.dynamic_rule_shrink is not None:
            result['DynamicRule'] = self.dynamic_rule_shrink

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')

        if m.get('DynamicOperator') is not None:
            self.dynamic_operator = m.get('DynamicOperator')

        if m.get('DynamicRule') is not None:
            self.dynamic_rule_shrink = m.get('DynamicRule')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

