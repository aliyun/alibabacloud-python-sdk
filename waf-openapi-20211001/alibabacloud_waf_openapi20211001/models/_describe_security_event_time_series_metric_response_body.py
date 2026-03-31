# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityEventTimeSeriesMetricResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        security_event_time_series: List[main_models.DescribeSecurityEventTimeSeriesMetricResponseBodySecurityEventTimeSeries] = None,
        time_series_meta_data: main_models.DescribeSecurityEventTimeSeriesMetricResponseBodyTimeSeriesMetaData = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The time series data returned. This operation can return time series for multiple metrics.
        self.security_event_time_series = security_event_time_series
        # The metadata of the time series data returned.
        self.time_series_meta_data = time_series_meta_data

    def validate(self):
        if self.security_event_time_series:
            for v1 in self.security_event_time_series:
                 if v1:
                    v1.validate()
        if self.time_series_meta_data:
            self.time_series_meta_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SecurityEventTimeSeries'] = []
        if self.security_event_time_series is not None:
            for k1 in self.security_event_time_series:
                result['SecurityEventTimeSeries'].append(k1.to_map() if k1 else None)

        if self.time_series_meta_data is not None:
            result['TimeSeriesMetaData'] = self.time_series_meta_data.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.security_event_time_series = []
        if m.get('SecurityEventTimeSeries') is not None:
            for k1 in m.get('SecurityEventTimeSeries'):
                temp_model = main_models.DescribeSecurityEventTimeSeriesMetricResponseBodySecurityEventTimeSeries()
                self.security_event_time_series.append(temp_model.from_map(k1))

        if m.get('TimeSeriesMetaData') is not None:
            temp_model = main_models.DescribeSecurityEventTimeSeriesMetricResponseBodyTimeSeriesMetaData()
            self.time_series_meta_data = temp_model.from_map(m.get('TimeSeriesMetaData'))

        return self

class DescribeSecurityEventTimeSeriesMetricResponseBodyTimeSeriesMetaData(DaraModel):
    def __init__(
        self,
        aggregate_interval: str = None,
        date_range: main_models.DescribeSecurityEventTimeSeriesMetricResponseBodyTimeSeriesMetaDataDateRange = None,
        units: str = None,
    ):
        # The time granularity of data points in the time series data returned. For example, a value of 15m indicates that data points are collected at 15-minute intervals. For more information about time granularities, see the **Time granularities of data points in time series** section below.
        self.aggregate_interval = aggregate_interval
        # The time range that is used for the query.
        self.date_range = date_range
        # The unit of the statistics returned. It is fixed as requests.
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
            temp_model = main_models.DescribeSecurityEventTimeSeriesMetricResponseBodyTimeSeriesMetaDataDateRange()
            self.date_range = temp_model.from_map(m.get('DateRange'))

        if m.get('Units') is not None:
            self.units = m.get('Units')

        return self

class DescribeSecurityEventTimeSeriesMetricResponseBodyTimeSeriesMetaDataDateRange(DaraModel):
    def __init__(
        self,
        end_date: int = None,
        start_date: int = None,
    ):
        # The end of the time range to query. The value is a Unix timestamp. Unit: seconds. This value is the same as the value of EndDate in the request parameters.
        self.end_date = end_date
        # The beginning of the time range to query. The value is a Unix timestamp. Unit: seconds. This value is the same as the value of StartDate in the request parameters.
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

class DescribeSecurityEventTimeSeriesMetricResponseBodySecurityEventTimeSeries(DaraModel):
    def __init__(
        self,
        metric: str = None,
        timestamps: List[str] = None,
        values: List[int] = None,
    ):
        # The metric. This value is the same as the value of Metric in the request parameters.
        self.metric = metric
        # The time points. Each point represents a time range.
        self.timestamps = timestamps
        # The data points. Each point represents a count for a time range.
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

