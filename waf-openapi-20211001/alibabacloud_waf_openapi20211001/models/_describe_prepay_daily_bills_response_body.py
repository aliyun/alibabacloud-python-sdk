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
        # The list of WAF burstable billing records.
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
        extension_plugin: bool = None,
        extension_plugin_request: int = None,
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
        # The burstable QPS specification of the WAF instance.
        self.elastic_qps_set_value = elastic_qps_set_value
        # The end time of the billing record. The value is a UNIX timestamp (UTC). Unit: seconds.
        self.end_time = end_time
        # The overuse status of the current period. Valid values:
        # - **0**: Normal.
        # - **1**: overused.
        # - **2**: sandboxed.
        self.exceed_status = exceed_status
        # Indicates whether the extension plug-in is enabled. Valid values:
        # - **true**: The extension plug-in is enabled.
        # - **false**: The extension plug-in is not enabled.
        self.extension_plugin = extension_plugin
        # The number of requests processed by the plug-in.
        self.extension_plugin_request = extension_plugin_request
        # The maximum QPS during the current period.
        self.max_qps = max_qps
        # The unit price for burstable billing. Unit: CNY for the China site and USD for the international site.
        self.price = price
        # The QPS extension specification of the WAF instance.
        self.qps = qps
        # The QPS specification included in the WAF instance edition.
        self.qps_version = qps_version
        # Indicates whether risk identification is enabled. Valid values:
        # - **true**: Risk identification is enabled.
        # - **false**: Risk identification is not enabled.
        self.risk_control = risk_control
        # The number of times risk identification is used.
        self.risk_traffic = risk_traffic
        # The start time of the billing record. The value is a UNIX timestamp (UTC). Unit: seconds.
        self.start_time = start_time
        # The total QPS that is billed.
        self.total = total
        # The burstable billing type.
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

        if self.extension_plugin is not None:
            result['ExtensionPlugin'] = self.extension_plugin

        if self.extension_plugin_request is not None:
            result['ExtensionPluginRequest'] = self.extension_plugin_request

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

        if m.get('ExtensionPlugin') is not None:
            self.extension_plugin = m.get('ExtensionPlugin')

        if m.get('ExtensionPluginRequest') is not None:
            self.extension_plugin_request = m.get('ExtensionPluginRequest')

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

