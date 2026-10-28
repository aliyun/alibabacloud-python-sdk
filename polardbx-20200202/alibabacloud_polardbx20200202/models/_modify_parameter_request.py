# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyParameterRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dbinstance_id: str = None,
        param_level: str = None,
        parameter_group_id: str = None,
        parameters: str = None,
        region_id: str = None,
    ):
        # The client token. It can be any unique string.
        self.client_token = client_token
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The parameter type. Valid values:
        # 
        # - **compute**: compute layer parameters
        # - **storage**: storage layer parameters
        self.param_level = param_level
        # The parameter template ID.
        # > You can call the [DescribeParameterGroups](https://help.aliyun.com/document_detail/207178.html) operation to query the details of all parameter templates in the specified region, including the parameter template IDs.
        self.parameter_group_id = parameter_group_id
        # The parameters in JSON format. The key represents the parameter name, and the value represents the parameter value. Modifiable parameters are dynamically added or removed. Call the [DescribeParameterTemplates](https://help.aliyun.com/document_detail/196856.html) operation to obtain the list of modifiable parameters. You can specify multiple parameters at a time.
        self.parameters = parameters
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.param_level is not None:
            result['ParamLevel'] = self.param_level

        if self.parameter_group_id is not None:
            result['ParameterGroupId'] = self.parameter_group_id

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('ParamLevel') is not None:
            self.param_level = m.get('ParamLevel')

        if m.get('ParameterGroupId') is not None:
            self.parameter_group_id = m.get('ParameterGroupId')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

