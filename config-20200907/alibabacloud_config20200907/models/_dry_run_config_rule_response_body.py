# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DryRunConfigRuleResponseBody(DaraModel):
    def __init__(
        self,
        compliance_type: str = None,
        request_id: str = None,
        rule_condition_context: str = None,
    ):
        self.compliance_type = compliance_type
        # Id of the request
        self.request_id = request_id
        self.rule_condition_context = rule_condition_context

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rule_condition_context is not None:
            result['RuleConditionContext'] = self.rule_condition_context

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RuleConditionContext') is not None:
            self.rule_condition_context = m.get('RuleConditionContext')

        return self

