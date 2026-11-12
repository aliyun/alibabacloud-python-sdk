# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ObserveGroupRuleCount(DaraModel):
    def __init__(
        self,
        main_count: int = None,
        related_count: int = None,
        rule_id: str = None,
        total_count: int = None,
    ):
        # The number of deduplicated primary entities.
        self.main_count = main_count
        # The number of deduplicated associated child entities.
        self.related_count = related_count
        # The stable ID of the managed rule.
        self.rule_id = rule_id
        # The total number of deduplicated entities.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.main_count is not None:
            result['mainCount'] = self.main_count

        if self.related_count is not None:
            result['relatedCount'] = self.related_count

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mainCount') is not None:
            self.main_count = m.get('mainCount')

        if m.get('relatedCount') is not None:
            self.related_count = m.get('relatedCount')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

