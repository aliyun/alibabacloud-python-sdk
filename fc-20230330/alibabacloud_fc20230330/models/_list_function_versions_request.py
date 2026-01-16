# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFunctionVersionsRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        limit: int = None,
        next_token: str = None,
    ):
        # The sorting mode of function versions. Valid values: BACKWARD and FORWARD.
        self.direction = direction
        # The number of function versions that are returned.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['direction'] = self.direction

        if self.limit is not None:
            result['limit'] = self.limit

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('direction') is not None:
            self.direction = m.get('direction')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

