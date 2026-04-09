# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshResolveCacheShrinkRequest(DaraModel):
    def __init__(
        self,
        domains_shrink: str = None,
    ):
        self.domains_shrink = domains_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domains_shrink is not None:
            result['Domains'] = self.domains_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains_shrink = m.get('Domains')

        return self

