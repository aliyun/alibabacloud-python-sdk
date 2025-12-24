# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeSnapshotMonitorDataResponseBody(DaraModel):
    def __init__(
        self,
        monitor_data: main_models.DescribeSnapshotMonitorDataResponseBodyMonitorData = None,
        request_id: str = None,
    ):
        # The monitoring data of snapshot sizes.
        self.monitor_data = monitor_data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.monitor_data:
            self.monitor_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.monitor_data is not None:
            result['MonitorData'] = self.monitor_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorData') is not None:
            temp_model = main_models.DescribeSnapshotMonitorDataResponseBodyMonitorData()
            self.monitor_data = temp_model.from_map(m.get('MonitorData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeSnapshotMonitorDataResponseBodyMonitorData(DaraModel):
    def __init__(
        self,
        data_point: List[main_models.DescribeSnapshotMonitorDataResponseBodyMonitorDataDataPoint] = None,
    ):
        self.data_point = data_point

    def validate(self):
        if self.data_point:
            for v1 in self.data_point:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataPoint'] = []
        if self.data_point is not None:
            for k1 in self.data_point:
                result['DataPoint'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_point = []
        if m.get('DataPoint') is not None:
            for k1 in m.get('DataPoint'):
                temp_model = main_models.DescribeSnapshotMonitorDataResponseBodyMonitorDataDataPoint()
                self.data_point.append(temp_model.from_map(k1))

        return self

class DescribeSnapshotMonitorDataResponseBodyMonitorDataDataPoint(DaraModel):
    def __init__(
        self,
        size: int = None,
        time_stamp: str = None,
    ):
        # The total size of snapshots. Unit: bytes.
        self.size = size
        # The timestamp that corresponds to a snapshot size.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.size is not None:
            result['Size'] = self.size

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

