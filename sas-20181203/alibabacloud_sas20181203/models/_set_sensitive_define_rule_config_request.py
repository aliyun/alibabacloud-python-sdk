# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetSensitiveDefineRuleConfigRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        enable_new_rule: int = None,
        source: str = None,
    ):
        # The configurations of the custom check rule. The value is in the JSON format. Valid values of keys:
        # 
        # *   **classKey**: the category keyword of the check rule.
        # *   **ruleList**: the keyword of the check rule.
        self.config = config
        # Specifies whether to enable the new ruled for automatic check only on agentless detection. Valid values:
        # 
        # *   **0**: no.
        # *   **1**: yes.
        self.enable_new_rule = enable_new_rule
        # The source of the check rules. Valid values:
        # 
        # *   **image**: image.
        # *   **agentless**: agentless detection.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.enable_new_rule is not None:
            result['EnableNewRule'] = self.enable_new_rule

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('EnableNewRule') is not None:
            self.enable_new_rule = m.get('EnableNewRule')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

