# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTablesRequest(DaraModel):
    def __init__(
        self,
        marker: str = None,
        max_item: int = None,
        prefix: str = None,
        schema_name: str = None,
        type: str = None,
    ):
        # Specifies the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries to return on each page.
        self.max_item = max_item
        # The names of the returned resources. The names must start with the value specified by the prefix parameter. If the prefix parameter is set to a, the names of the returned resources must start with a.
        self.prefix = prefix
        # The name of the schema.
        self.schema_name = schema_name
        # The type of the table.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.marker is not None:
            result['marker'] = self.marker

        if self.max_item is not None:
            result['maxItem'] = self.max_item

        if self.prefix is not None:
            result['prefix'] = self.prefix

        if self.schema_name is not None:
            result['schemaName'] = self.schema_name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')

        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')

        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

