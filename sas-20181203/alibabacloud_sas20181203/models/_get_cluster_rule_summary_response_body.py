# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetClusterRuleSummaryResponseBody(DaraModel):
    def __init__(
        self,
        cluster_rule_summary: main_models.GetClusterRuleSummaryResponseBodyClusterRuleSummary = None,
        request_id: str = None,
    ):
        # The overall information about the cluster defense rules.
        self.cluster_rule_summary = cluster_rule_summary
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.cluster_rule_summary:
            self.cluster_rule_summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_rule_summary is not None:
            result['ClusterRuleSummary'] = self.cluster_rule_summary.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterRuleSummary') is not None:
            temp_model = main_models.GetClusterRuleSummaryResponseBodyClusterRuleSummary()
            self.cluster_rule_summary = temp_model.from_map(m.get('ClusterRuleSummary'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetClusterRuleSummaryResponseBodyClusterRuleSummary(DaraModel):
    def __init__(
        self,
        close_rule_count: int = None,
        interception_count_7day: int = None,
        interception_switch: int = None,
        interception_type: int = None,
        open_rule_count: int = None,
        rule_count: int = None,
        suggest_rule_count: int = None,
    ):
        # The number of disabled cluster defense rules.
        self.close_rule_count = close_rule_count
        # The number of alerts that are triggered by the cluster defense rules in the last seven days.
        self.interception_count_7day = interception_count_7day
        # The status of the container firewall feature. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        self.interception_switch = interception_switch
        # The interception mode.
        self.interception_type = interception_type
        # The number of enabled cluster defense rules.
        self.open_rule_count = open_rule_count
        # The total number of configured cluster defense rules.
        self.rule_count = rule_count
        # The number of recommended cluster defense rules.
        self.suggest_rule_count = suggest_rule_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.close_rule_count is not None:
            result['CloseRuleCount'] = self.close_rule_count

        if self.interception_count_7day is not None:
            result['InterceptionCount7Day'] = self.interception_count_7day

        if self.interception_switch is not None:
            result['InterceptionSwitch'] = self.interception_switch

        if self.interception_type is not None:
            result['InterceptionType'] = self.interception_type

        if self.open_rule_count is not None:
            result['OpenRuleCount'] = self.open_rule_count

        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count

        if self.suggest_rule_count is not None:
            result['SuggestRuleCount'] = self.suggest_rule_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloseRuleCount') is not None:
            self.close_rule_count = m.get('CloseRuleCount')

        if m.get('InterceptionCount7Day') is not None:
            self.interception_count_7day = m.get('InterceptionCount7Day')

        if m.get('InterceptionSwitch') is not None:
            self.interception_switch = m.get('InterceptionSwitch')

        if m.get('InterceptionType') is not None:
            self.interception_type = m.get('InterceptionType')

        if m.get('OpenRuleCount') is not None:
            self.open_rule_count = m.get('OpenRuleCount')

        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')

        if m.get('SuggestRuleCount') is not None:
            self.suggest_rule_count = m.get('SuggestRuleCount')

        return self

