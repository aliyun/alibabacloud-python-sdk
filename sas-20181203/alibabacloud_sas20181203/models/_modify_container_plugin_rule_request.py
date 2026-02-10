# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyContainerPluginRuleRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        mode: int = None,
        rule_id: int = None,
        rule_name: str = None,
        rule_type: int = None,
        selected_policy: List[str] = None,
        white_images: List[str] = None,
    ):
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The action mode of the rule. Valid values:
        # 
        # *   **1**: alerts
        # *   **2**: block
        self.mode = mode
        # The ID of the rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The name of the rule.
        self.rule_name = rule_name
        # The type of the rule. Valid values:
        # 
        # *   **0**: user-defined rule
        # *   **1**: built-in rule
        self.rule_type = rule_type
        # The rule items.
        self.selected_policy = selected_policy
        # The images that are added to the whitelist.
        self.white_images = white_images

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.selected_policy is not None:
            result['SelectedPolicy'] = self.selected_policy

        if self.white_images is not None:
            result['WhiteImages'] = self.white_images

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('SelectedPolicy') is not None:
            self.selected_policy = m.get('SelectedPolicy')

        if m.get('WhiteImages') is not None:
            self.white_images = m.get('WhiteImages')

        return self

