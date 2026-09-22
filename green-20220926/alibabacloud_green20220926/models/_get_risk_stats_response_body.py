# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetRiskStatsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        risk_stats: List[main_models.GetRiskStatsResponseBodyRiskStats] = None,
    ):
        # The ID assigned by the backend to uniquely identify the request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # The list of risk posture statistics.
        self.risk_stats = risk_stats

    def validate(self):
        if self.risk_stats:
            for v1 in self.risk_stats:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RiskStats'] = []
        if self.risk_stats is not None:
            for k1 in self.risk_stats:
                result['RiskStats'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.risk_stats = []
        if m.get('RiskStats') is not None:
            for k1 in m.get('RiskStats'):
                temp_model = main_models.GetRiskStatsResponseBodyRiskStats()
                self.risk_stats.append(temp_model.from_map(k1))

        return self

class GetRiskStatsResponseBodyRiskStats(DaraModel):
    def __init__(
        self,
        request_count: int = None,
        risk_count: int = None,
        type: str = None,
    ):
        # The total number of requests.
        self.request_count = request_count
        # The number of detected risks.
        self.risk_count = risk_count
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_count is not None:
            result['RequestCount'] = self.request_count

        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestCount') is not None:
            self.request_count = m.get('RequestCount')

        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

