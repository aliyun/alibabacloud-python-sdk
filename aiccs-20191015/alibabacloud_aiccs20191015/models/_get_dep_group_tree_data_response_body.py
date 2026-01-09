# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class GetDepGroupTreeDataResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetDepGroupTreeDataResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetDepGroupTreeDataResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDepGroupTreeDataResponseBodyData(DaraModel):
    def __init__(
        self,
        dep_group_id: str = None,
        dep_group_name: str = None,
        group_dtos: List[main_models.GetDepGroupTreeDataResponseBodyDataGroupDTOS] = None,
    ):
        self.dep_group_id = dep_group_id
        self.dep_group_name = dep_group_name
        self.group_dtos = group_dtos

    def validate(self):
        if self.group_dtos:
            for v1 in self.group_dtos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dep_group_id is not None:
            result['DepGroupId'] = self.dep_group_id

        if self.dep_group_name is not None:
            result['DepGroupName'] = self.dep_group_name

        result['GroupDTOS'] = []
        if self.group_dtos is not None:
            for k1 in self.group_dtos:
                result['GroupDTOS'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepGroupId') is not None:
            self.dep_group_id = m.get('DepGroupId')

        if m.get('DepGroupName') is not None:
            self.dep_group_name = m.get('DepGroupName')

        self.group_dtos = []
        if m.get('GroupDTOS') is not None:
            for k1 in m.get('GroupDTOS'):
                temp_model = main_models.GetDepGroupTreeDataResponseBodyDataGroupDTOS()
                self.group_dtos.append(temp_model.from_map(k1))

        return self

class GetDepGroupTreeDataResponseBodyDataGroupDTOS(DaraModel):
    def __init__(
        self,
        name: str = None,
        skill_group_id: int = None,
    ):
        self.name = name
        self.skill_group_id = skill_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        return self

