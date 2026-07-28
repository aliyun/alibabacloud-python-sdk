# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DlfDatabase(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        description: str = None,
        table_count: int = None,
    ):
        # The name of the database.
        self.database_name = database_name
        # The description of the database.
        self.description = description
        # The number of tables in the database. Read-only.
        self.table_count = table_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_name is not None:
            result['databaseName'] = self.database_name

        if self.description is not None:
            result['description'] = self.description

        if self.table_count is not None:
            result['tableCount'] = self.table_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('databaseName') is not None:
            self.database_name = m.get('databaseName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('tableCount') is not None:
            self.table_count = m.get('tableCount')

        return self

