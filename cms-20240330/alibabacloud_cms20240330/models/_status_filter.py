# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StatusFilter(DaraModel):
    def __init__(
        self,
        eq: str = None,
    ):
        # The exact match condition for the alert status. Only alert rules whose status equals the specified value are returned. Valid values:
        # - Alarm: The alert rule is in the alerting state.
        # - Ok: The alert rule is in the normal state.
        # - InsufficientData: Insufficient data is available.
        self.eq = eq

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eq is not None:
            result['eq'] = self.eq

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eq') is not None:
            self.eq = m.get('eq')

        return self

