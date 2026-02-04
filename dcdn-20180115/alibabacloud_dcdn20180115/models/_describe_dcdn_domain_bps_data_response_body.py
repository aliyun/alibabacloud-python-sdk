# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnDomainBpsDataResponseBody(DaraModel):
    def __init__(
        self,
        bps_data_per_interval: main_models.DescribeDcdnDomainBpsDataResponseBodyBpsDataPerInterval = None,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The bandwidth data returned at each interval.
        self.bps_data_per_interval = bps_data_per_interval
        # The time interval between the data entries returned.
        self.data_interval = data_interval
        # The accelerated domain name.
        self.domain_name = domain_name
        # The end of the time range during which data was queried.
        self.end_time = end_time
        # The ID of the request.
        self.request_id = request_id
        # The start of the time range during which data was queried.
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
            temp_model = main_models.DescribeDcdnDomainBpsDataResponseBodyBpsDataPerInterval()
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

class DescribeDcdnDomainBpsDataResponseBodyBpsDataPerInterval(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeDcdnDomainBpsDataResponseBodyBpsDataPerIntervalDataModule] = None,
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
                temp_model = main_models.DescribeDcdnDomainBpsDataResponseBodyBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k1))

        return self

class DescribeDcdnDomainBpsDataResponseBodyBpsDataPerIntervalDataModule(DaraModel):
    def __init__(
        self,
        bps: float = None,
        dynamic_http_bps: float = None,
        dynamic_https_bps: float = None,
        static_http_bps: float = None,
        static_https_bps: float = None,
        time_stamp: str = None,
    ):
        # The bandwidth value. Unit: bit/s.
        self.bps = bps
        # The bandwidth that was consumed to deliver dynamic content over HTTP. Unit: bit/s.
        self.dynamic_http_bps = dynamic_http_bps
        # The bandwidth that was consumed to deliver dynamic content over HTTPS. Unit: bit/s.
        self.dynamic_https_bps = dynamic_https_bps
        # The bandwidth that was consumed to deliver static content over HTTP. Unit: bit/s.
        self.static_http_bps = static_http_bps
        # The bandwidth that was consumed to deliver static content over HTTPS. Unit: bit/s.
        self.static_https_bps = static_https_bps
        # The timestamp of the data returned.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bps is not None:
            result['Bps'] = self.bps

        if self.dynamic_http_bps is not None:
            result['DynamicHttpBps'] = self.dynamic_http_bps

        if self.dynamic_https_bps is not None:
            result['DynamicHttpsBps'] = self.dynamic_https_bps

        if self.static_http_bps is not None:
            result['StaticHttpBps'] = self.static_http_bps

        if self.static_https_bps is not None:
            result['StaticHttpsBps'] = self.static_https_bps

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')

        if m.get('DynamicHttpBps') is not None:
            self.dynamic_http_bps = m.get('DynamicHttpBps')

        if m.get('DynamicHttpsBps') is not None:
            self.dynamic_https_bps = m.get('DynamicHttpsBps')

        if m.get('StaticHttpBps') is not None:
            self.static_http_bps = m.get('StaticHttpBps')

        if m.get('StaticHttpsBps') is not None:
            self.static_https_bps = m.get('StaticHttpsBps')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

