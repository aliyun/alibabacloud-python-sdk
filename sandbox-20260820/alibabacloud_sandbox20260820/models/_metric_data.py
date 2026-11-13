# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class MetricData(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        group_by: List[str] = None,
        period: int = None,
        results: List[main_models.MetricDataResults] = None,
        start_time: str = None,
        time: str = None,
    ):
        # The end time of the time series query, exclusive.
        self.end_time = end_time
        # The grouping keys used for this query. An empty array is returned if no grouping is applied.
        # 
        # This parameter is required.
        self.group_by = group_by
        # The data point interval used for this query, in seconds.
        # 
        # This parameter is required.
        self.period = period
        # The result for each requested metric.
        # 
        # This parameter is required.
        self.results = results
        # The start time of the time series query, inclusive.
        self.start_time = start_time
        # The time of the query. Returned only for single-point queries.
        self.time = time

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.group_by is not None:
            result['groupBy'] = self.group_by

        if self.period is not None:
            result['period'] = self.period

        if self.results is not None:
            result['results'] = []
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.time is not None:
            result['time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')

        if m.get('period') is not None:
            self.period = m.get('period')

        if m.get('results') is not None:
            self.results = []
            for k1 in m.get('results'):
                temp_model = main_models.MetricDataResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('time') is not None:
            self.time = m.get('time')

        return self

class MetricDataResults(DaraModel):
    def __init__(
        self,
        metric_name: str = None,
        series: List[main_models.MetricDataResultsSeries] = None,
        unit: str = None,
    ):
        # The name of the metric in the request.
        # 
        # This parameter is required.
        self.metric_name = metric_name
        # The time series for the metric. An empty array is returned if no data points exist.
        # 
        # This parameter is required.
        self.series = series
        # The unit of the metric value, such as Core for CPU cores.
        # 
        # This parameter is required.
        self.unit = unit

    def validate(self):
        if self.series:
            for v1 in self.series:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_name is not None:
            result['metricName'] = self.metric_name

        if self.series is not None:
            result['series'] = []
            for k1 in self.series:
                result['series'].append(k1.to_map() if k1 else None)

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')

        if m.get('series') is not None:
            self.series = []
            for k1 in m.get('series'):
                temp_model = main_models.MetricDataResultsSeries()
                self.series.append(temp_model.from_map(k1))

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self

class MetricDataResultsSeries(DaraModel):
    def __init__(
        self,
        dimensions: Dict[str, str] = None,
        points: List[main_models.MetricDataResultsSeriesPoints] = None,
    ):
        # The team, template, or other grouping values for this series.
        # 
        # This parameter is required.
        self.dimensions = dimensions
        # The data points in chronological order. Only times with metric values are listed.
        # 
        # This parameter is required.
        self.points = points

    def validate(self):
        if self.points:
            for v1 in self.points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimensions is not None:
            result['dimensions'] = self.dimensions

        if self.points is not None:
            result['points'] = []
            for k1 in self.points:
                result['points'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dimensions') is not None:
            self.dimensions = m.get('dimensions')

        if m.get('points') is not None:
            self.points = []
            for k1 in m.get('points'):
                temp_model = main_models.MetricDataResultsSeriesPoints()
                self.points.append(temp_model.from_map(k1))

        return self

class MetricDataResultsSeriesPoints(DaraModel):
    def __init__(
        self,
        timestamp: str = None,
        value: float = None,
    ):
        # The time corresponding to the metric value, in UTC seconds.
        # 
        # This parameter is required.
        self.timestamp = timestamp
        # The metric value at this time. The unit is specified in unit.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

