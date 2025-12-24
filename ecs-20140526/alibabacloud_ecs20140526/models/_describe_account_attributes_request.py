# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeAccountAttributesRequest(DaraModel):
    def __init__(
        self,
        attribute_name: List[str] = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        zone_id: str = None,
    ):
        # The type of resource quota N. Valid values of N: 1 to 8. Valid values:
        # 
        # *   instance-network-type: the available network types.
        # 
        # *   max-security-groups: the maximum number of security groups.
        # 
        # *   max-elastic-network-interfaces: the maximum number of ENIs.
        # 
        # *   max-postpaid-instance-vcpu-count: the maximum number of vCPUs for pay-as-you-go instances.
        # 
        # *   max-spot-instance-vcpu-count: the maximum number of vCPUs for spot instances.
        # 
        # *   used-postpaid-instance-vcpu-count: the number of vCPUs that have been allocated to pay-as-you-go instances.
        # 
        # *   used-spot-instance-vcpu-count: the number of vCPUs that have been allocated to spot instances.
        # 
        # *   max-postpaid-yundisk-capacity: the maximum capacity of pay-as-you-go data disks. (The value is deprecated.)
        # 
        # *   used-postpaid-yundisk-capacity: the capacity of pay-as-you-go data disks that have been created. (The value is deprecated.)
        # 
        # *   max-dedicated-hosts: the maximum number of dedicated hosts.
        # 
        # *   supported-postpaid-instance-types: the instance types of pay-as-you-go I/O optimized instances.
        # 
        # *   max-axt-command-count: the maximum number of Cloud Assistant commands.
        # 
        # *   max-axt-invocation-daily: the maximum number of Cloud Assistant command executions per day.
        # 
        # *   real-name-authentication: whether the account has completed the real-name verification.
        # 
        #     **
        # 
        #     **Note** To create an ECS instance in a region in the Chinese mainland, you must complete the real-name verification.
        # 
        # *   max-cloud-assistant-activation-count: the maximum number of activation codes that can be created to use to register managed instances.
        # 
        # This parameter is empty by default.
        self.attribute_name = attribute_name
        self.owner_id = owner_id
        # The ID of the region. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent list of regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the zone in which the resource resides.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name

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
        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')

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

