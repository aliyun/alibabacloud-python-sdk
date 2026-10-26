# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryAlertRulesResourcesFilter(DaraModel):
    def __init__(
        self,
        contains: List[str] = None,
        not_contains: List[str] = None,
    ):
        # Matches any item in the list (OR semantics).
        self.contains = contains
        # The resource instance ID blacklist filter that excludes alert rules whose associated resources contain any instance ID in the array.
        self.not_contains = not_contains

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contains is not None:
            result['contains'] = self.contains

        if self.not_contains is not None:
            result['notContains'] = self.not_contains

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contains') is not None:
            self.contains = m.get('contains')

        if m.get('notContains') is not None:
            self.not_contains = m.get('notContains')

        return self

