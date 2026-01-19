# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CompareCopyRuleVariableRequest(DaraModel):
    def __init__(
        self,
        create_type: str = None,
        lang: str = None,
        reg_id: str = None,
        source_rule_id: str = None,
        source_rule_ids: str = None,
        target_event_code: str = None,
    ):
        # Creation type
        self.create_type = create_type
        # Sets the language type for requests and received messages, with a default value of **zh**. Values: 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Region code.
        self.reg_id = reg_id
        # Original policy ruleId.
        self.source_rule_id = source_rule_id
        # Original policy ruleIds.
        self.source_rule_ids = source_rule_ids
        # Target event eventCode.
        self.target_event_code = target_event_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_type is not None:
            result['CreateType'] = self.create_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reg_id is not None:
            result['RegId'] = self.reg_id

        if self.source_rule_id is not None:
            result['SourceRuleId'] = self.source_rule_id

        if self.source_rule_ids is not None:
            result['SourceRuleIds'] = self.source_rule_ids

        if self.target_event_code is not None:
            result['TargetEventCode'] = self.target_event_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateType') is not None:
            self.create_type = m.get('CreateType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegId') is not None:
            self.reg_id = m.get('RegId')

        if m.get('SourceRuleId') is not None:
            self.source_rule_id = m.get('SourceRuleId')

        if m.get('SourceRuleIds') is not None:
            self.source_rule_ids = m.get('SourceRuleIds')

        if m.get('TargetEventCode') is not None:
            self.target_event_code = m.get('TargetEventCode')

        return self

