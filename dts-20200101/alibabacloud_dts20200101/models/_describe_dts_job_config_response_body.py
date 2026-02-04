# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDtsJobConfigResponseBody(DaraModel):
    def __init__(
        self,
        parameters: List[main_models.DescribeDtsJobConfigResponseBodyParameters] = None,
        request_id: str = None,
    ):
        self.parameters = parameters
        self.request_id = request_id

    def validate(self):
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.DescribeDtsJobConfigResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDtsJobConfigResponseBodyParameters(DaraModel):
    def __init__(
        self,
        checking_code: str = None,
        default_value: str = None,
        description: str = None,
        force_restart: str = None,
        modifiable: str = None,
        module: str = None,
        name: str = None,
        recommend_value: str = None,
        running_value: str = None,
        value_type: int = None,
    ):
        self.checking_code = checking_code
        self.default_value = default_value
        self.description = description
        self.force_restart = force_restart
        self.modifiable = modifiable
        self.module = module
        self.name = name
        self.recommend_value = recommend_value
        self.running_value = running_value
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checking_code is not None:
            result['CheckingCode'] = self.checking_code

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.description is not None:
            result['Description'] = self.description

        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart

        if self.modifiable is not None:
            result['Modifiable'] = self.modifiable

        if self.module is not None:
            result['Module'] = self.module

        if self.name is not None:
            result['Name'] = self.name

        if self.recommend_value is not None:
            result['RecommendValue'] = self.recommend_value

        if self.running_value is not None:
            result['RunningValue'] = self.running_value

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')

        if m.get('Modifiable') is not None:
            self.modifiable = m.get('Modifiable')

        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RecommendValue') is not None:
            self.recommend_value = m.get('RecommendValue')

        if m.get('RunningValue') is not None:
            self.running_value = m.get('RunningValue')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        return self

