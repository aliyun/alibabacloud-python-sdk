# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class IcebergTable(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        created_by: str = None,
        iceberg_table_metadata: main_models.IcebergTableMetadata = None,
        id: str = None,
        name: str = None,
        owner: str = None,
        path: str = None,
        updated_at: int = None,
        updated_by: str = None,
        version: int = None,
    ):
        self.created_at = created_at
        self.created_by = created_by
        self.iceberg_table_metadata = iceberg_table_metadata
        self.id = id
        self.name = name
        self.owner = owner
        self.path = path
        self.updated_at = updated_at
        self.updated_by = updated_by
        self.version = version

    def validate(self):
        if self.iceberg_table_metadata:
            self.iceberg_table_metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.iceberg_table_metadata is not None:
            result['icebergTableMetadata'] = self.iceberg_table_metadata.to_map()

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.owner is not None:
            result['owner'] = self.owner

        if self.path is not None:
            result['path'] = self.path

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('icebergTableMetadata') is not None:
            temp_model = main_models.IcebergTableMetadata()
            self.iceberg_table_metadata = temp_model.from_map(m.get('icebergTableMetadata'))

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

