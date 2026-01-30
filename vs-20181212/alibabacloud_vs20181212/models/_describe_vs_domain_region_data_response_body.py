# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeVsDomainRegionDataResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        value: main_models.DescribeVsDomainRegionDataResponseBodyValue = None,
    ):
        self.data_interval = data_interval
        self.domain_name = domain_name
        self.end_time = end_time
        self.request_id = request_id
        self.start_time = start_time
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
            temp_model = main_models.DescribeVsDomainRegionDataResponseBodyValue()
            self.value = temp_model.from_map(m.get('Value'))

        return self

class DescribeVsDomainRegionDataResponseBodyValue(DaraModel):
    def __init__(
        self,
        region_proportion_data: List[main_models.DescribeVsDomainRegionDataResponseBodyValueRegionProportionData] = None,
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
                temp_model = main_models.DescribeVsDomainRegionDataResponseBodyValueRegionProportionData()
                self.region_proportion_data.append(temp_model.from_map(k1))

        return self

class DescribeVsDomainRegionDataResponseBodyValueRegionProportionData(DaraModel):
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
        req_err_rate: str = None,
        total_bytes: str = None,
        total_query: str = None,
    ):
        self.avg_object_size = avg_object_size
        self.avg_response_rate = avg_response_rate
        self.avg_response_time = avg_response_time
        self.bps = bps
        self.bytes_proportion = bytes_proportion
        self.proportion = proportion
        self.qps = qps
        self.region = region
        self.region_ename = region_ename
        self.req_err_rate = req_err_rate
        self.total_bytes = total_bytes
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

        if self.req_err_rate is not None:
            result['ReqErrRate'] = self.req_err_rate

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

        if m.get('ReqErrRate') is not None:
            self.req_err_rate = m.get('ReqErrRate')

        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')

        if m.get('TotalQuery') is not None:
            self.total_query = m.get('TotalQuery')

        return self

