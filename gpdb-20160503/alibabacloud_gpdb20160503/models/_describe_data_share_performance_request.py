# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataSharePerformanceRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        key: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.end_time = end_time
        # The name of the performance metric. Separate multiple values with commas (,). Valid values:
        # 
        # *   **adbpg_datashare_topic_count**: the number of shared topics.
        # *   **adbpg_datashare_data_size_mb**: the amount of data shared.
        # 
        # This parameter is required.
        self.key = key
        # The region ID of the instance.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # This parameter is no longer used.
        self.resource_group_id = resource_group_id
        # The beginning of the time range to query. Specify the time in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.key is not None:
            result['Key'] = self.key

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

