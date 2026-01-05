# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBNodesParametersResponseBody(DaraModel):
    def __init__(
        self,
        dbnode_ids: List[main_models.DescribeDBNodesParametersResponseBodyDBNodeIds] = None,
        dbtype: str = None,
        dbversion: str = None,
        engine: str = None,
        request_id: str = None,
    ):
        # The IDs of the nodes.
        self.dbnode_ids = dbnode_ids
        # The type of the database engine. Set the value to **MySQL**.
        self.dbtype = dbtype
        # The version of the MySQL database engine. Valid values:
        # 
        # *   **5.6**
        # *   **5.7**
        # *   **8.0**
        self.dbversion = dbversion
        # The cluster engine.
        self.engine = engine
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dbnode_ids:
            for v1 in self.dbnode_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBNodeIds'] = []
        if self.dbnode_ids is not None:
            for k1 in self.dbnode_ids:
                result['DBNodeIds'].append(k1.to_map() if k1 else None)

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbnode_ids = []
        if m.get('DBNodeIds') is not None:
            for k1 in m.get('DBNodeIds'):
                temp_model = main_models.DescribeDBNodesParametersResponseBodyDBNodeIds()
                self.dbnode_ids.append(temp_model.from_map(k1))

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBNodesParametersResponseBodyDBNodeIds(DaraModel):
    def __init__(
        self,
        dbnode_id: str = None,
        running_parameters: List[main_models.DescribeDBNodesParametersResponseBodyDBNodeIdsRunningParameters] = None,
    ):
        # The ID of the node.
        self.dbnode_id = dbnode_id
        # The parameters of the current node.
        self.running_parameters = running_parameters

    def validate(self):
        if self.running_parameters:
            for v1 in self.running_parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbnode_id is not None:
            result['DBNodeId'] = self.dbnode_id

        result['RunningParameters'] = []
        if self.running_parameters is not None:
            for k1 in self.running_parameters:
                result['RunningParameters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBNodeId') is not None:
            self.dbnode_id = m.get('DBNodeId')

        self.running_parameters = []
        if m.get('RunningParameters') is not None:
            for k1 in m.get('RunningParameters'):
                temp_model = main_models.DescribeDBNodesParametersResponseBodyDBNodeIdsRunningParameters()
                self.running_parameters.append(temp_model.from_map(k1))

        return self

class DescribeDBNodesParametersResponseBodyDBNodeIdsRunningParameters(DaraModel):
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
        # Indicates whether a cluster restart is required to allow the parameter modification to take effect. Valid values:
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
        # *   **0**: yes. The modified parameter value is synchronized to other nodes.
        # *   **1**: no. You can customize the nodes to which the modified parameter value can be synchronized to.
        self.is_node_available = is_node_available
        # The dependencies of the parameter.
        self.param_rely_rule = param_rely_rule
        # The description of the parameter.
        self.parameter_description = parameter_description
        # The name of the parameter.
        self.parameter_name = parameter_name
        # The status of the parameter. Valid values:
        # 
        # *   **normal**
        # *   **modifying**
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

