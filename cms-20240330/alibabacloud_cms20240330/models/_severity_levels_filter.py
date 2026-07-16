# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SeverityLevelsFilter(DaraModel):
    def __init__(
        self,
        contains: List[str] = None,
    ):
        # Matches a log entry if its severity level appears in this array of strings.
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

