# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ObserveResourceListFilter(DaraModel):
    def __init__(
        self,
        contains: List[str] = None,
    ):
        # The match condition that requires the observeResourceList of a rule to contain at least one instance ID from the array (OR semantics).
        self.contains = contains

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contains is not None:
            result['contains'] = self.contains

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contains') is not None:
            self.contains = m.get('contains')

        return self

