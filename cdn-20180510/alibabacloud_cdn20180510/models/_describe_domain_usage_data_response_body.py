# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainUsageDataResponseBody(DaraModel):
    def __init__(
        self,
        area: str = None,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        type: str = None,
        usage_data_per_interval: main_models.DescribeDomainUsageDataResponseBodyUsageDataPerInterval = None,
    ):
        # The ID of the billable region where the data was collected.
        self.area = area
        # The time interval between the data entries returned. Unit: seconds.
        self.data_interval = data_interval
        # The accelerated domain name.
        self.domain_name = domain_name
        # The end of the time range during which data was queried.
        self.end_time = end_time
        # The ID of the request.
        self.request_id = request_id
        # The beginning of the time range during which data was queried.
        self.start_time = start_time
        # The type of content.
        self.type = type
        self.usage_data_per_interval = usage_data_per_interval

    def validate(self):
        if self.usage_data_per_interval:
            self.usage_data_per_interval.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

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

        if self.type is not None:
            result['Type'] = self.type

        if self.usage_data_per_interval is not None:
            result['UsageDataPerInterval'] = self.usage_data_per_interval.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

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

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UsageDataPerInterval') is not None:
            temp_model = main_models.DescribeDomainUsageDataResponseBodyUsageDataPerInterval()
            self.usage_data_per_interval = temp_model.from_map(m.get('UsageDataPerInterval'))

        return self

class DescribeDomainUsageDataResponseBodyUsageDataPerInterval(DaraModel):
    def __init__(
        self,
        data_module: List[main_models.DescribeDomainUsageDataResponseBodyUsageDataPerIntervalDataModule] = None,
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
                temp_model = main_models.DescribeDomainUsageDataResponseBodyUsageDataPerIntervalDataModule()
                self.data_module.append(temp_model.from_map(k1))

        return self

class DescribeDomainUsageDataResponseBodyUsageDataPerIntervalDataModule(DaraModel):
    def __init__(
        self,
        peak_time: str = None,
        special_value: str = None,
        time_stamp: str = None,
        value: str = None,
    ):
        self.peak_time = peak_time
        self.special_value = special_value
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.peak_time is not None:
            result['PeakTime'] = self.peak_time

        if self.special_value is not None:
            result['SpecialValue'] = self.special_value

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PeakTime') is not None:
            self.peak_time = m.get('PeakTime')

        if m.get('SpecialValue') is not None:
            self.special_value = m.get('SpecialValue')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

