# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListApiByAppRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        page_query: main_models.ListApiByAppRequestPageQuery = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # This parameter is required.
        self.page_query = page_query

    def validate(self):
        if self.page_query:
            self.page_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.page_query is not None:
            result['PageQuery'] = self.page_query.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('PageQuery') is not None:
            temp_model = main_models.ListApiByAppRequestPageQuery()
            self.page_query = temp_model.from_map(m.get('PageQuery'))

        return self

class ListApiByAppRequestPageQuery(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # appKey
        # 
        # This parameter is required.
        self.app_key = app_key
        self.keyword = keyword
        # This parameter is required.
        self.page_num = page_num
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

