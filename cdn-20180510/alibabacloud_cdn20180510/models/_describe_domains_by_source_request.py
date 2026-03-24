# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainsBySourceRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        security_token: str = None,
        sources: str = None,
    ):
        self.owner_id = owner_id
        self.security_token = security_token
        # The origin servers. Separate multiple origin servers with commas (,). Fuzzy match is not supported.
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
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.sources is not None:
            result['Sources'] = self.sources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Sources') is not None:
            self.sources = m.get('Sources')

        return self

