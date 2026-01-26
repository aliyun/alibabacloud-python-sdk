# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class QueryMetricByPageRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        custom_filters: List[str] = None,
        dimensions: List[str] = None,
        end_time: int = None,
        filters: List[main_models.QueryMetricByPageRequestFilters] = None,
        interval_in_sec: int = None,
        measures: List[str] = None,
        metric: str = None,
        order: str = None,
        order_by: str = None,
        page_size: int = None,
        start_time: int = None,
    ):
        # The page number. Default value: `1`.
        self.current_page = current_page
        # Custom filter conditions.
        self.custom_filters = custom_filters
        # The dimensions of the metric that you want to query.
        self.dimensions = dimensions
        # The end of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The filter conditions.
        self.filters = filters
        # The time interval at which you want to query metric data. Unit: milliseconds. Minimum value: 60000.
        self.interval_in_sec = interval_in_sec
        # The measures of the metric that you want to query.
        self.measures = measures
        # The metric that you want to query. You cannot specify a custom metric. For more information, see the "Application monitoring metrics that can be queried" section.
        # 
        # This parameter is required.
        self.metric = metric
        # The order in which measures are sorted. Valid values:
        # 
        # *   `ASC`: ascending order
        # *   `DESC`: descending order
        # 
        # > If you do not specify the parameter, data is not sorted.
        self.order = order
        # The dimension for arranging metrics in sequence. For more information, see the supplementary metrics.
        self.order_by = order_by
        # This parameter is no longer supported. The number of entries per page.
        self.page_size = page_size
        # The start of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.custom_filters is not None:
            result['CustomFilters'] = self.custom_filters

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.interval_in_sec is not None:
            result['IntervalInSec'] = self.interval_in_sec

        if self.measures is not None:
            result['Measures'] = self.measures

        if self.metric is not None:
            result['Metric'] = self.metric

        if self.order is not None:
            result['Order'] = self.order

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('CustomFilters') is not None:
            self.custom_filters = m.get('CustomFilters')

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.QueryMetricByPageRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('IntervalInSec') is not None:
            self.interval_in_sec = m.get('IntervalInSec')

        if m.get('Measures') is not None:
            self.measures = m.get('Measures')

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class QueryMetricByPageRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the filter condition. You must set the key to `pid` or `regionId`.
        self.key = key
        # The value of the filter condition. You must set the value of the `pid` or `regionId` condition. For information about how to obtain the `pid`, see the "Obtain the PID of an application" section.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

