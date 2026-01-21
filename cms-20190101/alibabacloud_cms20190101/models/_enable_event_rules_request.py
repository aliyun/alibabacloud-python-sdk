# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class EnableEventRulesRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        rule_names: List[str] = None,
    ):
        self.region_id = region_id
        # This parameter is required.
        self.rule_names = rule_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_names is not None:
            result['RuleNames'] = self.rule_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleNames') is not None:
            self.rule_names = m.get('RuleNames')

        return self

