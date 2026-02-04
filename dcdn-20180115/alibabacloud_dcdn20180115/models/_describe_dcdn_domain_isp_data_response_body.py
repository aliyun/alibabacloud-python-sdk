# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnDomainIspDataResponseBody(DaraModel):
    def __init__(
        self,
        data_interval: str = None,
        domain_name: str = None,
        end_time: str = None,
        request_id: str = None,
        start_time: str = None,
        value: main_models.DescribeDcdnDomainIspDataResponseBodyValue = None,
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
        # The access statistics by ISP.
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
            temp_model = main_models.DescribeDcdnDomainIspDataResponseBodyValue()
            self.value = temp_model.from_map(m.get('Value'))

        return self

class DescribeDcdnDomainIspDataResponseBodyValue(DaraModel):
    def __init__(
        self,
        isp_proportion_data: List[main_models.DescribeDcdnDomainIspDataResponseBodyValueIspProportionData] = None,
    ):
        self.isp_proportion_data = isp_proportion_data

    def validate(self):
        if self.isp_proportion_data:
            for v1 in self.isp_proportion_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IspProportionData'] = []
        if self.isp_proportion_data is not None:
            for k1 in self.isp_proportion_data:
                result['IspProportionData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.isp_proportion_data = []
        if m.get('IspProportionData') is not None:
            for k1 in m.get('IspProportionData'):
                temp_model = main_models.DescribeDcdnDomainIspDataResponseBodyValueIspProportionData()
                self.isp_proportion_data.append(temp_model.from_map(k1))

        return self

class DescribeDcdnDomainIspDataResponseBodyValueIspProportionData(DaraModel):
    def __init__(
        self,
        avg_object_size: str = None,
        avg_response_rate: str = None,
        avg_response_time: str = None,
        bps: str = None,
        bytes_proportion: str = None,
        isp: str = None,
        isp_ename: str = None,
        proportion: str = None,
        qps: str = None,
        total_bytes: str = None,
        total_query: str = None,
    ):
        # The average response size. Unit: bytes.
        self.avg_object_size = avg_object_size
        # The average response speed. Unit: byte/ms.
        self.avg_response_rate = avg_response_rate
        # The average response time. Unit: milliseconds.
        self.avg_response_time = avg_response_time
        # The bandwidth.
        self.bps = bps
        # The proportion of network traffic. For example, a value of 90 indicates that 90% of network traffic was coming from the specified ISP.
        self.bytes_proportion = bytes_proportion
        # The information about the ISP.
        self.isp = isp
        # The name of the ISP.
        self.isp_ename = isp_ename
        # The proportion of the HTTP status code.
        self.proportion = proportion
        # The number of queries per second (QPS).
        self.qps = qps
        # The total volume of traffic.
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

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.isp_ename is not None:
            result['IspEname'] = self.isp_ename

        if self.proportion is not None:
            result['Proportion'] = self.proportion

        if self.qps is not None:
            result['Qps'] = self.qps

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

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('IspEname') is not None:
            self.isp_ename = m.get('IspEname')

        if m.get('Proportion') is not None:
            self.proportion = m.get('Proportion')

        if m.get('Qps') is not None:
            self.qps = m.get('Qps')

        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')

        if m.get('TotalQuery') is not None:
            self.total_query = m.get('TotalQuery')

        return self

