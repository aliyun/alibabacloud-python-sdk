# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class DescribePvtzStatisticsGlobalOverviewResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribePvtzStatisticsGlobalOverviewResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribePvtzStatisticsGlobalOverviewResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePvtzStatisticsGlobalOverviewResponseBodyData(DaraModel):
    def __init__(
        self,
        avg_resolve_latency: int = None,
        avg_resolve_latency_trend: int = None,
        avg_success_ratio: int = None,
        avg_success_ratio_trend: int = None,
        total_resolve_count: int = None,
        total_resolve_count_trend: int = None,
    ):
        self.avg_resolve_latency = avg_resolve_latency
        self.avg_resolve_latency_trend = avg_resolve_latency_trend
        self.avg_success_ratio = avg_success_ratio
        self.avg_success_ratio_trend = avg_success_ratio_trend
        self.total_resolve_count = total_resolve_count
        self.total_resolve_count_trend = total_resolve_count_trend

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_resolve_latency is not None:
            result['AvgResolveLatency'] = self.avg_resolve_latency

        if self.avg_resolve_latency_trend is not None:
            result['AvgResolveLatencyTrend'] = self.avg_resolve_latency_trend

        if self.avg_success_ratio is not None:
            result['AvgSuccessRatio'] = self.avg_success_ratio

        if self.avg_success_ratio_trend is not None:
            result['AvgSuccessRatioTrend'] = self.avg_success_ratio_trend

        if self.total_resolve_count is not None:
            result['TotalResolveCount'] = self.total_resolve_count

        if self.total_resolve_count_trend is not None:
            result['TotalResolveCountTrend'] = self.total_resolve_count_trend

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgResolveLatency') is not None:
            self.avg_resolve_latency = m.get('AvgResolveLatency')

        if m.get('AvgResolveLatencyTrend') is not None:
            self.avg_resolve_latency_trend = m.get('AvgResolveLatencyTrend')

        if m.get('AvgSuccessRatio') is not None:
            self.avg_success_ratio = m.get('AvgSuccessRatio')

        if m.get('AvgSuccessRatioTrend') is not None:
            self.avg_success_ratio_trend = m.get('AvgSuccessRatioTrend')

        if m.get('TotalResolveCount') is not None:
            self.total_resolve_count = m.get('TotalResolveCount')

        if m.get('TotalResolveCountTrend') is not None:
            self.total_resolve_count_trend = m.get('TotalResolveCountTrend')

        return self

