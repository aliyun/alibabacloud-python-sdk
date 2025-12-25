# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkFlowTimeSeriesMetricResponseBody(DaraModel):
    def __init__(
        self,
        network_flow_time_series: List[main_models.DescribeNetworkFlowTimeSeriesMetricResponseBodyNetworkFlowTimeSeries] = None,
        request_id: str = None,
        time_series_meta_data: main_models.DescribeNetworkFlowTimeSeriesMetricResponseBodyTimeSeriesMetaData = None,
    ):
        # The array of time-series data. Supports returning data with multiple values.
        self.network_flow_time_series = network_flow_time_series
        # The ID of the request.
        self.request_id = request_id
        # The metadata of the returned data.
        self.time_series_meta_data = time_series_meta_data

    def validate(self):
        if self.network_flow_time_series:
            for v1 in self.network_flow_time_series:
                 if v1:
                    v1.validate()
        if self.time_series_meta_data:
            self.time_series_meta_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkFlowTimeSeries'] = []
        if self.network_flow_time_series is not None:
            for k1 in self.network_flow_time_series:
                result['NetworkFlowTimeSeries'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.time_series_meta_data is not None:
            result['TimeSeriesMetaData'] = self.time_series_meta_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_flow_time_series = []
        if m.get('NetworkFlowTimeSeries') is not None:
            for k1 in m.get('NetworkFlowTimeSeries'):
                temp_model = main_models.DescribeNetworkFlowTimeSeriesMetricResponseBodyNetworkFlowTimeSeries()
                self.network_flow_time_series.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TimeSeriesMetaData') is not None:
            temp_model = main_models.DescribeNetworkFlowTimeSeriesMetricResponseBodyTimeSeriesMetaData()
            self.time_series_meta_data = temp_model.from_map(m.get('TimeSeriesMetaData'))

        return self

class DescribeNetworkFlowTimeSeriesMetricResponseBodyTimeSeriesMetaData(DaraModel):
    def __init__(
        self,
        aggregate_interval: str = None,
        date_range: main_models.DescribeNetworkFlowTimeSeriesMetricResponseBodyTimeSeriesMetaDataDateRange = None,
        units: str = None,
    ):
        # The time granularity. For example, 15m indicates that each data point is counted every 15 minutes. For details, see the **Time granularity of time series data points** section below.
        self.aggregate_interval = aggregate_interval
        # The query time range.
        self.date_range = date_range
        # The unit of the returned data. It is fixed as requests.
        self.units = units

    def validate(self):
        if self.date_range:
            self.date_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregate_interval is not None:
            result['AggregateInterval'] = self.aggregate_interval

        if self.date_range is not None:
            result['DateRange'] = self.date_range.to_map()

        if self.units is not None:
            result['Units'] = self.units

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregateInterval') is not None:
            self.aggregate_interval = m.get('AggregateInterval')

        if m.get('DateRange') is not None:
            temp_model = main_models.DescribeNetworkFlowTimeSeriesMetricResponseBodyTimeSeriesMetaDataDateRange()
            self.date_range = temp_model.from_map(m.get('DateRange'))

        if m.get('Units') is not None:
            self.units = m.get('Units')

        return self

class DescribeNetworkFlowTimeSeriesMetricResponseBodyTimeSeriesMetaDataDateRange(DaraModel):
    def __init__(
        self,
        end_date: int = None,
        start_date: int = None,
    ):
        # The end time of the query range (Unix timestamp, seconds). Same as the EndDate request parameter.
        self.end_date = end_date
        # The start time of the query range (Unix timestamp, seconds). Same as the StartDate request parameter.
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        return self

class DescribeNetworkFlowTimeSeriesMetricResponseBodyNetworkFlowTimeSeries(DaraModel):
    def __init__(
        self,
        metric: str = None,
        timestamps: List[str] = None,
        values: List[int] = None,
    ):
        # The metric name, consistent with the Metric request parameter.
        self.metric = metric
        # The array of timestamps (seconds) marking the start of each time interval.
        self.timestamps = timestamps
        # The array of counts, each representing the count for the corresponding time interval.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric is not None:
            result['Metric'] = self.metric

        if self.timestamps is not None:
            result['Timestamps'] = self.timestamps

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('Timestamps') is not None:
            self.timestamps = m.get('Timestamps')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

