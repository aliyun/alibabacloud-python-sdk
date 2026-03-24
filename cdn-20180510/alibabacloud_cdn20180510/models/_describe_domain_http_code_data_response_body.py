# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainHttpCodeDataResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        http_code_data: main_models.DescribeDomainHttpCodeDataResponseBodyHttpCodeData = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The time interval.
        self.data_interval = data_interval
        # The accelerated domain name.
        self.domain_name = domain_name
        # The end of the time range during which data was queried.
        self.end_time = end_time
        self.http_code_data = http_code_data
        # The ID of the request.
        self.request_id = request_id
        # The beginning of the time range during which data was queried.
        self.start_time = start_time

    def validate(self):
        if self.http_code_data:
            self.http_code_data.validate()

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

        if self.http_code_data is not None:
            result['HttpCodeData'] = self.http_code_data.to_map()

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

        if m.get('HttpCodeData') is not None:
            temp_model = main_models.DescribeDomainHttpCodeDataResponseBodyHttpCodeData()
            self.http_code_data = temp_model.from_map(m.get('HttpCodeData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeDomainHttpCodeDataResponseBodyHttpCodeData(DaraModel):
    def __init__(
        self,
        usage_data: List[main_models.DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageData] = None,
    ):
        self.usage_data = usage_data

    def validate(self):
        if self.usage_data:
            for v1 in self.usage_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UsageData'] = []
        if self.usage_data is not None:
            for k1 in self.usage_data:
                result['UsageData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_data = []
        if m.get('UsageData') is not None:
            for k1 in m.get('UsageData'):
                temp_model = main_models.DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageData()
                self.usage_data.append(temp_model.from_map(k1))

        return self

class DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageData(DaraModel):
    def __init__(
        self,
        time_stamp: str = None,
        value: main_models.DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValue = None,
    ):
        self.time_stamp = time_stamp
        self.value = value

    def validate(self):
        if self.value:
            self.value.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.value is not None:
            result['Value'] = self.value.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('Value') is not None:
            temp_model = main_models.DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValue()
            self.value = temp_model.from_map(m.get('Value'))

        return self

class DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValue(DaraModel):
    def __init__(
        self,
        code_proportion_data: List[main_models.DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData] = None,
    ):
        self.code_proportion_data = code_proportion_data

    def validate(self):
        if self.code_proportion_data:
            for v1 in self.code_proportion_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CodeProportionData'] = []
        if self.code_proportion_data is not None:
            for k1 in self.code_proportion_data:
                result['CodeProportionData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.code_proportion_data = []
        if m.get('CodeProportionData') is not None:
            for k1 in m.get('CodeProportionData'):
                temp_model = main_models.DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData()
                self.code_proportion_data.append(temp_model.from_map(k1))

        return self

class DescribeDomainHttpCodeDataResponseBodyHttpCodeDataUsageDataValueCodeProportionData(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: str = None,
        proportion: str = None,
    ):
        self.code = code
        self.count = count
        self.proportion = proportion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        if self.proportion is not None:
            result['Proportion'] = self.proportion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')

        return self

