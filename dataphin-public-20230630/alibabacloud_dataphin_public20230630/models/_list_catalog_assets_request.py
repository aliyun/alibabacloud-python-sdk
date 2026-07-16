# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListCatalogAssetsRequest(DaraModel):
    def __init__(
        self,
        list_catalog_assets_query: main_models.ListCatalogAssetsRequestListCatalogAssetsQuery = None,
        op_tenant_id: int = None,
    ):
        # The query parameters.
        # 
        # This parameter is required.
        self.list_catalog_assets_query = list_catalog_assets_query
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.list_catalog_assets_query:
            self.list_catalog_assets_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_catalog_assets_query is not None:
            result['ListCatalogAssetsQuery'] = self.list_catalog_assets_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListCatalogAssetsQuery') is not None:
            temp_model = main_models.ListCatalogAssetsRequestListCatalogAssetsQuery()
            self.list_catalog_assets_query = temp_model.from_map(m.get('ListCatalogAssetsQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListCatalogAssetsRequestListCatalogAssetsQuery(DaraModel):
    def __init__(
        self,
        asset_type: str = None,
        keyword: str = None,
        name: str = None,
        page_num: int = None,
        page_size: int = None,
        query_mode: str = None,
    ):
        # The asset type. Default value: TABLE. Valid values:
        # - TABLE: table, including views and materialized views.
        # - INDEX: technical metric.
        # - BIZ_INDEX: business metric.
        # - API: API.
        # - PAGE: dashboard.
        self.asset_type = asset_type
        # The search keyword. Used when queryMode is set to ASSET_SEARCH. Supports keyword matching against the asset full name, asset name, asset display name, and asset description. If this parameter is not specified, all assets are queried.
        self.keyword = keyword
        # The asset name. Used when queryMode is set to EXACT_MATCH. If this parameter is not specified, all assets are queried.
        self.name = name
        # The page number. Default value: 1.
        self.page_num = page_num
        # The page size. Default value: 10.
        self.page_size = page_size
        # The query type. Determines whether to use name for exact matching or keyword for fuzzy search. Default value: EXACT_MATCH. Valid values:
        # - EXACT_MATCH: exact match.
        # - ASSET_SEARCH: fuzzy search.
        self.query_mode = query_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.name is not None:
            result['Name'] = self.name

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_mode is not None:
            result['QueryMode'] = self.query_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryMode') is not None:
            self.query_mode = m.get('QueryMode')

        return self

