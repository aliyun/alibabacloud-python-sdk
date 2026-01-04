# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddGlobalAccelerationInstanceIpRequest(DaraModel):
    def __init__(
        self,
        global_acceleration_instance_id: str = None,
        ip_instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the shared-bandwidth GA instance.
        # 
        # This parameter is required.
        self.global_acceleration_instance_id = global_acceleration_instance_id
        # The EIP ID. You can call the [DescribeEipAddresses](https://help.aliyun.com/document_detail/36018.html) operation to query EIP IDs.
        # 
        # >  Make sure that the billing method of the EIP is pay-as-you-go, and the EIP and the shared-bandwidth GA instance belong to the same region.
        # 
        # This parameter is required.
        self.ip_instance_id = ip_instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region of the shared-bandwidth GA instance.
        # 
        # You can call the **DescribeRegions** operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.global_acceleration_instance_id is not None:
            result['GlobalAccelerationInstanceId'] = self.global_acceleration_instance_id

        if self.ip_instance_id is not None:
            result['IpInstanceId'] = self.ip_instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalAccelerationInstanceId') is not None:
            self.global_acceleration_instance_id = m.get('GlobalAccelerationInstanceId')

        if m.get('IpInstanceId') is not None:
            self.ip_instance_id = m.get('IpInstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

