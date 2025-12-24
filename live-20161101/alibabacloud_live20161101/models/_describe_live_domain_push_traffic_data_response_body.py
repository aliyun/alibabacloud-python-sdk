# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDomainPushTrafficDataResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        traffic_data_per_interval: main_models.DescribeLiveDomainPushTrafficDataResponseBodyTrafficDataPerInterval = None,
    ):
        # The time granularity.
        self.data_interval = data_interval
        # The ingest domain.
        self.domain_name = domain_name
        # The end of the time range during which the data was queried.
        self.end_time = end_time
        # The request ID.
        self.request_id = request_id
        # The beginning of the time range during which the data was queried.
        self.start_time = start_time
        # The traffic data that was collected at each interval.
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
            temp_model = main_models.DescribeLiveDomainPushTrafficDataResponseBodyTrafficDataPerInterval()
            self.traffic_data_per_interval = temp_model.from_map(m.get('TrafficDataPerInterval'))

        return self

class DescribeLiveDomainPushTrafficDataResponseBodyTrafficDataPerInterval(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeLiveDomainPushTrafficDataResponseBodyTrafficDataPerIntervalDataModule] = None,
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
                temp_model = main_models.DescribeLiveDomainPushTrafficDataResponseBodyTrafficDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k1))

        return self

class DescribeLiveDomainPushTrafficDataResponseBodyTrafficDataPerIntervalDataModule(DaraModel):
    def __init__(
        self,
        time_stamp: str = None,
        traffic_value: str = None,
    ):
        # The timestamp of the data returned.
        self.time_stamp = time_stamp
        # The traffic. Unit: bytes.
        self.traffic_value = traffic_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.traffic_value is not None:
            result['TrafficValue'] = self.traffic_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('TrafficValue') is not None:
            self.traffic_value = m.get('TrafficValue')

        return self

