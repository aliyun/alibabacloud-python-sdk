# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgenticTableIndexRequest(DaraModel):
    def __init__(
        self,
        database_uuid: str = None,
        table_qualified_name: str = None,
    ):
        # The UUID of the database to which the table belongs. You can obtain this value by calling ListAgenticDatabase or SearchAgenticDatabase.
        # 
        # This parameter is required.
        self.database_uuid = database_uuid
        # The fully qualified name of the table. You can obtain this value from the QualifiedName parameter returned by ListAgenticTableBaseInfo. You must specify the full name.
        # 
        # This parameter is required.
        self.table_qualified_name = table_qualified_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_uuid is not None:
            result['DatabaseUuid'] = self.database_uuid

        if self.table_qualified_name is not None:
            result['TableQualifiedName'] = self.table_qualified_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseUuid') is not None:
            self.database_uuid = m.get('DatabaseUuid')

        if m.get('TableQualifiedName') is not None:
            self.table_qualified_name = m.get('TableQualifiedName')

        return self

