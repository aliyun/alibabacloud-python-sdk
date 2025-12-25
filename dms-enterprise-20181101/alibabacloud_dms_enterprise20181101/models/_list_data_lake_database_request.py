# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataLakeDatabaseRequest(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        data_region: str = None,
        max_results: int = None,
        next_token: str = None,
        search_key: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # The name of the data catalog. You can view the name of the data catalog in the [DLF console](https://dlf.console.aliyun.com/cn-hangzhou/metadata/catalog?spm=a2c4g.11186623.0.0.5a225658pT4Dkr).
        # 
        # This parameter is required.
        self.catalog_name = catalog_name
        # The region where the data lake resides.
        # 
        # This parameter is required.
        self.data_region = data_region
        # The number of entries per page. Valid values: 1 to 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token
        # The keyword that is used to search for databases.
        self.search_key = search_key
        # The ID of the tenant.
        # 
        # > To view the tenant ID, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.data_region is not None:
            result['DataRegion'] = self.data_region

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('DataRegion') is not None:
            self.data_region = m.get('DataRegion')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

