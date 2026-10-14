# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListTablesRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListTablesRequestListQuery = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The paged query conditions.
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
            temp_model = main_models.ListTablesRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class ListTablesRequestListQuery(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        keyword: str = None,
        owner_id: str = None,
        page_no: int = None,
        page_size: int = None,
        sub_types: List[str] = None,
    ):
        # The asset catalog: project name and business unit name.
        self.catalog = catalog
        # The supported keyword: table name.
        self.keyword = keyword
        # The ID of the owner.
        self.owner_id = owner_id
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The table types. If you do not specify this parameter or pass an empty list, all table types are queried. Valid values:
        # - PHYSICAL_TABLE: Physical table of the compute source.
        # - PHYSICAL_VIEW: View of the compute source.
        # - PHYSICAL_MATERIALIZED_VIEW: Materialized view of the compute source.
        # - STREAM_TABLE: Meta table.
        # - MIRROR_TABLE: Mirror table.
        # - DIM: Logical dimension table.
        # - FACT: Logical fact table.
        # - SUM_BIZ_UNIT: Logical aggregate table.
        # - LOGIC_VIEW: Logical view.
        # - DATASOURCE_TABLE: Data source table.
        # - DATASOURCE_VIEW: Data source view.
        # - DATASOURCE_MATERIALIZED_VIEW: Data source materialized view.
        self.sub_types = sub_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sub_types is not None:
            result['SubTypes'] = self.sub_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SubTypes') is not None:
            self.sub_types = m.get('SubTypes')

        return self

