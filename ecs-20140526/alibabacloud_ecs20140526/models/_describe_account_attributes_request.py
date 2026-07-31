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
        # The type of resource quota to query in the specified region. Valid values of N: 1 to 8. Valid values:
        # 
        # - instance-network-type: available network types.
        # - max-security-groups: the maximum number of security groups.
        # - max-elastic-network-interfaces: the maximum number of Elastic Network Interfaces (ENIs).
        # - max-postpaid-instance-vcpu-count: the maximum number of vCPUs for pay-as-you-go instances.
        # - max-spot-instance-vcpu-count: the maximum number of vCPUs for spot instances.
        # - used-postpaid-instance-vcpu-count: the number of vCPUs that have been used by pay-as-you-go instances.
        # - used-spot-instance-vcpu-count: the number of vCPUs that have been used by spot instances.
        # - max-postpaid-yundisk-capacity: the maximum total capacity of pay-as-you-go cloud disks used as data disks. (This parameter value is deprecated.)
        # - used-postpaid-yundisk-capacity: the capacity of pay-as-you-go cloud disks that have been used as data disks. (This parameter value is deprecated.)
        # - max-dedicated-hosts: the maximum number of dedicated hosts.
        # - supported-postpaid-instance-types: the instance types of pay-as-you-go I/O optimized instances.
        # - max-axt-command-count: the maximum number of Cloud Assistant commands.
        # - max-axt-invocation-daily: the maximum number of Cloud Assistant commands that can be executed per day.
        # - real-name-authentication: whether the account has completed real-name registration.
        # 
        #     > You must complete real-name registration before you can create ECS instances in regions in the Chinese mainland.
        # - max-cloud-assistant-activation-count: the maximum number of Cloud Assistant managed instance dynamic codes that can be created.
        # 
        # Default value: null.
        self.attribute_name = attribute_name
        self.owner_id = owner_id
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
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

