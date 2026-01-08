# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeNatFirewallTrafficTrendResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeNatFirewallTrafficTrendResponseBodyDataList] = None,
        max_in_bps: int = None,
        max_out_bps: int = None,
        max_total_bps: int = None,
        request_id: str = None,
    ):
        # The statistics on traffic.
        self.data_list = data_list
        # The maximum inbound network throughput, which indicates the maximum number of bits that are sent inbound per second. Unit: bit/s.
        self.max_in_bps = max_in_bps
        # The maximum outbound network throughput, which indicates the maximum number of bits that are sent outbound per second. Unit: bit/s.
        self.max_out_bps = max_out_bps
        # The total maximum inbound and outbound network throughput, which indicates the maximum number of bits that are sent inbound and outbound per second. Unit: bit/s.
        self.max_total_bps = max_total_bps
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.max_in_bps is not None:
            result['MaxInBps'] = self.max_in_bps

        if self.max_out_bps is not None:
            result['MaxOutBps'] = self.max_out_bps

        if self.max_total_bps is not None:
            result['MaxTotalBps'] = self.max_total_bps

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeNatFirewallTrafficTrendResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('MaxInBps') is not None:
            self.max_in_bps = m.get('MaxInBps')

        if m.get('MaxOutBps') is not None:
            self.max_out_bps = m.get('MaxOutBps')

        if m.get('MaxTotalBps') is not None:
            self.max_total_bps = m.get('MaxTotalBps')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeNatFirewallTrafficTrendResponseBodyDataList(DaraModel):
    def __init__(
        self,
        max_in_bps: int = None,
        max_out_bps: int = None,
        max_total_bps: int = None,
        traffic_time: int = None,
    ):
        # The maximum inbound network throughput, which indicates the maximum number of bits that are sent inbound per second. Unit: bit/s.
        self.max_in_bps = max_in_bps
        # The maximum outbound network throughput, which indicates the maximum number of bits that are sent outbound per second. Unit: bit/s.
        self.max_out_bps = max_out_bps
        # The total maximum inbound and outbound network throughput, which indicates the maximum number of bits that are sent inbound and outbound per second. Unit: bit/s.
        self.max_total_bps = max_total_bps
        # The time range to query. The value is a UNIX timestamp. Unit: seconds.
        self.traffic_time = traffic_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_in_bps is not None:
            result['MaxInBps'] = self.max_in_bps

        if self.max_out_bps is not None:
            result['MaxOutBps'] = self.max_out_bps

        if self.max_total_bps is not None:
            result['MaxTotalBps'] = self.max_total_bps

        if self.traffic_time is not None:
            result['TrafficTime'] = self.traffic_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxInBps') is not None:
            self.max_in_bps = m.get('MaxInBps')

        if m.get('MaxOutBps') is not None:
            self.max_out_bps = m.get('MaxOutBps')

        if m.get('MaxTotalBps') is not None:
            self.max_total_bps = m.get('MaxTotalBps')

        if m.get('TrafficTime') is not None:
            self.traffic_time = m.get('TrafficTime')

        return self

