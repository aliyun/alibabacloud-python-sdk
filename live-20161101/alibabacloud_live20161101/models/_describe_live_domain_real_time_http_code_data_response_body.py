# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDomainRealTimeHttpCodeDataResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        real_time_http_code_data: main_models.DescribeLiveDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The time interval between the entries returned. Unit: seconds Default value: 60.
        self.data_interval = data_interval
        # The streaming domain.
        self.domain_name = domain_name
        # The end of the time range during which the data was queried. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.end_time = end_time
        # The proportions of HTTP status codes at each time interval.
        self.real_time_http_code_data = real_time_http_code_data
        # The request ID.
        self.request_id = request_id
        # The beginning of the time range during which the data was queried. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.start_time = start_time

    def validate(self):
        if self.real_time_http_code_data:
            self.real_time_http_code_data.validate()

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

        if self.real_time_http_code_data is not None:
            result['RealTimeHttpCodeData'] = self.real_time_http_code_data.to_map()

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

        if m.get('RealTimeHttpCodeData') is not None:
            temp_model = main_models.DescribeLiveDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData()
            self.real_time_http_code_data = temp_model.from_map(m.get('RealTimeHttpCodeData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeLiveDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeData(DaraModel):
    def __init__(
        self,
        usage_data: List[main_models.DescribeLiveDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData] = None,
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
                temp_model = main_models.DescribeLiveDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData()
                self.usage_data.append(temp_model.from_map(k1))

        return self

class DescribeLiveDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageData(DaraModel):
    def __init__(
        self,
        time_stamp: str = None,
        value: main_models.DescribeLiveDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue = None,
    ):
        # The timestamp of the data returned.
        self.time_stamp = time_stamp
        # The proportions of HTTP status codes.
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
            temp_model = main_models.DescribeLiveDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue()
            self.value = temp_model.from_map(m.get('Value'))

        return self

class DescribeLiveDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValue(DaraModel):
    def __init__(
        self,
        real_time_code_proportion_data: List[main_models.DescribeLiveDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData] = None,
    ):
        self.real_time_code_proportion_data = real_time_code_proportion_data

    def validate(self):
        if self.real_time_code_proportion_data:
            for v1 in self.real_time_code_proportion_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RealTimeCodeProportionData'] = []
        if self.real_time_code_proportion_data is not None:
            for k1 in self.real_time_code_proportion_data:
                result['RealTimeCodeProportionData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.real_time_code_proportion_data = []
        if m.get('RealTimeCodeProportionData') is not None:
            for k1 in m.get('RealTimeCodeProportionData'):
                temp_model = main_models.DescribeLiveDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData()
                self.real_time_code_proportion_data.append(temp_model.from_map(k1))

        return self

class DescribeLiveDomainRealTimeHttpCodeDataResponseBodyRealTimeHttpCodeDataUsageDataValueRealTimeCodeProportionData(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: str = None,
        proportion: str = None,
    ):
        # The HTTP status code.
        self.code = code
        # The number of times the HTTP status code was returned.
        self.count = count
        # The proportion of the HTTP status code.
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

