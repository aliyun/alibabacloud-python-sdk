# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSpotPriceHistoryRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        spot_duration: int = None,
        start_time: str = None,
    ):
        # The end time for querying historical spot instance prices. Specify the time in ISO 8601 format using UTC+0, as yyyy-MM-ddTHH:mm:ssZ. Default value: empty. An empty value means the current time.
        self.end_time = end_time
        # The sort order. Default value: asc. Valid values:
        # 
        # - desc: descending order.
        # 
        # - asc: ascending order.
        # 
        # This parameter applies only when you query historical prices for Lingjun instance types.
        self.order = order
        # The page number of the current page. Default value: ***1***. This parameter applies only when you query historical prices for Lingjun instance types.
        self.page_number = page_number
        # The number of entries per page. Default value: **10**. This parameter applies only when you query historical prices for Lingjun instance types.
        self.page_size = page_size
        # The field to sort by. Default value: GmtCreatedTime. Valid values:
        # 
        # - GmtCreatedTime
        # 
        # This parameter applies only when you query historical prices for Lingjun instance types.
        self.sort_by = sort_by
        # The retention period for the spot instance, in hours. Note that only ECS instance types support this parameter. Default value: 0. Valid values:
        # 
        # - 1: Alibaba Cloud guarantees that the instance runs for at least one hour after creation. After one hour, the system compares your bid price with the current market price and checks resource inventory to decide whether to retain or revoke the instance.
        # 
        # - 0: Alibaba Cloud does not guarantee one-hour runtime. The system compares your bid price with the current market price and checks resource inventory to decide whether to retain or revoke the instance.
        self.spot_duration = spot_duration
        # The start time for querying historical spot instance prices. This time must be no more than seven days before the end time. Specify the time in ISO 8601 format using UTC+0, as yyyy-MM-ddTHH:mm:ssZ. Default value: empty. An empty value means three days before the end time.
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

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

