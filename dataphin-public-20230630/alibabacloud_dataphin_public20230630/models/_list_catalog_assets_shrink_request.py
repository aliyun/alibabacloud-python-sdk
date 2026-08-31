# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCatalogAssetsShrinkRequest(DaraModel):
    def __init__(
        self,
        list_catalog_assets_query_shrink: str = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The query parameters.
        # 
        # This parameter is required.
        self.list_catalog_assets_query_shrink = list_catalog_assets_query_shrink
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator user.
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_catalog_assets_query_shrink is not None:
            result['ListCatalogAssetsQuery'] = self.list_catalog_assets_query_shrink

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListCatalogAssetsQuery') is not None:
            self.list_catalog_assets_query_shrink = m.get('ListCatalogAssetsQuery')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

