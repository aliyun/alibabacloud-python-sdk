# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgenticCatalogRequest(DaraModel):
    def __init__(
        self,
        catalog_type: str = None,
        max_results: int = None,
        next_token: str = None,
        search_key: str = None,
    ):
        # The catalog type. This parameter is used to filter catalogs by exact type. Valid values:
        # 
        # - **JDBC**: relational database catalog
        # - **DataLake**: data lake catalog
        # - **Dataset**: knowledge base catalog
        self.catalog_type = catalog_type
        # The maximum number of entries to return per page.
        self.max_results = max_results
        # The token for the next query. You do not need to specify this parameter for the first query. To query the next page, set this parameter to the NextToken value returned from the previous query.
        self.next_token = next_token
        # The search keyword for the catalog name. Matches catalogs by name prefix.
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_type is not None:
            result['CatalogType'] = self.catalog_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogType') is not None:
            self.catalog_type = m.get('CatalogType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        return self

