# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetInterceptionSummaryResponseBody(DaraModel):
    def __init__(
        self,
        interception_summary: main_models.GetInterceptionSummaryResponseBodyInterceptionSummary = None,
        request_id: str = None,
    ):
        # The statistics.
        self.interception_summary = interception_summary
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.interception_summary:
            self.interception_summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interception_summary is not None:
            result['InterceptionSummary'] = self.interception_summary.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InterceptionSummary') is not None:
            temp_model = main_models.GetInterceptionSummaryResponseBodyInterceptionSummary()
            self.interception_summary = temp_model.from_map(m.get('InterceptionSummary'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetInterceptionSummaryResponseBodyInterceptionSummary(DaraModel):
    def __init__(
        self,
        close_cluster_count: int = None,
        close_rule_count: int = None,
        cluster_count: int = None,
        interception_count_in_days: int = None,
        open_cluster_count: int = None,
        open_rule_count: int = None,
        risk_count_180day: int = None,
        risk_count_30day: int = None,
        risk_count_today: int = None,
        rule_count: int = None,
    ):
        # The number of clusters that are not protected.
        self.close_cluster_count = close_cluster_count
        # The number of disabled cluster defense rules.
        self.close_rule_count = close_rule_count
        # The total number of clusters.
        self.cluster_count = cluster_count
        # The total number of interception records for the specified cluster.
        self.interception_count_in_days = interception_count_in_days
        # The number of clusters that are protected.
        self.open_cluster_count = open_cluster_count
        # The number of enabled cluster defense rules.
        self.open_rule_count = open_rule_count
        # The number of security risks that are detected in the last 180 days.
        self.risk_count_180day = risk_count_180day
        # The number of security risks that are detected in the last 30 days.
        self.risk_count_30day = risk_count_30day
        # The number of security risks that are detected in the last 24 hours.
        self.risk_count_today = risk_count_today
        # The total number of cluster defense rules.
        self.rule_count = rule_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.close_cluster_count is not None:
            result['CloseClusterCount'] = self.close_cluster_count

        if self.close_rule_count is not None:
            result['CloseRuleCount'] = self.close_rule_count

        if self.cluster_count is not None:
            result['ClusterCount'] = self.cluster_count

        if self.interception_count_in_days is not None:
            result['InterceptionCountInDays'] = self.interception_count_in_days

        if self.open_cluster_count is not None:
            result['OpenClusterCount'] = self.open_cluster_count

        if self.open_rule_count is not None:
            result['OpenRuleCount'] = self.open_rule_count

        if self.risk_count_180day is not None:
            result['RiskCount180Day'] = self.risk_count_180day

        if self.risk_count_30day is not None:
            result['RiskCount30Day'] = self.risk_count_30day

        if self.risk_count_today is not None:
            result['RiskCountToday'] = self.risk_count_today

        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloseClusterCount') is not None:
            self.close_cluster_count = m.get('CloseClusterCount')

        if m.get('CloseRuleCount') is not None:
            self.close_rule_count = m.get('CloseRuleCount')

        if m.get('ClusterCount') is not None:
            self.cluster_count = m.get('ClusterCount')

        if m.get('InterceptionCountInDays') is not None:
            self.interception_count_in_days = m.get('InterceptionCountInDays')

        if m.get('OpenClusterCount') is not None:
            self.open_cluster_count = m.get('OpenClusterCount')

        if m.get('OpenRuleCount') is not None:
            self.open_rule_count = m.get('OpenRuleCount')

        if m.get('RiskCount180Day') is not None:
            self.risk_count_180day = m.get('RiskCount180Day')

        if m.get('RiskCount30Day') is not None:
            self.risk_count_30day = m.get('RiskCount30Day')

        if m.get('RiskCountToday') is not None:
            self.risk_count_today = m.get('RiskCountToday')

        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')

        return self

