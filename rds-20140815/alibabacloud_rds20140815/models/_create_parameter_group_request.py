# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateParameterGroupRequest(DaraModel):
    def __init__(
        self,
        engine: str = None,
        engine_version: str = None,
        owner_id: int = None,
        parameter_group_desc: str = None,
        parameter_group_name: str = None,
        parameters: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The database engine. Valid values:
        # 
        # *   **mysql**
        # *   **PostgreSQL**
        # 
        # This parameter is required.
        self.engine = engine
        # The database engine version of the instance.
        # 
        # *   If the instance runs MySQL, the instance must run one of the following MySQL versions:
        # 
        #     *   **5.6**
        #     *   **5.7**
        #     *   **8.0**
        # 
        # *   If the instance runs PostgreSQL, the instance must run one of the following PostgreSQL versions:
        # 
        #     *   **10.0**
        #     *   **11.0**
        #     *   **12.0**
        #     *   **13.0**
        #     *   **14.0**
        #     *   **15.0**
        # 
        # This parameter is required.
        self.engine_version = engine_version
        self.owner_id = owner_id
        # The description of the parameter template. The value can be up to 200 characters in length.
        self.parameter_group_desc = parameter_group_desc
        # The name of the parameter template.
        # 
        # *   The value must start with a letter and can contain letters, digits, periods (.), and underscores (_).
        # *   The value can be 8 to 64 characters in length.
        # 
        # This parameter is required.
        self.parameter_group_name = parameter_group_name
        # A JSON string that consists of parameters and their values in the parameter template. Format: {"Parameter 1":"Value of Parameter 1","Parameter 2":"Value of Parameter 2"...}. For more information about the parameters that can be modified, see [Modify the parameters of an ApsaraDB RDS for MySQL instance](https://help.aliyun.com/document_detail/96063.html) or [Modify the parameters of an ApsaraDB RDS for PostgreSQL instance](https://help.aliyun.com/document_detail/96751.html).
        # 
        # This parameter is required.
        self.parameters = parameters
        # The region ID of the parameter template. You can call the DescribeRegions operation to query the most recent zone list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID. You can call the DescribeDBInstanceAttribute operation to obtain the resource group ID.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.parameter_group_desc is not None:
            result['ParameterGroupDesc'] = self.parameter_group_desc

        if self.parameter_group_name is not None:
            result['ParameterGroupName'] = self.parameter_group_name

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ParameterGroupDesc') is not None:
            self.parameter_group_desc = m.get('ParameterGroupDesc')

        if m.get('ParameterGroupName') is not None:
            self.parameter_group_name = m.get('ParameterGroupName')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

