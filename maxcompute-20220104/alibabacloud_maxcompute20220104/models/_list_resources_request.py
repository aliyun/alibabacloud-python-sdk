# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListResourcesRequest(DaraModel):
    def __init__(
        self,
        marker: str = None,
        max_item: int = None,
        name: str = None,
        schema_name: str = None,
    ):
        # Specifies the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries to return on each page.
        self.max_item = max_item
        # The name of the resource.
        self.name = name
        # The name of the schema.
        self.schema_name = schema_name

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

        if self.name is not None:
            result['name'] = self.name

        if self.schema_name is not None:
            result['schemaName'] = self.schema_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')

        return self

