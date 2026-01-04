# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEipMonitorDataRequest(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        end_time: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_time: str = None,
    ):
        # The ID of the EIP.
        # 
        # This parameter is required.
        self.allocation_id = allocation_id
        # The end of the time range to query. The time must be in UTC. Specify the time in the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format. For example, `2013-01-10T12:00:00Z` specifies 20:00:00 (UTC+8) on January 10, 2013.
        # 
        # If the value of seconds (ss) is not 00, the end time is automatically rounded up to the next minute.
        # 
        # This parameter is required.
        self.end_time = end_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The duration of each monitoring data entry. Unit: seconds. Valid values: **60** (default), **300**, **900**, and **3600**.
        # 
        # *   If the value of **(EndTime** - **StartTime**)/**Period** is greater than 200, a maximum of 200 monitoring data entries are returned at a time.
        # *   If the value of (**EndTime** - **StartTime**)/**Period** is less than or equal to 200, only the monitoring data collected between the start time and end time is returned.
        self.period = period
        # The ID of the region to which the EIP belongs. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The beginning of the time range to query. The time must be in UTC. Specify the time in the ISO 8601 standard in `YYYY-MM-DDThh:mm:ssZ` format. For example, `2013-01-10T12:00:00Z` specifies 20:00:00 (UTC+8) on January 10, 2013.
        # 
        # If the value of seconds (ss) is not 00, the start time is automatically rounded up to the next minute.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

