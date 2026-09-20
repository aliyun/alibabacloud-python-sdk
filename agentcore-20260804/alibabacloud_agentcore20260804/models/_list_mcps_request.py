# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMcpsRequest(DaraModel):
    def __init__(
        self,
        custom_tag: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        official_tag: str = None,
        search_type: str = None,
        usage_active: bool = None,
    ):
        # Filters results by custom tag. The tag must be an exact match.
        self.custom_tag = custom_tag
        # The maximum number of entries per page.
        self.max_results = max_results
        # The MCP service name or service ID. Used together with SearchType.
        self.name = name
        # The pagination token for the next page.
        self.next_token = next_token
        # Filters results by official usage tag.
        self.official_tag = official_tag
        # The name matching method. Takes effect only when Name is specified. Valid values:
        # - accurate: exact match.
        # - blur: fuzzy match.
        # 
        # Default value: blur.
        self.search_type = search_type
        # Specifies whether the service is still bound by the official template usage.
        self.usage_active = usage_active

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_tag is not None:
            result['customTag'] = self.custom_tag

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.name is not None:
            result['name'] = self.name

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.official_tag is not None:
            result['officialTag'] = self.official_tag

        if self.search_type is not None:
            result['searchType'] = self.search_type

        if self.usage_active is not None:
            result['usageActive'] = self.usage_active

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customTag') is not None:
            self.custom_tag = m.get('customTag')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('officialTag') is not None:
            self.official_tag = m.get('officialTag')

        if m.get('searchType') is not None:
            self.search_type = m.get('searchType')

        if m.get('usageActive') is not None:
            self.usage_active = m.get('usageActive')

        return self

