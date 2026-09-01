# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class AgenticKnowledgeView(DaraModel):
    def __init__(
        self,
        catalog_uuid: str = None,
        column_name: str = None,
        create_time: int = None,
        database_uuid: str = None,
        description: str = None,
        entity_type: str = None,
        extra: Dict[str, Any] = None,
        knowledge_uuid: str = None,
        level: str = None,
        locked: bool = None,
        locked_by: str = None,
        locked_time: int = None,
        modify_time: int = None,
        qualified_name: str = None,
        source: str = None,
        summary: str = None,
        title: str = None,
        unit_catalog_uuid: str = None,
        unit_database_uuid: str = None,
        version: str = None,
    ):
        self.catalog_uuid = catalog_uuid
        self.column_name = column_name
        self.create_time = create_time
        self.database_uuid = database_uuid
        self.description = description
        self.entity_type = entity_type
        self.extra = extra
        self.knowledge_uuid = knowledge_uuid
        self.level = level
        self.locked = locked
        self.locked_by = locked_by
        self.locked_time = locked_time
        self.modify_time = modify_time
        self.qualified_name = qualified_name
        self.source = source
        self.summary = summary
        self.title = title
        self.unit_catalog_uuid = unit_catalog_uuid
        self.unit_database_uuid = unit_database_uuid
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_uuid is not None:
            result['CatalogUuid'] = self.catalog_uuid

        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.database_uuid is not None:
            result['DatabaseUuid'] = self.database_uuid

        if self.description is not None:
            result['Description'] = self.description

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.extra is not None:
            result['Extra'] = self.extra

        if self.knowledge_uuid is not None:
            result['KnowledgeUuid'] = self.knowledge_uuid

        if self.level is not None:
            result['Level'] = self.level

        if self.locked is not None:
            result['Locked'] = self.locked

        if self.locked_by is not None:
            result['LockedBy'] = self.locked_by

        if self.locked_time is not None:
            result['LockedTime'] = self.locked_time

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.qualified_name is not None:
            result['QualifiedName'] = self.qualified_name

        if self.source is not None:
            result['Source'] = self.source

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.unit_catalog_uuid is not None:
            result['UnitCatalogUuid'] = self.unit_catalog_uuid

        if self.unit_database_uuid is not None:
            result['UnitDatabaseUuid'] = self.unit_database_uuid

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogUuid') is not None:
            self.catalog_uuid = m.get('CatalogUuid')

        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DatabaseUuid') is not None:
            self.database_uuid = m.get('DatabaseUuid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('KnowledgeUuid') is not None:
            self.knowledge_uuid = m.get('KnowledgeUuid')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Locked') is not None:
            self.locked = m.get('Locked')

        if m.get('LockedBy') is not None:
            self.locked_by = m.get('LockedBy')

        if m.get('LockedTime') is not None:
            self.locked_time = m.get('LockedTime')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('QualifiedName') is not None:
            self.qualified_name = m.get('QualifiedName')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UnitCatalogUuid') is not None:
            self.unit_catalog_uuid = m.get('UnitCatalogUuid')

        if m.get('UnitDatabaseUuid') is not None:
            self.unit_database_uuid = m.get('UnitDatabaseUuid')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

