# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListProjectsRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListProjectsRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.list_query = list_query
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            temp_model = main_models.ListProjectsRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListProjectsRequestListQuery(DaraModel):
    def __init__(
        self,
        env: str = None,
        keyword: str = None,
        mode: str = None,
        page_no: int = None,
        page_size: int = None,
        tag_list: List[str] = None,
    ):
        self.env = env
        self.keyword = keyword
        self.mode = mode
        self.page_no = page_no
        self.page_size = page_size
        self.tag_list = tag_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['Env'] = self.env

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.tag_list is not None:
            result['TagList'] = self.tag_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')

        return self

