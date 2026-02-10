# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeChartListResponseBody(DaraModel):
    def __init__(
        self,
        chart_list: List[main_models.DescribeChartListResponseBodyChartList] = None,
        request_id: str = None,
    ):
        # The charts.
        self.chart_list = chart_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.chart_list:
            for v1 in self.chart_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ChartList'] = []
        if self.chart_list is not None:
            for k1 in self.chart_list:
                result['ChartList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chart_list = []
        if m.get('ChartList') is not None:
            for k1 in m.get('ChartList'):
                temp_model = main_models.DescribeChartListResponseBodyChartList()
                self.chart_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeChartListResponseBodyChartList(DaraModel):
    def __init__(
        self,
        business_name: str = None,
        business_type: str = None,
        chart_id: str = None,
        chart_name: str = None,
        chart_type: str = None,
    ):
        # The name of the business type. Valid values:
        # 
        # *   Overall Operations Metrics
        # *   Asset Operations Metrics
        # *   Security Alert Operations Metrics
        # *   Vulnerability Operations Metrics
        # *   Baseline Operations Metrics
        # *   Cloud Product Operations Metrics
        # *   Honeypot Operations Metrics
        self.business_name = business_name
        # The business type. Valid values:
        # 
        # *   INDEX_SECURITY_OVERALL_OPERATION
        # *   INDEX_ASSET_OPERATION
        # *   INDEX_SUSPICIOUS_OPERATION
        # *   INDEX_VUL_OPERATION
        # *   INDEX_BASELINE_CHECK_OPERATION
        # *   INDEX_CLOUD_ASSET_OPERATION
        # *   INDEX_HONEYPOT_RISK_OPERATION
        self.business_type = business_type
        # The ID of the chart.
        self.chart_id = chart_id
        # The name of the chart.
        self.chart_name = chart_name
        # The type of the chart. Valid values:
        # 
        # *   **text**
        # *   **table**
        # *   **gauge**
        # *   **pie**
        # *   **line**
        # *   **bar**
        # *   **timeBar**
        # *   **timeLine**
        self.chart_type = chart_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_name is not None:
            result['BusinessName'] = self.business_name

        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.chart_id is not None:
            result['ChartId'] = self.chart_id

        if self.chart_name is not None:
            result['ChartName'] = self.chart_name

        if self.chart_type is not None:
            result['ChartType'] = self.chart_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')

        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('ChartId') is not None:
            self.chart_id = m.get('ChartId')

        if m.get('ChartName') is not None:
            self.chart_name = m.get('ChartName')

        if m.get('ChartType') is not None:
            self.chart_type = m.get('ChartType')

        return self

