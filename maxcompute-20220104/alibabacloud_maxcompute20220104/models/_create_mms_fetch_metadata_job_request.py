# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateMmsFetchMetadataJobRequest(DaraModel):
    def __init__(
        self,
        db_name: str = None,
        table_names: List[str] = None,
    ):
        # Updates metadata for the specified source database, schema, or dataset.
        self.db_name = db_name
        # Updates metadata for the specified source tables.
        self.table_names = table_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_name is not None:
            result['dbName'] = self.db_name

        if self.table_names is not None:
            result['tableNames'] = self.table_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')

        if m.get('tableNames') is not None:
            self.table_names = m.get('tableNames')

        return self

