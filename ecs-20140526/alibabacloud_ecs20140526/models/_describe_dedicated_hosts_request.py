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
        need_host_detail: str = None,
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
        # The IDs of the dedicated hosts. You can specify up to 100 IDs. Separate multiple IDs with commas (,).
        self.dedicated_host_ids = dedicated_host_ids
        # The name of the dedicated host.
        self.dedicated_host_name = dedicated_host_name
        # The type of the dedicated host. You can call the [DescribeDedicatedHostTypes](https://help.aliyun.com/document_detail/134240.html) operation to query the most recent dedicated host type list.
        self.dedicated_host_type = dedicated_host_type
        # The reason why the dedicated host is locked. Valid values:
        # - financial: The dedicated host is locked due to overdue payments.
        # - security: The dedicated host is locked due to security reasons.
        self.lock_reason = lock_reason
        # The maximum number of entries per page for a paged query. If you specify this parameter, the query uses the combination of MaxResults and NextToken for pagination.
        # 
        # Maximum value: 100.
        # 
        # Default value: 10.
        self.max_results = max_results
        # Specifies whether to return the details of the dedicated host.
        self.need_host_detail = need_host_detail
        # The query token. Set the value to the NextToken value returned in the previous call to this operation. You do not need to specify this parameter when you call this operation for the first time.
        self.next_token = next_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # > This parameter will be deprecated soon. We recommend that you use NextToken and MaxResults for pagination.
        self.page_number = page_number
        # > This parameter will be deprecated soon. We recommend that you use NextToken and MaxResults for pagination.
        self.page_size = page_size
        # Specifies whether to query the inventory information of the dedicated host.
        self.query_inventory = query_inventory
        # The region ID of the dedicated host. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the dedicated host belongs. When you use this parameter to filter resources, the resource count cannot exceed 1,000.
        # 
        # > Filtering by the default resource group is not supported.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether to display socket-level capacity information. You can view the remaining resource information (vCPU and memory usage, remaining capacity, and total capacity) at the socket level to determine whether ECS instances of the corresponding type can be created. Valid values:
        # 
        # - true: Display the information. Only dedicated hosts of specific types support displaying socket-level resource information. For more information, see [View and export dedicated host information](https://help.aliyun.com/document_detail/68989.html).
        # - false: Do not display the information.
        # 
        # >Notice: 
        # 
        # Generally, each dedicated host has two CPUs, and the ID of each CPU is Socket 0 or Socket 1. On an exclusive dedicated host, to ensure that the ECS instances on the dedicated host deliver maximum performance, ECS instances are not created across sockets. This means that an ECS instance is created based on only one socket.
        # 
        # - If the remaining computing resources of one socket are greater than or equal to the resources required by the ECS instance type to be created, the ECS instance is created.
        # - If the remaining computing resources of each socket are less than the resources required by the ECS instance type to be created, the ECS instance fails to be created. Even if the total remaining resources of the two sockets on the dedicated host are greater than the resources required by the ECS instance type, the ECS instance still cannot be created.
        # </notice>
        self.socket_details = socket_details
        # The status of the dedicated host. Valid values:
        # 
        # - Available: The dedicated host is running. This is the normal status of a dedicated host.
        # 
        # - UnderAssessment: The physical machine has risks. The physical machine is available during the fault incubation period, but issues may occur on the ECS instances on the dedicated host.
        # 
        # - PermanentFailure: A permanent failure occurred. The dedicated host is unavailable.
        # 
        # - TempUnavailable: The dedicated host is temporarily unavailable.
        # 
        # - Redeploying: The dedicated host is being recovered.
        # 
        # Default value: Available.
        self.status = status
        # The list of tags. You can specify 0 to 20 tags.
        self.tag = tag
        # The zone ID. You can call the [DescribeZones](https://help.aliyun.com/document_detail/25610.html) operation to query the most recent zone list.
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

        if self.need_host_detail is not None:
            result['NeedHostDetail'] = self.need_host_detail

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

        if m.get('NeedHostDetail') is not None:
            self.need_host_detail = m.get('NeedHostDetail')

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
        # The tag key of the dedicated host. If you specify this parameter, it cannot be an empty string. The tag key can be up to 128 characters in length, and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the dedicated host. If you specify this parameter, it can be an empty string. The tag value can be up to 128 characters in length, and cannot contain `http://` or `https://`.
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

