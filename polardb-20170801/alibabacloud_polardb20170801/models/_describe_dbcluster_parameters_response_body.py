# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterParametersResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dbtype: str = None,
        dbversion: str = None,
        engine: str = None,
        parameter_numbers: str = None,
        parameters: main_models.DescribeDBClusterParametersResponseBodyParameters = None,
        request_id: str = None,
        running_parameters: main_models.DescribeDBClusterParametersResponseBodyRunningParameters = None,
    ):
        # The ID of the cluster.
        self.dbcluster_id = dbcluster_id
        # The database engine that the clusters runs. Valid values:
        # 
        # *   **MySQL**
        # *   **PostgreSQL**
        # *   **Oracle**
        self.dbtype = dbtype
        # The version of the database engine. 
        # 
        # - Valid values for the MySQL database engine:   
        #   - **5.6**
        #   - **5.7**
        #   - **8.0**
        # - Valid value for the PostgreSQL database engine:    
        #   - **11**
        #   - **14**
        # - Valid value for the Oracle database engine:  **11**
        self.dbversion = dbversion
        # The cluster engine.
        self.engine = engine
        # The number of parameters.
        self.parameter_numbers = parameter_numbers
        # A comparison of parameters between the source RDS instance and the destination PolarDB cluster.
        self.parameters = parameters
        # The ID of the request.
        self.request_id = request_id
        # The parameters of the PolarDB cluster.
        self.running_parameters = running_parameters

    def validate(self):
        if self.parameters:
            self.parameters.validate()
        if self.running_parameters:
            self.running_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.parameter_numbers is not None:
            result['ParameterNumbers'] = self.parameter_numbers

        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.running_parameters is not None:
            result['RunningParameters'] = self.running_parameters.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('ParameterNumbers') is not None:
            self.parameter_numbers = m.get('ParameterNumbers')

        if m.get('Parameters') is not None:
            temp_model = main_models.DescribeDBClusterParametersResponseBodyParameters()
            self.parameters = temp_model.from_map(m.get('Parameters'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RunningParameters') is not None:
            temp_model = main_models.DescribeDBClusterParametersResponseBodyRunningParameters()
            self.running_parameters = temp_model.from_map(m.get('RunningParameters'))

        return self

class DescribeDBClusterParametersResponseBodyRunningParameters(DaraModel):
    def __init__(
        self,
        parameter: List[main_models.DescribeDBClusterParametersResponseBodyRunningParametersParameter] = None,
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
                temp_model = main_models.DescribeDBClusterParametersResponseBodyRunningParametersParameter()
                self.parameter.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterParametersResponseBodyRunningParametersParameter(DaraModel):
    def __init__(
        self,
        checking_code: str = None,
        data_type: str = None,
        default_parameter_value: str = None,
        factor: str = None,
        force_restart: bool = None,
        is_modifiable: bool = None,
        is_node_available: str = None,
        param_rely_rule: str = None,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_status: str = None,
        parameter_value: str = None,
    ):
        # The valid values of the parameter.
        self.checking_code = checking_code
        # The data type of the parameter value. Valid values:
        # 
        # *   **INT**
        # *   **STRING**
        # *   **B**
        self.data_type = data_type
        # The default value of the parameter.
        self.default_parameter_value = default_parameter_value
        # A divisor of the parameter. For a parameter of the integer or byte type, the valid values must be a multiple of Factor unless you set Factor to 0.
        self.factor = factor
        # Indicates whether a cluster restart is required for the parameter modification to take effect. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.force_restart = force_restart
        # Indicates whether the parameter can be modified. Valid values:
        # 
        # *   **false**
        # *   **true**
        self.is_modifiable = is_modifiable
        # Indicates whether the parameter is a global parameter. Valid values:
        # 
        # *   **0**: The parameter is a global parameter. The modified parameter value is synchronized to other nodes.
        # *   **1**: The parameter is not a global parameter. You can specify the nodes to which the modified parameter value can be synchronized.
        self.is_node_available = is_node_available
        # The dependencies of the parameter.
        self.param_rely_rule = param_rely_rule
        # The description of the parameter.
        self.parameter_description = parameter_description
        # The name of the parameter.
        self.parameter_name = parameter_name
        # The status of the parameter. Valid values:
        # 
        # *   **Normal**
        # *   **Modifying**
        self.parameter_status = parameter_status
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

        if self.is_node_available is not None:
            result['IsNodeAvailable'] = self.is_node_available

        if self.param_rely_rule is not None:
            result['ParamRelyRule'] = self.param_rely_rule

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

        if m.get('IsNodeAvailable') is not None:
            self.is_node_available = m.get('IsNodeAvailable')

        if m.get('ParamRelyRule') is not None:
            self.param_rely_rule = m.get('ParamRelyRule')

        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterStatus') is not None:
            self.parameter_status = m.get('ParameterStatus')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        return self

class DescribeDBClusterParametersResponseBodyParameters(DaraModel):
    def __init__(
        self,
        parameters: List[main_models.DescribeDBClusterParametersResponseBodyParametersParameters] = None,
    ):
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
        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.DescribeDBClusterParametersResponseBodyParametersParameters()
                self.parameters.append(temp_model.from_map(k1))

        return self

class DescribeDBClusterParametersResponseBodyParametersParameters(DaraModel):
    def __init__(
        self,
        is_equal: str = None,
        is_instance_polar_dbkey: str = None,
        is_instance_rds_key: str = None,
        is_polar_dbkey: str = None,
        is_rds_key: str = None,
        dist_parameter_description: str = None,
        dist_parameter_name: str = None,
        dist_parameter_optional: str = None,
        dist_parameter_value: str = None,
        rds_parameter_description: str = None,
        rds_parameter_name: str = None,
        rds_parameter_optional: str = None,
        rds_parameter_value: str = None,
    ):
        # Indicates whether the source and current parameters have the same value.
        self.is_equal = is_equal
        # Indicate whether the parameter is a primary parameter of the destination cluster. Valid values:
        # 
        # *   **1**: The parameter is a primary parameter of the destination cluster.
        # *   **0**: The parameter is not a primary parameter of the destination cluster.
        self.is_instance_polar_dbkey = is_instance_polar_dbkey
        # Indicate whether the parameter is a primary parameter of the source instance. Valid values:
        # 
        # *   **1**: The parameter is a primary parameter of the source instance.
        # *   **0**: The parameter is not a primary parameter of the source instance.
        self.is_instance_rds_key = is_instance_rds_key
        # Indicate whether the parameter is a primary parameter of the destination cluster. Valid values:
        # 
        # *   **1**: The parameter is a primary parameter of the destination cluster.
        # *   **0**: The parameter is not a primary parameter of the destination cluster.
        self.is_polar_dbkey = is_polar_dbkey
        # Indicate whether the parameter is a primary parameter of the source instance. Valid values:
        # 
        # *   **1**: The parameter is a primary parameter of the source instance.
        # *   **0**: The parameter is not a primary parameter of the source instance.
        self.is_rds_key = is_rds_key
        # The description of the parameter of the destination cluster.
        self.dist_parameter_description = dist_parameter_description
        # The name of the parameter of the destination cluster.
        self.dist_parameter_name = dist_parameter_name
        # The valid values of the parameter of the destination cluster.
        self.dist_parameter_optional = dist_parameter_optional
        # The value of the parameter of the destination cluster.
        self.dist_parameter_value = dist_parameter_value
        # The description of the parameter of the source instance.
        self.rds_parameter_description = rds_parameter_description
        # The name of the parameter of the source instance.
        self.rds_parameter_name = rds_parameter_name
        # The valid values of the parameter of the source instance.
        self.rds_parameter_optional = rds_parameter_optional
        # The value of the parameter of the source instance.
        self.rds_parameter_value = rds_parameter_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_equal is not None:
            result['IsEqual'] = self.is_equal

        if self.is_instance_polar_dbkey is not None:
            result['IsInstancePolarDBKey'] = self.is_instance_polar_dbkey

        if self.is_instance_rds_key is not None:
            result['IsInstanceRdsKey'] = self.is_instance_rds_key

        if self.is_polar_dbkey is not None:
            result['IsPolarDBKey'] = self.is_polar_dbkey

        if self.is_rds_key is not None:
            result['IsRdsKey'] = self.is_rds_key

        if self.dist_parameter_description is not None:
            result['distParameterDescription'] = self.dist_parameter_description

        if self.dist_parameter_name is not None:
            result['distParameterName'] = self.dist_parameter_name

        if self.dist_parameter_optional is not None:
            result['distParameterOptional'] = self.dist_parameter_optional

        if self.dist_parameter_value is not None:
            result['distParameterValue'] = self.dist_parameter_value

        if self.rds_parameter_description is not None:
            result['rdsParameterDescription'] = self.rds_parameter_description

        if self.rds_parameter_name is not None:
            result['rdsParameterName'] = self.rds_parameter_name

        if self.rds_parameter_optional is not None:
            result['rdsParameterOptional'] = self.rds_parameter_optional

        if self.rds_parameter_value is not None:
            result['rdsParameterValue'] = self.rds_parameter_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsEqual') is not None:
            self.is_equal = m.get('IsEqual')

        if m.get('IsInstancePolarDBKey') is not None:
            self.is_instance_polar_dbkey = m.get('IsInstancePolarDBKey')

        if m.get('IsInstanceRdsKey') is not None:
            self.is_instance_rds_key = m.get('IsInstanceRdsKey')

        if m.get('IsPolarDBKey') is not None:
            self.is_polar_dbkey = m.get('IsPolarDBKey')

        if m.get('IsRdsKey') is not None:
            self.is_rds_key = m.get('IsRdsKey')

        if m.get('distParameterDescription') is not None:
            self.dist_parameter_description = m.get('distParameterDescription')

        if m.get('distParameterName') is not None:
            self.dist_parameter_name = m.get('distParameterName')

        if m.get('distParameterOptional') is not None:
            self.dist_parameter_optional = m.get('distParameterOptional')

        if m.get('distParameterValue') is not None:
            self.dist_parameter_value = m.get('distParameterValue')

        if m.get('rdsParameterDescription') is not None:
            self.rds_parameter_description = m.get('rdsParameterDescription')

        if m.get('rdsParameterName') is not None:
            self.rds_parameter_name = m.get('rdsParameterName')

        if m.get('rdsParameterOptional') is not None:
            self.rds_parameter_optional = m.get('rdsParameterOptional')

        if m.get('rdsParameterValue') is not None:
            self.rds_parameter_value = m.get('rdsParameterValue')

        return self

