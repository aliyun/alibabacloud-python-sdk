# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDedicatedHostsRequest(DaraModel):
    def __init__(
        self,
        allocation_status: str = None,
        dedicated_host_group_id: str = None,
        dedicated_host_id: str = None,
        host_status: str = None,
        host_type: str = None,
        order_id: int = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        zone_id: str = None,
    ):
        # Specifies whether instances can be deployed on the host. Valid values:
        # 
        # *   **0**: Instances cannot be deployed on the host.
        # *   **1**: Instances can be deployed on the host.
        self.allocation_status = allocation_status
        # The dedicated cluster ID. You can call the DescribeDedicatedHostGroups operation to query the dedicated cluster ID.
        self.dedicated_host_group_id = dedicated_host_group_id
        # The ID of the host in the dedicated cluster.
        self.dedicated_host_id = dedicated_host_id
        # The status of the host. Valid values:
        # 
        # *   **0**: creating
        # *   **1**: running
        # *   **2**: faulty
        # *   **3**: being replaced
        # *   **4**: deprecated
        # *   **5**: deleting
        # *   **6**: restarting
        self.host_status = host_status
        # The storage type of the host. Valid values:
        # 
        # *   **dhg_cloud_ssd**: enhanced SSD (ESSD)
        # *   **dhg_local_ssd**: local SSD
        self.host_type = host_type
        # The order ID.
        self.order_id = order_id
        self.owner_id = owner_id
        # The region ID. You can call the DescribeRegions operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status

        if self.dedicated_host_group_id is not None:
            result['DedicatedHostGroupId'] = self.dedicated_host_group_id

        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id

        if self.host_status is not None:
            result['HostStatus'] = self.host_status

        if self.host_type is not None:
            result['HostType'] = self.host_type

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')

        if m.get('DedicatedHostGroupId') is not None:
            self.dedicated_host_group_id = m.get('DedicatedHostGroupId')

        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')

        if m.get('HostStatus') is not None:
            self.host_status = m.get('HostStatus')

        if m.get('HostType') is not None:
            self.host_type = m.get('HostType')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

