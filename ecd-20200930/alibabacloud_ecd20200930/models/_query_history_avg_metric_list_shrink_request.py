# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryHistoryAvgMetricListShrinkRequest(DaraModel):
    def __init__(
        self,
        data_date: str = None,
        desktop_id: List[str] = None,
        metric_name: str = None,
        page_num: int = None,
        page_size: int = None,
        range_shrink: str = None,
        resource_region_id: str = None,
        sort_type: str = None,
    ):
        self.data_date = data_date
        self.desktop_id = desktop_id
        self.metric_name = metric_name
        self.page_num = page_num
        self.page_size = page_size
        self.range_shrink = range_shrink
        self.resource_region_id = resource_region_id
        self.sort_type = sort_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_date is not None:
            result['DataDate'] = self.data_date

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.range_shrink is not None:
            result['Range'] = self.range_shrink

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDate') is not None:
            self.data_date = m.get('DataDate')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Range') is not None:
            self.range_shrink = m.get('Range')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        return self

