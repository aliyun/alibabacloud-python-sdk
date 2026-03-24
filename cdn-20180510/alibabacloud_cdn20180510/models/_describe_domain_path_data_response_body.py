# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainPathDataResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        path_data_per_interval: main_models.DescribeDomainPathDataResponseBodyPathDataPerInterval = None,
        request_id: str = None,
        start_time: str = None,
        total_count: int = None,
    ):
        # The time interval. Unit: seconds.
        self.data_interval = data_interval
        # The accelerated domain name.
        self.domain_name = domain_name
        # The end of the time range during which data was queried.
        self.end_time = end_time
        # The page number of the returned page. Pages start from page **1**.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        self.path_data_per_interval = path_data_per_interval
        # The ID of the request.
        self.request_id = request_id
        # The start of the time range during which data was queried.
        self.start_time = start_time
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.path_data_per_interval:
            self.path_data_per_interval.validate()

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.path_data_per_interval is not None:
            result['PathDataPerInterval'] = self.path_data_per_interval.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataInterval') is not None:
            self.data_interval = m.get('DataInterval')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PathDataPerInterval') is not None:
            temp_model = main_models.DescribeDomainPathDataResponseBodyPathDataPerInterval()
            self.path_data_per_interval = temp_model.from_map(m.get('PathDataPerInterval'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDomainPathDataResponseBodyPathDataPerInterval(DaraModel):
    def __init__(
        self,
        usage_data: List[main_models.DescribeDomainPathDataResponseBodyPathDataPerIntervalUsageData] = None,
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
                temp_model = main_models.DescribeDomainPathDataResponseBodyPathDataPerIntervalUsageData()
                self.usage_data.append(temp_model.from_map(k1))

        return self

class DescribeDomainPathDataResponseBodyPathDataPerIntervalUsageData(DaraModel):
    def __init__(
        self,
        acc: int = None,
        path: str = None,
        time: str = None,
        traffic: int = None,
    ):
        self.acc = acc
        self.path = path
        self.time = time
        self.traffic = traffic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acc is not None:
            result['Acc'] = self.acc

        if self.path is not None:
            result['Path'] = self.path

        if self.time is not None:
            result['Time'] = self.time

        if self.traffic is not None:
            result['Traffic'] = self.traffic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acc') is not None:
            self.acc = m.get('Acc')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Traffic') is not None:
            self.traffic = m.get('Traffic')

        return self

