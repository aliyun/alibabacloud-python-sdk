# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeParametersResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeParametersResponseBodyData = None,
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
            temp_model = main_models.DescribeParametersResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeParametersResponseBodyData(DaraModel):
    def __init__(
        self,
        config_parameters: List[main_models.DescribeParametersResponseBodyDataConfigParameters] = None,
        dbinstance_id: str = None,
        engine: str = None,
        engine_version: str = None,
        running_parameters: List[main_models.DescribeParametersResponseBodyDataRunningParameters] = None,
    ):
        self.config_parameters = config_parameters
        self.dbinstance_id = dbinstance_id
        self.engine = engine
        self.engine_version = engine_version
        self.running_parameters = running_parameters

    def validate(self):
        if self.config_parameters:
            for v1 in self.config_parameters:
                 if v1:
                    v1.validate()
        if self.running_parameters:
            for v1 in self.running_parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigParameters'] = []
        if self.config_parameters is not None:
            for k1 in self.config_parameters:
                result['ConfigParameters'].append(k1.to_map() if k1 else None)

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        result['RunningParameters'] = []
        if self.running_parameters is not None:
            for k1 in self.running_parameters:
                result['RunningParameters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_parameters = []
        if m.get('ConfigParameters') is not None:
            for k1 in m.get('ConfigParameters'):
                temp_model = main_models.DescribeParametersResponseBodyDataConfigParameters()
                self.config_parameters.append(temp_model.from_map(k1))

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        self.running_parameters = []
        if m.get('RunningParameters') is not None:
            for k1 in m.get('RunningParameters'):
                temp_model = main_models.DescribeParametersResponseBodyDataRunningParameters()
                self.running_parameters.append(temp_model.from_map(k1))

        return self

class DescribeParametersResponseBodyDataRunningParameters(DaraModel):
    def __init__(
        self,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        self.parameter_description = parameter_description
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        return self

class DescribeParametersResponseBodyDataConfigParameters(DaraModel):
    def __init__(
        self,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        self.parameter_description = parameter_description
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        return self

