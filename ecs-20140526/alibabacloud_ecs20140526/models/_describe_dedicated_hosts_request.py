# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeDedicatedHostsRequest(DaraModel):
    def __init__(
        self,
        dedicated_host_cluster_id: str = None,
        dedicated_host_ids: str = None,
        dedicated_host_name: str = None,
        dedicated_host_type: str = None,
        lock_reason: str = None,
        max_results: int = None,
        next_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        query_inventory: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        socket_details: str = None,
        status: str = None,
        tag: List[main_models.DescribeDedicatedHostsRequestTag] = None,
        zone_id: str = None,
    ):
        # The ID of the dedicated host cluster.
        self.dedicated_host_cluster_id = dedicated_host_cluster_id
        # The IDs of dedicated hosts. You can specify up to 100 dedicated host IDs in a JSON array.
        self.dedicated_host_ids = dedicated_host_ids
        # The name of the dedicated host.
        self.dedicated_host_name = dedicated_host_name
        # The dedicated host type. Call the [`DescribeDedicatedHostTypes`](https://help.aliyun.com/document_detail/134240.html) operation to get the latest list of dedicated host types.
        self.dedicated_host_type = dedicated_host_type
        # The reason that the dedicated host is locked. Valid values:
        # 
        # - `financial`: The dedicated host is locked due to an overdue payment.
        # 
        # - `security`: The dedicated host is locked for security reasons.
        self.lock_reason = lock_reason
        # The maximum number of results to return per page.
        # 
        # Maximum value: 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The token used to retrieve the next page of results. Do not set this parameter for the first request. For subsequent requests, set this parameter to the `NextToken` value returned from the previous response.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # > This parameter is deprecated. Use `NextToken` and `MaxResults` for pagination.
        self.page_number = page_number
        # > This parameter is deprecated. Use `NextToken` and `MaxResults` for pagination.
        self.page_size = page_size
        self.query_inventory = query_inventory
        # The ID of the region where the dedicated host resides. Call the [`DescribeRegions`](https://help.aliyun.com/document_detail/25609.html) operation to get the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the dedicated host belongs. When you use this parameter to filter resources, the number of resources cannot exceed 1,000.
        # 
        # > Filtering by the default resource group is not supported.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to return socket-level capacity information. You can use the information to check the remaining vCPU and memory resources and determine whether an ECS instance of a specific instance type can be created on the dedicated host. Valid values:
        # 
        # - `true`: returns the information. Only specific dedicated host types support this feature. For more information, see [View and export information about dedicated hosts](https://help.aliyun.com/document_detail/68989.html).
        # 
        # - `false`: does not return the information.
        # 
        # >Notice: 
        # 
        # A dedicated host typically has two CPUs, which correspond to Socket 0 and Socket 1. To maximize performance, an ECS instance created on a dedicated host is allocated to a single socket and does not span sockets.
        # 
        # - If the remaining resources on a socket are sufficient for the specified ECS instance type, the instance can be created.
        # 
        # - If the remaining resources on each socket are insufficient for the specified ECS instance type, the instance cannot be created, even if the total remaining resources on both sockets are sufficient.
        self.socket_details = socket_details
        # The state of the dedicated host. Valid values:
        # 
        # - `Available`: The dedicated host is running as expected.
        # 
        # - `UnderAssessment`: The dedicated host is being assessed for physical hardware risks. The host is available but may have hardware issues that could affect its ECS instances.
        # 
        # - `PermanentFailure`: The dedicated host has a permanent failure and is unavailable.
        # 
        # - `TempUnavailable`: The dedicated host is temporarily unavailable.
        # 
        # - `Redeploying`: The dedicated host is being redeployed.
        # 
        # The default value is `Available`.
        self.status = status
        # The tags used to filter dedicated hosts. You can specify up to 20 tags.
        self.tag = tag
        # The zone ID. Call the [`DescribeZones`](https://help.aliyun.com/document_detail/25610.html) operation to get the latest list of Alibaba Cloud zones.
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_host_cluster_id is not None:
            result['DedicatedHostClusterId'] = self.dedicated_host_cluster_id

        if self.dedicated_host_ids is not None:
            result['DedicatedHostIds'] = self.dedicated_host_ids

        if self.dedicated_host_name is not None:
            result['DedicatedHostName'] = self.dedicated_host_name

        if self.dedicated_host_type is not None:
            result['DedicatedHostType'] = self.dedicated_host_type

        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_inventory is not None:
            result['QueryInventory'] = self.query_inventory

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.socket_details is not None:
            result['SocketDetails'] = self.socket_details

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostClusterId') is not None:
            self.dedicated_host_cluster_id = m.get('DedicatedHostClusterId')

        if m.get('DedicatedHostIds') is not None:
            self.dedicated_host_ids = m.get('DedicatedHostIds')

        if m.get('DedicatedHostName') is not None:
            self.dedicated_host_name = m.get('DedicatedHostName')

        if m.get('DedicatedHostType') is not None:
            self.dedicated_host_type = m.get('DedicatedHostType')

        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryInventory') is not None:
            self.query_inventory = m.get('QueryInventory')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SocketDetails') is not None:
            self.socket_details = m.get('SocketDetails')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeDedicatedHostsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDedicatedHostsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The key can be up to 128 characters long. It cannot be an empty string, start with `aliyun` or `acs:`, or contain `http://` or `https://`.
        self.key = key
        # The tag value. The value can be up to 128 characters long and cannot contain `http://` or `https://`. You can leave the value empty.
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

