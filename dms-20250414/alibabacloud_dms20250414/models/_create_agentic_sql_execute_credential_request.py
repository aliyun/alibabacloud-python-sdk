# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAgenticSqlExecuteCredentialRequest(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        catalog_uuid: str = None,
        database_uuid: str = None,
        qualified_name: str = None,
    ):
        # The name of the instance.
        self.catalog_name = catalog_name
        # The UUID of the instance.
        self.catalog_uuid = catalog_uuid
        # The UUID of the database. If you specify this parameter, the credential is restricted to this database. You can call the ListDatabases operation to obtain the UUID.
        self.database_uuid = database_uuid
        # The fully qualified name of the database. This parameter must be used together with CatalogUuid or CatalogName.
        # 
        # - MySQL database: The value is the same as the database name.
        # - PostgreSQL database or other databases with schemas: The value is in the database.schema format.
        self.qualified_name = qualified_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.catalog_uuid is not None:
            result['CatalogUuid'] = self.catalog_uuid

        if self.database_uuid is not None:
            result['DatabaseUuid'] = self.database_uuid

        if self.qualified_name is not None:
            result['QualifiedName'] = self.qualified_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('CatalogUuid') is not None:
            self.catalog_uuid = m.get('CatalogUuid')

        if m.get('DatabaseUuid') is not None:
            self.database_uuid = m.get('DatabaseUuid')

        if m.get('QualifiedName') is not None:
            self.qualified_name = m.get('QualifiedName')

        return self

