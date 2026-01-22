# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeParameterTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeParameterTemplatesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeParameterTemplatesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeParameterTemplatesResponseBodyData(DaraModel):
    def __init__(
        self,
        engine: str = None,
        engine_version: str = None,
        parameter_count: int = None,
        parameters: List[main_models.DescribeParameterTemplatesResponseBodyDataParameters] = None,
    ):
        self.engine = engine
        self.engine_version = engine_version
        self.parameter_count = parameter_count
        self.parameters = parameters

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
        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.parameter_count is not None:
            result['ParameterCount'] = self.parameter_count

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ParameterCount') is not None:
            self.parameter_count = m.get('ParameterCount')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.DescribeParameterTemplatesResponseBodyDataParameters()
                self.parameters.append(temp_model.from_map(k1))

        return self

class DescribeParameterTemplatesResponseBodyDataParameters(DaraModel):
    def __init__(
        self,
        checking_code: str = None,
        dynamic: int = None,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
        revisable: int = None,
    ):
        self.checking_code = checking_code
        self.dynamic = dynamic
        self.parameter_description = parameter_description
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value
        self.revisable = revisable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checking_code is not None:
            result['CheckingCode'] = self.checking_code

        if self.dynamic is not None:
            result['Dynamic'] = self.dynamic

        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        if self.revisable is not None:
            result['Revisable'] = self.revisable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')

        if m.get('Dynamic') is not None:
            self.dynamic = m.get('Dynamic')

        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        if m.get('Revisable') is not None:
            self.revisable = m.get('Revisable')

        return self

