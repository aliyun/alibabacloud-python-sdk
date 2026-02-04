# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyConsumptionTimestampRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        consumption_timestamp: str = None,
        owner_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        subscription_instance_id: str = None,
    ):
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future.
        self.account_id = account_id
        # The consumption checkpoint. The format is *yyyy-MM-dd*T*HH:mm:ss*Z. The time is displayed in UTC.
        # 
        # This parameter is required.
        self.consumption_timestamp = consumption_timestamp
        self.owner_id = owner_id
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # The ID of the change tracking instance. You can call the DescribeSubscriptionInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.subscription_instance_id = subscription_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.consumption_timestamp is not None:
            result['ConsumptionTimestamp'] = self.consumption_timestamp

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceId'] = self.subscription_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('ConsumptionTimestamp') is not None:
            self.consumption_timestamp = m.get('ConsumptionTimestamp')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SubscriptionInstanceId') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceId')

        return self

