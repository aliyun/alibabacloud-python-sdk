# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDomainBpsDataResponseBody(DaraModel):
    def __init__(
        self,
        bps_data_per_interval: main_models.DescribeLiveDomainBpsDataResponseBodyBpsDataPerInterval = None,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The bandwidth data returned at each interval.
        self.bps_data_per_interval = bps_data_per_interval
        # The time granularity of the query. Unit: seconds.
        self.data_interval = data_interval
        # The streaming domain.
        self.domain_name = domain_name
        # The end of the time range during which the data was queried. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.end_time = end_time
        # The request ID.
        self.request_id = request_id
        # The beginning of the time range during which the data was queried. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.start_time = start_time

    def validate(self):
        if self.bps_data_per_interval:
            self.bps_data_per_interval.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bps_data_per_interval is not None:
            result['BpsDataPerInterval'] = self.bps_data_per_interval.to_map()

        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BpsDataPerInterval') is not None:
            temp_model = main_models.DescribeLiveDomainBpsDataResponseBodyBpsDataPerInterval()
            self.bps_data_per_interval = temp_model.from_map(m.get('BpsDataPerInterval'))

        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeLiveDomainBpsDataResponseBodyBpsDataPerInterval(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeLiveDomainBpsDataResponseBodyBpsDataPerIntervalDataModule] = None,
    ):
        self.data_module = data_module

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
        result['DataModule'] = []
        if self.data_module is not None:
            for k1 in self.data_module:
                result['DataModule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_module = []
        if m.get('DataModule') is not None:
            for k1 in m.get('DataModule'):
                temp_model = main_models.DescribeLiveDomainBpsDataResponseBodyBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k1))

        return self

class DescribeLiveDomainBpsDataResponseBodyBpsDataPerIntervalDataModule(DaraModel):
    def __init__(
        self,
        bps_value: str = None,
        http_bps_value: str = None,
        https_bps_value: str = None,
        time_stamp: str = None,
    ):
        # The bandwidth. Unit: bit/s.
        self.bps_value = bps_value
        # The bandwidth over HTTP. Unit: bit/s.
        self.http_bps_value = http_bps_value
        # The bandwidth over HTTPS. Unit: bit/s.
        self.https_bps_value = https_bps_value
        # The timestamp of the data returned.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bps_value is not None:
            result['BpsValue'] = self.bps_value

        if self.http_bps_value is not None:
            result['HttpBpsValue'] = self.http_bps_value

        if self.https_bps_value is not None:
            result['HttpsBpsValue'] = self.https_bps_value

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BpsValue') is not None:
            self.bps_value = m.get('BpsValue')

        if m.get('HttpBpsValue') is not None:
            self.http_bps_value = m.get('HttpBpsValue')

        if m.get('HttpsBpsValue') is not None:
            self.https_bps_value = m.get('HttpsBpsValue')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

