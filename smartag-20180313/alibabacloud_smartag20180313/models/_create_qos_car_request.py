# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateQosCarRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        limit_type: str = None,
        max_bandwidth_abs: int = None,
        max_bandwidth_percent: int = None,
        min_bandwidth_abs: int = None,
        min_bandwidth_percent: int = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        percent_source_type: str = None,
        priority: int = None,
        qos_id: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The description of the traffic throttling rule.
        self.description = description
        # The type of the traffic throttling rule. Valid values:
        # 
        # *   **Absolute**: throttles traffic based on a specific range of bandwidth values.
        # *   **Percent**: throttles traffic based on a specific range of bandwidth percentage.
        # 
        # This parameter is required.
        self.limit_type = limit_type
        # The maximum bandwidth value. The value must be an integer. Unit: Mbit/s.
        # 
        # This parameter is returned when **LimitType** is set to **Absolute**.
        # 
        # >  The maximum bandwidth value must be greater than the minimum bandwidth value.
        self.max_bandwidth_abs = max_bandwidth_abs
        # The maximum bandwidth percentage. Unit: percent (%). Valid values: **1 to 100**.
        # 
        # This parameter is required when you set **LimitType** to **Percent**.
        # 
        # >  The maximum bandwidth percentage must be greater than the minimum bandwidth percentage.
        self.max_bandwidth_percent = max_bandwidth_percent
        # The minimum bandwidth value. The value must be an integer. Unit: Mbit/s.
        # 
        # This parameter is returned when **LimitType** is set to **Absolute**.
        self.min_bandwidth_abs = min_bandwidth_abs
        # The minimum bandwidth percentage. Unit: percent (%). Valid values: **1 to 100**.
        # 
        # This parameter is required when you set **LimitType** to **Percent**.
        self.min_bandwidth_percent = min_bandwidth_percent
        # The name of the traffic throttling rule.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The type of bandwidth when traffic is throttled based on bandwidth percentage. Valid values:
        # 
        # *   **CcnBandwidth**: CCN bandwidth
        # *   **InternetUpBandwidth**: total Internet bandwidth
        self.percent_source_type = percent_source_type
        # The priority of the traffic throttling rule.
        # 
        # Valid values: **1** to **3**. A smaller value indicates a higher priority. If rules have the same priority, the one created the earliest is applied.
        # 
        # This parameter is required.
        self.priority = priority
        # The ID of the QoS policy.
        # 
        # This parameter is required.
        self.qos_id = qos_id
        # The ID of the region to which the QoS policy belongs.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/69813.html) operation to query the most recent region list.
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
        if self.description is not None:
            result['Description'] = self.description

        if self.limit_type is not None:
            result['LimitType'] = self.limit_type

        if self.max_bandwidth_abs is not None:
            result['MaxBandwidthAbs'] = self.max_bandwidth_abs

        if self.max_bandwidth_percent is not None:
            result['MaxBandwidthPercent'] = self.max_bandwidth_percent

        if self.min_bandwidth_abs is not None:
            result['MinBandwidthAbs'] = self.min_bandwidth_abs

        if self.min_bandwidth_percent is not None:
            result['MinBandwidthPercent'] = self.min_bandwidth_percent

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.percent_source_type is not None:
            result['PercentSourceType'] = self.percent_source_type

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.qos_id is not None:
            result['QosId'] = self.qos_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')

        if m.get('MaxBandwidthAbs') is not None:
            self.max_bandwidth_abs = m.get('MaxBandwidthAbs')

        if m.get('MaxBandwidthPercent') is not None:
            self.max_bandwidth_percent = m.get('MaxBandwidthPercent')

        if m.get('MinBandwidthAbs') is not None:
            self.min_bandwidth_abs = m.get('MinBandwidthAbs')

        if m.get('MinBandwidthPercent') is not None:
            self.min_bandwidth_percent = m.get('MinBandwidthPercent')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PercentSourceType') is not None:
            self.percent_source_type = m.get('PercentSourceType')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('QosId') is not None:
            self.qos_id = m.get('QosId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

