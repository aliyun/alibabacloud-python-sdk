# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpcipam20230228 import models as main_models
from darabonba.model import DaraModel

class ListIpamScopesResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        ipam_scopes: List[main_models.ListIpamScopesResponseBodyIpamScopes] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # A list of IPAM scopes.
        self.ipam_scopes = ipam_scopes
        # The maximum number of entries returned per page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The token that is used for the next page of results. Valid values:
        # 
        # - If **NextToken** is empty, no next page exists.
        # 
        # - If a value is returned for **NextToken**, the value is the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ipam_scopes:
            for v1 in self.ipam_scopes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['IpamScopes'] = []
        if self.ipam_scopes is not None:
            for k1 in self.ipam_scopes:
                result['IpamScopes'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.ipam_scopes = []
        if m.get('IpamScopes') is not None:
            for k1 in m.get('IpamScopes'):
                temp_model = main_models.ListIpamScopesResponseBodyIpamScopes()
                self.ipam_scopes.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIpamScopesResponseBodyIpamScopes(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        ipam_id: str = None,
        ipam_scope_description: str = None,
        ipam_scope_id: str = None,
        ipam_scope_name: str = None,
        ipam_scope_type: str = None,
        is_default: bool = None,
        owner_id: int = None,
        pool_count: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.ListIpamScopesResponseBodyIpamScopesTags] = None,
    ):
        # The time when the IPAM scope was created.
        self.create_time = create_time
        # The instance ID of the IPAM.
        self.ipam_id = ipam_id
        # The description of the IPAM scope.
        self.ipam_scope_description = ipam_scope_description
        # The instance ID of the IPAM scope.
        self.ipam_scope_id = ipam_scope_id
        # The name of the IPAM scope.
        self.ipam_scope_name = ipam_scope_name
        # The type of the IPAM scope. Valid values:
        # 
        # - **public**: the public scope.
        # 
        # - **private**: the private scope.
        self.ipam_scope_type = ipam_scope_type
        # Indicates whether the scope is the default scope. Valid values:
        # 
        # - **true**: The scope is the default scope.
        # 
        # - **false**: The scope is not the default scope.
        self.is_default = is_default
        # The ID of the Alibaba Cloud account to which the IPAM scope belongs.
        self.owner_id = owner_id
        # The number of IPAM pools in the IPAM scope.
        self.pool_count = pool_count
        # The region ID of the IPAM scope.
        self.region_id = region_id
        # The ID of the resource group to which the IPAM scope belongs.
        self.resource_group_id = resource_group_id
        # The status of the IPAM scope. Valid values:
        # 
        # - **Creating**: The IPAM scope is being created.
        # 
        # - **Created**: The IPAM scope is created.
        # 
        # - **Deleting**: The IPAM scope is being deleted.
        # 
        # - **Deleted**: The IPAM scope is deleted.
        self.status = status
        # The tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id

        if self.ipam_scope_description is not None:
            result['IpamScopeDescription'] = self.ipam_scope_description

        if self.ipam_scope_id is not None:
            result['IpamScopeId'] = self.ipam_scope_id

        if self.ipam_scope_name is not None:
            result['IpamScopeName'] = self.ipam_scope_name

        if self.ipam_scope_type is not None:
            result['IpamScopeType'] = self.ipam_scope_type

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pool_count is not None:
            result['PoolCount'] = self.pool_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')

        if m.get('IpamScopeDescription') is not None:
            self.ipam_scope_description = m.get('IpamScopeDescription')

        if m.get('IpamScopeId') is not None:
            self.ipam_scope_id = m.get('IpamScopeId')

        if m.get('IpamScopeName') is not None:
            self.ipam_scope_name = m.get('IpamScopeName')

        if m.get('IpamScopeType') is not None:
            self.ipam_scope_type = m.get('IpamScopeType')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PoolCount') is not None:
            self.pool_count = m.get('PoolCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListIpamScopesResponseBodyIpamScopesTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListIpamScopesResponseBodyIpamScopesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

