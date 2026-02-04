# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnDomainsBySourceRequest(DaraModel):
    def __init__(
        self,
        sources: str = None,
    ):
        # The list of origin servers. Separate origin servers with commas (,). You can specify a maximum of 20 origin servers. Fuzzy match is not supported.
        # 
        # This parameter is required.
        self.sources = sources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sources is not None:
            result['Sources'] = self.sources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sources') is not None:
            self.sources = m.get('Sources')

        return self

