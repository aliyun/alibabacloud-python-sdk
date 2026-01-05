# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListDIJobMetricsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListDIJobMetricsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListDIJobMetricsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDIJobMetricsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        job_metrics: List[main_models.ListDIJobMetricsResponseBodyPagingInfoJobMetrics] = None,
    ):
        # The metrics returned.
        self.job_metrics = job_metrics

    def validate(self):
        if self.job_metrics:
            for v1 in self.job_metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JobMetrics'] = []
        if self.job_metrics is not None:
            for k1 in self.job_metrics:
                result['JobMetrics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_metrics = []
        if m.get('JobMetrics') is not None:
            for k1 in m.get('JobMetrics'):
                temp_model = main_models.ListDIJobMetricsResponseBodyPagingInfoJobMetrics()
                self.job_metrics.append(temp_model.from_map(k1))

        return self

class ListDIJobMetricsResponseBodyPagingInfoJobMetrics(DaraModel):
    def __init__(
        self,
        name: str = None,
        series_list: List[main_models.ListDIJobMetricsResponseBodyPagingInfoJobMetricsSeriesList] = None,
    ):
        # The name of the metric.
        self.name = name
        # The metric data.
        self.series_list = series_list

    def validate(self):
        if self.series_list:
            for v1 in self.series_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        result['SeriesList'] = []
        if self.series_list is not None:
            for k1 in self.series_list:
                result['SeriesList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.series_list = []
        if m.get('SeriesList') is not None:
            for k1 in m.get('SeriesList'):
                temp_model = main_models.ListDIJobMetricsResponseBodyPagingInfoJobMetricsSeriesList()
                self.series_list.append(temp_model.from_map(k1))

        return self

class ListDIJobMetricsResponseBodyPagingInfoJobMetricsSeriesList(DaraModel):
    def __init__(
        self,
        time: int = None,
        value: float = None,
    ):
        # The point in time at which data is sampled based on the metric.
        self.time = time
        # The sample value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time is not None:
            result['Time'] = self.time

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

