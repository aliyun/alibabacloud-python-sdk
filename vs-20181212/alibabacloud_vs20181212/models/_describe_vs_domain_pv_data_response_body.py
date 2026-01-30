# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeVsDomainPvDataResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        pv_data_interval: main_models.DescribeVsDomainPvDataResponseBodyPvDataInterval = None,
        request_id: str = None,
        start_time: str = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.pv_data_interval = pv_data_interval
        self.request_id = request_id
        self.start_time = start_time

    def validate(self):
        if self.pv_data_interval:
            self.pv_data_interval.validate()

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

        if self.pv_data_interval is not None:
            result['PvDataInterval'] = self.pv_data_interval.to_map()

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

        if m.get('PvDataInterval') is not None:
            temp_model = main_models.DescribeVsDomainPvDataResponseBodyPvDataInterval()
            self.pv_data_interval = temp_model.from_map(m.get('PvDataInterval'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeVsDomainPvDataResponseBodyPvDataInterval(DaraModel):
    def __init__(
        self,
        usage_data: List[main_models.DescribeVsDomainPvDataResponseBodyPvDataIntervalUsageData] = None,
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
                temp_model = main_models.DescribeVsDomainPvDataResponseBodyPvDataIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k1))

        return self

class DescribeVsDomainPvDataResponseBodyPvDataIntervalUsageData(DaraModel):
    def __init__(
        self,
        time_stamp: str = None,
        value: str = None,
    ):
        self.time_stamp = time_stamp
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

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

