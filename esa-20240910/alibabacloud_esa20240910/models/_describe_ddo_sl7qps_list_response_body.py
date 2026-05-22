# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class DescribeDDoSL7QpsListResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: int = None,
        data_module: List[main_models.DescribeDDoSL7QpsListResponseBodyDataModule] = None,
        end_time: str = None,
        record_id: int = None,
        request_id: str = None,
        site_id: int = None,
        start_time: str = None,
    ):
        # The time granularity of the queried data, in seconds.
        self.data_interval = data_interval
        # Application layer time trend data list.
        self.data_module = data_module
        # The end time of the query.
        # 
        # The date format follows ISO8601 notation and uses UTC+0, formatted as yyyy-MM-ddTHH:mm:ssZ.
        self.end_time = end_time
        # Record ID.
        self.record_id = record_id
        # Request ID.
        self.request_id = request_id
        # Site ID.
        self.site_id = site_id
        # The start time of the query.
        # 
        # The date format follows ISO8601 notation and uses UTC+0, formatted as yyyy-MM-ddTHH:mm:ssZ.
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

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

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
                temp_model = main_models.DescribeDDoSL7QpsListResponseBodyDataModule()
                self.data_module.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeDDoSL7QpsListResponseBodyDataModule(DaraModel):
    def __init__(
        self,
        attack: int = None,
        normal: int = None,
        time_stamp: str = None,
        total: int = None,
    ):
        # Attack QPS.
        self.attack = attack
        # Normal QPS.
        self.normal = normal
        # Data time, following ISO8601 notation and using UTC+0, formatted as yyyy-MM-ddTHH:mm:ssZ.
        self.time_stamp = time_stamp
        # Total QPS.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack is not None:
            result['Attack'] = self.attack

        if self.normal is not None:
            result['Normal'] = self.normal

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attack') is not None:
            self.attack = m.get('Attack')

        if m.get('Normal') is not None:
            self.normal = m.get('Normal')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

