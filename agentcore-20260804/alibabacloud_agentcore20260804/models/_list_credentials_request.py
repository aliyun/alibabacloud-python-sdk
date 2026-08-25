# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCredentialsRequest(DaraModel):
    def __init__(
        self,
        credential_type: str = None,
        max_results: int = None,
        name_like: str = None,
        next_token: str = None,
    ):
        self.credential_type = credential_type
        self.max_results = max_results
        self.name_like = name_like
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_type is not None:
            result['credentialType'] = self.credential_type

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.name_like is not None:
            result['nameLike'] = self.name_like

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('credentialType') is not None:
            self.credential_type = m.get('credentialType')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nameLike') is not None:
            self.name_like = m.get('nameLike')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

