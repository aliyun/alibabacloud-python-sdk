# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListDeviceGroupsResponseBody(DaraModel):
    def __init__(
        self,
        device_groups: List[main_models.ListDeviceGroupsResponseBodyDeviceGroups] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        # The list of device labels.
        self.device_groups = device_groups
        # Id of the request
        self.request_id = request_id
        # The total number of device labels.
        self.total_num = total_num

    def validate(self):
        if self.device_groups:
            for v1 in self.device_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeviceGroups'] = []
        if self.device_groups is not None:
            for k1 in self.device_groups:
                result['DeviceGroups'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_groups = []
        if m.get('DeviceGroups') is not None:
            for k1 in m.get('DeviceGroups'):
                temp_model = main_models.ListDeviceGroupsResponseBodyDeviceGroups()
                self.device_groups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListDeviceGroupsResponseBodyDeviceGroups(DaraModel):
    def __init__(
        self,
        description: str = None,
        device_group_id: str = None,
        dynamic_operator: str = None,
        dynamic_rule: main_models.Rule = None,
        group_type: str = None,
        is_default: str = None,
        match_dev_tags: List[str] = None,
        name: str = None,
    ):
        # The device label description.
        self.description = description
        # The device label ID.
        self.device_group_id = device_group_id
        # The rule operator of the dynamic device group.
        self.dynamic_operator = dynamic_operator
        # The matching rule of the dynamic device label.
        self.dynamic_rule = dynamic_rule
        # The device label type. Valid values:
        # - **static**: A static device label. Members consist of manually added terminal devices.
        # - **dynamic**: A dynamic device label. Members are automatically calculated by matching rules when terminal devices report heartbeats.
        self.group_type = group_type
        # Indicates whether the device label is a system built-in device label. Valid values:
        # - **true**: A system built-in device label.
        # - **false**: A user-defined device label.
        self.is_default = is_default
        # The collection of terminal device IDs associated with the device label.
        self.match_dev_tags = match_dev_tags
        # The device label name.
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

        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id

        if self.dynamic_operator is not None:
            result['DynamicOperator'] = self.dynamic_operator

        if self.dynamic_rule is not None:
            result['DynamicRule'] = self.dynamic_rule.to_map()

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.match_dev_tags is not None:
            result['MatchDevTags'] = self.match_dev_tags

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
            temp_model = main_models.Rule()
            self.dynamic_rule = temp_model.from_map(m.get('DynamicRule'))

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('MatchDevTags') is not None:
            self.match_dev_tags = m.get('MatchDevTags')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

