# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class Table(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        created_by: str = None,
        id: str = None,
        is_external: bool = None,
        name: str = None,
        owner: str = None,
        path: str = None,
        schema: main_models.Schema = None,
        schema_id: int = None,
        storage_action: str = None,
        storage_action_timestamp: int = None,
        storage_class: str = None,
        updated_at: int = None,
        updated_by: str = None,
    ):
        self.created_at = created_at
        self.created_by = created_by
        self.id = id
        self.is_external = is_external
        self.name = name
        self.owner = owner
        self.path = path
        self.schema = schema
        self.schema_id = schema_id
        self.storage_action = storage_action
        self.storage_action_timestamp = storage_action_timestamp
        self.storage_class = storage_class
        self.updated_at = updated_at
        self.updated_by = updated_by

    def validate(self):
        if self.schema:
            self.schema.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.id is not None:
            result['id'] = self.id

        if self.is_external is not None:
            result['isExternal'] = self.is_external

        if self.name is not None:
            result['name'] = self.name

        if self.owner is not None:
            result['owner'] = self.owner

        if self.path is not None:
            result['path'] = self.path

        if self.schema is not None:
            result['schema'] = self.schema.to_map()

        if self.schema_id is not None:
            result['schemaId'] = self.schema_id

        if self.storage_action is not None:
            result['storageAction'] = self.storage_action

        if self.storage_action_timestamp is not None:
            result['storageActionTimestamp'] = self.storage_action_timestamp

        if self.storage_class is not None:
            result['storageClass'] = self.storage_class

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('isExternal') is not None:
            self.is_external = m.get('isExternal')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('schema') is not None:
            temp_model = main_models.Schema()
            self.schema = temp_model.from_map(m.get('schema'))

        if m.get('schemaId') is not None:
            self.schema_id = m.get('schemaId')

        if m.get('storageAction') is not None:
            self.storage_action = m.get('storageAction')

        if m.get('storageActionTimestamp') is not None:
            self.storage_action_timestamp = m.get('storageActionTimestamp')

        if m.get('storageClass') is not None:
            self.storage_class = m.get('storageClass')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')

        return self

