# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListSecurityIdentifyRecordsRequest(DaraModel):
    def __init__(
        self,
        list_query: main_models.ListSecurityIdentifyRecordsRequestListQuery = None,
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
            temp_model = main_models.ListSecurityIdentifyRecordsRequestListQuery()
            self.list_query = temp_model.from_map(m.get('ListQuery'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ListSecurityIdentifyRecordsRequestListQuery(DaraModel):
    def __init__(
        self,
        datasource_env: str = None,
        datasource_name: str = None,
        field_name: str = None,
        is_datasource_table: bool = None,
        keyword: str = None,
        page_no: int = None,
        page_size: int = None,
        table_catalog: str = None,
        table_name: str = None,
    ):
        self.datasource_env = datasource_env
        self.datasource_name = datasource_name
        # This parameter is required.
        self.field_name = field_name
        self.is_datasource_table = is_datasource_table
        self.keyword = keyword
        self.page_no = page_no
        self.page_size = page_size
        # This parameter is required.
        self.table_catalog = table_catalog
        # This parameter is required.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.datasource_env is not None:
            result['DatasourceEnv'] = self.datasource_env

        if self.datasource_name is not None:
            result['DatasourceName'] = self.datasource_name

        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.is_datasource_table is not None:
            result['IsDatasourceTable'] = self.is_datasource_table

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.table_catalog is not None:
            result['TableCatalog'] = self.table_catalog

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasourceEnv') is not None:
            self.datasource_env = m.get('DatasourceEnv')

        if m.get('DatasourceName') is not None:
            self.datasource_name = m.get('DatasourceName')

        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('IsDatasourceTable') is not None:
            self.is_datasource_table = m.get('IsDatasourceTable')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TableCatalog') is not None:
            self.table_catalog = m.get('TableCatalog')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

