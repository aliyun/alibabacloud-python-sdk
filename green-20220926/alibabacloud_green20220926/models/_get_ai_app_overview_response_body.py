# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetAiAppOverviewResponseBody(DaraModel):
    def __init__(
        self,
        app_total: int = None,
        request_id: str = None,
        risk_event_level_distribution: Dict[str, Any] = None,
        risk_event_resolved_total: int = None,
        risk_event_total: int = None,
        risk_event_unhandled_total: int = None,
    ):
        # The total number of agents.
        self.app_total = app_total
        # The ID assigned by the backend to uniquely identify a request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # The distribution of risk events by level.
        self.risk_event_level_distribution = risk_event_level_distribution
        # The total number of resolved risk events.
        self.risk_event_resolved_total = risk_event_resolved_total
        # The total number of risk events.
        self.risk_event_total = risk_event_total
        # The total number of unhandled risk events.
        self.risk_event_unhandled_total = risk_event_unhandled_total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_total is not None:
            result['AppTotal'] = self.app_total

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_event_level_distribution is not None:
            result['RiskEventLevelDistribution'] = self.risk_event_level_distribution

        if self.risk_event_resolved_total is not None:
            result['RiskEventResolvedTotal'] = self.risk_event_resolved_total

        if self.risk_event_total is not None:
            result['RiskEventTotal'] = self.risk_event_total

        if self.risk_event_unhandled_total is not None:
            result['RiskEventUnhandledTotal'] = self.risk_event_unhandled_total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppTotal') is not None:
            self.app_total = m.get('AppTotal')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskEventLevelDistribution') is not None:
            self.risk_event_level_distribution = m.get('RiskEventLevelDistribution')

        if m.get('RiskEventResolvedTotal') is not None:
            self.risk_event_resolved_total = m.get('RiskEventResolvedTotal')

        if m.get('RiskEventTotal') is not None:
            self.risk_event_total = m.get('RiskEventTotal')

        if m.get('RiskEventUnhandledTotal') is not None:
            self.risk_event_unhandled_total = m.get('RiskEventUnhandledTotal')

        return self

