# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartAggregateConfigRuleEvaluationRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        compliance_pack_id: str = None,
        config_rule_id: str = None,
        revert_evaluation: bool = None,
    ):
        # This parameter is required.
        self.aggregator_id = aggregator_id
        self.compliance_pack_id = compliance_pack_id
        self.config_rule_id = config_rule_id
        self.revert_evaluation = revert_evaluation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id

        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id

        if self.revert_evaluation is not None:
            result['RevertEvaluation'] = self.revert_evaluation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')

        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('RevertEvaluation') is not None:
            self.revert_evaluation = m.get('RevertEvaluation')

        return self

