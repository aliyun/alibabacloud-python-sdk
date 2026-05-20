# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class AgenticDatabase(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        catalog_type: str = None,
        catalog_uuid: str = None,
        data_source_type: str = None,
        database_biz_attrs: Dict[str, Any] = None,
        database_uuid: str = None,
        description: str = None,
        engine_meta: main_models.AgenticDatabaseEngineMeta = None,
        name: str = None,
        properties: Dict[str, Any] = None,
        qualified_name: str = None,
        region_id: str = None,
        search_name: str = None,
        state: int = None,
        storage_location: str = None,
    ):
        self.catalog_name = catalog_name
        self.catalog_type = catalog_type
        self.catalog_uuid = catalog_uuid
        self.data_source_type = data_source_type
        self.database_biz_attrs = database_biz_attrs
        self.database_uuid = database_uuid
        self.description = description
        self.engine_meta = engine_meta
        self.name = name
        self.properties = properties
        self.qualified_name = qualified_name
        self.region_id = region_id
        self.search_name = search_name
        self.state = state
        self.storage_location = storage_location

    def validate(self):
        if self.engine_meta:
            self.engine_meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.catalog_type is not None:
            result['CatalogType'] = self.catalog_type

        if self.catalog_uuid is not None:
            result['CatalogUuid'] = self.catalog_uuid

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.database_biz_attrs is not None:
            result['DatabaseBizAttrs'] = self.database_biz_attrs

        if self.database_uuid is not None:
            result['DatabaseUuid'] = self.database_uuid

        if self.description is not None:
            result['Description'] = self.description

        if self.engine_meta is not None:
            result['EngineMeta'] = self.engine_meta.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.qualified_name is not None:
            result['QualifiedName'] = self.qualified_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        if self.state is not None:
            result['State'] = self.state

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('CatalogType') is not None:
            self.catalog_type = m.get('CatalogType')

        if m.get('CatalogUuid') is not None:
            self.catalog_uuid = m.get('CatalogUuid')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('DatabaseBizAttrs') is not None:
            self.database_biz_attrs = m.get('DatabaseBizAttrs')

        if m.get('DatabaseUuid') is not None:
            self.database_uuid = m.get('DatabaseUuid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EngineMeta') is not None:
            temp_model = main_models.AgenticDatabaseEngineMeta()
            self.engine_meta = temp_model.from_map(m.get('EngineMeta'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('QualifiedName') is not None:
            self.qualified_name = m.get('QualifiedName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        return self

