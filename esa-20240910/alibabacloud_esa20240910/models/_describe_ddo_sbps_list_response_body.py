# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class DescribeDDoSBpsListResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: int = None,
        data_module: List[main_models.DescribeDDoSBpsListResponseBodyDataModule] = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The interval between each piece of data, in seconds.
        # 
        # Generated based on the interval between StartTime and EndTime: less than 1 hour, 60s; 1 hour or more but less than 1 day, 300s; 1 day or more but less than a week, 1800s; 1 week or more, 3600s.
        self.data_interval = data_interval
        # A list of network bandwidth data for each time interval.
        self.data_module = data_module
        # The end time for fetching data. In ISO8601 format, using UTC+0, formatted as: yyyy-MM-ddTHH:mm:ssZ.
        # 
        # The end time must be later than the start time, and the span between start and end times should not exceed 31 days.
        self.end_time = end_time
        # Request ID.
        self.request_id = request_id
        # The start time for fetching data. In ISO8601 format, using UTC, formatted as: YYYY-MM-DDThh:mm:ssZ.
        self.start_time = start_time

    def validate(self):
        if self.data_module:
            for v1 in self.data_module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval

        result['DataModule'] = []
        if self.data_module is not None:
            for k1 in self.data_module:
                result['DataModule'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')

        self.data_module = []
        if m.get('DataModule') is not None:
            for k1 in m.get('DataModule'):
                temp_model = main_models.DescribeDDoSBpsListResponseBodyDataModule()
                self.data_module.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeDDoSBpsListResponseBodyDataModule(DaraModel):
    def __init__(
        self,
        attack_bps: int = None,
        attack_pps: int = None,
        normal_bps: int = None,
        normal_pps: int = None,
        time_stamp: str = None,
        total_bps: int = None,
        total_pps: int = None,
    ):
        # Attack bandwidth, in bps.
        self.attack_bps = attack_bps
        # Attack PPS.
        self.attack_pps = attack_pps
        # Normal business bandwidth, in bps.
        self.normal_bps = normal_bps
        # Normal business PPS.
        self.normal_pps = normal_pps
        # The timestamp of this data, in ISO8601 format, using UTC+0, formatted as: yyyy-MM-ddTHH:mm:ssZ.
        self.time_stamp = time_stamp
        # Total bandwidth, in bps.
        self.total_bps = total_bps
        # Total PPS.
        self.total_pps = total_pps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_bps is not None:
            result['AttackBps'] = self.attack_bps

        if self.attack_pps is not None:
            result['AttackPps'] = self.attack_pps

        if self.normal_bps is not None:
            result['NormalBps'] = self.normal_bps

        if self.normal_pps is not None:
            result['NormalPps'] = self.normal_pps

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.total_bps is not None:
            result['TotalBps'] = self.total_bps

        if self.total_pps is not None:
            result['TotalPps'] = self.total_pps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackBps') is not None:
            self.attack_bps = m.get('AttackBps')

        if m.get('AttackPps') is not None:
            self.attack_pps = m.get('AttackPps')

        if m.get('NormalBps') is not None:
            self.normal_bps = m.get('NormalBps')

        if m.get('NormalPps') is not None:
            self.normal_pps = m.get('NormalPps')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('TotalBps') is not None:
            self.total_bps = m.get('TotalBps')

        if m.get('TotalPps') is not None:
            self.total_pps = m.get('TotalPps')

        return self

