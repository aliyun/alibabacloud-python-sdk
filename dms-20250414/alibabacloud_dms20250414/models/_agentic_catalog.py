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
        data_source_uuid: str = None,
        db_type: str = None,
        description: str = None,
        name: str = None,
        properties: Dict[str, Any] = None,
        region_id: str = None,
        state: int = None,
        storage_location: str = None,
    ):
        # The business attributes of the catalog, returned as key-value pairs. The following keys may be included:
        # 
        # - **ALIAS**: the alias of the data source
        # - **HOST**: the endpoint of the data source
        # - **PORT**: the connection port of the data source
        # - **ENV_TYPE**: the environment type of the data source
        # - **VERSION**: the database version of the data source
        # - **SYNC_ALIAS**: whether automatic synchronization of instance aliases is enabled
        self.catalog_biz_attrs = catalog_biz_attrs
        # The type of the catalog. Valid values:
        # 
        # - **JDBC**: relational database catalog
        # - **DataLake**: data lake catalog
        # - **Dataset**: knowledge base catalog
        self.catalog_type = catalog_type
        # The unique identifier of the catalog.
        self.catalog_uuid = catalog_uuid
        # The unique identifier of the data source associated with the catalog.
        self.data_source_uuid = data_source_uuid
        # The database type of the data source associated with the catalog. The value is the uppercase name of the database type, such as MYSQL.
        self.db_type = db_type
        # The description of the catalog.
        self.description = description
        # The name of the catalog.
        self.name = name
        # The extended properties of the catalog, returned as key-value pairs.
        self.properties = properties
        # The region ID of the data source associated with the catalog.
        self.region_id = region_id
        # The status of the catalog. Valid values:
        # 
        # - **0**: Normal. This value is set when the data source is created.
        # - **-1**: Deleted. This value is set when the data source is deleted.
        # 
        # Disabling a data source does not change the status of the catalog.
        self.state = state
        # The storage location. This property is returned only for catalogs of the DataLake type.
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

        if self.data_source_uuid is not None:
            result['DataSourceUuid'] = self.data_source_uuid

        if self.db_type is not None:
            result['DbType'] = self.db_type

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

        if m.get('DataSourceUuid') is not None:
            self.data_source_uuid = m.get('DataSourceUuid')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

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

