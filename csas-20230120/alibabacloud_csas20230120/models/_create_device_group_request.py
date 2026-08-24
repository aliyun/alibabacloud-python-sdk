# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class CreateDeviceGroupRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        dynamic_operator: str = None,
        dynamic_rule: main_models.Rule = None,
        group_type: str = None,
        name: str = None,
    ):
        # The description of the device label. The description can contain letters, digits, Chinese characters, spaces, periods (.), underscores (_), and hyphens (-). This parameter can be left empty.
        self.description = description
        # The operator of the dynamic device group rule.
        self.dynamic_operator = dynamic_operator
        # The matching rule of the dynamic device label.
        self.dynamic_rule = dynamic_rule
        # The type of the device label. Valid values:
        # 
        # - **static**: static device label. After creation, manually add terminal devices by calling [AddDeviceGroupMatchDevices](~~AddDeviceGroupMatchDevices~~).
        # - **dynamic**: dynamic device label. Members are automatically matched by the DynamicRule matching rule.
        self.group_type = group_type
        # The name of the device label. The name must be 1 to 128 characters in length and can contain letters, digits, Chinese characters, periods (.), underscores (_), and hyphens (-). Spaces are not supported.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.dynamic_rule:
            self.dynamic_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.dynamic_operator is not None:
            result['DynamicOperator'] = self.dynamic_operator

        if self.dynamic_rule is not None:
            result['DynamicRule'] = self.dynamic_rule.to_map()

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DynamicOperator') is not None:
            self.dynamic_operator = m.get('DynamicOperator')

        if m.get('DynamicRule') is not None:
            temp_model = main_models.Rule()
            self.dynamic_rule = temp_model.from_map(m.get('DynamicRule'))

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

