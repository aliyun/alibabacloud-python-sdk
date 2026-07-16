# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListComputeMetricsBySignatureResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListComputeMetricsBySignatureResponseBodyData = None,
        http_code: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.http_code = http_code
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListComputeMetricsBySignatureResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListComputeMetricsBySignatureResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        signature_compute_metrics: List[main_models.ListComputeMetricsBySignatureResponseBodyDataSignatureComputeMetrics] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.signature_compute_metrics = signature_compute_metrics
        self.total_count = total_count

    def validate(self):
        if self.signature_compute_metrics:
            for v1 in self.signature_compute_metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['signatureComputeMetrics'] = []
        if self.signature_compute_metrics is not None:
            for k1 in self.signature_compute_metrics:
                result['signatureComputeMetrics'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.signature_compute_metrics = []
        if m.get('signatureComputeMetrics') is not None:
            for k1 in m.get('signatureComputeMetrics'):
                temp_model = main_models.ListComputeMetricsBySignatureResponseBodyDataSignatureComputeMetrics()
                self.signature_compute_metrics.append(temp_model.from_map(k1))

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListComputeMetricsBySignatureResponseBodyDataSignatureComputeMetrics(DaraModel):
    def __init__(
        self,
        instances: List[main_models.ListComputeMetricsBySignatureResponseBodyDataSignatureComputeMetricsInstances] = None,
        project_names: List[str] = None,
        signature: str = None,
        unit: str = None,
        usage: float = None,
    ):
        self.instances = instances
        self.project_names = project_names
        self.signature = signature
        self.unit = unit
        self.usage = usage

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['instances'].append(k1.to_map() if k1 else None)

        if self.project_names is not None:
            result['projectNames'] = self.project_names

        if self.signature is not None:
            result['signature'] = self.signature

        if self.unit is not None:
            result['unit'] = self.unit

        if self.usage is not None:
            result['usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('instances') is not None:
            for k1 in m.get('instances'):
                temp_model = main_models.ListComputeMetricsBySignatureResponseBodyDataSignatureComputeMetricsInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('projectNames') is not None:
            self.project_names = m.get('projectNames')

        if m.get('signature') is not None:
            self.signature = m.get('signature')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        if m.get('usage') is not None:
            self.usage = m.get('usage')

        return self

class ListComputeMetricsBySignatureResponseBodyDataSignatureComputeMetricsInstances(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.instance_id = instance_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

