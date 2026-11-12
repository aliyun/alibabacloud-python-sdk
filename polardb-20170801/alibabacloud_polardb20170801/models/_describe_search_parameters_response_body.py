# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeSearchParametersResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbversion: str = None,
        engine: str = None,
        request_id: str = None,
        running_parameters: main_models.DescribeSearchParametersResponseBodyRunningParameters = None,
    ):
        # The ID of the PolarDB primary cluster.
        self.dbcluster_id = dbcluster_id
        # The Search engine version. This is not the MySQL version of the primary cluster.
        self.dbversion = dbversion
        # The type of the Search engine.
        self.engine = engine
        # The request ID.
        self.request_id = request_id
        # The visible parameters and their modification status.
        self.running_parameters = running_parameters

    def validate(self):
        if self.running_parameters:
            self.running_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.running_parameters is not None:
            result['RunningParameters'] = self.running_parameters.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RunningParameters') is not None:
            temp_model = main_models.DescribeSearchParametersResponseBodyRunningParameters()
            self.running_parameters = temp_model.from_map(m.get('RunningParameters'))

        return self

class DescribeSearchParametersResponseBodyRunningParameters(DaraModel):
    def __init__(
        self,
        parameter: List[main_models.DescribeSearchParametersResponseBodyRunningParametersParameter] = None,
    ):
        # The list of parameters.
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
                temp_model = main_models.DescribeSearchParametersResponseBodyRunningParametersParameter()
                self.parameter.append(temp_model.from_map(k1))

        return self

class DescribeSearchParametersResponseBodyRunningParametersParameter(DaraModel):
    def __init__(
        self,
        checking_code: str = None,
        data_type: str = None,
        default_parameter_value: str = None,
        factor: str = None,
        force_restart: bool = None,
        is_modifiable: bool = None,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_status: str = None,
        parameter_value: str = None,
    ):
        # The value validation rule of the template. The rule can be a numeric range, an enumeration, or a regular expression, and must be interpreted in combination with the data type.
        self.checking_code = checking_code
        # The data type of the parameter value. Valid values: INT, DOUBLE, B/BYTE, MEMORY, PERCENT, TIME, BOOLEAN, and STRING. The MEMORY type supports percentages or capacities with units.
        self.data_type = data_type
        # The default value of the current active template. This value is independent of the value modified by the user.
        self.default_parameter_value = default_parameter_value
        # The divisibility factor. If the value is not zero, the numeric value parsed based on the template type must be a multiple of this factor.
        self.factor = factor
        # Specifies whether a restart is required for the parameter to take effect. The value is true for static parameters and false for dynamic parameters.
        self.force_restart = force_restart
        # Specifies whether the parameter is modifiable.
        self.is_modifiable = is_modifiable
        # The parameter description.
        self.parameter_description = parameter_description
        # The name of the parameter.
        self.parameter_name = parameter_name
        # The modification status of the parameter. A value of Normal indicates that no modifications are pending. A value of Modifying indicates that the modification task is not completed.
        self.parameter_status = parameter_status
        # The configuration value on the control plane. If a modification is in progress, the value to be applied is displayed. This value is not read from the kernel in real time.
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

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.default_parameter_value is not None:
            result['DefaultParameterValue'] = self.default_parameter_value

        if self.factor is not None:
            result['Factor'] = self.factor

        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart

        if self.is_modifiable is not None:
            result['IsModifiable'] = self.is_modifiable

        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.parameter_status is not None:
            result['ParameterStatus'] = self.parameter_status

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('DefaultParameterValue') is not None:
            self.default_parameter_value = m.get('DefaultParameterValue')

        if m.get('Factor') is not None:
            self.factor = m.get('Factor')

        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')

        if m.get('IsModifiable') is not None:
            self.is_modifiable = m.get('IsModifiable')

        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterStatus') is not None:
            self.parameter_status = m.get('ParameterStatus')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        return self

