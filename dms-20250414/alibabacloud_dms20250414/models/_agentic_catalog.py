# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class AgenticCatalog(DaraModel):
    def __init__(
        self,
        catalog_biz_attrs: Dict[str, Any] = None,
        catalog_type: str = None,
        catalog_uuid: str = None,
        data_source_type: str = None,
        data_source_uuid: str = None,
        description: str = None,
        name: str = None,
        properties: Dict[str, Any] = None,
        region_id: str = None,
        state: int = None,
        storage_location: str = None,
    ):
        # A collection of key-value pairs that represents business attributes for the catalog, such as the data owner or department.
        self.catalog_biz_attrs = catalog_biz_attrs
        # The type of the catalog. For example, `INTERNAL_METADATA` or `THIRD_PARTY`.
        self.catalog_type = catalog_type
        # The unique identifier (UUID) of the catalog. This parameter is system-generated and output-only.
        self.catalog_uuid = catalog_uuid
        # The type of the data source associated with the catalog. For example, `MySQL`, `PostgreSQL`, or `OSS`.
        self.data_source_type = data_source_type
        # The unique identifier (UUID) of the associated data source.
        self.data_source_uuid = data_source_uuid
        # The description of the catalog. It can be up to 2,048 characters long.
        self.description = description
        # The display name of the catalog. The name can be up to 256 characters long.
        self.name = name
        # A collection of key-value pairs that represents additional technical properties for the catalog.
        self.properties = properties
        # The ID of the region where the catalog is located. For example, `cn-hangzhou`.
        self.region_id = region_id
        # The current state of the catalog. Valid values are: `0` (Creating), `1` (Active), `2` (Deleting), and `3` (Error).
        self.state = state
        # The storage location for the catalog\\"s metadata, such as a database name or a file path.
        self.storage_location = storage_location

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_biz_attrs is not None:
            result['CatalogBizAttrs'] = self.catalog_biz_attrs

        if self.catalog_type is not None:
            result['CatalogType'] = self.catalog_type

        if self.catalog_uuid is not None:
            result['CatalogUuid'] = self.catalog_uuid

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.data_source_uuid is not None:
            result['DataSourceUuid'] = self.data_source_uuid

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.state is not None:
            result['State'] = self.state

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogBizAttrs') is not None:
            self.catalog_biz_attrs = m.get('CatalogBizAttrs')

        if m.get('CatalogType') is not None:
            self.catalog_type = m.get('CatalogType')

        if m.get('CatalogUuid') is not None:
            self.catalog_uuid = m.get('CatalogUuid')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('DataSourceUuid') is not None:
            self.data_source_uuid = m.get('DataSourceUuid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        return self

