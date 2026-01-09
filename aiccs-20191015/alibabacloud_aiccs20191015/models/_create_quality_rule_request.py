# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateQualityRuleRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        key_words: List[str] = None,
        match_type: int = None,
        name: str = None,
        rule_tag: int = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.key_words = key_words
        # This parameter is required.
        self.match_type = match_type
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.rule_tag = rule_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.key_words is not None:
            result['KeyWords'] = self.key_words

        if self.match_type is not None:
            result['MatchType'] = self.match_type

        if self.name is not None:
            result['Name'] = self.name

        if self.rule_tag is not None:
            result['RuleTag'] = self.rule_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KeyWords') is not None:
            self.key_words = m.get('KeyWords')

        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RuleTag') is not None:
            self.rule_tag = m.get('RuleTag')

        return self

