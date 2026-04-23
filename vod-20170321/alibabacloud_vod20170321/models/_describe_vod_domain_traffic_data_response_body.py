# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class DescribeVodDomainTrafficDataResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        total_traffic: str = None,
        traffic_data_per_interval: main_models.DescribeVodDomainTrafficDataResponseBodyTrafficDataPerInterval = None,
    ):
        # The time interval at which data is returned, which is the time granularity. Unit: seconds.
        self.data_interval = data_interval
        # The accelerated domain name.
        self.domain_name = domain_name
        # The end of the time range.
        self.end_time = end_time
        # The ID of the request.
        self.request_id = request_id
        # The beginning of the time range.
        self.start_time = start_time
        # The total amount of network traffic.
        self.total_traffic = total_traffic
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

        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic

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

        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')

        if m.get('TrafficDataPerInterval') is not None:
            temp_model = main_models.DescribeVodDomainTrafficDataResponseBodyTrafficDataPerInterval()
            self.traffic_data_per_interval = temp_model.from_map(m.get('TrafficDataPerInterval'))

        return self

class DescribeVodDomainTrafficDataResponseBodyTrafficDataPerInterval(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeVodDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule] = None,
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
                temp_model = main_models.DescribeVodDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k1))

        return self

class DescribeVodDomainTrafficDataResponseBodyTrafficDataPerIntervalDataModule(DaraModel):
    def __init__(
        self,
        domestic_value: str = None,
        https_domestic_value: str = None,
        https_overseas_value: str = None,
        https_value: str = None,
        overseas_value: str = None,
        time_stamp: str = None,
        value: str = None,
    ):
        self.domestic_value = domestic_value
        self.https_domestic_value = https_domestic_value
        self.https_overseas_value = https_overseas_value
        self.https_value = https_value
        self.overseas_value = overseas_value
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domestic_value is not None:
            result['DomesticValue'] = self.domestic_value

        if self.https_domestic_value is not None:
            result['HttpsDomesticValue'] = self.https_domestic_value

        if self.https_overseas_value is not None:
            result['HttpsOverseasValue'] = self.https_overseas_value

        if self.https_value is not None:
            result['HttpsValue'] = self.https_value

        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomesticValue') is not None:
            self.domestic_value = m.get('DomesticValue')

        if m.get('HttpsDomesticValue') is not None:
            self.https_domestic_value = m.get('HttpsDomesticValue')

        if m.get('HttpsOverseasValue') is not None:
            self.https_overseas_value = m.get('HttpsOverseasValue')

        if m.get('HttpsValue') is not None:
            self.https_value = m.get('HttpsValue')

        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

