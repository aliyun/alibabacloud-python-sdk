# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainsUsageByDayResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        usage_by_days: main_models.DescribeDomainsUsageByDayResponseBodyUsageByDays = None,
        usage_total: main_models.DescribeDomainsUsageByDayResponseBodyUsageTotal = None,
    ):
        # The time interval between the data entries returned. Unit: seconds.
        self.data_interval = data_interval
        # The accelerated domain name.
        self.domain_name = domain_name
        # The end of the time range during which data was queried.
        self.end_time = end_time
        # The ID of the request.
        self.request_id = request_id
        # The start of the time range during which data was queried.
        self.start_time = start_time
        self.usage_by_days = usage_by_days
        # The summarized monitoring data.
        self.usage_total = usage_total

    def validate(self):
        if self.usage_by_days:
            self.usage_by_days.validate()
        if self.usage_total:
            self.usage_total.validate()

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

        if self.usage_by_days is not None:
            result['UsageByDays'] = self.usage_by_days.to_map()

        if self.usage_total is not None:
            result['UsageTotal'] = self.usage_total.to_map()

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

        if m.get('UsageByDays') is not None:
            temp_model = main_models.DescribeDomainsUsageByDayResponseBodyUsageByDays()
            self.usage_by_days = temp_model.from_map(m.get('UsageByDays'))

        if m.get('UsageTotal') is not None:
            temp_model = main_models.DescribeDomainsUsageByDayResponseBodyUsageTotal()
            self.usage_total = temp_model.from_map(m.get('UsageTotal'))

        return self

class DescribeDomainsUsageByDayResponseBodyUsageTotal(DaraModel):
    def __init__(
        self,
        bytes_hit_rate: str = None,
        max_bps: str = None,
        max_bps_time: str = None,
        max_src_bps: str = None,
        max_src_bps_time: str = None,
        request_hit_rate: str = None,
        total_access: str = None,
        total_traffic: str = None,
    ):
        # The byte hit ratio. The byte hit ratio is measured in percentage.
        self.bytes_hit_rate = bytes_hit_rate
        # The peak bandwidth value. Unit: bit/s.
        self.max_bps = max_bps
        # The time when the bandwidth reached the peak value.
        self.max_bps_time = max_bps_time
        # The peak bandwidth value during back-to-origin routing. Unit: bit/s.
        self.max_src_bps = max_src_bps
        # The time when the bandwidth during back-to-origin routing reached the peak value.
        self.max_src_bps_time = max_src_bps_time
        # The cache hit ratio that is calculated based on requests. The cache hit ratio is measured in percentage.
        self.request_hit_rate = request_hit_rate
        # The total amount of requests.
        self.total_access = total_access
        # The total amount of network traffic. Unit: bytes.
        self.total_traffic = total_traffic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bytes_hit_rate is not None:
            result['BytesHitRate'] = self.bytes_hit_rate

        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps

        if self.max_bps_time is not None:
            result['MaxBpsTime'] = self.max_bps_time

        if self.max_src_bps is not None:
            result['MaxSrcBps'] = self.max_src_bps

        if self.max_src_bps_time is not None:
            result['MaxSrcBpsTime'] = self.max_src_bps_time

        if self.request_hit_rate is not None:
            result['RequestHitRate'] = self.request_hit_rate

        if self.total_access is not None:
            result['TotalAccess'] = self.total_access

        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BytesHitRate') is not None:
            self.bytes_hit_rate = m.get('BytesHitRate')

        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')

        if m.get('MaxBpsTime') is not None:
            self.max_bps_time = m.get('MaxBpsTime')

        if m.get('MaxSrcBps') is not None:
            self.max_src_bps = m.get('MaxSrcBps')

        if m.get('MaxSrcBpsTime') is not None:
            self.max_src_bps_time = m.get('MaxSrcBpsTime')

        if m.get('RequestHitRate') is not None:
            self.request_hit_rate = m.get('RequestHitRate')

        if m.get('TotalAccess') is not None:
            self.total_access = m.get('TotalAccess')

        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')

        return self

class DescribeDomainsUsageByDayResponseBodyUsageByDays(DaraModel):
    def __init__(
        self,
        usage_by_day: List[main_models.DescribeDomainsUsageByDayResponseBodyUsageByDaysUsageByDay] = None,
    ):
        self.usage_by_day = usage_by_day

    def validate(self):
        if self.usage_by_day:
            for v1 in self.usage_by_day:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UsageByDay'] = []
        if self.usage_by_day is not None:
            for k1 in self.usage_by_day:
                result['UsageByDay'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.usage_by_day = []
        if m.get('UsageByDay') is not None:
            for k1 in m.get('UsageByDay'):
                temp_model = main_models.DescribeDomainsUsageByDayResponseBodyUsageByDaysUsageByDay()
                self.usage_by_day.append(temp_model.from_map(k1))

        return self

class DescribeDomainsUsageByDayResponseBodyUsageByDaysUsageByDay(DaraModel):
    def __init__(
        self,
        bytes_hit_rate: str = None,
        max_bps: str = None,
        max_bps_time: str = None,
        max_src_bps: str = None,
        max_src_bps_time: str = None,
        qps: str = None,
        request_hit_rate: str = None,
        time_stamp: str = None,
        total_access: str = None,
        total_traffic: str = None,
    ):
        self.bytes_hit_rate = bytes_hit_rate
        self.max_bps = max_bps
        self.max_bps_time = max_bps_time
        self.max_src_bps = max_src_bps
        self.max_src_bps_time = max_src_bps_time
        self.qps = qps
        self.request_hit_rate = request_hit_rate
        self.time_stamp = time_stamp
        self.total_access = total_access
        self.total_traffic = total_traffic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bytes_hit_rate is not None:
            result['BytesHitRate'] = self.bytes_hit_rate

        if self.max_bps is not None:
            result['MaxBps'] = self.max_bps

        if self.max_bps_time is not None:
            result['MaxBpsTime'] = self.max_bps_time

        if self.max_src_bps is not None:
            result['MaxSrcBps'] = self.max_src_bps

        if self.max_src_bps_time is not None:
            result['MaxSrcBpsTime'] = self.max_src_bps_time

        if self.qps is not None:
            result['Qps'] = self.qps

        if self.request_hit_rate is not None:
            result['RequestHitRate'] = self.request_hit_rate

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.total_access is not None:
            result['TotalAccess'] = self.total_access

        if self.total_traffic is not None:
            result['TotalTraffic'] = self.total_traffic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BytesHitRate') is not None:
            self.bytes_hit_rate = m.get('BytesHitRate')

        if m.get('MaxBps') is not None:
            self.max_bps = m.get('MaxBps')

        if m.get('MaxBpsTime') is not None:
            self.max_bps_time = m.get('MaxBpsTime')

        if m.get('MaxSrcBps') is not None:
            self.max_src_bps = m.get('MaxSrcBps')

        if m.get('MaxSrcBpsTime') is not None:
            self.max_src_bps_time = m.get('MaxSrcBpsTime')

        if m.get('Qps') is not None:
            self.qps = m.get('Qps')

        if m.get('RequestHitRate') is not None:
            self.request_hit_rate = m.get('RequestHitRate')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('TotalAccess') is not None:
            self.total_access = m.get('TotalAccess')

        if m.get('TotalTraffic') is not None:
            self.total_traffic = m.get('TotalTraffic')

        return self

