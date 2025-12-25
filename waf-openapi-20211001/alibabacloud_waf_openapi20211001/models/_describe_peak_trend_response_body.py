# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribePeakTrendResponseBody(DaraModel):
    def __init__(
        self,
        flow_chart: List[main_models.DescribePeakTrendResponseBodyFlowChart] = None,
        request_id: str = None,
    ):
        # An array of the QPS statistics of the WAF instance.
        self.flow_chart = flow_chart
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.flow_chart:
            for v1 in self.flow_chart:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FlowChart'] = []
        if self.flow_chart is not None:
            for k1 in self.flow_chart:
                result['FlowChart'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flow_chart = []
        if m.get('FlowChart') is not None:
            for k1 in m.get('FlowChart'):
                temp_model = main_models.DescribePeakTrendResponseBodyFlowChart()
                self.flow_chart.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePeakTrendResponseBodyFlowChart(DaraModel):
    def __init__(
        self,
        acl_sum: int = None,
        anti_scan_sum: int = None,
        cc_sum: int = None,
        count: int = None,
        index: int = None,
        waf_sum: int = None,
    ):
        # The number of requests that are monitored or blocked by the custom rule (access control) module.
        self.acl_sum = acl_sum
        # The number of requests that are monitored or blocked by the scan protection module.
        self.anti_scan_sum = anti_scan_sum
        # The number of requests that are monitored or blocked by the HTTP flood protection module.
        self.cc_sum = cc_sum
        # The total number of requests.
        self.count = count
        # The serial number of the time interval. The serial numbers are arranged in chronological order.
        self.index = index
        # The number of requests that are monitored or blocked by the regular expression protection engine.
        self.waf_sum = waf_sum

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_sum is not None:
            result['AclSum'] = self.acl_sum

        if self.anti_scan_sum is not None:
            result['AntiScanSum'] = self.anti_scan_sum

        if self.cc_sum is not None:
            result['CcSum'] = self.cc_sum

        if self.count is not None:
            result['Count'] = self.count

        if self.index is not None:
            result['Index'] = self.index

        if self.waf_sum is not None:
            result['WafSum'] = self.waf_sum

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclSum') is not None:
            self.acl_sum = m.get('AclSum')

        if m.get('AntiScanSum') is not None:
            self.anti_scan_sum = m.get('AntiScanSum')

        if m.get('CcSum') is not None:
            self.cc_sum = m.get('CcSum')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('WafSum') is not None:
            self.waf_sum = m.get('WafSum')

        return self

