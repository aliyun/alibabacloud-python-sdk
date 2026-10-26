# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgentConversationsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        purpose: str = None,
        q: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.purpose = purpose
        self.q = q

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.purpose is not None:
            result['purpose'] = self.purpose

        if self.q is not None:
            result['q'] = self.q

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('purpose') is not None:
            self.purpose = m.get('purpose')

        if m.get('q') is not None:
            self.q = m.get('q')

        return self

