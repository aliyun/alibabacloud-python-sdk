# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListSecurityClassifyRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListSecurityClassifyRequestListQuery = None,
        op_tenant_id: int = None,
    ):
        # The query conditions.
        self.list_query = list_query
        # The tenant ID.
        # 
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
            temp_model = main_models.ListSecurityClassifyRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListSecurityClassifyRequestListQuery(DaraModel):
    def __init__(
        self,
        level_index: int = None,
        name: str = None,
        page_no: int = None,
        page_size: int = None,
        status_list: List[str] = None,
    ):
        # The data level ID.
        self.level_index = level_index
        # The classification name. Fuzzy match is supported.
        self.name = name
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The list of effective statuses. Valid values: ENABLE, DISABLE.
        self.status_list = status_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level_index is not None:
            result['LevelIndex'] = self.level_index

        if self.name is not None:
            result['Name'] = self.name

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LevelIndex') is not None:
            self.level_index = m.get('LevelIndex')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        return self

