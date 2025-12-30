# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListDataSourceWithConfigRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListDataSourceWithConfigRequestListQuery = None,
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
            temp_model = main_models.ListDataSourceWithConfigRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListDataSourceWithConfigRequestListQuery(DaraModel):
    def __init__(
        self,
        name: str = None,
        owner_list: List[str] = None,
        page: int = None,
        page_size: int = None,
        scope_list: List[str] = None,
        tag: str = None,
        type_list: List[str] = None,
    ):
        self.name = name
        self.owner_list = owner_list
        # This parameter is required.
        self.page = page
        # This parameter is required.
        self.page_size = page_size
        self.scope_list = scope_list
        self.tag = tag
        self.type_list = type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.owner_list is not None:
            result['OwnerList'] = self.owner_list

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.scope_list is not None:
            result['ScopeList'] = self.scope_list

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.type_list is not None:
            result['TypeList'] = self.type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerList') is not None:
            self.owner_list = m.get('OwnerList')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ScopeList') is not None:
            self.scope_list = m.get('ScopeList')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('TypeList') is not None:
            self.type_list = m.get('TypeList')

        return self

