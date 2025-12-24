# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDomainBpsDataByLayerResponseBody(DaraModel):
    def __init__(
        self,
        bps_data_interval: main_models.DescribeLiveDomainBpsDataByLayerResponseBodyBpsDataInterval = None,
        data_interval: str = None,
        request_id: str = None,
    ):
        # The data returned at each time interval.
        self.bps_data_interval = bps_data_interval
        # The time interval between the data entries returned. Unit: seconds.
        self.data_interval = data_interval
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.bps_data_interval:
            self.bps_data_interval.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bps_data_interval is not None:
            result['BpsDataInterval'] = self.bps_data_interval.to_map()

        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BpsDataInterval') is not None:
            temp_model = main_models.DescribeLiveDomainBpsDataByLayerResponseBodyBpsDataInterval()
            self.bps_data_interval = temp_model.from_map(m.get('BpsDataInterval'))

        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveDomainBpsDataByLayerResponseBodyBpsDataInterval(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeLiveDomainBpsDataByLayerResponseBodyBpsDataIntervalDataModule] = None,
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
                temp_model = main_models.DescribeLiveDomainBpsDataByLayerResponseBodyBpsDataIntervalDataModule()
                self.data_module.append(temp_model.from_map(k1))

        return self

class DescribeLiveDomainBpsDataByLayerResponseBodyBpsDataIntervalDataModule(DaraModel):
    def __init__(
        self,
        time_stamp: str = None,
        traffic_value: str = None,
        value: str = None,
    ):
        # The timestamp of the data returned.
        self.time_stamp = time_stamp
        # The total traffic. Unit: bytes.
        self.traffic_value = traffic_value
        # The peak bandwidth. Unit: bit/s.
        self.value = value

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

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('TrafficValue') is not None:
            self.traffic_value = m.get('TrafficValue')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

