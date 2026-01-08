# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVpcFirewallDefaultIPSConfigResponseBody(DaraModel):
    def __init__(
        self,
        basic_rules: int = None,
        enable_all_patch: int = None,
        request_id: str = None,
        rule_class: int = None,
        run_mode: int = None,
    ):
        # Indicates whether basic policies are enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.basic_rules = basic_rules
        # Indicates whether virtual patching is enabled. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.enable_all_patch = enable_all_patch
        # The ID of the request.
        self.request_id = request_id
        # The level of the rule group for the IPS. Valid values:
        # 
        # *   **1**: loose.
        # *   **2**: medium.
        # *   **3**: strict.
        self.rule_class = rule_class
        # The mode of the intrusion prevention system (IPS). Valid values:
        # 
        # *   **1**: block mode
        # *   **0**: monitor mode
        self.run_mode = run_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic_rules is not None:
            result['BasicRules'] = self.basic_rules

        if self.enable_all_patch is not None:
            result['EnableAllPatch'] = self.enable_all_patch

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rule_class is not None:
            result['RuleClass'] = self.rule_class

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')

        if m.get('EnableAllPatch') is not None:
            self.enable_all_patch = m.get('EnableAllPatch')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RuleClass') is not None:
            self.rule_class = m.get('RuleClass')

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        return self

