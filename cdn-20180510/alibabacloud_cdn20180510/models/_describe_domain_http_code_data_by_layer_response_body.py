# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainHttpCodeDataByLayerResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        http_code_data_interval: main_models.DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataInterval = None,
        request_id: str = None,
    ):
        # The time interval between the data entries returned. Unit: seconds.
        self.data_interval = data_interval
        self.http_code_data_interval = http_code_data_interval
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.http_code_data_interval:
            self.http_code_data_interval.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_interval is not None:
            result['DataInterval'] = self.data_interval

        if self.http_code_data_interval is not None:
            result['HttpCodeDataInterval'] = self.http_code_data_interval.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')

        if m.get('HttpCodeDataInterval') is not None:
            temp_model = main_models.DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataInterval()
            self.http_code_data_interval = temp_model.from_map(m.get('HttpCodeDataInterval'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataInterval(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataIntervalDataModule] = None,
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
                temp_model = main_models.DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataIntervalDataModule()
                self.data_module.append(temp_model.from_map(k1))

        return self

class DescribeDomainHttpCodeDataByLayerResponseBodyHttpCodeDataIntervalDataModule(DaraModel):
    def __init__(
        self,
        time_stamp: str = None,
        total_value: str = None,
        value: str = None,
    ):
        self.time_stamp = time_stamp
        self.total_value = total_value
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

        if self.total_value is not None:
            result['TotalValue'] = self.total_value

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('TotalValue') is not None:
            self.total_value = m.get('TotalValue')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

