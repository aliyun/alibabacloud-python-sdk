# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartConfigRuleEvaluationRequest(DaraModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        config_rule_id: str = None,
        revert_evaluation: bool = None,
    ):
        # The ID of the compliance package.
        # 
        # For more information, see [ListCompliancePacks](https://help.aliyun.com/document_detail/606968.html).
        # 
        # > Specify either `CompliancePackId` or `ConfigRuleId`.
        self.compliance_pack_id = compliance_pack_id
        # The ID of the rule.
        # 
        # For more information, see [ListConfigRules](https://help.aliyun.com/document_detail/609222.html).
        # 
        # > Specify either `CompliancePackId` or `ConfigRuleId`.
        self.config_rule_id = config_rule_id
        # Specifies whether to restore evaluation results that were ignored. Valid values:
        # 
        # - true: Restores ignored evaluation results.
        # 
        # - false (default): Does not restore ignored evaluation results.
        self.revert_evaluation = revert_evaluation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id

        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id

        if self.revert_evaluation is not None:
            result['RevertEvaluation'] = self.revert_evaluation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')

        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('RevertEvaluation') is not None:
            self.revert_evaluation = m.get('RevertEvaluation')

        return self

