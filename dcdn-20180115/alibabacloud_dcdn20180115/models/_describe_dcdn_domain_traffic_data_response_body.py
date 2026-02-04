# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnDomainTrafficDataResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        traffic_data_per_interval: main_models.DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerInterval = None,
    ):
        # The time interval between the data entries returned. Unit: seconds.
        self.data_interval = data_interval
        # The accelerated domain name.
        self.domain_name = domain_name
        # The end of the time range during which data was queried.
        self.end_time = end_time
        # The ID of the request.
        self.request_id = request_id
        # The start of the time range during which data was queried.
        self.start_time = start_time
        # The network traffic returned at each time interval. Unit: bytes.
        self.traffic_data_per_interval = traffic_data_per_interval

    def validate(self):
        if self.traffic_data_per_interval:
            self.traffic_data_per_interval.validate()

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.traffic_data_per_interval is not None:
            result['TrafficDataPerInterval'] = self.traffic_data_per_interval.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('TrafficDataPerInterval') is not None:
            temp_model = main_models.DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerInterval()
            self.traffic_data_per_interval = temp_model.from_map(m.get('TrafficDataPerInterval'))

        return self

class DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerInterval(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule] = None,
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
                temp_model = main_models.DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k1))

        return self

class DescribeDcdnDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule(DaraModel):
    def __init__(
        self,
        dynamic_http_traffic: float = None,
        dynamic_https_traffic: float = None,
        static_http_traffic: float = None,
        static_https_traffic: float = None,
        time_stamp: str = None,
        traffic: float = None,
    ):
        # The network traffic that was consumed to deliver dynamic content over HTTP.
        self.dynamic_http_traffic = dynamic_http_traffic
        # The network traffic that was consumed to deliver dynamic content over HTTPS.
        self.dynamic_https_traffic = dynamic_https_traffic
        # The network traffic that was consumed to deliver static content over HTTP.
        self.static_http_traffic = static_http_traffic
        # The network traffic that was consumed to deliver static content over HTTPS.
        self.static_https_traffic = static_https_traffic
        # The timestamp of the data returned.
        self.time_stamp = time_stamp
        # The total amount of network traffic.
        self.traffic = traffic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dynamic_http_traffic is not None:
            result['DynamicHttpTraffic'] = self.dynamic_http_traffic

        if self.dynamic_https_traffic is not None:
            result['DynamicHttpsTraffic'] = self.dynamic_https_traffic

        if self.static_http_traffic is not None:
            result['StaticHttpTraffic'] = self.static_http_traffic

        if self.static_https_traffic is not None:
            result['StaticHttpsTraffic'] = self.static_https_traffic

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.traffic is not None:
            result['Traffic'] = self.traffic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicHttpTraffic') is not None:
            self.dynamic_http_traffic = m.get('DynamicHttpTraffic')

        if m.get('DynamicHttpsTraffic') is not None:
            self.dynamic_https_traffic = m.get('DynamicHttpsTraffic')

        if m.get('StaticHttpTraffic') is not None:
            self.static_http_traffic = m.get('StaticHttpTraffic')

        if m.get('StaticHttpsTraffic') is not None:
            self.static_https_traffic = m.get('StaticHttpsTraffic')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')

        return self

