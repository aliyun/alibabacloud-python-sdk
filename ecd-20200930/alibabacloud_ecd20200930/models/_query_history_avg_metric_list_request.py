# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class QueryHistoryAvgMetricListRequest(DaraModel):
    def __init__(
        self,
        data_date: str = None,
        desktop_id: List[str] = None,
        metric_name: str = None,
        page_num: int = None,
        page_size: int = None,
        range: main_models.QueryHistoryAvgMetricListRequestRange = None,
        resource_region_id: str = None,
        sort_type: str = None,
    ):
        # The start date of the statistics. The format is `YYYY-MM-DD`. The default value is T-1.
        self.data_date = data_date
        # The desktop ID list. A maximum of 100 IDs are supported.
        self.desktop_id = desktop_id
        # The metric to query.
        self.metric_name = metric_name
        # The page number, which must be greater than 0. Default value: 1.
        self.page_num = page_num
        # The page size. Valid values: 1 to 200. Default value: 20.
        self.page_size = page_size
        # The list of custom numeric ranges.
        self.range = range
        # The desktop region.
        self.resource_region_id = resource_region_id
        # The sorting method.
        self.sort_type = sort_type

    def validate(self):
        if self.range:
            self.range.validate()

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

        if self.range is not None:
            result['Range'] = self.range.to_map()

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
            temp_model = main_models.QueryHistoryAvgMetricListRequestRange()
            self.range = temp_model.from_map(m.get('Range'))

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        return self

class QueryHistoryAvgMetricListRequestRange(DaraModel):
    def __init__(
        self,
        include_max: bool = None,
        include_min: bool = None,
        label: str = None,
        max: float = None,
        min: float = None,
    ):
        # Specifies whether to include the maximum value. Default value: false.
        self.include_max = include_max
        # Specifies whether to include the minimum value. Default value: true.
        self.include_min = include_min
        # The range label, which is used for the return value.
        self.label = label
        # The maximum value.
        self.max = max
        # The minimum value.
        self.min = min

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_max is not None:
            result['IncludeMax'] = self.include_max

        if self.include_min is not None:
            result['IncludeMin'] = self.include_min

        if self.label is not None:
            result['Label'] = self.label

        if self.max is not None:
            result['Max'] = self.max

        if self.min is not None:
            result['Min'] = self.min

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeMax') is not None:
            self.include_max = m.get('IncludeMax')

        if m.get('IncludeMin') is not None:
            self.include_min = m.get('IncludeMin')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Max') is not None:
            self.max = m.get('Max')

        if m.get('Min') is not None:
            self.min = m.get('Min')

        return self

