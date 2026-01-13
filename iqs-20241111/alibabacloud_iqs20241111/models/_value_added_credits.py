# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ValueAddedCredits(DaraModel):
    def __init__(
        self,
        advanced: int = None,
        summary: int = None,
    ):
        self.advanced = advanced
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced is not None:
            result['advanced'] = self.advanced

        if self.summary is not None:
            result['summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advanced') is not None:
            self.advanced = m.get('advanced')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        return self

