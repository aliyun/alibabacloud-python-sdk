# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class Catalog(DaraModel):
    def __init__(
        self,
        comment: str = None,
        connection_name: str = None,
        name: str = None,
        properties: Dict[str, Any] = None,
        provider: str = None,
        type: str = None,
    ):
        # The comment or description of the data catalog
        self.comment = comment
        # The connection name associated with a mounted-type Catalog. Only has a value when Provider is MySQL/PostgreSQL/Elasticsearch
        self.connection_name = connection_name
        # The unique identifier name of the data catalog
        self.name = name
        # Extended properties (JSON object). The Elasticsearch type contains information such as IndexPattern
        self.properties = properties
        # The data source provider. EventHouse is the built-in storage; MySQL/PostgreSQL/Elasticsearch are externally mounted
        self.provider = provider
        # The type of the data catalog, such as RELATIONAL
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name

        if self.name is not None:
            result['Name'] = self.name

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

