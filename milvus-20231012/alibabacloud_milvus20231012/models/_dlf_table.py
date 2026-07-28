# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DlfTable(DaraModel):
    def __init__(
        self,
        description: str = None,
        location: str = None,
        table_format: str = None,
        table_name: str = None,
        table_type: str = None,
    ):
        # A description of the table.
        self.description = description
        # The location of the table data, specified as an Object Storage Service (OSS) URI.
        self.location = location
        # The table format, such as `PAIMON`.
        self.table_format = table_format
        # The table name.
        self.table_name = table_name
        # The table type. For example, `MANAGED` indicates that DLF manages the data and metadata lifecycle.
        self.table_type = table_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.location is not None:
            result['location'] = self.location

        if self.table_format is not None:
            result['tableFormat'] = self.table_format

        if self.table_name is not None:
            result['tableName'] = self.table_name

        if self.table_type is not None:
            result['tableType'] = self.table_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('location') is not None:
            self.location = m.get('location')

        if m.get('tableFormat') is not None:
            self.table_format = m.get('tableFormat')

        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')

        if m.get('tableType') is not None:
            self.table_type = m.get('tableType')

        return self

