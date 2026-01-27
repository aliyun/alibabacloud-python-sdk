# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_ebs20210730 import models as main_models
from darabonba.model import DaraModel

class DescribeMetricDataResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeMetricDataResponseBodyDataList] = None,
        request_id: str = None,
        total_count: int = None,
        warnings: List[str] = None,
    ):
        # Collection of monitoring data for the cloud disk.
        self.data_list = data_list
        # Request ID.
        self.request_id = request_id
        # Total number of data points queried.
        self.total_count = total_count
        # List of warning messages.
        self.warnings = warnings

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.warnings is not None:
            result['Warnings'] = self.warnings

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeMetricDataResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('Warnings') is not None:
            self.warnings = m.get('Warnings')

        return self

class DescribeMetricDataResponseBodyDataList(DaraModel):
    def __init__(
        self,
        datapoints: Any = None,
        labels: Any = None,
    ):
        # List of monitoring data, consisting of a series of consecutive second-level timestamps and the corresponding metric values at those times.
        self.datapoints = datapoints
        # Labels.
        self.labels = labels

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.datapoints is not None:
            result['Datapoints'] = self.datapoints

        if self.labels is not None:
            result['Labels'] = self.labels

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Datapoints') is not None:
            self.datapoints = m.get('Datapoints')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        return self

