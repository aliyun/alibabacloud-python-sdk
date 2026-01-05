# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeMetricLastResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        metric_total_model: List[main_models.DescribeMetricLastResponseBodyMetricTotalModel] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.count = count
        self.metric_total_model = metric_total_model
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.metric_total_model:
            for v1 in self.metric_total_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['MetricTotalModel'] = []
        if self.metric_total_model is not None:
            for k1 in self.metric_total_model:
                result['MetricTotalModel'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.metric_total_model = []
        if m.get('MetricTotalModel') is not None:
            for k1 in m.get('MetricTotalModel'):
                temp_model = main_models.DescribeMetricLastResponseBodyMetricTotalModel()
                self.metric_total_model.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeMetricLastResponseBodyMetricTotalModel(DaraModel):
    def __init__(
        self,
        android_instance_id: str = None,
        metric_model_list: List[main_models.DescribeMetricLastResponseBodyMetricTotalModelMetricModelList] = None,
    ):
        self.android_instance_id = android_instance_id
        self.metric_model_list = metric_model_list

    def validate(self):
        if self.metric_model_list:
            for v1 in self.metric_model_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_id is not None:
            result['AndroidInstanceId'] = self.android_instance_id

        result['MetricModelList'] = []
        if self.metric_model_list is not None:
            for k1 in self.metric_model_list:
                result['MetricModelList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')

        self.metric_model_list = []
        if m.get('MetricModelList') is not None:
            for k1 in m.get('MetricModelList'):
                temp_model = main_models.DescribeMetricLastResponseBodyMetricTotalModelMetricModelList()
                self.metric_model_list.append(temp_model.from_map(k1))

        return self

class DescribeMetricLastResponseBodyMetricTotalModelMetricModelList(DaraModel):
    def __init__(
        self,
        data_points: List[main_models.DescribeMetricLastResponseBodyMetricTotalModelMetricModelListDataPoints] = None,
        metric_name: str = None,
        process_last_infos: List[main_models.DescribeMetricLastResponseBodyMetricTotalModelMetricModelListProcessLastInfos] = None,
    ):
        self.data_points = data_points
        self.metric_name = metric_name
        self.process_last_infos = process_last_infos

    def validate(self):
        if self.data_points:
            for v1 in self.data_points:
                 if v1:
                    v1.validate()
        if self.process_last_infos:
            for v1 in self.process_last_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataPoints'] = []
        if self.data_points is not None:
            for k1 in self.data_points:
                result['DataPoints'].append(k1.to_map() if k1 else None)

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        result['ProcessLastInfos'] = []
        if self.process_last_infos is not None:
            for k1 in self.process_last_infos:
                result['ProcessLastInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_points = []
        if m.get('DataPoints') is not None:
            for k1 in m.get('DataPoints'):
                temp_model = main_models.DescribeMetricLastResponseBodyMetricTotalModelMetricModelListDataPoints()
                self.data_points.append(temp_model.from_map(k1))

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        self.process_last_infos = []
        if m.get('ProcessLastInfos') is not None:
            for k1 in m.get('ProcessLastInfos'):
                temp_model = main_models.DescribeMetricLastResponseBodyMetricTotalModelMetricModelListProcessLastInfos()
                self.process_last_infos.append(temp_model.from_map(k1))

        return self

class DescribeMetricLastResponseBodyMetricTotalModelMetricModelListProcessLastInfos(DaraModel):
    def __init__(
        self,
        cpu_usage: float = None,
        memory_usage: float = None,
        name: str = None,
        process_ids: List[int] = None,
        timestamp: int = None,
    ):
        self.cpu_usage = cpu_usage
        self.memory_usage = memory_usage
        self.name = name
        self.process_ids = process_ids
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_usage is not None:
            result['CpuUsage'] = self.cpu_usage

        if self.memory_usage is not None:
            result['MemoryUsage'] = self.memory_usage

        if self.name is not None:
            result['Name'] = self.name

        if self.process_ids is not None:
            result['ProcessIds'] = self.process_ids

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuUsage') is not None:
            self.cpu_usage = m.get('CpuUsage')

        if m.get('MemoryUsage') is not None:
            self.memory_usage = m.get('MemoryUsage')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProcessIds') is not None:
            self.process_ids = m.get('ProcessIds')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class DescribeMetricLastResponseBodyMetricTotalModelMetricModelListDataPoints(DaraModel):
    def __init__(
        self,
        average: float = None,
        gpu_id: str = None,
        maximum: float = None,
        minimum: float = None,
        timestamp: int = None,
    ):
        self.average = average
        self.gpu_id = gpu_id
        self.maximum = maximum
        self.minimum = minimum
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.average is not None:
            result['Average'] = self.average

        if self.gpu_id is not None:
            result['GpuId'] = self.gpu_id

        if self.maximum is not None:
            result['Maximum'] = self.maximum

        if self.minimum is not None:
            result['Minimum'] = self.minimum

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Average') is not None:
            self.average = m.get('Average')

        if m.get('GpuId') is not None:
            self.gpu_id = m.get('GpuId')

        if m.get('Maximum') is not None:
            self.maximum = m.get('Maximum')

        if m.get('Minimum') is not None:
            self.minimum = m.get('Minimum')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

