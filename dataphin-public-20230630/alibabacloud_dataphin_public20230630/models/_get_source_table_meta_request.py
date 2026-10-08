# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetSourceTableMetaRequest(DaraModel):
    def __init__(
        self,
        context: main_models.GetSourceTableMetaRequestContext = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
        query: main_models.GetSourceTableMetaRequestQuery = None,
    ):
        # This parameter is required.
        self.context = context
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.op_user_id = op_user_id
        # This parameter is required.
        self.query = query

    def validate(self):
        if self.context:
            self.context.validate()
        if self.query:
            self.query.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context is not None:
            result['Context'] = self.context.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.query is not None:
            result['Query'] = self.query.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            temp_model = main_models.GetSourceTableMetaRequestContext()
            self.context = temp_model.from_map(m.get('Context'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('Query') is not None:
            temp_model = main_models.GetSourceTableMetaRequestQuery()
            self.query = temp_model.from_map(m.get('Query'))

        return self

class GetSourceTableMetaRequestQuery(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        id: str = None,
        query_mode: str = None,
        schema_name: str = None,
        table_name: str = None,
    ):
        self.catalog = catalog
        self.id = id
        self.query_mode = query_mode
        self.schema_name = schema_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.id is not None:
            result['Id'] = self.id

        if self.query_mode is not None:
            result['QueryMode'] = self.query_mode

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('QueryMode') is not None:
            self.query_mode = m.get('QueryMode')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class GetSourceTableMetaRequestContext(DaraModel):
    def __init__(
        self,
        env: str = None,
        project_id: int = None,
    ):
        self.env = env
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['Env'] = self.env

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

