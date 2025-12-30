# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListDataDomainsRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListDataDomainsRequestListQuery = None,
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
            temp_model = main_models.ListDataDomainsRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListDataDomainsRequestListQuery(DaraModel):
    def __init__(
        self,
        biz_unit_id_list: List[int] = None,
        keyword: str = None,
        parent_id_list: List[int] = None,
    ):
        self.biz_unit_id_list = biz_unit_id_list
        self.keyword = keyword
        self.parent_id_list = parent_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_unit_id_list is not None:
            result['BizUnitIdList'] = self.biz_unit_id_list

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.parent_id_list is not None:
            result['ParentIdList'] = self.parent_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitIdList') is not None:
            self.biz_unit_id_list = m.get('BizUnitIdList')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('ParentIdList') is not None:
            self.parent_id_list = m.get('ParentIdList')

        return self

