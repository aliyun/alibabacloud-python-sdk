# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetBuildRiskDefineRuleConfigRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
    ):
        # The risk items in the risk scan configuration for image build instructions. Valid values:
        # - **classKey**: the ClassKey field value from RuleTree
        # - **ruleList**: the RuleKey field values under RuleList
        # > Call the [GetBuildRiskDefineRuleConfig](~~GetBuildRiskDefineRuleConfig~~) operation to obtain this parameter.
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        return self

