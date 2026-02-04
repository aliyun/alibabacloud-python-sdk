# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnDomainRegionDataResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        value: main_models.DescribeDcdnDomainRegionDataResponseBodyValue = None,
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
        # The proportions of requests that were initiated from each region.
        self.value = value

    def validate(self):
        if self.value:
            self.value.validate()

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

        if self.value is not None:
            result['Value'] = self.value.to_map()

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

        if m.get('Value') is not None:
            temp_model = main_models.DescribeDcdnDomainRegionDataResponseBodyValue()
            self.value = temp_model.from_map(m.get('Value'))

        return self

class DescribeDcdnDomainRegionDataResponseBodyValue(DaraModel):
    def __init__(
        self,
        region_proportion_data: List[main_models.DescribeDcdnDomainRegionDataResponseBodyValueRegionProportionData] = None,
    ):
        self.region_proportion_data = region_proportion_data

    def validate(self):
        if self.region_proportion_data:
            for v1 in self.region_proportion_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RegionProportionData'] = []
        if self.region_proportion_data is not None:
            for k1 in self.region_proportion_data:
                result['RegionProportionData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_proportion_data = []
        if m.get('RegionProportionData') is not None:
            for k1 in m.get('RegionProportionData'):
                temp_model = main_models.DescribeDcdnDomainRegionDataResponseBodyValueRegionProportionData()
                self.region_proportion_data.append(temp_model.from_map(k1))

        return self

class DescribeDcdnDomainRegionDataResponseBodyValueRegionProportionData(DaraModel):
    def __init__(
        self,
        avg_object_size: str = None,
        avg_response_rate: str = None,
        avg_response_time: str = None,
        bps: str = None,
        bytes_proportion: str = None,
        proportion: str = None,
        qps: str = None,
        region: str = None,
        region_ename: str = None,
        total_bytes: str = None,
        total_query: str = None,
    ):
        # The average response size. Unit: bytes.
        self.avg_object_size = avg_object_size
        # The average response speed. Unit: byte/s.
        self.avg_response_rate = avg_response_rate
        # The average response time. Unit: milliseconds.
        self.avg_response_time = avg_response_time
        # The bandwidth.
        self.bps = bps
        # The proportion of network traffic. For example, a value of 90 indicates that 90% of network traffic was coming from the specified ISP.
        self.bytes_proportion = bytes_proportion
        # The proportion of requests from the specified region based on the total number of requests in percentile. For example, a value of 90 indicates that 90% of the requests were coming from the specified region.
        self.proportion = proportion
        # The number of queries per second (QPS).
        self.qps = qps
        # The information of the regions.
        self.region = region
        # The name of the region.
        self.region_ename = region_ename
        # The total amount of network traffic.
        self.total_bytes = total_bytes
        # The total number of requests that are destined for your website.
        self.total_query = total_query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_object_size is not None:
            result['AvgObjectSize'] = self.avg_object_size

        if self.avg_response_rate is not None:
            result['AvgResponseRate'] = self.avg_response_rate

        if self.avg_response_time is not None:
            result['AvgResponseTime'] = self.avg_response_time

        if self.bps is not None:
            result['Bps'] = self.bps

        if self.bytes_proportion is not None:
            result['BytesProportion'] = self.bytes_proportion

        if self.proportion is not None:
            result['Proportion'] = self.proportion

        if self.qps is not None:
            result['Qps'] = self.qps

        if self.region is not None:
            result['Region'] = self.region

        if self.region_ename is not None:
            result['RegionEname'] = self.region_ename

        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes

        if self.total_query is not None:
            result['TotalQuery'] = self.total_query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgObjectSize') is not None:
            self.avg_object_size = m.get('AvgObjectSize')

        if m.get('AvgResponseRate') is not None:
            self.avg_response_rate = m.get('AvgResponseRate')

        if m.get('AvgResponseTime') is not None:
            self.avg_response_time = m.get('AvgResponseTime')

        if m.get('Bps') is not None:
            self.bps = m.get('Bps')

        if m.get('BytesProportion') is not None:
            self.bytes_proportion = m.get('BytesProportion')

        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')

        if m.get('Qps') is not None:
            self.qps = m.get('Qps')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionEname') is not None:
            self.region_ename = m.get('RegionEname')

        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')

        if m.get('TotalQuery') is not None:
            self.total_query = m.get('TotalQuery')

        return self

