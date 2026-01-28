# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class OneMetaTableBaseInfo(DaraModel):
    def __init__(
        self,
        catalog_type: str = None,
        database_uuid: str = None,
        description: str = None,
        engine_meta: main_models.OneMetaTableEngineMeta = None,
        name: str = None,
        qualified_name: str = None,
        table_type: str = None,
        table_uuid: str = None,
    ):
        self.catalog_type = catalog_type
        self.database_uuid = database_uuid
        self.description = description
        self.engine_meta = engine_meta
        self.name = name
        self.qualified_name = qualified_name
        self.table_type = table_type
        self.table_uuid = table_uuid

    def validate(self):
        if self.engine_meta:
            self.engine_meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_type is not None:
            result['CatalogType'] = self.catalog_type

        if self.database_uuid is not None:
            result['DatabaseUuid'] = self.database_uuid

        if self.description is not None:
            result['Description'] = self.description

        if self.engine_meta is not None:
            result['EngineMeta'] = self.engine_meta.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.qualified_name is not None:
            result['QualifiedName'] = self.qualified_name

        if self.table_type is not None:
            result['TableType'] = self.table_type

        if self.table_uuid is not None:
            result['TableUuid'] = self.table_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogType') is not None:
            self.catalog_type = m.get('CatalogType')

        if m.get('DatabaseUuid') is not None:
            self.database_uuid = m.get('DatabaseUuid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EngineMeta') is not None:
            temp_model = main_models.OneMetaTableEngineMeta()
            self.engine_meta = temp_model.from_map(m.get('EngineMeta'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('QualifiedName') is not None:
            self.qualified_name = m.get('QualifiedName')

        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')

        if m.get('TableUuid') is not None:
            self.table_uuid = m.get('TableUuid')

        return self

