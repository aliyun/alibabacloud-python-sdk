# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUsersRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        name: str = None,
        name_like: str = None,
        next_token: str = None,
    ):
        # The maximum number of records to return per page. Valid values: 1 to 100. If this parameter is not specified, 10 records are returned by default.
        self.max_results = max_results
        # The filter condition for exact match on the username.
        self.name = name
        # The filter condition for fuzzy match on the username. The value can be up to 128 characters in length.
        self.name_like = name_like
        # The cursor for querying the next page. Do not specify this parameter in the first call. In subsequent calls, specify the nextToken value returned in the previous call.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.name is not None:
            result['name'] = self.name

        if self.name_like is not None:
            result['nameLike'] = self.name_like

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameLike') is not None:
            self.name_like = m.get('nameLike')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

