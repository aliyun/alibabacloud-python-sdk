# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class Describe95TrafficResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_95summary: main_models.Describe95TrafficResponseBodyTraffic95Summary = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information returned.
        self.traffic_95summary = traffic_95summary

    def validate(self):
        if self.traffic_95summary:
            self.traffic_95summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.traffic_95summary is not None:
            result['Traffic95Summary'] = self.traffic_95summary.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Traffic95Summary') is not None:
            temp_model = main_models.Describe95TrafficResponseBodyTraffic95Summary()
            self.traffic_95summary = temp_model.from_map(m.get('Traffic95Summary'))

        return self

class Describe95TrafficResponseBodyTraffic95Summary(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        fifth_peak_bandwidth: str = None,
        instance_id: str = None,
        internet_charge_type: str = None,
        minimum_consume_bandwidth: str = None,
        traffic_95detail_list: main_models.Describe95TrafficResponseBodyTraffic95SummaryTraffic95DetailList = None,
    ):
        # The peak bandwidth of the Internet Shared Bandwidth instance. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The daily peak bandwidth. Unit: Mbit/s.
        # <props="china"> For more information, see [Daily peak bandwidth](https://help.aliyun.com/document_detail/89729.html).
        self.fifth_peak_bandwidth = fifth_peak_bandwidth
        # The resource ID.
        self.instance_id = instance_id
        # The metering method of the Internet Shared Bandwidth instance. Valid values:
        # 
        # *   PayBy95: pay-by-enhanced-95th-percentile
        # *   PayByBandwidth: pay-by-bandwidth
        # *   PayByDominantTraffic: pay-by-dominant-traffic
        self.internet_charge_type = internet_charge_type
        # The guaranteed bandwidth of the Internet Shared Bandwidth instance. Unit: Mbit/s.
        self.minimum_consume_bandwidth = minimum_consume_bandwidth
        # The average bandwidth every 5 minutes in the inbound and outbound directions.
        self.traffic_95detail_list = traffic_95detail_list

    def validate(self):
        if self.traffic_95detail_list:
            self.traffic_95detail_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.fifth_peak_bandwidth is not None:
            result['FifthPeakBandwidth'] = self.fifth_peak_bandwidth

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.minimum_consume_bandwidth is not None:
            result['MinimumConsumeBandwidth'] = self.minimum_consume_bandwidth

        if self.traffic_95detail_list is not None:
            result['Traffic95DetailList'] = self.traffic_95detail_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('FifthPeakBandwidth') is not None:
            self.fifth_peak_bandwidth = m.get('FifthPeakBandwidth')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('MinimumConsumeBandwidth') is not None:
            self.minimum_consume_bandwidth = m.get('MinimumConsumeBandwidth')

        if m.get('Traffic95DetailList') is not None:
            temp_model = main_models.Describe95TrafficResponseBodyTraffic95SummaryTraffic95DetailList()
            self.traffic_95detail_list = temp_model.from_map(m.get('Traffic95DetailList'))

        return self

class Describe95TrafficResponseBodyTraffic95SummaryTraffic95DetailList(DaraModel):
    def __init__(
        self,
        traffic_95detail: List[main_models.Describe95TrafficResponseBodyTraffic95SummaryTraffic95DetailListTraffic95Detail] = None,
    ):
        self.traffic_95detail = traffic_95detail

    def validate(self):
        if self.traffic_95detail:
            for v1 in self.traffic_95detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Traffic95Detail'] = []
        if self.traffic_95detail is not None:
            for k1 in self.traffic_95detail:
                result['Traffic95Detail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.traffic_95detail = []
        if m.get('Traffic95Detail') is not None:
            for k1 in m.get('Traffic95Detail'):
                temp_model = main_models.Describe95TrafficResponseBodyTraffic95SummaryTraffic95DetailListTraffic95Detail()
                self.traffic_95detail.append(temp_model.from_map(k1))

        return self

class Describe95TrafficResponseBodyTraffic95SummaryTraffic95DetailListTraffic95Detail(DaraModel):
    def __init__(
        self,
        bill_bandwidth: str = None,
        in_bandwidth: str = None,
        out_bandwidth: str = None,
        time: str = None,
    ):
        # The sampled bandwidth value, which is the larger bandwidth value in the inbound and outbound directions within a sampling interval. Unit: Mbit/s.
        self.bill_bandwidth = bill_bandwidth
        # The inbound bandwidth. Unit: Mbit/s.
        self.in_bandwidth = in_bandwidth
        # The outbound bandwidth. Unit: Mbit/s.
        self.out_bandwidth = out_bandwidth
        # The statistical time. The value is a string.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_bandwidth is not None:
            result['BillBandwidth'] = self.bill_bandwidth

        if self.in_bandwidth is not None:
            result['InBandwidth'] = self.in_bandwidth

        if self.out_bandwidth is not None:
            result['OutBandwidth'] = self.out_bandwidth

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillBandwidth') is not None:
            self.bill_bandwidth = m.get('BillBandwidth')

        if m.get('InBandwidth') is not None:
            self.in_bandwidth = m.get('InBandwidth')

        if m.get('OutBandwidth') is not None:
            self.out_bandwidth = m.get('OutBandwidth')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

