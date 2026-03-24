# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainQpsDataByLayerResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        layer: str = None,
        qps_data_interval: main_models.DescribeDomainQpsDataByLayerResponseBodyQpsDataInterval = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The time interval between the data entries returned. Unit: seconds.
        self.data_interval = data_interval
        # The accelerated domain name.
        self.domain_name = domain_name
        # The end of the time range during which data was queried.
        self.end_time = end_time
        # The layer at which the data was collected.
        self.layer = layer
        self.qps_data_interval = qps_data_interval
        # The ID of the request.
        self.request_id = request_id
        # The start of the time range during which data was queried.
        self.start_time = start_time

    def validate(self):
        if self.qps_data_interval:
            self.qps_data_interval.validate()

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

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.qps_data_interval is not None:
            result['QpsDataInterval'] = self.qps_data_interval.to_map()

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

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('QpsDataInterval') is not None:
            temp_model = main_models.DescribeDomainQpsDataByLayerResponseBodyQpsDataInterval()
            self.qps_data_interval = temp_model.from_map(m.get('QpsDataInterval'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeDomainQpsDataByLayerResponseBodyQpsDataInterval(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeDomainQpsDataByLayerResponseBodyQpsDataIntervalDataModule] = None,
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
                temp_model = main_models.DescribeDomainQpsDataByLayerResponseBodyQpsDataIntervalDataModule()
                self.data_module.append(temp_model.from_map(k1))

        return self

class DescribeDomainQpsDataByLayerResponseBodyQpsDataIntervalDataModule(DaraModel):
    def __init__(
        self,
        acc_domestic_value: str = None,
        acc_overseas_value: str = None,
        acc_value: str = None,
        domestic_value: str = None,
        overseas_value: str = None,
        time_stamp: str = None,
        value: str = None,
    ):
        self.acc_domestic_value = acc_domestic_value
        self.acc_overseas_value = acc_overseas_value
        self.acc_value = acc_value
        self.domestic_value = domestic_value
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
        if self.acc_domestic_value is not None:
            result['AccDomesticValue'] = self.acc_domestic_value

        if self.acc_overseas_value is not None:
            result['AccOverseasValue'] = self.acc_overseas_value

        if self.acc_value is not None:
            result['AccValue'] = self.acc_value

        if self.domestic_value is not None:
            result['DomesticValue'] = self.domestic_value

        if self.overseas_value is not None:
            result['OverseasValue'] = self.overseas_value

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccDomesticValue') is not None:
            self.acc_domestic_value = m.get('AccDomesticValue')

        if m.get('AccOverseasValue') is not None:
            self.acc_overseas_value = m.get('AccOverseasValue')

        if m.get('AccValue') is not None:
            self.acc_value = m.get('AccValue')

        if m.get('DomesticValue') is not None:
            self.domestic_value = m.get('DomesticValue')

        if m.get('OverseasValue') is not None:
            self.overseas_value = m.get('OverseasValue')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

