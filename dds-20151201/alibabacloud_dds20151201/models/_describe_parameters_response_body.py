# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeParametersResponseBody(DaraModel):
    def __init__(
        self,
        config_parameters: main_models.DescribeParametersResponseBodyConfigParameters = None,
        engine: str = None,
        engine_version: str = None,
        request_id: str = None,
        running_parameters: main_models.DescribeParametersResponseBodyRunningParameters = None,
    ):
        # The parameter settings in the configuration template.
        self.config_parameters = config_parameters
        # The database engine of the instance. Default value: **mongodb**.
        self.engine = engine
        # The database engine version of the instance.
        self.engine_version = engine_version
        # The request ID.
        self.request_id = request_id
        # The settings of the parameters that have taken effect.
        self.running_parameters = running_parameters

    def validate(self):
        if self.config_parameters:
            self.config_parameters.validate()
        if self.running_parameters:
            self.running_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_parameters is not None:
            result['ConfigParameters'] = self.config_parameters.to_map()

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.running_parameters is not None:
            result['RunningParameters'] = self.running_parameters.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigParameters') is not None:
            temp_model = main_models.DescribeParametersResponseBodyConfigParameters()
            self.config_parameters = temp_model.from_map(m.get('ConfigParameters'))

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RunningParameters') is not None:
            temp_model = main_models.DescribeParametersResponseBodyRunningParameters()
            self.running_parameters = temp_model.from_map(m.get('RunningParameters'))

        return self

class DescribeParametersResponseBodyRunningParameters(DaraModel):
    def __init__(
        self,
        parameter: List[main_models.DescribeParametersResponseBodyRunningParametersParameter] = None,
    ):
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            for v1 in self.parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Parameter'] = []
        if self.parameter is not None:
            for k1 in self.parameter:
                result['Parameter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameter = []
        if m.get('Parameter') is not None:
            for k1 in m.get('Parameter'):
                temp_model = main_models.DescribeParametersResponseBodyRunningParametersParameter()
                self.parameter.append(temp_model.from_map(k1))

        return self

class DescribeParametersResponseBodyRunningParametersParameter(DaraModel):
    def __init__(
        self,
        character_type: str = None,
        checking_code: str = None,
        force_restart: str = None,
        modifiable_status: str = None,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        # 实例的角色类型，取值说明：
        # 
        # - **db**：shard角色。
        # - **cs**：config server角色。
        # - **mongos**：mongos角色。
        self.character_type = character_type
        # The valid values of the parameter.
        self.checking_code = checking_code
        # Indicates whether a restart is required for parameter modifications to take effect. Valid values:
        # 
        # *   **false**: A restart is not required. Modifications take effect immediately.
        # *   **true**: A restart is required for parameter modifications to take effect.
        self.force_restart = force_restart
        # Indicates whether the parameter value can be modified. Valid values:
        # 
        # *   **false**: The parameter value cannot be modified.
        # *   **true**: The parameter value can be modified.
        self.modifiable_status = modifiable_status
        # The description of the parameter.
        self.parameter_description = parameter_description
        # The name of the parameter.
        self.parameter_name = parameter_name
        # The value of the parameter.
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.character_type is not None:
            result['CharacterType'] = self.character_type

        if self.checking_code is not None:
            result['CheckingCode'] = self.checking_code

        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart

        if self.modifiable_status is not None:
            result['ModifiableStatus'] = self.modifiable_status

        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CharacterType') is not None:
            self.character_type = m.get('CharacterType')

        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')

        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')

        if m.get('ModifiableStatus') is not None:
            self.modifiable_status = m.get('ModifiableStatus')

        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        return self

class DescribeParametersResponseBodyConfigParameters(DaraModel):
    def __init__(
        self,
        parameter: List[main_models.DescribeParametersResponseBodyConfigParametersParameter] = None,
    ):
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            for v1 in self.parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Parameter'] = []
        if self.parameter is not None:
            for k1 in self.parameter:
                result['Parameter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameter = []
        if m.get('Parameter') is not None:
            for k1 in m.get('Parameter'):
                temp_model = main_models.DescribeParametersResponseBodyConfigParametersParameter()
                self.parameter.append(temp_model.from_map(k1))

        return self

class DescribeParametersResponseBodyConfigParametersParameter(DaraModel):
    def __init__(
        self,
        checking_code: str = None,
        force_restart: bool = None,
        modifiable_status: bool = None,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        # The valid values of the parameter.
        self.checking_code = checking_code
        # Indicates whether a restart is required for parameter modifications to take effect. Valid values:
        # 
        # *   **false**: A restart is not required. Modifications take effect immediately.
        # *   **true**: A restart is required for parameter modifications to take effect.
        self.force_restart = force_restart
        # Indicates whether the parameter value can be modified. Valid values:
        # 
        # *   **false**: The parameter value cannot be modified.
        # *   **true**: The parameter value can be modified.
        self.modifiable_status = modifiable_status
        # The description of the parameter.
        self.parameter_description = parameter_description
        # The name of the parameter.
        self.parameter_name = parameter_name
        # The value of the parameter.
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

        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart

        if self.modifiable_status is not None:
            result['ModifiableStatus'] = self.modifiable_status

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

        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')

        if m.get('ModifiableStatus') is not None:
            self.modifiable_status = m.get('ModifiableStatus')

        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        return self

