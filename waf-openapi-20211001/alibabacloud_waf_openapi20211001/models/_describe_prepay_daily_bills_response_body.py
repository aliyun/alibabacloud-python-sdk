# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribePrepayDailyBillsResponseBody(DaraModel):
    def __init__(
        self,
        bills: List[main_models.DescribePrepayDailyBillsResponseBodyBills] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The bills of the burstable QPS (pay-as-you-go) feature.
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
                temp_model = main_models.DescribePrepayDailyBillsResponseBodyBills()
                self.bills.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribePrepayDailyBillsResponseBodyBills(DaraModel):
    def __init__(
        self,
        elastic_qps_set_value: int = None,
        end_time: int = None,
        exceed_status: int = None,
        max_qps: int = None,
        price: float = None,
        qps: int = None,
        qps_version: int = None,
        risk_control: bool = None,
        risk_traffic: int = None,
        start_time: int = None,
        total: int = None,
        type: List[str] = None,
    ):
        # The burstable QPS of the WAF instance.
        self.elastic_qps_set_value = elastic_qps_set_value
        # The billing end time. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end_time = end_time
        # The status of QPS usage within the current period of time. Valid values:
        # 
        # *   **0**: normal.
        # *   **1**: excess.
        # *   **2**: sandbox.
        self.exceed_status = exceed_status
        # The peak QPS within the current period of time.
        self.max_qps = max_qps
        # The unit price in the bill. The price is measured in CNY for bills at the China site (aliyun.com) and in USD for bills at the international site (alibabacloud.com).
        self.price = price
        # The extended QPS of the WAF instance.
        self.qps = qps
        # The default QPS of the WAF instance.
        self.qps_version = qps_version
        # Indicates whether risk identification is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.risk_control = risk_control
        # The number of times that risk identification is performed.
        self.risk_traffic = risk_traffic
        # The billing start time. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time
        # The actual QPS in total.
        self.total = total
        # The billing types.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_qps_set_value is not None:
            result['ElasticQpsSetValue'] = self.elastic_qps_set_value

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.exceed_status is not None:
            result['ExceedStatus'] = self.exceed_status

        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps

        if self.price is not None:
            result['Price'] = self.price

        if self.qps is not None:
            result['Qps'] = self.qps

        if self.qps_version is not None:
            result['QpsVersion'] = self.qps_version

        if self.risk_control is not None:
            result['RiskControl'] = self.risk_control

        if self.risk_traffic is not None:
            result['RiskTraffic'] = self.risk_traffic

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total is not None:
            result['Total'] = self.total

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticQpsSetValue') is not None:
            self.elastic_qps_set_value = m.get('ElasticQpsSetValue')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExceedStatus') is not None:
            self.exceed_status = m.get('ExceedStatus')

        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')

        if m.get('Price') is not None:
            self.price = m.get('Price')

        if m.get('Qps') is not None:
            self.qps = m.get('Qps')

        if m.get('QpsVersion') is not None:
            self.qps_version = m.get('QpsVersion')

        if m.get('RiskControl') is not None:
            self.risk_control = m.get('RiskControl')

        if m.get('RiskTraffic') is not None:
            self.risk_traffic = m.get('RiskTraffic')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

