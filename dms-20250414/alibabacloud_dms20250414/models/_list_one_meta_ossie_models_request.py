# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOneMetaOssieModelsRequest(DaraModel):
    def __init__(
        self,
        catalog_uuid: str = None,
        database_uuid: str = None,
        enable_vector_search: bool = None,
        max_results: int = None,
        next_token: str = None,
        query: str = None,
        tag: str = None,
    ):
        # The UUID of the associated folder.
        self.catalog_uuid = catalog_uuid
        # The UUID of the associated database.
        self.database_uuid = database_uuid
        # Specifies whether to use semantic search.
        self.enable_vector_search = enable_vector_search
        # The maximum number of records per page.
        self.max_results = max_results
        # The token for the next query.
        self.next_token = next_token
        # The search keyword.
        # 
        # This parameter is required.
        self.query = query
        # The semantic model tag.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_uuid is not None:
            result['CatalogUuid'] = self.catalog_uuid

        if self.database_uuid is not None:
            result['DatabaseUuid'] = self.database_uuid

        if self.enable_vector_search is not None:
            result['EnableVectorSearch'] = self.enable_vector_search

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.query is not None:
            result['Query'] = self.query

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogUuid') is not None:
            self.catalog_uuid = m.get('CatalogUuid')

        if m.get('DatabaseUuid') is not None:
            self.database_uuid = m.get('DatabaseUuid')

        if m.get('EnableVectorSearch') is not None:
            self.enable_vector_search = m.get('EnableVectorSearch')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

