# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeFirewallTrafficTrendResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeFirewallTrafficTrendResponseBodyDataList] = None,
        max_bandwidth_time: int = None,
        max_bandwidth_time_bps: main_models.DescribeFirewallTrafficTrendResponseBodyMaxBandwidthTimeBps = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.max_bandwidth_time = max_bandwidth_time
        self.max_bandwidth_time_bps = max_bandwidth_time_bps
        self.request_id = request_id

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()
        if self.max_bandwidth_time_bps:
            self.max_bandwidth_time_bps.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.max_bandwidth_time is not None:
            result['MaxBandwidthTime'] = self.max_bandwidth_time

        if self.max_bandwidth_time_bps is not None:
            result['MaxBandwidthTimeBps'] = self.max_bandwidth_time_bps.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeFirewallTrafficTrendResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('MaxBandwidthTime') is not None:
            self.max_bandwidth_time = m.get('MaxBandwidthTime')

        if m.get('MaxBandwidthTimeBps') is not None:
            temp_model = main_models.DescribeFirewallTrafficTrendResponseBodyMaxBandwidthTimeBps()
            self.max_bandwidth_time_bps = temp_model.from_map(m.get('MaxBandwidthTimeBps'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeFirewallTrafficTrendResponseBodyMaxBandwidthTimeBps(DaraModel):
    def __init__(
        self,
        internet_bps: int = None,
        nat_bps: int = None,
        total_bps: int = None,
        vpc_bps: int = None,
    ):
        self.internet_bps = internet_bps
        self.nat_bps = nat_bps
        self.total_bps = total_bps
        self.vpc_bps = vpc_bps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internet_bps is not None:
            result['InternetBps'] = self.internet_bps

        if self.nat_bps is not None:
            result['NatBps'] = self.nat_bps

        if self.total_bps is not None:
            result['TotalBps'] = self.total_bps

        if self.vpc_bps is not None:
            result['VpcBps'] = self.vpc_bps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetBps') is not None:
            self.internet_bps = m.get('InternetBps')

        if m.get('NatBps') is not None:
            self.nat_bps = m.get('NatBps')

        if m.get('TotalBps') is not None:
            self.total_bps = m.get('TotalBps')

        if m.get('VpcBps') is not None:
            self.vpc_bps = m.get('VpcBps')

        return self

class DescribeFirewallTrafficTrendResponseBodyDataList(DaraModel):
    def __init__(
        self,
        internet_bps: int = None,
        nat_bps: int = None,
        time: int = None,
        total_bps: int = None,
        vpc_bps: int = None,
    ):
        self.internet_bps = internet_bps
        self.nat_bps = nat_bps
        self.time = time
        self.total_bps = total_bps
        self.vpc_bps = vpc_bps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internet_bps is not None:
            result['InternetBps'] = self.internet_bps

        if self.nat_bps is not None:
            result['NatBps'] = self.nat_bps

        if self.time is not None:
            result['Time'] = self.time

        if self.total_bps is not None:
            result['TotalBps'] = self.total_bps

        if self.vpc_bps is not None:
            result['VpcBps'] = self.vpc_bps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetBps') is not None:
            self.internet_bps = m.get('InternetBps')

        if m.get('NatBps') is not None:
            self.nat_bps = m.get('NatBps')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('TotalBps') is not None:
            self.total_bps = m.get('TotalBps')

        if m.get('VpcBps') is not None:
            self.vpc_bps = m.get('VpcBps')

        return self

