# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OneMetaDatabaseEngineMeta(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        encoding: str = None,
        schema_name: str = None,
        storage_capacity: int = None,
    ):
        self.catalog_name = catalog_name
        self.encoding = encoding
        self.schema_name = schema_name
        self.storage_capacity = storage_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.encoding is not None:
            result['Encoding'] = self.encoding

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.storage_capacity is not None:
            result['StorageCapacity'] = self.storage_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('StorageCapacity') is not None:
            self.storage_capacity = m.get('StorageCapacity')

        return self

