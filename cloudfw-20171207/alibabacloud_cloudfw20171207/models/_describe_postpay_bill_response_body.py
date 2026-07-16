# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribePostpayBillResponseBody(DaraModel):
    def __init__(
        self,
        aggregate_internet_traffic: float = None,
        aggregate_nat_traffic: float = None,
        aggregate_sdl_traffic: float = None,
        aggregate_total_traffic: float = None,
        aggregate_vpc_traffic: float = None,
        bill_list: List[main_models.DescribePostpayBillResponseBodyBillList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The aggregated Internet traffic, in GB.
        self.aggregate_internet_traffic = aggregate_internet_traffic
        # The aggregated NAT traffic, in GB.
        self.aggregate_nat_traffic = aggregate_nat_traffic
        # The aggregated sensitive data detection traffic, in GB.
        self.aggregate_sdl_traffic = aggregate_sdl_traffic
        # The aggregated total traffic, in GB.
        self.aggregate_total_traffic = aggregate_total_traffic
        # The aggregated VPC traffic, in GB.
        self.aggregate_vpc_traffic = aggregate_vpc_traffic
        # The bill list.
        self.bill_list = bill_list
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.bill_list:
            for v1 in self.bill_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregate_internet_traffic is not None:
            result['AggregateInternetTraffic'] = self.aggregate_internet_traffic

        if self.aggregate_nat_traffic is not None:
            result['AggregateNatTraffic'] = self.aggregate_nat_traffic

        if self.aggregate_sdl_traffic is not None:
            result['AggregateSdlTraffic'] = self.aggregate_sdl_traffic

        if self.aggregate_total_traffic is not None:
            result['AggregateTotalTraffic'] = self.aggregate_total_traffic

        if self.aggregate_vpc_traffic is not None:
            result['AggregateVpcTraffic'] = self.aggregate_vpc_traffic

        result['BillList'] = []
        if self.bill_list is not None:
            for k1 in self.bill_list:
                result['BillList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregateInternetTraffic') is not None:
            self.aggregate_internet_traffic = m.get('AggregateInternetTraffic')

        if m.get('AggregateNatTraffic') is not None:
            self.aggregate_nat_traffic = m.get('AggregateNatTraffic')

        if m.get('AggregateSdlTraffic') is not None:
            self.aggregate_sdl_traffic = m.get('AggregateSdlTraffic')

        if m.get('AggregateTotalTraffic') is not None:
            self.aggregate_total_traffic = m.get('AggregateTotalTraffic')

        if m.get('AggregateVpcTraffic') is not None:
            self.aggregate_vpc_traffic = m.get('AggregateVpcTraffic')

        self.bill_list = []
        if m.get('BillList') is not None:
            for k1 in m.get('BillList'):
                temp_model = main_models.DescribePostpayBillResponseBodyBillList()
                self.bill_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribePostpayBillResponseBodyBillList(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        internet_instance_cnt: int = None,
        internet_traffic: float = None,
        is_derated: int = None,
        log_storage: int = None,
        nat_instance_cnt: int = None,
        nat_traffic: float = None,
        sdl: int = None,
        sdl_traffic: float = None,
        start_time: int = None,
        threat_intelligence: int = None,
        vpc_instance_cnt: int = None,
        vpc_traffic: float = None,
    ):
        # The end time, expressed as a UNIX timestamp in seconds. The value is on the hour or on the day.
        self.end_time = end_time
        # The number of Internet instances.
        self.internet_instance_cnt = internet_instance_cnt
        # The Internet traffic, in GB.
        self.internet_traffic = internet_traffic
        # Indicates whether a deduction is applied. A value of 0 indicates that no deduction is applied. Any value greater than 0 indicates that a deduction is applied. If a deduction is applied, the bill is not generated.
        # > This field is meaningful only when you query data at the hourly level.
        self.is_derated = is_derated
        # The log service usage duration, in TB × hours.
        self.log_storage = log_storage
        # The number of NAT instances.
        self.nat_instance_cnt = nat_instance_cnt
        # The NAT traffic, in GB.
        self.nat_traffic = nat_traffic
        # The sensitive data leak detection usage duration, in hours.
        self.sdl = sdl
        # The sensitive data detection traffic, in GB.
        self.sdl_traffic = sdl_traffic
        # The start time, expressed as a UNIX timestamp in seconds. The value is on the hour or on the day.
        self.start_time = start_time
        # The threat intelligence usage duration, in hours.
        self.threat_intelligence = threat_intelligence
        # The number of VPC instances.
        self.vpc_instance_cnt = vpc_instance_cnt
        # The VPC traffic, in GB.
        self.vpc_traffic = vpc_traffic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.internet_instance_cnt is not None:
            result['InternetInstanceCnt'] = self.internet_instance_cnt

        if self.internet_traffic is not None:
            result['InternetTraffic'] = self.internet_traffic

        if self.is_derated is not None:
            result['IsDerated'] = self.is_derated

        if self.log_storage is not None:
            result['LogStorage'] = self.log_storage

        if self.nat_instance_cnt is not None:
            result['NatInstanceCnt'] = self.nat_instance_cnt

        if self.nat_traffic is not None:
            result['NatTraffic'] = self.nat_traffic

        if self.sdl is not None:
            result['Sdl'] = self.sdl

        if self.sdl_traffic is not None:
            result['SdlTraffic'] = self.sdl_traffic

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.threat_intelligence is not None:
            result['ThreatIntelligence'] = self.threat_intelligence

        if self.vpc_instance_cnt is not None:
            result['VpcInstanceCnt'] = self.vpc_instance_cnt

        if self.vpc_traffic is not None:
            result['VpcTraffic'] = self.vpc_traffic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InternetInstanceCnt') is not None:
            self.internet_instance_cnt = m.get('InternetInstanceCnt')

        if m.get('InternetTraffic') is not None:
            self.internet_traffic = m.get('InternetTraffic')

        if m.get('IsDerated') is not None:
            self.is_derated = m.get('IsDerated')

        if m.get('LogStorage') is not None:
            self.log_storage = m.get('LogStorage')

        if m.get('NatInstanceCnt') is not None:
            self.nat_instance_cnt = m.get('NatInstanceCnt')

        if m.get('NatTraffic') is not None:
            self.nat_traffic = m.get('NatTraffic')

        if m.get('Sdl') is not None:
            self.sdl = m.get('Sdl')

        if m.get('SdlTraffic') is not None:
            self.sdl_traffic = m.get('SdlTraffic')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('ThreatIntelligence') is not None:
            self.threat_intelligence = m.get('ThreatIntelligence')

        if m.get('VpcInstanceCnt') is not None:
            self.vpc_instance_cnt = m.get('VpcInstanceCnt')

        if m.get('VpcTraffic') is not None:
            self.vpc_traffic = m.get('VpcTraffic')

        return self

