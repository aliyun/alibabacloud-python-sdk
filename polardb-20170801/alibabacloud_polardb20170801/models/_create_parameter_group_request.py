# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateParameterGroupRequest(DaraModel):
    def __init__(
        self,
        dbtype: str = None,
        dbversion: str = None,
        owner_account: str = None,
        owner_id: int = None,
        parameter_group_desc: str = None,
        parameter_group_name: str = None,
        parameters: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The type of the database engine. Only **MySQL** is supported.
        # 
        # This parameter is required.
        self.dbtype = dbtype
        # The version of the database engine. Valid values:
        # 
        # *   **5.6**
        # *   **5.7**
        # *   **8.0**
        # 
        # This parameter is required.
        self.dbversion = dbversion
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The description of the parameter template. It must be 0 to 199 characters in length.
        self.parameter_group_desc = parameter_group_desc
        # The name of the parameter template. The name must meet the following requirements:
        # 
        # *   It can contain letters, digits, and underscores (_). It must start with a letter and cannot end with an underscore.**
        # *   It must be 8 to 64 characters in length.
        # 
        # This parameter is required.
        self.parameter_group_name = parameter_group_name
        # The JSON string that consists of parameters and values. The parameter values are strings. Example: `{"wait_timeout":"86400","innodb_old_blocks_time":"1000"}`.
        # 
        # > You can call the [DescribeParameterTemplates](https://help.aliyun.com/document_detail/207428.html) operation to query the details of all parameters in the cluster of a specified engine version, such as the parameter name and valid values.
        # 
        # This parameter is required.
        self.parameters = parameters
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query available regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
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
        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

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
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

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

