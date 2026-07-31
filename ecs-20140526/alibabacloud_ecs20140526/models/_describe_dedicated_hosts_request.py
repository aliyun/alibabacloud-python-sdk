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
        # The list of dedicated host IDs. You can specify up to 100 IDs, separated by commas (,).
        self.dedicated_host_ids = dedicated_host_ids
        # The name of the dedicated host.
        self.dedicated_host_name = dedicated_host_name
        # The type of the dedicated host. You can call [DescribeDedicatedHostTypes](https://help.aliyun.com/document_detail/134240.html) to query the most recent list of dedicated host types.
        self.dedicated_host_type = dedicated_host_type
        # The reason why the dedicated host is locked. Valid values:
        # - financial: The dedicated host is locked due to an overdue payment.
        # - security: The dedicated host is locked for security reasons.
        self.lock_reason = lock_reason
        # The maximum number of entries per page for a paging query. If you set this parameter, it indicates that you are using the MaxResults and NextToken paging method.
        # 
        # Maximum value: 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # The pagination token. Set this parameter to the NextToken value returned in the previous call. You do not need to set this parameter for the first request.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # > This parameter is about to go offline. Use NextToken and MaxResults to perform paging query operations.
        self.page_number = page_number
        # > This parameter is about to go offline. Use NextToken and MaxResults to perform paging query operations.
        self.page_size = page_size
        self.query_inventory = query_inventory
        # The region ID of the dedicated host. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the dedicated host belongs. When you use this parameter to filter resources, the resource count cannot exceed 1000.
        # 
        # > Filtering by the default resource group is not supported.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to display socket-level capacity information. You can use socket-level capacity information to view remaining resources (vCPU, memory usage, remaining capacity, and total capacity) to determine whether an ECS instance of a specific instance type can be created. Valid values:
        # 
        # - true: Display socket-level capacity information. Only specific dedicated host types support displaying socket-level resource information. For more information, see [View and export DDH information](https://help.aliyun.com/document_detail/68989.html).
        # - false: Do not display socket-level capacity information.
        # 
        # >Notice: 
        # 
        # Each dedicated host typically has two CPUs, numbered Socket 0 and Socket 1. On a dedicated host, ECS instances are not created across sockets to ensure maximum performance. An ECS instance is created based on a single socket only.
        # 
        # - If the remaining computing resources of one socket are greater than or equal to the instance type to be created, the ECS instance is created.
        # - If the remaining computing resources of each socket are less than the instance type to be created, the ECS instance fails to be created, even if the combined remaining resources of both sockets exceed the instance type requirements.
        # </notice>
        self.socket_details = socket_details
        # The usage status of the dedicated host. Valid values:
        # 
        # - Available: The dedicated host is running normally.
        # 
        # - UnderAssessment: The physical machine is at risk. The physical machine is available but may cause issues for ECS instances on the dedicated host.
        # 
        # - PermanentFailure: The dedicated host has a permanent failure and is unavailable.
        # 
        # - TempUnavailable: The dedicated host is temporarily unavailable.
        # 
        # - Redeploying: The dedicated host is being restored.
        # 
        # Default value: Available.
        self.status = status
        # The list of tags. Valid values of N: 0 to 20.
        self.tag = tag
        # The zone ID. You can call [DescribeZones](https://help.aliyun.com/document_detail/25610.html) to query the most recent zone list.
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
        # The tag key of the dedicated host. If you specify this parameter, the value cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the dedicated host. If you specify this parameter, the value can be an empty string. The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`.
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

