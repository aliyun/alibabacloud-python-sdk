# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class DescribeMetricTopResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        metric_total_model: List[main_models.DescribeMetricTopResponseBodyMetricTotalModel] = None,
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
                temp_model = main_models.DescribeMetricTopResponseBodyMetricTotalModel()
                self.metric_total_model.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeMetricTopResponseBodyMetricTotalModel(DaraModel):
    def __init__(
        self,
        android_instance_id: str = None,
        instance_id: str = None,
        metric_model_list: List[main_models.DescribeMetricTopResponseBodyMetricTotalModelMetricModelList] = None,
    ):
        self.android_instance_id = android_instance_id
        self.instance_id = instance_id
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['MetricModelList'] = []
        if self.metric_model_list is not None:
            for k1 in self.metric_model_list:
                result['MetricModelList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceId') is not None:
            self.android_instance_id = m.get('AndroidInstanceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.metric_model_list = []
        if m.get('MetricModelList') is not None:
            for k1 in m.get('MetricModelList'):
                temp_model = main_models.DescribeMetricTopResponseBodyMetricTotalModelMetricModelList()
                self.metric_model_list.append(temp_model.from_map(k1))

        return self

class DescribeMetricTopResponseBodyMetricTotalModelMetricModelList(DaraModel):
    def __init__(
        self,
        data_points: List[main_models.DescribeMetricTopResponseBodyMetricTotalModelMetricModelListDataPoints] = None,
        metric_name: str = None,
    ):
        self.data_points = data_points
        self.metric_name = metric_name

    def validate(self):
        if self.data_points:
            for v1 in self.data_points:
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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_points = []
        if m.get('DataPoints') is not None:
            for k1 in m.get('DataPoints'):
                temp_model = main_models.DescribeMetricTopResponseBodyMetricTotalModelMetricModelListDataPoints()
                self.data_points.append(temp_model.from_map(k1))

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        return self

class DescribeMetricTopResponseBodyMetricTotalModelMetricModelListDataPoints(DaraModel):
    def __init__(
        self,
        average: float = None,
        id: str = None,
        maximum: float = None,
        minimum: float = None,
        name: str = None,
        properties: str = None,
        timestamp: int = None,
    ):
        self.average = average
        self.id = id
        self.maximum = maximum
        self.minimum = minimum
        self.name = name
        self.properties = properties
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

        if self.id is not None:
            result['Id'] = self.id

        if self.maximum is not None:
            result['Maximum'] = self.maximum

        if self.minimum is not None:
            result['Minimum'] = self.minimum

        if self.name is not None:
            result['Name'] = self.name

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Average') is not None:
            self.average = m.get('Average')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Maximum') is not None:
            self.maximum = m.get('Maximum')

        if m.get('Minimum') is not None:
            self.minimum = m.get('Minimum')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

