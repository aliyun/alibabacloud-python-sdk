# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class KeyFilterItem(DaraModel):
    def __init__(
        self,
        regex: List[str] = None,
    ):
        self.regex = regex

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.regex is not None:
            result['Regex'] = self.regex

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')

        return self

