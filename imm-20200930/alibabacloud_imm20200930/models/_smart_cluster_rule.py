# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SmartClusterRule(DaraModel):
    def __init__(
        self,
        keywords: List[str] = None,
        sensitivity: float = None,
    ):
        # Keywords
        self.keywords = keywords
        # Sensitivity
        self.sensitivity = sensitivity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.sensitivity is not None:
            result['Sensitivity'] = self.sensitivity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('Sensitivity') is not None:
            self.sensitivity = m.get('Sensitivity')

        return self

