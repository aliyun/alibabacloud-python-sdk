# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTableKnowledgeInfoRequest(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        table_name: str = None,
        table_schema_name: str = None,
    ):
        # The ID of the physical database. You can call the [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.db_id = db_id
        # The name of the table.
        # 
        # This parameter is required.
        self.table_name = table_name
        # The schema name of the table, which is required only for SQL Server instances.
        self.table_schema_name = table_schema_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.table_schema_name is not None:
            result['TableSchemaName'] = self.table_schema_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TableSchemaName') is not None:
            self.table_schema_name = m.get('TableSchemaName')

        return self

