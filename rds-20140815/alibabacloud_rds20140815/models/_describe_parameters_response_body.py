# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeParametersResponseBody(DaraModel):
    def __init__(
        self,
        config_parameters: main_models.DescribeParametersResponseBodyConfigParameters = None,
        engine: str = None,
        engine_version: str = None,
        param_group_info: main_models.DescribeParametersResponseBodyParamGroupInfo = None,
        request_id: str = None,
        running_parameters: main_models.DescribeParametersResponseBodyRunningParameters = None,
    ):
        # The list of parameters that are being synchronized.
        # 
        # > After you modify and submit the parameters, you must wait for the parameters to be synchronized to the instance. After the synchronization, you can delete the parameters from the list.
        self.config_parameters = config_parameters
        # The type of the database engine.
        self.engine = engine
        # The version of the database engine.
        self.engine_version = engine_version
        # The information about the parameter template.
        self.param_group_info = param_group_info
        # The ID of the request.
        self.request_id = request_id
        # The parameters that are in use.
        self.running_parameters = running_parameters

    def validate(self):
        if self.config_parameters:
            self.config_parameters.validate()
        if self.param_group_info:
            self.param_group_info.validate()
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

        if self.param_group_info is not None:
            result['ParamGroupInfo'] = self.param_group_info.to_map()

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

        if m.get('ParamGroupInfo') is not None:
            temp_model = main_models.DescribeParametersResponseBodyParamGroupInfo()
            self.param_group_info = temp_model.from_map(m.get('ParamGroupInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RunningParameters') is not None:
            temp_model = main_models.DescribeParametersResponseBodyRunningParameters()
            self.running_parameters = temp_model.from_map(m.get('RunningParameters'))

        return self

class DescribeParametersResponseBodyRunningParameters(DaraModel):
    def __init__(
        self,
        dbinstance_parameter: List[main_models.DescribeParametersResponseBodyRunningParametersDBInstanceParameter] = None,
    ):
        self.dbinstance_parameter = dbinstance_parameter

    def validate(self):
        if self.dbinstance_parameter:
            for v1 in self.dbinstance_parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstanceParameter'] = []
        if self.dbinstance_parameter is not None:
            for k1 in self.dbinstance_parameter:
                result['DBInstanceParameter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_parameter = []
        if m.get('DBInstanceParameter') is not None:
            for k1 in m.get('DBInstanceParameter'):
                temp_model = main_models.DescribeParametersResponseBodyRunningParametersDBInstanceParameter()
                self.dbinstance_parameter.append(temp_model.from_map(k1))

        return self

class DescribeParametersResponseBodyRunningParametersDBInstanceParameter(DaraModel):
    def __init__(
        self,
        parameter_default_value: str = None,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
        parameter_value_range: str = None,
    ):
        # The default value of the parameter.
        self.parameter_default_value = parameter_default_value
        # The description of the parameter.
        self.parameter_description = parameter_description
        # The name of the parameter.
        self.parameter_name = parameter_name
        # The value of the parameter.
        self.parameter_value = parameter_value
        # The valid values of the parameter.
        self.parameter_value_range = parameter_value_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_default_value is not None:
            result['ParameterDefaultValue'] = self.parameter_default_value

        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        if self.parameter_value_range is not None:
            result['ParameterValueRange'] = self.parameter_value_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterDefaultValue') is not None:
            self.parameter_default_value = m.get('ParameterDefaultValue')

        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        if m.get('ParameterValueRange') is not None:
            self.parameter_value_range = m.get('ParameterValueRange')

        return self

class DescribeParametersResponseBodyParamGroupInfo(DaraModel):
    def __init__(
        self,
        param_group_id: str = None,
        parameter_group_desc: str = None,
        parameter_group_name: str = None,
        parameter_group_type: str = None,
    ):
        # The ID of the parameter template.
        self.param_group_id = param_group_id
        # The description of the parameter template.
        self.parameter_group_desc = parameter_group_desc
        # The name of the parameter template.
        self.parameter_group_name = parameter_group_name
        # The type of the parameter template.
        self.parameter_group_type = parameter_group_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_group_id is not None:
            result['ParamGroupId'] = self.param_group_id

        if self.parameter_group_desc is not None:
            result['ParameterGroupDesc'] = self.parameter_group_desc

        if self.parameter_group_name is not None:
            result['ParameterGroupName'] = self.parameter_group_name

        if self.parameter_group_type is not None:
            result['ParameterGroupType'] = self.parameter_group_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamGroupId') is not None:
            self.param_group_id = m.get('ParamGroupId')

        if m.get('ParameterGroupDesc') is not None:
            self.parameter_group_desc = m.get('ParameterGroupDesc')

        if m.get('ParameterGroupName') is not None:
            self.parameter_group_name = m.get('ParameterGroupName')

        if m.get('ParameterGroupType') is not None:
            self.parameter_group_type = m.get('ParameterGroupType')

        return self

class DescribeParametersResponseBodyConfigParameters(DaraModel):
    def __init__(
        self,
        dbinstance_parameter: List[main_models.DescribeParametersResponseBodyConfigParametersDBInstanceParameter] = None,
    ):
        self.dbinstance_parameter = dbinstance_parameter

    def validate(self):
        if self.dbinstance_parameter:
            for v1 in self.dbinstance_parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBInstanceParameter'] = []
        if self.dbinstance_parameter is not None:
            for k1 in self.dbinstance_parameter:
                result['DBInstanceParameter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbinstance_parameter = []
        if m.get('DBInstanceParameter') is not None:
            for k1 in m.get('DBInstanceParameter'):
                temp_model = main_models.DescribeParametersResponseBodyConfigParametersDBInstanceParameter()
                self.dbinstance_parameter.append(temp_model.from_map(k1))

        return self

class DescribeParametersResponseBodyConfigParametersDBInstanceParameter(DaraModel):
    def __init__(
        self,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
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

