# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnDomainOriginBpsDataResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        origin_bps_data_per_interval: main_models.DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerInterval = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The time interval between the data entries returned. Unit: seconds.
        self.data_interval = data_interval
        # The accelerated domain name.
        self.domain_name = domain_name
        # The end of the time range during which data was queried.
        self.end_time = end_time
        # The origin bandwidth data returned at each time interval. Unit: bit/s.
        self.origin_bps_data_per_interval = origin_bps_data_per_interval
        # The ID of the request.
        self.request_id = request_id
        # The start of the time range during which data was queried.
        self.start_time = start_time

    def validate(self):
        if self.origin_bps_data_per_interval:
            self.origin_bps_data_per_interval.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.origin_bps_data_per_interval is not None:
            result['OriginBpsDataPerInterval'] = self.origin_bps_data_per_interval.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OriginBpsDataPerInterval') is not None:
            temp_model = main_models.DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerInterval()
            self.origin_bps_data_per_interval = temp_model.from_map(m.get('OriginBpsDataPerInterval'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerInterval(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerIntervalDataModule] = None,
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
                temp_model = main_models.DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k1))

        return self

class DescribeDcdnDomainOriginBpsDataResponseBodyOriginBpsDataPerIntervalDataModule(DaraModel):
    def __init__(
        self,
        dynamic_http_origin_bps: float = None,
        dynamic_https_origin_bps: float = None,
        origin_bps: float = None,
        static_http_origin_bps: float = None,
        static_https_origin_bps: float = None,
        time_stamp: str = None,
    ):
        # The bandwidth that was consumed for fetching dynamic content from the origin over HTTP.
        self.dynamic_http_origin_bps = dynamic_http_origin_bps
        # The bandwidth that was consumed for fetching dynamic content from the origin over HTTPS.
        self.dynamic_https_origin_bps = dynamic_https_origin_bps
        # The bandwidth that was consumed for fetching content from the origin.
        self.origin_bps = origin_bps
        # The bandwidth that was consumed for fetching static content from the origin over HTTP.
        self.static_http_origin_bps = static_http_origin_bps
        # The bandwidth that was consumed for fetching static content from the origin over HTTPS.
        self.static_https_origin_bps = static_https_origin_bps
        # The timestamp of the returned data.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_http_origin_bps is not None:
            result['DynamicHttpOriginBps'] = self.dynamic_http_origin_bps

        if self.dynamic_https_origin_bps is not None:
            result['DynamicHttpsOriginBps'] = self.dynamic_https_origin_bps

        if self.origin_bps is not None:
            result['OriginBps'] = self.origin_bps

        if self.static_http_origin_bps is not None:
            result['StaticHttpOriginBps'] = self.static_http_origin_bps

        if self.static_https_origin_bps is not None:
            result['StaticHttpsOriginBps'] = self.static_https_origin_bps

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicHttpOriginBps') is not None:
            self.dynamic_http_origin_bps = m.get('DynamicHttpOriginBps')

        if m.get('DynamicHttpsOriginBps') is not None:
            self.dynamic_https_origin_bps = m.get('DynamicHttpsOriginBps')

        if m.get('OriginBps') is not None:
            self.origin_bps = m.get('OriginBps')

        if m.get('StaticHttpOriginBps') is not None:
            self.static_http_origin_bps = m.get('StaticHttpOriginBps')

        if m.get('StaticHttpsOriginBps') is not None:
            self.static_https_origin_bps = m.get('StaticHttpsOriginBps')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

