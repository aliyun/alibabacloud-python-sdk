# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWebApplicationRevisionsRequest(DaraModel):
    def __init__(
        self,
        limit: int = None,
        namespace_id: str = None,
        next_token: str = None,
    ):
        # The number of applications returned.
        self.limit = limit
        # The namespace ID.
        # 
        # This parameter is required.
        self.namespace_id = namespace_id
        # The pagination token.
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

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

