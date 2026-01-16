# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCustomDomainsRequest(DaraModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        prefix: str = None,
    ):
        # The number of custom domain names returned.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The domain name prefix.
        self.prefix = prefix

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['limit'] = self.limit

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.prefix is not None:
            result['prefix'] = self.prefix

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')

        return self

