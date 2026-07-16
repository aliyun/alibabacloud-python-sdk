# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetCatalogAssetDetailsRequest(DaraModel):
    def __init__(
        self,
        get_catalog_asset_details_query: main_models.GetCatalogAssetDetailsRequestGetCatalogAssetDetailsQuery = None,
        op_tenant_id: int = None,
    ):
        # The paging query for the listing asset catalog list.
        # 
        # This parameter is required.
        self.get_catalog_asset_details_query = get_catalog_asset_details_query
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.get_catalog_asset_details_query:
            self.get_catalog_asset_details_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.get_catalog_asset_details_query is not None:
            result['GetCatalogAssetDetailsQuery'] = self.get_catalog_asset_details_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetCatalogAssetDetailsQuery') is not None:
            temp_model = main_models.GetCatalogAssetDetailsRequestGetCatalogAssetDetailsQuery()
            self.get_catalog_asset_details_query = temp_model.from_map(m.get('GetCatalogAssetDetailsQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class GetCatalogAssetDetailsRequestGetCatalogAssetDetailsQuery(DaraModel):
    def __init__(
        self,
        guid: str = None,
        include_columns: bool = None,
        include_detailed_attributes: bool = None,
    ):
        # The asset GUID.
        # 
        # This parameter is required.
        self.guid = guid
        # Specifies whether to include the field list. Default value: false. Valid values:
        # - false: Not included.
        # - true: Included.
        self.include_columns = include_columns
        # Specifies whether to include detailed data. Default value: false. Valid values:
        # - false: Not included.
        # - true: Included.
        self.include_detailed_attributes = include_detailed_attributes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.guid is not None:
            result['Guid'] = self.guid

        if self.include_columns is not None:
            result['IncludeColumns'] = self.include_columns

        if self.include_detailed_attributes is not None:
            result['IncludeDetailedAttributes'] = self.include_detailed_attributes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Guid') is not None:
            self.guid = m.get('Guid')

        if m.get('IncludeColumns') is not None:
            self.include_columns = m.get('IncludeColumns')

        if m.get('IncludeDetailedAttributes') is not None:
            self.include_detailed_attributes = m.get('IncludeDetailedAttributes')

        return self

