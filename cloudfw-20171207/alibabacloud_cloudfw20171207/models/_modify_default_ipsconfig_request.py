# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDefaultIPSConfigRequest(DaraModel):
    def __init__(
        self,
        basic_rules: int = None,
        cti_rules: int = None,
        lang: str = None,
        max_sdl: int = None,
        patch_rules: int = None,
        rule_class: int = None,
        run_mode: int = None,
    ):
        # Specifies whether to enable basic protection. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.basic_rules = basic_rules
        # Specifies whether to enable threat intelligence. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.cti_rules = cti_rules
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh** (default)
        # *   **en**
        self.lang = lang
        # The maximum amount of traffic that can be processed by the sensitive data leak detection feature each day.
        self.max_sdl = max_sdl
        # Specifies whether to enable virtual patching. Valid values:
        # 
        # *   **1**: yes
        # *   **0**: no
        self.patch_rules = patch_rules
        # The level of the rule group for the IPS. Valid values:
        # 
        # *   **1**: loose
        # *   **2**: medium
        # *   **3**: strict
        self.rule_class = rule_class
        # The mode of the IPS. Valid values:
        # 
        # *   **1**: block mode
        # *   **0**: monitor mode
        # 
        # This parameter is required.
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

        if self.cti_rules is not None:
            result['CtiRules'] = self.cti_rules

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.max_sdl is not None:
            result['MaxSdl'] = self.max_sdl

        if self.patch_rules is not None:
            result['PatchRules'] = self.patch_rules

        if self.rule_class is not None:
            result['RuleClass'] = self.rule_class

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicRules') is not None:
            self.basic_rules = m.get('BasicRules')

        if m.get('CtiRules') is not None:
            self.cti_rules = m.get('CtiRules')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxSdl') is not None:
            self.max_sdl = m.get('MaxSdl')

        if m.get('PatchRules') is not None:
            self.patch_rules = m.get('PatchRules')

        if m.get('RuleClass') is not None:
            self.rule_class = m.get('RuleClass')

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        return self

