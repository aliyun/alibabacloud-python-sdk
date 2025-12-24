# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveStreamMonitorListRequest(DaraModel):
    def __init__(
        self,
        monitor_id: str = None,
        order_rule: int = None,
        owner_id: int = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        status: int = None,
    ):
        # The ID of the monitoring session.
        # 
        # >  You can obtain the monitoring session ID from the response parameter MonitorId of the [CreateLiveStreamMonitor](https://help.aliyun.com/document_detail/2848129.html) operation. If you leave this parameter empty, the data of all monitoring sessions is returned.
        self.monitor_id = monitor_id
        # The sorting order of monitoring sessions. Valid values:
        # 
        # *   0: Monitoring sessions are sorted by status.
        # *   1: Monitoring sessions are sorted by start time in descending order.
        # *   2: Monitoring sessions are sorted by start time in ascending order.
        self.order_rule = order_rule
        self.owner_id = owner_id
        # The page number.
        self.page_num = page_num
        # The number of monitoring sessions to return per page.
        self.page_size = page_size
        self.region_id = region_id
        # The status of the monitoring session. Valid values:
        # 
        # *   1: Monitoring
        # *   0: Unmonitored
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.monitor_id is not None:
            result['MonitorId'] = self.monitor_id

        if self.order_rule is not None:
            result['OrderRule'] = self.order_rule

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorId') is not None:
            self.monitor_id = m.get('MonitorId')

        if m.get('OrderRule') is not None:
            self.order_rule = m.get('OrderRule')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

