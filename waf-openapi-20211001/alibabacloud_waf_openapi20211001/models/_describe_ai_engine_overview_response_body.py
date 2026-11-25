# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeAiEngineOverviewResponseBody(DaraModel):
    def __init__(
        self,
        analyzed_request_count: int = None,
        event_count: int = None,
        handle_status_counts: main_models.DescribeAiEngineOverviewResponseBodyHandleStatusCounts = None,
        protected_group_count: int = None,
        protected_resource_count: int = None,
        request_id: str = None,
        risk_counts: main_models.DescribeAiEngineOverviewResponseBodyRiskCounts = None,
    ):
        # The number of analyzed requests.
        self.analyzed_request_count = analyzed_request_count
        # The number of events within the specified time range.
        self.event_count = event_count
        # The number of events within the specified time range, categorized by handling status.
        self.handle_status_counts = handle_status_counts
        # The number of protection groups for which AI Engine is enabled.
        self.protected_group_count = protected_group_count
        # The number of protected objects for which AI Engine is enabled. This count does not include protected objects that belong to a protection group.
        self.protected_resource_count = protected_resource_count
        # The ID of the request.
        self.request_id = request_id
        # The number of events within the specified time range, categorized by risk level.
        self.risk_counts = risk_counts

    def validate(self):
        if self.handle_status_counts:
            self.handle_status_counts.validate()
        if self.risk_counts:
            self.risk_counts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analyzed_request_count is not None:
            result['AnalyzedRequestCount'] = self.analyzed_request_count

        if self.event_count is not None:
            result['EventCount'] = self.event_count

        if self.handle_status_counts is not None:
            result['HandleStatusCounts'] = self.handle_status_counts.to_map()

        if self.protected_group_count is not None:
            result['ProtectedGroupCount'] = self.protected_group_count

        if self.protected_resource_count is not None:
            result['ProtectedResourceCount'] = self.protected_resource_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.risk_counts is not None:
            result['RiskCounts'] = self.risk_counts.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnalyzedRequestCount') is not None:
            self.analyzed_request_count = m.get('AnalyzedRequestCount')

        if m.get('EventCount') is not None:
            self.event_count = m.get('EventCount')

        if m.get('HandleStatusCounts') is not None:
            temp_model = main_models.DescribeAiEngineOverviewResponseBodyHandleStatusCounts()
            self.handle_status_counts = temp_model.from_map(m.get('HandleStatusCounts'))

        if m.get('ProtectedGroupCount') is not None:
            self.protected_group_count = m.get('ProtectedGroupCount')

        if m.get('ProtectedResourceCount') is not None:
            self.protected_resource_count = m.get('ProtectedResourceCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RiskCounts') is not None:
            temp_model = main_models.DescribeAiEngineOverviewResponseBodyRiskCounts()
            self.risk_counts = temp_model.from_map(m.get('RiskCounts'))

        return self

class DescribeAiEngineOverviewResponseBodyRiskCounts(DaraModel):
    def __init__(
        self,
        critical: int = None,
        high: int = None,
        low: int = None,
        medium: int = None,
    ):
        # The number of critical events.
        self.critical = critical
        # The number of high-risk events.
        self.high = high
        # The number of low-risk events.
        self.low = low
        # The number of medium-risk events.
        self.medium = medium

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.critical is not None:
            result['Critical'] = self.critical

        if self.high is not None:
            result['High'] = self.high

        if self.low is not None:
            result['Low'] = self.low

        if self.medium is not None:
            result['Medium'] = self.medium

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Critical') is not None:
            self.critical = m.get('Critical')

        if m.get('High') is not None:
            self.high = m.get('High')

        if m.get('Low') is not None:
            self.low = m.get('Low')

        if m.get('Medium') is not None:
            self.medium = m.get('Medium')

        return self

class DescribeAiEngineOverviewResponseBodyHandleStatusCounts(DaraModel):
    def __init__(
        self,
        handled: int = None,
        handling: int = None,
        unhandled: int = None,
    ):
        # The number of handled events.
        self.handled = handled
        # The number of events being handled.
        self.handling = handling
        # The number of unhandled events.
        self.unhandled = unhandled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.handled is not None:
            result['Handled'] = self.handled

        if self.handling is not None:
            result['Handling'] = self.handling

        if self.unhandled is not None:
            result['Unhandled'] = self.unhandled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Handled') is not None:
            self.handled = m.get('Handled')

        if m.get('Handling') is not None:
            self.handling = m.get('Handling')

        if m.get('Unhandled') is not None:
            self.unhandled = m.get('Unhandled')

        return self

