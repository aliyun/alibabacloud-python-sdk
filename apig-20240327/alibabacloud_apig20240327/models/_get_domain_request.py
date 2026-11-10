# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDomainRequest(DaraModel):
    def __init__(
        self,
        with_statistics: bool = None,
    ):
        # Specifies whether to return online resource information.
        self.with_statistics = with_statistics

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.with_statistics is not None:
            result['withStatistics'] = self.with_statistics

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('withStatistics') is not None:
            self.with_statistics = m.get('withStatistics')

        return self

