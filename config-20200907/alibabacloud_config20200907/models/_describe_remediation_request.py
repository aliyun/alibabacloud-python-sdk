# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRemediationRequest(DaraModel):
    def __init__(
        self,
        config_rule_id: str = None,
        remediation_id: str = None,
    ):
        # The rule ID.
        self.config_rule_id = config_rule_id
        # The ID of the remediation configuration.
        self.remediation_id = remediation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id

        if self.remediation_id is not None:
            result['RemediationId'] = self.remediation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('RemediationId') is not None:
            self.remediation_id = m.get('RemediationId')

        return self

