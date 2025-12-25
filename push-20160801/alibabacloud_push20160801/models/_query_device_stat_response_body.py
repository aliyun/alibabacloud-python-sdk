# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_push20160801 import models as main_models
from darabonba.model import DaraModel

class QueryDeviceStatResponseBody(DaraModel):
    def __init__(
        self,
        app_device_stats: main_models.QueryDeviceStatResponseBodyAppDeviceStats = None,
        request_id: str = None,
    ):
        self.app_device_stats = app_device_stats
        self.request_id = request_id

    def validate(self):
        if self.app_device_stats:
            self.app_device_stats.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_device_stats is not None:
            result['AppDeviceStats'] = self.app_device_stats.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppDeviceStats') is not None:
            temp_model = main_models.QueryDeviceStatResponseBodyAppDeviceStats()
            self.app_device_stats = temp_model.from_map(m.get('AppDeviceStats'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryDeviceStatResponseBodyAppDeviceStats(DaraModel):
    def __init__(
        self,
        app_device_stat: List[main_models.QueryDeviceStatResponseBodyAppDeviceStatsAppDeviceStat] = None,
    ):
        self.app_device_stat = app_device_stat

    def validate(self):
        if self.app_device_stat:
            for v1 in self.app_device_stat:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppDeviceStat'] = []
        if self.app_device_stat is not None:
            for k1 in self.app_device_stat:
                result['AppDeviceStat'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_device_stat = []
        if m.get('AppDeviceStat') is not None:
            for k1 in m.get('AppDeviceStat'):
                temp_model = main_models.QueryDeviceStatResponseBodyAppDeviceStatsAppDeviceStat()
                self.app_device_stat.append(temp_model.from_map(k1))

        return self

class QueryDeviceStatResponseBodyAppDeviceStatsAppDeviceStat(DaraModel):
    def __init__(
        self,
        count: int = None,
        device_type: str = None,
        time: str = None,
    ):
        self.count = count
        self.device_type = device_type
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

