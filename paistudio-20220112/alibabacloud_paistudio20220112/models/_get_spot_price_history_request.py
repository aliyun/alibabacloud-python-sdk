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
        # The end time for querying the historical prices of spot instances. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Default value: null, which indicates the current time.
        self.end_time = end_time
        # The sort order. Default value: asc. Valid values:
        # - desc: descending order.
        # - asc: ascending order.
        # 
        # This parameter takes effect only when you query the historical prices of Lingjun instance types.
        self.order = order
        # The page number. Default value: ***1***. This parameter takes effect only when you query the historical prices of Lingjun instance types.
        self.page_number = page_number
        # The number of entries per page. Default value: **10**. This parameter takes effect only when you query the historical prices of Lingjun instance types.
        self.page_size = page_size
        # The field used for sorting. Default value: GmtCreatedTime. Valid values:
        # 
        # - GmtCreatedTime
        # 
        # This parameter takes effect only when you query the historical prices of Lingjun instance types.
        self.sort_by = sort_by
        # The protection period of the spot instance. Unit: hours. Note that only ECS instance types support Settings for the protection period of spot instances. Default value: 0. Valid values:
        # 
        # - 1: After the spot instance is created, Alibaba Cloud ensures that the instance runs for 1 hour without automatic release. After 1 hour, the system automatically compares the bid price with the marketplace price and checks resource inventory to determine whether to retain or revoke the instance.
        # - 0: After the spot instance is created, Alibaba Cloud does not guarantee that the instance runs for 1 hour. The system automatically compares the bid price with the marketplace price and checks resource inventory to determine whether to retain or revoke the instance.
        self.spot_duration = spot_duration
        # The start time for querying the historical prices of spot instances. The maximum value cannot exceed 7 days before the specified end time. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Default value: null, which indicates 3 days before the end time.
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

