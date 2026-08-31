# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListAssetTopicsRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListAssetTopicsRequestListQuery = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The query parameters.
        # 
        # This parameter is required.
        self.list_query = list_query
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator.
        self.op_user_id = op_user_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = main_models.ListAssetTopicsRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class ListAssetTopicsRequestListQuery(DaraModel):
    def __init__(
        self,
        asset_type: str = None,
        keyword: str = None,
        page: int = None,
        page_size: int = None,
    ):
        # The asset type. Valid values: TABLE, INDEX, API, DASHBOARD.
        # 
        # This parameter is required.
        self.asset_type = asset_type
        # The keyword for the topic name. Maximum length: 256 characters.
        self.keyword = keyword
        # The page number. Default value: 1.
        self.page = page
        # The number of entries per page. Default value: 50. Valid values: 1 to 200.
        self.page_size = page_size

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

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

