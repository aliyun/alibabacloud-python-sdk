# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class GetKafkaClientIpResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetKafkaClientIpResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The data returned.
        self.data = data
        # The message returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetKafkaClientIpResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetKafkaClientIpResponseBodyData(DaraModel):
    def __init__(
        self,
        alert: bool = None,
        data: main_models.GetKafkaClientIpResponseBodyDataData = None,
        end_date: int = None,
        search_time_range: int = None,
        start_date: int = None,
        time_limit_day: int = None,
    ):
        # The value true indicates that the broker is not of the latest minor version.
        # 
        # >  If the broker is not of the latest minor version, the sampled logs may not be accurate. This may cause inaccurate IP information. Therefore, we recommend that you update your broker to the latest version at the earliest opportunity.
        self.alert = alert
        self.data = data
        # The end of the date range within which data is queried.
        self.end_date = end_date
        # The time range within which the client IP addresses are queried.
        # 
        # >  The valid value is 1 hour. If the beginning of the time range to query and the end of the time range to query exceeds 1 hour, only data within 1 hour is returned.
        self.search_time_range = search_time_range
        # The beginning of the date range within which data is queried.
        self.start_date = start_date
        # The date range within which the client IP addresses are queried.
        # 
        # >  The valid value is 7 days. If the beginning of the date range to query and the end of the date range to query exceeds 7 days, only data within 7 days is returned.
        self.time_limit_day = time_limit_day

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert is not None:
            result['Alert'] = self.alert

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.search_time_range is not None:
            result['SearchTimeRange'] = self.search_time_range

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.time_limit_day is not None:
            result['TimeLimitDay'] = self.time_limit_day

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alert') is not None:
            self.alert = m.get('Alert')

        if m.get('Data') is not None:
            temp_model = main_models.GetKafkaClientIpResponseBodyDataData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('SearchTimeRange') is not None:
            self.search_time_range = m.get('SearchTimeRange')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('TimeLimitDay') is not None:
            self.time_limit_day = m.get('TimeLimitDay')

        return self

class GetKafkaClientIpResponseBodyDataData(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetKafkaClientIpResponseBodyDataDataData] = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetKafkaClientIpResponseBodyDataDataData()
                self.data.append(temp_model.from_map(k1))

        return self

class GetKafkaClientIpResponseBodyDataDataData(DaraModel):
    def __init__(
        self,
        data: main_models.GetKafkaClientIpResponseBodyDataDataDataData = None,
        name: str = None,
    ):
        self.data = data
        self.name = name

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetKafkaClientIpResponseBodyDataDataDataData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetKafkaClientIpResponseBodyDataDataDataData(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetKafkaClientIpResponseBodyDataDataDataDataData] = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetKafkaClientIpResponseBodyDataDataDataDataData()
                self.data.append(temp_model.from_map(k1))

        return self

class GetKafkaClientIpResponseBodyDataDataDataDataData(DaraModel):
    def __init__(
        self,
        ip: str = None,
        num: int = None,
    ):
        self.ip = ip
        self.num = num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        if self.num is not None:
            result['Num'] = self.num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Num') is not None:
            self.num = m.get('Num')

        return self

