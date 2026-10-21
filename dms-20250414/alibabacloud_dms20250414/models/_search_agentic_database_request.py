# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchAgenticDatabaseRequest(DaraModel):
    def __init__(
        self,
        catalog_uuid: str = None,
        db_type: str = None,
        env_type: str = None,
        max_results: int = None,
        next_token: str = None,
        search_key: str = None,
    ):
        # The UUID of the catalog that limits the search scope. If you do not specify this parameter, the search is performed across all catalogs.
        self.catalog_uuid = catalog_uuid
        # The database type. This parameter filters the results exactly by the database type of the data source associated with the catalog. The value is the uppercase name of the database type, such as MYSQL.
        self.db_type = db_type
        # The environment type. This parameter filters the results exactly by the environment of the associated data source. Valid values: product, pre, dev, test, sit, uat, pet, and stag.
        self.env_type = env_type
        # The maximum number of entries to return per page.
        self.max_results = max_results
        # The token for the next query. You do not need to specify this parameter for the first query. When you query the next page, set this parameter to the NextToken value returned from the previous query.
        self.next_token = next_token
        # The search keyword. It matches the name, fully qualified name, and search name of the database, as well as the name or data source alias of the associated catalog.
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_uuid is not None:
            result['CatalogUuid'] = self.catalog_uuid

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogUuid') is not None:
            self.catalog_uuid = m.get('CatalogUuid')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        return self

