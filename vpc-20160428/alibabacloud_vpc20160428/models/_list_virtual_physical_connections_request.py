# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListVirtualPhysicalConnectionsRequest(DaraModel):
    def __init__(
        self,
        is_confirmed: bool = None,
        max_results: int = None,
        next_token: str = None,
        physical_connection_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: List[main_models.ListVirtualPhysicalConnectionsRequestTags] = None,
        virtual_physical_connection_ali_uids: List[str] = None,
        virtual_physical_connection_business_status: str = None,
        virtual_physical_connection_ids: List[str] = None,
        virtual_physical_connection_statuses: List[str] = None,
        vlan_ids: List[str] = None,
    ):
        # Specifies whether the shared Express Connect circuits have been confirmed and accepted by the tenant. Valid values:
        # 
        # - **true**: Yes.
        # - **false**: No.
        self.is_confirmed = is_confirmed
        # The number of entries per page when you query results by page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results
        # Specifies whether a next query token exists. Valid values:
        # - You do not need to specify this parameter for the first query or if no next query exists.
        # - If a next query exists, set this parameter to the NextToken value returned by the previous API call.
        self.next_token = next_token
        # The ID of the Express Connect circuit associated with the shared Express Connect circuits.
        # 
        # In the following content of this topic, the Express Connect circuit associated with the shared Express Connect circuits is referred to as the Express Connect circuit, to distinguish it from the shared Express Connect circuits.
        self.physical_connection_id = physical_connection_id
        # The region ID of the shared Express Connect circuits.
        # 
        # You can invoke the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the shared Express Connect circuits belong.
        self.resource_group_id = resource_group_id
        # The tag list.
        self.tags = tags
        # The Alibaba Cloud account information of the shared Express Connect circuits owner.
        self.virtual_physical_connection_ali_uids = virtual_physical_connection_ali_uids
        # The business status of the shared Express Connect circuits. Valid values:
        # 
        # - **Normal**: Normal.
        # - **FinancialLocked**: Locked due to overdue payment.
        # - **SecurityLocked**: Locked for security reasons.
        self.virtual_physical_connection_business_status = virtual_physical_connection_business_status
        # The shared Express Connect circuits information.
        self.virtual_physical_connection_ids = virtual_physical_connection_ids
        # The business status information of the shared Express Connect circuits.
        self.virtual_physical_connection_statuses = virtual_physical_connection_statuses
        # The VLAN ID of the shared Express Connect circuits.
        self.vlan_ids = vlan_ids

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
        if self.is_confirmed is not None:
            result['IsConfirmed'] = self.is_confirmed

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.physical_connection_id is not None:
            result['PhysicalConnectionId'] = self.physical_connection_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.virtual_physical_connection_ali_uids is not None:
            result['VirtualPhysicalConnectionAliUids'] = self.virtual_physical_connection_ali_uids

        if self.virtual_physical_connection_business_status is not None:
            result['VirtualPhysicalConnectionBusinessStatus'] = self.virtual_physical_connection_business_status

        if self.virtual_physical_connection_ids is not None:
            result['VirtualPhysicalConnectionIds'] = self.virtual_physical_connection_ids

        if self.virtual_physical_connection_statuses is not None:
            result['VirtualPhysicalConnectionStatuses'] = self.virtual_physical_connection_statuses

        if self.vlan_ids is not None:
            result['VlanIds'] = self.vlan_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsConfirmed') is not None:
            self.is_confirmed = m.get('IsConfirmed')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PhysicalConnectionId') is not None:
            self.physical_connection_id = m.get('PhysicalConnectionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListVirtualPhysicalConnectionsRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VirtualPhysicalConnectionAliUids') is not None:
            self.virtual_physical_connection_ali_uids = m.get('VirtualPhysicalConnectionAliUids')

        if m.get('VirtualPhysicalConnectionBusinessStatus') is not None:
            self.virtual_physical_connection_business_status = m.get('VirtualPhysicalConnectionBusinessStatus')

        if m.get('VirtualPhysicalConnectionIds') is not None:
            self.virtual_physical_connection_ids = m.get('VirtualPhysicalConnectionIds')

        if m.get('VirtualPhysicalConnectionStatuses') is not None:
            self.virtual_physical_connection_statuses = m.get('VirtualPhysicalConnectionStatuses')

        if m.get('VlanIds') is not None:
            self.vlan_ids = m.get('VlanIds')

        return self

class ListVirtualPhysicalConnectionsRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and can contain digits, periods (.), underscores (_), and hyphens (-). It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
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

