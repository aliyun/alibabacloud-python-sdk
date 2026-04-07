# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLineageRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        entity_qualified_name: str = None,
        keyword: str = None,
        next_token: str = None,
        page_size: int = None,
    ):
        # The lineage type. Valid values:
        # 
        # *   up: ancestor lineage
        # *   down: descendant lineage
        # 
        # This parameter is required.
        self.direction = direction
        # The unique identifier of the entity.
        # 
        # This parameter is required.
        self.entity_qualified_name = entity_qualified_name
        # The keyword of the entity name.
        self.keyword = keyword
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The number of entries per page. Maximum value: 100.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.entity_qualified_name is not None:
            result['EntityQualifiedName'] = self.entity_qualified_name

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EntityQualifiedName') is not None:
            self.entity_qualified_name = m.get('EntityQualifiedName')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

