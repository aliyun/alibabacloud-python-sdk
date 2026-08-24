# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class GetUserDeviceWorkloadTrendResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        title_en: str = None,
        title_zh: str = None,
        workload_list: List[main_models.GetUserDeviceWorkloadTrendResponseBodyWorkloadList] = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The English name of the workload type. Valid values:
        # - **CPU Usage**: returned when WorkloadType is set to cpu.
        # - **Memory Usage**: returned when WorkloadType is set to mem.
        self.title_en = title_en
        # The Chinese name of the workload type. Valid values:
        # - **CPU使用率**: returned when WorkloadType is set to cpu.
        # - **内存使用率**: returned when WorkloadType is set to mem.
        self.title_zh = title_zh
        # The list of workload trend data points, sorted by time in ascending order.
        self.workload_list = workload_list

    def validate(self):
        if self.workload_list:
            for v1 in self.workload_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.title_en is not None:
            result['TitleEn'] = self.title_en

        if self.title_zh is not None:
            result['TitleZh'] = self.title_zh

        result['WorkloadList'] = []
        if self.workload_list is not None:
            for k1 in self.workload_list:
                result['WorkloadList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TitleEn') is not None:
            self.title_en = m.get('TitleEn')

        if m.get('TitleZh') is not None:
            self.title_zh = m.get('TitleZh')

        self.workload_list = []
        if m.get('WorkloadList') is not None:
            for k1 in m.get('WorkloadList'):
                temp_model = main_models.GetUserDeviceWorkloadTrendResponseBodyWorkloadList()
                self.workload_list.append(temp_model.from_map(k1))

        return self

class GetUserDeviceWorkloadTrendResponseBodyWorkloadList(DaraModel):
    def __init__(
        self,
        timestamp: int = None,
        workload: float = None,
    ):
        # The collection time of the data point. This value is a UNIX timestamp in seconds.
        self.timestamp = timestamp
        # The workload usage percentage. Valid values: 0 to 100, with two decimal places.
        self.workload = workload

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.workload is not None:
            result['Workload'] = self.workload

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Workload') is not None:
            self.workload = m.get('Workload')

        return self

