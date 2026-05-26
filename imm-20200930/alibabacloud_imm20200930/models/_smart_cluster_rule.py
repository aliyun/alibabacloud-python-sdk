# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SmartClusterRule(DaraModel):
    def __init__(
        self,
        base_uris: List[str] = None,
        keywords: List[str] = None,
        rule_type: str = None,
        sensitivity: float = None,
    ):
        self.base_uris = base_uris
        # Keywords
        self.keywords = keywords
        self.rule_type = rule_type
        # Sensitivity
        self.sensitivity = sensitivity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_uris is not None:
            result['BaseURIs'] = self.base_uris

        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.sensitivity is not None:
            result['Sensitivity'] = self.sensitivity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseURIs') is not None:
            self.base_uris = m.get('BaseURIs')

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Sensitivity') is not None:
            self.sensitivity = m.get('Sensitivity')

        return self

