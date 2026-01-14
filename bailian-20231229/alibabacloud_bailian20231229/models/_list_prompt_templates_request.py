# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPromptTemplatesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        type: str = None,
    ):
        # The maximum number of returned entries.
        self.max_results = max_results
        # The keyword that is used to search for templates.
        self.name = name
        # The token that determines the start position of the query. Set this parameter to the value of the NextToken parameter that is returned from the last call.
        self.next_token = next_token
        # The type of the template. Valid values: · System · Custom
        self.type = type

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

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

