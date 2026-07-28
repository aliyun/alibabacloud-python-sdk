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
        # The instance ID of the EIP.
        # 
        # This parameter is required.
        self.allocation_id = allocation_id
        # The end time of the data to retrieve. Specify the time in UTC in the ISO 8601 standard format: `YYYY-MM-DDThh:mm:ssZ`. For example, `2013-01-10T12:00:00Z` represents 20:00:00 (UTC+8) on January 10, 2013.
        # 
        # If the specified time is not on the minute, the end time is automatically rounded up to the next minute.
        # 
        # This parameter is required.
        self.end_time = end_time
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The duration of each monitoring data entry. Unit: seconds. Valid values: **60** (default), **300**, **900**, or **3600**.
        # - If (**EndTime** – **StartTime**) / **Period** is less than or equal to 400, all monitoring data from the start time to the end time is returned.
        # - If (**EndTime** – **StartTime**) / **Period** is greater than 400, monitoring data cannot be returned.
        self.period = period
        # The region ID of the EIP.
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query region IDs.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The start time of the data to retrieve. Specify the time in UTC in the ISO 8601 standard format: `YYYY-MM-DDThh:mm:ssZ`. For example, `2013-01-10T12:00:00Z` represents 20:00:00 (UTC+8) on January 10, 2013.
        # 
        # If the specified time is not on the minute, the start time is automatically rounded up to the next minute.
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

