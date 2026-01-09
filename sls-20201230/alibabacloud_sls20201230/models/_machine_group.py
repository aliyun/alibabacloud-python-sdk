# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class MachineGroup(DaraModel):
    def __init__(
        self,
        group_attribute: main_models.MachineGroupGroupAttribute = None,
        group_name: str = None,
        group_type: str = None,
        machine_identify_type: str = None,
        machine_list: List[str] = None,
    ):
        self.group_attribute = group_attribute
        # This parameter is required.
        self.group_name = group_name
        self.group_type = group_type
        # This parameter is required.
        self.machine_identify_type = machine_identify_type
        # This parameter is required.
        self.machine_list = machine_list

    def validate(self):
        if self.group_attribute:
            self.group_attribute.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_attribute is not None:
            result['groupAttribute'] = self.group_attribute.to_map()

        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.group_type is not None:
            result['groupType'] = self.group_type

        if self.machine_identify_type is not None:
            result['machineIdentifyType'] = self.machine_identify_type

        if self.machine_list is not None:
            result['machineList'] = self.machine_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupAttribute') is not None:
            temp_model = main_models.MachineGroupGroupAttribute()
            self.group_attribute = temp_model.from_map(m.get('groupAttribute'))

        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')

        if m.get('machineIdentifyType') is not None:
            self.machine_identify_type = m.get('machineIdentifyType')

        if m.get('machineList') is not None:
            self.machine_list = m.get('machineList')

        return self

class MachineGroupGroupAttribute(DaraModel):
    def __init__(
        self,
        external_name: str = None,
        group_topic: str = None,
    ):
        self.external_name = external_name
        self.group_topic = group_topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_name is not None:
            result['externalName'] = self.external_name

        if self.group_topic is not None:
            result['groupTopic'] = self.group_topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('externalName') is not None:
            self.external_name = m.get('externalName')

        if m.get('groupTopic') is not None:
            self.group_topic = m.get('groupTopic')

        return self

