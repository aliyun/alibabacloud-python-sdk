# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataTotalStatValue(DaraModel):
    def __init__(
        self,
        total: int = None,
        share: str = None,
    ):
        # The total count.
        self.total = total
        # The proportion.
        self.share = share

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total is not None:
            result['Total'] = self.total

        if self.share is not None:
            result['Share'] = self.share

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('Share') is not None:
            self.share = m.get('Share')

        return self

