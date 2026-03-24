# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeElasticBillsResponseBody(DaraModel):
    def __init__(
        self,
        bills: List[main_models.DescribeElasticBillsResponseBodyBills] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of bills for the on-demand WAF instance.
        self.bills = bills
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.bills:
            for v1 in self.bills:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Bills'] = []
        if self.bills is not None:
            for k1 in self.bills:
                result['Bills'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bills = []
        if m.get('Bills') is not None:
            for k1 in m.get('Bills'):
                temp_model = main_models.DescribeElasticBillsResponseBodyBills()
                self.bills.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeElasticBillsResponseBodyBills(DaraModel):
    def __init__(
        self,
        cu: float = None,
        end_time: int = None,
        function_cu: float = None,
        start_time: int = None,
        traffic_cu: float = None,
    ):
        # The total number of SCUs.
        self.cu = cu
        # The end time of the bill. This value is a UNIX timestamp that is in UTC. Unit: milliseconds.
        self.end_time = end_time
        # The number of SCUs consumed by WAF features.
        self.function_cu = function_cu
        # The start time of the bill. This value is a UNIX timestamp that is in UTC. Unit: milliseconds.
        self.start_time = start_time
        # The number of security capacity units (SCUs) consumed by traffic processing.
        self.traffic_cu = traffic_cu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['Cu'] = self.cu

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.function_cu is not None:
            result['FunctionCu'] = self.function_cu

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.traffic_cu is not None:
            result['TrafficCu'] = self.traffic_cu

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FunctionCu') is not None:
            self.function_cu = m.get('FunctionCu')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TrafficCu') is not None:
            self.traffic_cu = m.get('TrafficCu')

        return self

