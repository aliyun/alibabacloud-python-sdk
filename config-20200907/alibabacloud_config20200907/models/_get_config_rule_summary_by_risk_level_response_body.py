# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetConfigRuleSummaryByRiskLevelResponseBody(DaraModel):
    def __init__(
        self,
        config_rule_summaries: List[main_models.GetConfigRuleSummaryByRiskLevelResponseBodyConfigRuleSummaries] = None,
        request_id: str = None,
    ):
        # The summary of compliance evaluation results by rule risk level.
        self.config_rule_summaries = config_rule_summaries
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.config_rule_summaries:
            for v1 in self.config_rule_summaries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigRuleSummaries'] = []
        if self.config_rule_summaries is not None:
            for k1 in self.config_rule_summaries:
                result['ConfigRuleSummaries'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_rule_summaries = []
        if m.get('ConfigRuleSummaries') is not None:
            for k1 in m.get('ConfigRuleSummaries'):
                temp_model = main_models.GetConfigRuleSummaryByRiskLevelResponseBodyConfigRuleSummaries()
                self.config_rule_summaries.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetConfigRuleSummaryByRiskLevelResponseBodyConfigRuleSummaries(DaraModel):
    def __init__(
        self,
        compliant_count: int = None,
        non_compliant_count: int = None,
        risk_level: int = None,
    ):
        # The number of rules against which specific resources are evaluated as compliant.
        self.compliant_count = compliant_count
        # The number of rules against which specific resources are evaluated as non-compliant.
        self.non_compliant_count = non_compliant_count
        # The risk level of the resources that are not compliant with the rules. Valid values:
        # 
        # *   1: high risk level.
        # *   2: medium risk level.
        # *   3: low risk level.
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliant_count is not None:
            result['CompliantCount'] = self.compliant_count

        if self.non_compliant_count is not None:
            result['NonCompliantCount'] = self.non_compliant_count

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliantCount') is not None:
            self.compliant_count = m.get('CompliantCount')

        if m.get('NonCompliantCount') is not None:
            self.non_compliant_count = m.get('NonCompliantCount')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

