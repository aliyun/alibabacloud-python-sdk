# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribePostpayBillsResponseBody(DaraModel):
    def __init__(
        self,
        bill_detail: List[main_models.DescribePostpayBillsResponseBodyBillDetail] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.bill_detail = bill_detail
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.bill_detail:
            for v1 in self.bill_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BillDetail'] = []
        if self.bill_detail is not None:
            for k1 in self.bill_detail:
                result['BillDetail'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bill_detail = []
        if m.get('BillDetail') is not None:
            for k1 in m.get('BillDetail'):
                temp_model = main_models.DescribePostpayBillsResponseBodyBillDetail()
                self.bill_detail.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePostpayBillsResponseBodyBillDetail(DaraModel):
    def __init__(
        self,
        charge_data: str = None,
        cu: str = None,
        end_time: int = None,
        function_cu: str = None,
        start_time: int = None,
        traffic_cu: str = None,
    ):
        self.charge_data = charge_data
        self.cu = cu
        self.end_time = end_time
        self.function_cu = function_cu
        self.start_time = start_time
        self.traffic_cu = traffic_cu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_data is not None:
            result['ChargeData'] = self.charge_data

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
        if m.get('ChargeData') is not None:
            self.charge_data = m.get('ChargeData')

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

