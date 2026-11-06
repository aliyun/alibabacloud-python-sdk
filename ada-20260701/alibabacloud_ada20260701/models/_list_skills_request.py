# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSkillsRequest(DaraModel):
    def __init__(
        self,
        creator_id: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        q: str = None,
        scope: str = None,
        visibility: str = None,
    ):
        # Filters the skills by creator ID.
        self.creator_id = creator_id
        # The number of entries per page for cursor-based pagination. Valid values: 1 to 100. Default value: 20. If you explicitly specify this parameter, cursor-based pagination takes precedence.
        self.max_results = max_results
        # The next token returned by the server. Do not pass this parameter for the first query. For subsequent queries, use the value from the previous response.
        self.next_token = next_token
        # The compatible page number parameter for page number-based pagination. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The compatible number of entries per page for page number-based pagination. Valid values: 1 to 100. Default value: 20.
        self.page_size = page_size
        # Performs a fuzzy match on the skill name or description.
        self.q = q
        # The query scope for skills. Valid values: `SYSTEM` and `CUSTOM`. If this parameter is omitted, both official and custom skills are queried.
        self.scope = scope
        # Filters skills by visibility. Common values are `user` and `tenant`.
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.q is not None:
            result['Q'] = self.q

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Q') is not None:
            self.q = m.get('Q')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

