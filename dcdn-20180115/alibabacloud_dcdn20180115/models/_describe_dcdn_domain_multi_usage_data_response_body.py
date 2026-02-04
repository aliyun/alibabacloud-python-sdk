# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnDomainMultiUsageDataResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        request_id: str = None,
        request_per_interval: main_models.DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerInterval = None,
        start_time: str = None,
        traffic_per_interval: main_models.DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerInterval = None,
    ):
        # The end of the time range that was queried.
        self.end_time = end_time
        # The ID of the request.
        self.request_id = request_id
        # The information about requests collected every 5 minutes.
        self.request_per_interval = request_per_interval
        # The beginning of the time range that was queried.
        self.start_time = start_time
        # The statistics of network traffic collected every 5 minutes.
        self.traffic_per_interval = traffic_per_interval

    def validate(self):
        if self.request_per_interval:
            self.request_per_interval.validate()
        if self.traffic_per_interval:
            self.traffic_per_interval.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.request_per_interval is not None:
            result['RequestPerInterval'] = self.request_per_interval.to_map()

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.traffic_per_interval is not None:
            result['TrafficPerInterval'] = self.traffic_per_interval.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequestPerInterval') is not None:
            temp_model = main_models.DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerInterval()
            self.request_per_interval = temp_model.from_map(m.get('RequestPerInterval'))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TrafficPerInterval') is not None:
            temp_model = main_models.DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerInterval()
            self.traffic_per_interval = temp_model.from_map(m.get('TrafficPerInterval'))

        return self

class DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerInterval(DaraModel):
    def __init__(
        self,
        traffic_data_module: List[main_models.DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerIntervalTrafficDataModule] = None,
    ):
        self.traffic_data_module = traffic_data_module

    def validate(self):
        if self.traffic_data_module:
            for v1 in self.traffic_data_module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TrafficDataModule'] = []
        if self.traffic_data_module is not None:
            for k1 in self.traffic_data_module:
                result['TrafficDataModule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.traffic_data_module = []
        if m.get('TrafficDataModule') is not None:
            for k1 in m.get('TrafficDataModule'):
                temp_model = main_models.DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerIntervalTrafficDataModule()
                self.traffic_data_module.append(temp_model.from_map(k1))

        return self

class DescribeDcdnDomainMultiUsageDataResponseBodyTrafficPerIntervalTrafficDataModule(DaraModel):
    def __init__(
        self,
        area: str = None,
        bps: float = None,
        domain: str = None,
        time_stamp: str = None,
        type: str = None,
    ):
        # The name of the region.
        self.area = area
        # The number of bits per second.
        self.bps = bps
        # The domain name.
        self.domain = domain
        # The timestamp of the data returned.
        self.time_stamp = time_stamp
        # The type of the network traffic. Valid values: Simple, IPA, and WebSocket.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.bps is not None:
            result['Bps'] = self.bps

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('Bps') is not None:
            self.bps = m.get('Bps')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerInterval(DaraModel):
    def __init__(
        self,
        request_data_module: List[main_models.DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerIntervalRequestDataModule] = None,
    ):
        self.request_data_module = request_data_module

    def validate(self):
        if self.request_data_module:
            for v1 in self.request_data_module:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RequestDataModule'] = []
        if self.request_data_module is not None:
            for k1 in self.request_data_module:
                result['RequestDataModule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_data_module = []
        if m.get('RequestDataModule') is not None:
            for k1 in m.get('RequestDataModule'):
                temp_model = main_models.DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerIntervalRequestDataModule()
                self.request_data_module.append(temp_model.from_map(k1))

        return self

class DescribeDcdnDomainMultiUsageDataResponseBodyRequestPerIntervalRequestDataModule(DaraModel):
    def __init__(
        self,
        domain: str = None,
        request: int = None,
        time_stamp: str = None,
        type: str = None,
    ):
        # The domain name.
        self.domain = domain
        # The number of requests.
        self.request = request
        # The timestamp of the data returned.
        self.time_stamp = time_stamp
        # The type of the requests. Valid values: StaticHttps, DynamicHttps, DynamicHttp, StaticQuic, and DynamicQuic.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.request is not None:
            result['Request'] = self.request

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Request') is not None:
            self.request = m.get('Request')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

