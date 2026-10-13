# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class AgenticTableBaseInfo(DaraModel):
    def __init__(
        self,
        catalog_type: str = None,
        database_qualified_name: str = None,
        database_uuid: str = None,
        description: str = None,
        engine_meta: main_models.AgenticTableEngineMeta = None,
        name: str = None,
        qualified_name: str = None,
        table_type: str = None,
    ):
        # The type of the catalog to which the table belongs. Valid values:
        # - **JDBC**: relational database catalog
        # - **DataLake**: data lake catalog
        # - **Dataset**: knowledge base catalog
        self.catalog_type = catalog_type
        # The fully qualified name of the database to which the table belongs.
        self.database_qualified_name = database_qualified_name
        # The UUID of the database to which the table belongs.
        self.database_uuid = database_uuid
        # The description of the table.
        self.description = description
        # The engine metadata of the table.
        self.engine_meta = engine_meta
        # The table name.
        self.name = name
        # The fully qualified name of the table. You can use this name as the TableQualifiedName parameter for GetAgenticTableColumn and GetAgenticTableIndex. For SQL Server, the format is schema name.table name.
        self.qualified_name = qualified_name
        # The table type. Valid values:
        # - **NORMAL**: regular table
        # - **VIEW**: view
        # - **FOREIGN**: foreign table
        # - **SYNONYM**: synonym, supported only for Oracle data sources
        self.table_type = table_type

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

        if self.database_qualified_name is not None:
            result['DatabaseQualifiedName'] = self.database_qualified_name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogType') is not None:
            self.catalog_type = m.get('CatalogType')

        if m.get('DatabaseQualifiedName') is not None:
            self.database_qualified_name = m.get('DatabaseQualifiedName')

        if m.get('DatabaseUuid') is not None:
            self.database_uuid = m.get('DatabaseUuid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EngineMeta') is not None:
            temp_model = main_models.AgenticTableEngineMeta()
            self.engine_meta = temp_model.from_map(m.get('EngineMeta'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('QualifiedName') is not None:
            self.qualified_name = m.get('QualifiedName')

        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')

        return self

