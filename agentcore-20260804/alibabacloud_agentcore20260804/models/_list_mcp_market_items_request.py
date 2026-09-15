# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMcpMarketItemsRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        mcp_type: str = None,
        next_token: str = None,
        official_tag: str = None,
    ):
        # The keyword used to filter MCP marketplace templates.
        self.keyword = keyword
        # The maximum number of records to return in this query.
        self.max_results = max_results
        # The MCP type.
        self.mcp_type = mcp_type
        # The pagination token used to retrieve the next page of results.
        self.next_token = next_token
        # The official usage tag.
        self.official_tag = official_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.mcp_type is not None:
            result['mcpType'] = self.mcp_type

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.official_tag is not None:
            result['officialTag'] = self.official_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('mcpType') is not None:
            self.mcp_type = m.get('mcpType')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('officialTag') is not None:
            self.official_tag = m.get('officialTag')

        return self

