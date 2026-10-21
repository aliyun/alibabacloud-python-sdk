# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgenticDatabaseRequest(DaraModel):
    def __init__(
        self,
        catalog_uuid: str = None,
        max_results: int = None,
        next_token: str = None,
        search_key: str = None,
        sort_field_name: str = None,
        sort_order: str = None,
    ):
        # The UUID of the catalog to which the database belongs. You can obtain the UUID by calling ListAgenticCatalog or SearchAgenticCatalog.
        # 
        # This parameter is required.
        self.catalog_uuid = catalog_uuid
        # The maximum number of entries to return per page.
        self.max_results = max_results
        # The token for the next query. You do not need to specify this parameter for the first query. When you query the next page, set this parameter to the NextToken value returned in the previous response.
        self.next_token = next_token
        # The search keyword used to match the database name or the prefix of the fully qualified name.
        self.search_key = search_key
        # The field used for sorting. This parameter is case-sensitive. Valid values:
        # 
        # - **name**: Sorts by database name.
        # - **qualifiedName**: Sorts by the fully qualified name of the database.
        # 
        # If you specify other values, the request fails. If you do not specify this parameter, the results are returned in the default order, and the SortOrder parameter does not take effect.
        self.sort_field_name = sort_field_name
        # The sort order. This parameter takes effect only when SortFieldName is specified. This parameter is case-insensitive. Valid values:
        # 
        # - **ASC** (default): Ascending order.
        # - **DESC**: Descending order.
        # 
        # If you specify other values, the request fails.
        self.sort_order = sort_order

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_uuid is not None:
            result['CatalogUuid'] = self.catalog_uuid

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.sort_field_name is not None:
            result['SortFieldName'] = self.sort_field_name

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogUuid') is not None:
            self.catalog_uuid = m.get('CatalogUuid')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('SortFieldName') is not None:
            self.sort_field_name = m.get('SortFieldName')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        return self

