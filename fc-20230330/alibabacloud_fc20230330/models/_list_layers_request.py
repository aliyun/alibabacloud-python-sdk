# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLayersRequest(DaraModel):
    def __init__(
        self,
        limit: int = None,
        next_token: str = None,
        official: str = None,
        prefix: str = None,
        public: str = None,
    ):
        # The number of layers that are returned
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # Specifies whether the layer is official. Valid values: true and false.
        self.official = official
        # The name prefix of the layer.
        self.prefix = prefix
        # Specifies whether the layer is public. Valid values: true and false.
        self.public = public

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

        if self.official is not None:
            result['official'] = self.official

        if self.prefix is not None:
            result['prefix'] = self.prefix

        if self.public is not None:
            result['public'] = self.public

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('official') is not None:
            self.official = m.get('official')

        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')

        if m.get('public') is not None:
            self.public = m.get('public')

        return self

