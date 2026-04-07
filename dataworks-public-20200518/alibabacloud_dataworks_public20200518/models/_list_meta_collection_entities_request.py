# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMetaCollectionEntitiesRequest(DaraModel):
    def __init__(
        self,
        collection_qualified_name: str = None,
        entity_type: str = None,
        keyword: str = None,
        next_token: str = None,
        page_size: int = None,
    ):
        # The unique identifier of the collection.
        # 
        # This parameter is required.
        self.collection_qualified_name = collection_qualified_name
        # The type of the entities.
        # 
        # For example, if this parameter is set to maxcompute-table, the entity is a MaxCompute table.
        self.entity_type = entity_type
        # The search keyword.
        self.keyword = keyword
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collection_qualified_name is not None:
            result['CollectionQualifiedName'] = self.collection_qualified_name

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CollectionQualifiedName') is not None:
            self.collection_qualified_name = m.get('CollectionQualifiedName')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

