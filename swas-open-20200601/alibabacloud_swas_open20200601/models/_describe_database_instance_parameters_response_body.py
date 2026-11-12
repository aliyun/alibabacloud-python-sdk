# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class DescribeDatabaseInstanceParametersResponseBody(DaraModel):
    def __init__(
        self,
        config_parameters: List[main_models.DescribeDatabaseInstanceParametersResponseBodyConfigParameters] = None,
        engine: str = None,
        engine_version: str = None,
        request_id: str = None,
        running_parameters: List[main_models.DescribeDatabaseInstanceParametersResponseBodyRunningParameters] = None,
    ):
        # A list of configuration parameters being synchronized. After you modify and submit parameters, the instance starts to synchronize them. Once synchronization is complete, these parameters are removed from this list.
        self.config_parameters = config_parameters
        # The database engine. Currently, only `MySQL` is supported.
        self.engine = engine
        # The engine version. Valid values:
        # 
        # - `5.7`: MySQL 5.7.
        # 
        # - `8.0`: MySQL 8.0.
        self.engine_version = engine_version
        # The request ID.
        self.request_id = request_id
        # A list of running parameters.
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

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
                temp_model = main_models.DescribeDatabaseInstanceParametersResponseBodyConfigParameters()
                self.config_parameters.append(temp_model.from_map(k1))

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.running_parameters = []
        if m.get('RunningParameters') is not None:
            for k1 in m.get('RunningParameters'):
                temp_model = main_models.DescribeDatabaseInstanceParametersResponseBodyRunningParameters()
                self.running_parameters.append(temp_model.from_map(k1))

        return self

class DescribeDatabaseInstanceParametersResponseBodyRunningParameters(DaraModel):
    def __init__(
        self,
        checking_code: str = None,
        force_modify: str = None,
        force_restart: str = None,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        # The value range of the parameter.
        # 
        # > The value range varies by parameter.
        self.checking_code = checking_code
        # Indicates whether you can modify the parameter value. Valid values:
        # 
        # - `true`: You can modify the parameter value.
        # 
        # - `false`: You cannot modify the parameter value.
        self.force_modify = force_modify
        # Indicates if the database must be restarted for a parameter modification to take effect. Valid values:
        # 
        # - `true`: A restart is required. To apply changes for a parameter that requires a restart, you must set the `ForceRestart` parameter to `true`.
        # 
        # - `false`: A restart is not required.
        # 
        # Default value: `false`.
        self.force_restart = force_restart
        # The description of the running parameter.
        self.parameter_description = parameter_description
        # The name of the parameter.
        self.parameter_name = parameter_name
        # The value of the running parameter.
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checking_code is not None:
            result['CheckingCode'] = self.checking_code

        if self.force_modify is not None:
            result['ForceModify'] = self.force_modify

        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart

        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')

        if m.get('ForceModify') is not None:
            self.force_modify = m.get('ForceModify')

        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')

        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        return self

class DescribeDatabaseInstanceParametersResponseBodyConfigParameters(DaraModel):
    def __init__(
        self,
        checking_code: str = None,
        force_modify: str = None,
        force_restart: str = None,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        # The value range of the parameter.
        # 
        # > The value range varies by parameter.
        self.checking_code = checking_code
        # Indicates whether you can modify the parameter value. Valid values:
        # 
        # - `true`: You can modify the parameter value.
        # 
        # - `false`: You cannot modify the parameter value.
        self.force_modify = force_modify
        # Indicates if the database must be restarted for a parameter modification to take effect. Valid values:
        # 
        # - `true`: A restart is required. To apply changes for a parameter that requires a restart, you must set the `ForceRestart` parameter to `true`.
        # 
        # - `false`: A restart is not required.
        # 
        # Default value: `false`.
        self.force_restart = force_restart
        # The description of the parameter.
        self.parameter_description = parameter_description
        # The name of the parameter.
        self.parameter_name = parameter_name
        # The value of the parameter.
        # 
        # > The value varies by parameter.
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checking_code is not None:
            result['CheckingCode'] = self.checking_code

        if self.force_modify is not None:
            result['ForceModify'] = self.force_modify

        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart

        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')

        if m.get('ForceModify') is not None:
            self.force_modify = m.get('ForceModify')

        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')

        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        return self

