# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApiKeysRequest(DaraModel):
    def __init__(
        self,
        api_key_id: int = None,
        description: str = None,
        max_results: int = None,
        next_token: str = None,
        workspace_id: str = None,
    ):
        # API Key ID。
        self.api_key_id = api_key_id
        self.description = description
        self.max_results = max_results
        self.next_token = next_token
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key_id is not None:
            result['apiKeyId'] = self.api_key_id

        if self.description is not None:
            result['description'] = self.description

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKeyId') is not None:
            self.api_key_id = m.get('apiKeyId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

