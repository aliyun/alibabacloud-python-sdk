# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BackfillStrategy(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        end_time: int = None,
        immediate: bool = None,
        start_time: int = None,
    ):
        self.enabled = enabled
        self.end_time = end_time
        self.immediate = immediate
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.immediate is not None:
            result['immediate'] = self.immediate

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('immediate') is not None:
            self.immediate = m.get('immediate')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

