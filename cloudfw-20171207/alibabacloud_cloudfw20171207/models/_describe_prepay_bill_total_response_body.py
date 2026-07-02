# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribePrepayBillTotalResponseBody(DaraModel):
    def __init__(
        self,
        bill_list: List[main_models.DescribePrepayBillTotalResponseBodyBillList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The bill list, aggregated by day.
        self.bill_list = bill_list
        # The request ID.
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
        self.bill_list = []
        if m.get('BillList') is not None:
            for k1 in m.get('BillList'):
                temp_model = main_models.DescribePrepayBillTotalResponseBodyBillList()
                self.bill_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribePrepayBillTotalResponseBodyBillList(DaraModel):
    def __init__(
        self,
        billed_detection_traffic: float = None,
        daily_detection_traffic: float = None,
        daily_overflow_traffic: float = None,
        default_bandwidth: int = None,
        elastic_bandwidth: int = None,
        end_time: int = None,
        extension_bandwidth: int = None,
        internet_traffic_bandwidth: float = None,
        monthly_remaining_free_traffic: float = None,
        nat_traffic_bandwidth: float = None,
        overflow_time: int = None,
        start_time: int = None,
        temporary_bandwidth: int = None,
        vpc_traffic_bandwidth: float = None,
    ):
        # The actual billed traffic for sensitive data leak detection.
        self.billed_detection_traffic = billed_detection_traffic
        # The sensitive data detection traffic for the day.
        self.daily_detection_traffic = daily_detection_traffic
        # The total elastic traffic for the day. Unit: GB.
        self.daily_overflow_traffic = daily_overflow_traffic
        # The default bandwidth of the edition. Unit: Mbit/s.
        self.default_bandwidth = default_bandwidth
        # The elastic bandwidth. Unit: Mbit/s.
        self.elastic_bandwidth = elastic_bandwidth
        # The end time of the day. The value is a UNIX timestamp in seconds.
        self.end_time = end_time
        # The extended bandwidth. Unit: Mbit/s.
        self.extension_bandwidth = extension_bandwidth
        # The Internet traffic bandwidth. Unit: Gbit/s.
        self.internet_traffic_bandwidth = internet_traffic_bandwidth
        # The monthly free traffic quota for sensitive data detection. Unit: GB.
        self.monthly_remaining_free_traffic = monthly_remaining_free_traffic
        # The NAT traffic bandwidth. Unit: Gbit/s.
        self.nat_traffic_bandwidth = nat_traffic_bandwidth
        # The timestamp when the maximum combined bandwidth (Internet + VPC + NAT) occurred on that day.
        self.overflow_time = overflow_time
        # The start time of the day. The value is a UNIX timestamp in seconds.
        self.start_time = start_time
        # The temporary upgrade bandwidth. Unit: Mbit/s.
        self.temporary_bandwidth = temporary_bandwidth
        # The VPC traffic bandwidth. Unit: Gbit/s.
        self.vpc_traffic_bandwidth = vpc_traffic_bandwidth

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billed_detection_traffic is not None:
            result['BilledDetectionTraffic'] = self.billed_detection_traffic

        if self.daily_detection_traffic is not None:
            result['DailyDetectionTraffic'] = self.daily_detection_traffic

        if self.daily_overflow_traffic is not None:
            result['DailyOverflowTraffic'] = self.daily_overflow_traffic

        if self.default_bandwidth is not None:
            result['DefaultBandwidth'] = self.default_bandwidth

        if self.elastic_bandwidth is not None:
            result['ElasticBandwidth'] = self.elastic_bandwidth

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.extension_bandwidth is not None:
            result['ExtensionBandwidth'] = self.extension_bandwidth

        if self.internet_traffic_bandwidth is not None:
            result['InternetTrafficBandwidth'] = self.internet_traffic_bandwidth

        if self.monthly_remaining_free_traffic is not None:
            result['MonthlyRemainingFreeTraffic'] = self.monthly_remaining_free_traffic

        if self.nat_traffic_bandwidth is not None:
            result['NatTrafficBandwidth'] = self.nat_traffic_bandwidth

        if self.overflow_time is not None:
            result['OverflowTime'] = self.overflow_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.temporary_bandwidth is not None:
            result['TemporaryBandwidth'] = self.temporary_bandwidth

        if self.vpc_traffic_bandwidth is not None:
            result['VpcTrafficBandwidth'] = self.vpc_traffic_bandwidth

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BilledDetectionTraffic') is not None:
            self.billed_detection_traffic = m.get('BilledDetectionTraffic')

        if m.get('DailyDetectionTraffic') is not None:
            self.daily_detection_traffic = m.get('DailyDetectionTraffic')

        if m.get('DailyOverflowTraffic') is not None:
            self.daily_overflow_traffic = m.get('DailyOverflowTraffic')

        if m.get('DefaultBandwidth') is not None:
            self.default_bandwidth = m.get('DefaultBandwidth')

        if m.get('ElasticBandwidth') is not None:
            self.elastic_bandwidth = m.get('ElasticBandwidth')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExtensionBandwidth') is not None:
            self.extension_bandwidth = m.get('ExtensionBandwidth')

        if m.get('InternetTrafficBandwidth') is not None:
            self.internet_traffic_bandwidth = m.get('InternetTrafficBandwidth')

        if m.get('MonthlyRemainingFreeTraffic') is not None:
            self.monthly_remaining_free_traffic = m.get('MonthlyRemainingFreeTraffic')

        if m.get('NatTrafficBandwidth') is not None:
            self.nat_traffic_bandwidth = m.get('NatTrafficBandwidth')

        if m.get('OverflowTime') is not None:
            self.overflow_time = m.get('OverflowTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TemporaryBandwidth') is not None:
            self.temporary_bandwidth = m.get('TemporaryBandwidth')

        if m.get('VpcTrafficBandwidth') is not None:
            self.vpc_traffic_bandwidth = m.get('VpcTrafficBandwidth')

        return self

