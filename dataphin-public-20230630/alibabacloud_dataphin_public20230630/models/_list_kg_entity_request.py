# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListKgEntityRequest(DaraModel):
    def __init__(
        self,
        entity_type: str = None,
        list_query: main_models.ListKgEntityRequestListQuery = None,
        op_tenant_id: int = None,
        workspace_id: str = None,
    ):
        # The entity type code.
        self.entity_type = entity_type
        # The paged query filter conditions.
        self.list_query = list_query
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.list_query:
            self.list_query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.list_query is not None:
            result['ListQuery'] = self.list_query.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('ListQuery') is not None:
            temp_model = main_models.ListKgEntityRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class ListKgEntityRequestListQuery(DaraModel):
    def __init__(
        self,
        filter_list: List[main_models.ListKgEntityRequestListQueryFilterList] = None,
        keyword: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # The property filter conditions.
        self.filter_list = filter_list
        # The keyword for searching display properties.
        self.keyword = keyword
        # The page number. Default value: 1.
        self.page_num = page_num
        # The number of records per page. Default value: 20.
        self.page_size = page_size

    def validate(self):
        if self.filter_list:
            for v1 in self.filter_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FilterList'] = []
        if self.filter_list is not None:
            for k1 in self.filter_list:
                result['FilterList'].append(k1.to_map() if k1 else None)

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter_list = []
        if m.get('FilterList') is not None:
            for k1 in m.get('FilterList'):
                temp_model = main_models.ListKgEntityRequestListQueryFilterList()
                self.filter_list.append(temp_model.from_map(k1))

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class ListKgEntityRequestListQueryFilterList(DaraModel):
    def __init__(
        self,
        op: str = None,
        property_code: str = None,
        value: str = None,
    ):
        # The operator. Valid values:
        # - eq: equal to.
        # - neq: not equal to.
        # - contains: contains.
        # - gt: greater than.
        # - gte: greater than or equal to.
        # - lt: less than.
        # - lte: less than or equal to.
        # - like: fuzzy match.
        # 
        # This parameter is required.
        self.op = op
        # The property code.
        # 
        # This parameter is required.
        self.property_code = property_code
        # The property match value.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op is not None:
            result['Op'] = self.op

        if self.property_code is not None:
            result['PropertyCode'] = self.property_code

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Op') is not None:
            self.op = m.get('Op')

        if m.get('PropertyCode') is not None:
            self.property_code = m.get('PropertyCode')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

