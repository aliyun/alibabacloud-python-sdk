# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEventBusesRequest(DaraModel):
    def __init__(
        self,
        limit: int = None,
        name_prefix: str = None,
        next_token: str = None,
    ):
        # The maximum number of entries to return in a request. You can use this parameter and NextToken to implement paging.
        # 
        # >  A maximum of 100 entries can be returned in a request.
        self.limit = limit
        # The prefix of the names of the event buses that you want to query.
        self.name_prefix = name_prefix
        # If you configure Limit and excess return values exist, this parameter is returned. You can use this parameter and Limit to implement paging.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['Limit'] = self.limit

        if self.name_prefix is not None:
            result['NamePrefix'] = self.name_prefix

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NamePrefix') is not None:
            self.name_prefix = m.get('NamePrefix')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

