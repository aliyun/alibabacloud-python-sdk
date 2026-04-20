# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpcipam20230228 import models as main_models
from darabonba.model import DaraModel

class ListIpamPoolsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        ipam_pools: List[main_models.ListIpamPoolsResponseBodyIpamPools] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries returned.
        self.count = count
        # The IPAM pools.
        self.ipam_pools = ipam_pools
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.ipam_pools:
            for v1 in self.ipam_pools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['IpamPools'] = []
        if self.ipam_pools is not None:
            for k1 in self.ipam_pools:
                result['IpamPools'].append(k1.to_map() if k1 else None)

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

        self.ipam_pools = []
        if m.get('IpamPools') is not None:
            for k1 in m.get('IpamPools'):
                temp_model = main_models.ListIpamPoolsResponseBodyIpamPools()
                self.ipam_pools.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListIpamPoolsResponseBodyIpamPools(DaraModel):
    def __init__(
        self,
        allocation_default_cidr_mask: int = None,
        allocation_max_cidr_mask: int = None,
        allocation_min_cidr_mask: int = None,
        auto_import: bool = None,
        cidrs: List[str] = None,
        create_time: str = None,
        has_sub_pool: bool = None,
        ip_version: str = None,
        ipam_id: str = None,
        ipam_pool_description: str = None,
        ipam_pool_id: str = None,
        ipam_pool_name: str = None,
        ipam_region_id: str = None,
        ipam_scope_id: str = None,
        ipam_scope_type: str = None,
        ipv_6isp: str = None,
        is_shared: bool = None,
        owner_id: int = None,
        pool_depth: int = None,
        pool_region_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        source_ipam_pool_id: str = None,
        status: str = None,
        tags: List[main_models.ListIpamPoolsResponseBodyIpamPoolsTags] = None,
    ):
        # The default network mask assigned to the IPAM pool.
        # 
        # An IPv4 mask must be **0 to 32** bits in length.
        self.allocation_default_cidr_mask = allocation_default_cidr_mask
        # The maximum network mask assigned to the IPAM pool.
        # 
        # An IPv4 mask must be **0 to 32** bits in length.
        self.allocation_max_cidr_mask = allocation_max_cidr_mask
        # The minimum network mask assigned to the IPAM pool.
        # 
        # An IPv4 mask must be **0 to 32** bits in length.
        self.allocation_min_cidr_mask = allocation_min_cidr_mask
        # Whether the pool has the auto-import feature enabled.
        self.auto_import = auto_import
        self.cidrs = cidrs
        # The time when the IPAM pool was created.
        self.create_time = create_time
        # Indicates whether the pool is a subpool. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.has_sub_pool = has_sub_pool
        # The IP version. Only **IPv4** may be returned.
        self.ip_version = ip_version
        # The ID of the IPAM.
        self.ipam_id = ipam_id
        # The description of the IPAM pool.
        self.ipam_pool_description = ipam_pool_description
        # The ID of the IPAM pool.
        self.ipam_pool_id = ipam_pool_id
        # The name of the IPAM pool.
        self.ipam_pool_name = ipam_pool_name
        # The ID of the region where the IPAM to which the IPAM pool belongs is hosted.
        self.ipam_region_id = ipam_region_id
        # The ID of the IPAM scope.
        self.ipam_scope_id = ipam_scope_id
        # The type of the IPAM scope. Valid values:
        # 
        # *   **public**
        # *   **private**
        self.ipam_scope_type = ipam_scope_type
        self.ipv_6isp = ipv_6isp
        # Whether it is a shared pool.
        self.is_shared = is_shared
        # The Alibaba Cloud account of the owner for the IPAM pool.
        self.owner_id = owner_id
        # The depth of the IPAM pool. Valid values: **0 to 10**.
        self.pool_depth = pool_depth
        # The effective region of the IPAM pool. The ID of the effective region for the IPAM pool.
        self.pool_region_id = pool_region_id
        # The ID of the region where the operation is called.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The ID of the source IPAM pool.
        self.source_ipam_pool_id = source_ipam_pool_id
        # The status of the IPAM pool. Valid values:
        # 
        # *   **Creating**
        # *   **Created**: indicates that the creation is complete.
        # *   **Modifying**
        # *   **Deleting**
        # *   **Deleted**
        self.status = status
        # The tag list.
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
        if self.allocation_default_cidr_mask is not None:
            result['AllocationDefaultCidrMask'] = self.allocation_default_cidr_mask

        if self.allocation_max_cidr_mask is not None:
            result['AllocationMaxCidrMask'] = self.allocation_max_cidr_mask

        if self.allocation_min_cidr_mask is not None:
            result['AllocationMinCidrMask'] = self.allocation_min_cidr_mask

        if self.auto_import is not None:
            result['AutoImport'] = self.auto_import

        if self.cidrs is not None:
            result['Cidrs'] = self.cidrs

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.has_sub_pool is not None:
            result['HasSubPool'] = self.has_sub_pool

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.ipam_id is not None:
            result['IpamId'] = self.ipam_id

        if self.ipam_pool_description is not None:
            result['IpamPoolDescription'] = self.ipam_pool_description

        if self.ipam_pool_id is not None:
            result['IpamPoolId'] = self.ipam_pool_id

        if self.ipam_pool_name is not None:
            result['IpamPoolName'] = self.ipam_pool_name

        if self.ipam_region_id is not None:
            result['IpamRegionId'] = self.ipam_region_id

        if self.ipam_scope_id is not None:
            result['IpamScopeId'] = self.ipam_scope_id

        if self.ipam_scope_type is not None:
            result['IpamScopeType'] = self.ipam_scope_type

        if self.ipv_6isp is not None:
            result['Ipv6Isp'] = self.ipv_6isp

        if self.is_shared is not None:
            result['IsShared'] = self.is_shared

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pool_depth is not None:
            result['PoolDepth'] = self.pool_depth

        if self.pool_region_id is not None:
            result['PoolRegionId'] = self.pool_region_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source_ipam_pool_id is not None:
            result['SourceIpamPoolId'] = self.source_ipam_pool_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationDefaultCidrMask') is not None:
            self.allocation_default_cidr_mask = m.get('AllocationDefaultCidrMask')

        if m.get('AllocationMaxCidrMask') is not None:
            self.allocation_max_cidr_mask = m.get('AllocationMaxCidrMask')

        if m.get('AllocationMinCidrMask') is not None:
            self.allocation_min_cidr_mask = m.get('AllocationMinCidrMask')

        if m.get('AutoImport') is not None:
            self.auto_import = m.get('AutoImport')

        if m.get('Cidrs') is not None:
            self.cidrs = m.get('Cidrs')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('HasSubPool') is not None:
            self.has_sub_pool = m.get('HasSubPool')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('IpamId') is not None:
            self.ipam_id = m.get('IpamId')

        if m.get('IpamPoolDescription') is not None:
            self.ipam_pool_description = m.get('IpamPoolDescription')

        if m.get('IpamPoolId') is not None:
            self.ipam_pool_id = m.get('IpamPoolId')

        if m.get('IpamPoolName') is not None:
            self.ipam_pool_name = m.get('IpamPoolName')

        if m.get('IpamRegionId') is not None:
            self.ipam_region_id = m.get('IpamRegionId')

        if m.get('IpamScopeId') is not None:
            self.ipam_scope_id = m.get('IpamScopeId')

        if m.get('IpamScopeType') is not None:
            self.ipam_scope_type = m.get('IpamScopeType')

        if m.get('Ipv6Isp') is not None:
            self.ipv_6isp = m.get('Ipv6Isp')

        if m.get('IsShared') is not None:
            self.is_shared = m.get('IsShared')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PoolDepth') is not None:
            self.pool_depth = m.get('PoolDepth')

        if m.get('PoolRegionId') is not None:
            self.pool_region_id = m.get('PoolRegionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceIpamPoolId') is not None:
            self.source_ipam_pool_id = m.get('SourceIpamPoolId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListIpamPoolsResponseBodyIpamPoolsTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListIpamPoolsResponseBodyIpamPoolsTags(DaraModel):
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

