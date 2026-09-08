# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20260120 import models as main_models
from darabonba.model import DaraModel

class ListRiskLevelsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        risk_level_list: List[main_models.ListRiskLevelsResponseBodyRiskLevelList] = None,
    ):
        self.request_id = request_id
        self.risk_level_list = risk_level_list

    def validate(self):
        if self.risk_level_list:
            for v1 in self.risk_level_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RiskLevelList'] = []
        if self.risk_level_list is not None:
            for k1 in self.risk_level_list:
                result['RiskLevelList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.risk_level_list = []
        if m.get('RiskLevelList') is not None:
            for k1 in m.get('RiskLevelList'):
                temp_model = main_models.ListRiskLevelsResponseBodyRiskLevelList()
                self.risk_level_list.append(temp_model.from_map(k1))

        return self

class ListRiskLevelsResponseBodyRiskLevelList(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
        reference_num: int = None,
    ):
        self.description = description
        self.id = id
        self.name = name
        self.reference_num = reference_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.reference_num is not None:
            result['ReferenceNum'] = self.reference_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ReferenceNum') is not None:
            self.reference_num = m.get('ReferenceNum')

        return self

