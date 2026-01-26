# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class QueryCommercialUsageRequest(DaraModel):
    def __init__(
        self,
        advanced_filters: List[main_models.QueryCommercialUsageRequestAdvancedFilters] = None,
        dimensions: List[str] = None,
        end_time: int = None,
        interval_in_sec: int = None,
        measures: List[str] = None,
        metric: str = None,
        order: str = None,
        order_by: str = None,
        query_type: str = None,
        start_time: int = None,
    ):
        # The filter conditions.
        self.advanced_filters = advanced_filters
        # The dimensions of the metric that you want to query. Valid values:
        # 
        # *   dataType: data type
        # *   productType: product type
        # *   instanceId: instance ID
        # *   instanceName: instance name
        # *   instanceType: instance type
        self.dimensions = dimensions
        # The end of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The time interval between data slices. Unit: seconds. Minimum value: 3600.
        # 
        # Valid values:
        # 
        # *   3600: 1 hour
        # *   86400: 1 day
        self.interval_in_sec = interval_in_sec
        # The measures of the metric that you want to query.
        self.measures = measures
        # The name of the metric. Valid value: USAGEFEE.STAT.
        # 
        # This parameter is required.
        self.metric = metric
        # The order in which data is sorted. Valid value:
        # 
        # *   `ASC`: ascending order
        # *   `DESC`: descending order
        self.order = order
        # The dimension by which data is sorted.
        # 
        # Valid value:
        # 
        # *   dataType
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.order_by = order_by
        # The data type. Valid values:
        # 
        # *   instantQuery: non-time series
        # *   timeSeriesQuery: time series
        # 
        # This parameter is required.
        self.query_type = query_type
        # The start of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        if self.advanced_filters:
            for v1 in self.advanced_filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdvancedFilters'] = []
        if self.advanced_filters is not None:
            for k1 in self.advanced_filters:
                result['AdvancedFilters'].append(k1.to_map() if k1 else None)

        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions

        if self.end_time is not None:
            result['EndTime'] = self.end_time

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

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.advanced_filters = []
        if m.get('AdvancedFilters') is not None:
            for k1 in m.get('AdvancedFilters'):
                temp_model = main_models.QueryCommercialUsageRequestAdvancedFilters()
                self.advanced_filters.append(temp_model.from_map(k1))

        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

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

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class QueryCommercialUsageRequestAdvancedFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        op_type: str = None,
        value: str = None,
    ):
        # The key of the filter condition.
        self.key = key
        # The operator. Valid values: eq and in.
        self.op_type = op_type
        # The value of the filter condition.
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

        if self.op_type is not None:
            result['OpType'] = self.op_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

