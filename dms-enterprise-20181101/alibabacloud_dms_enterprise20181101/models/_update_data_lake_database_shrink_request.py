# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDataLakeDatabaseShrinkRequest(DaraModel):
    def __init__(
        self,
        catalog_name: str = None,
        data_region: str = None,
        db_name: str = None,
        description: str = None,
        location: str = None,
        parameters_shrink: str = None,
        tid: int = None,
        workspace_id: int = None,
    ):
        # The catalog name.
        # 
        # This parameter is required.
        self.catalog_name = catalog_name
        # The region where the data lake resides.
        # 
        # This parameter is required.
        self.data_region = data_region
        # The name of the database that you want to query.
        # 
        # This parameter is required.
        self.db_name = db_name
        # The description of the database.
        self.description = description
        # The storage path of the database. Supports the OSS, S3, and S3A protocols.
        # 
        # This parameter is required.
        self.location = location
        # The key-value pairs of the database attributes.
        self.parameters_shrink = parameters_shrink
        # The ID of the tenant.
        # 
        # > To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.data_region is not None:
            result['DataRegion'] = self.data_region

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.description is not None:
            result['Description'] = self.description

        if self.location is not None:
            result['Location'] = self.location

        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('DataRegion') is not None:
            self.data_region = m.get('DataRegion')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

