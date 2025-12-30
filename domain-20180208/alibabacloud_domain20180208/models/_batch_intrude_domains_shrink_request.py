# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchIntrudeDomainsShrinkRequest(DaraModel):
    def __init__(
        self,
        domain_names_shrink: str = None,
    ):
        self.domain_names_shrink = domain_names_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_names_shrink is not None:
            result['DomainNames'] = self.domain_names_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names_shrink = m.get('DomainNames')

        return self

