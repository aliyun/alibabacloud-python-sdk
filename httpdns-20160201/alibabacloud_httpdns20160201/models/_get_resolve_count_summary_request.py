# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetResolveCountSummaryRequest(DaraModel):
    def __init__(
        self,
        granularity: str = None,
        time_span: int = None,
    ):
        # This parameter is required.
        self.granularity = granularity
        # This parameter is required.
        self.time_span = time_span

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.time_span is not None:
            result['TimeSpan'] = self.time_span

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('TimeSpan') is not None:
            self.time_span = m.get('TimeSpan')

        return self

