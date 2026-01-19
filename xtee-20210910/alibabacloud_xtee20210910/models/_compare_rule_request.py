# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CompareRuleRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        previous_rule_version_id: int = None,
        reg_id: str = None,
        rule_version_id: int = None,
    ):
        # Sets the language type for requests and received messages, with a default value of **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Primary key ID of the previous policy version.
        self.previous_rule_version_id = previous_rule_version_id
        # Region code.
        self.reg_id = reg_id
        # Primary key ID of the policy version.
        self.rule_version_id = rule_version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.previous_rule_version_id is not None:
            result['previousRuleVersionId'] = self.previous_rule_version_id

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.rule_version_id is not None:
            result['ruleVersionId'] = self.rule_version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('previousRuleVersionId') is not None:
            self.previous_rule_version_id = m.get('previousRuleVersionId')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('ruleVersionId') is not None:
            self.rule_version_id = m.get('ruleVersionId')

        return self

