# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddContainerPluginRuleRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        mode: int = None,
        rule_name: str = None,
        rule_template_id: int = None,
        rule_type: int = None,
        selected_policy: List[str] = None,
        white_images: List[str] = None,
    ):
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The action that you want to specify for the rule. Valid values:
        # 
        # *   **1**: triggers alerts.
        # *   **2**: blocks escapes.
        # 
        # This parameter is required.
        self.mode = mode
        # The name of the rule. The name must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores (_). The names of rules that are created for the same user must be unique.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The ID of the rule template. You can call the ListSystemClientRules operation to query the ID of the rule template.
        # 
        # This parameter is required.
        self.rule_template_id = rule_template_id
        # The type of the rule. Valid values:
        # 
        # *   **0**: custom rule
        # *   **1**: system rule
        self.rule_type = rule_type
        # The check items that are enabled for the rule.
        # 
        # This parameter is required.
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

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_template_id is not None:
            result['RuleTemplateId'] = self.rule_template_id

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

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleTemplateId') is not None:
            self.rule_template_id = m.get('RuleTemplateId')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('SelectedPolicy') is not None:
            self.selected_policy = m.get('SelectedPolicy')

        if m.get('WhiteImages') is not None:
            self.white_images = m.get('WhiteImages')

        return self

