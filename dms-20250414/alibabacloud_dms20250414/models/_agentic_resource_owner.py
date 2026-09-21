# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AgenticResourceOwner(DaraModel):
    def __init__(
        self,
        catalog_uuid: str = None,
        database_qualified_name: str = None,
        database_uuid: str = None,
        grant_by: str = None,
        grant_from: str = None,
        owner_principal_id: str = None,
        owner_principal_type: str = None,
        resource_type: str = None,
    ):
        # The UUID of the Catalog to which the resource belongs.
        self.catalog_uuid = catalog_uuid
        # The qualified name of the database. This field has a value only when ResourceType is DATABASE and the downstream backfills the value. This field is provided for direct display on the frontend. For MySQL, this is the database name itself. For PostgreSQL or SQL Server, this is in the format of DatabaseName.SchemaName.
        self.database_qualified_name = database_qualified_name
        # The UUID of the database. This field has a value only when ResourceType is DATABASE.
        self.database_uuid = database_uuid
        # The principal ID of the operator who registered this ownership relationship. In the "My Assets" scenario, the downstream does not return this field, and the value is null.
        self.grant_by = grant_by
        # The source channel of the ownership. Valid values:
        # - CONSOLE: Manually registered in the console.
        # - Other values: Written by the system built-in ownership mechanism.
        # 
        # In the "My Assets" scenario, the downstream does not return this field, and the value is null.
        self.grant_from = grant_from
        # The Owner principal ID. This is a gateway internal principal ID with the usr_ or agt_ prefix, not an Alibaba Cloud UID.
        self.owner_principal_id = owner_principal_id
        # The Owner principal type. Valid values:
        # - USER: Human user.
        # - AGENT: Managed Agent.
        self.owner_principal_type = owner_principal_type
        # The ownership level. Valid values:
        # - INSTANCE: Instance-level ownership. The coordinate contains only CatalogUuid.
        # - DATABASE: Database-level ownership. The coordinate contains CatalogUuid + DatabaseUuid.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_uuid is not None:
            result['CatalogUuid'] = self.catalog_uuid

        if self.database_qualified_name is not None:
            result['DatabaseQualifiedName'] = self.database_qualified_name

        if self.database_uuid is not None:
            result['DatabaseUuid'] = self.database_uuid

        if self.grant_by is not None:
            result['GrantBy'] = self.grant_by

        if self.grant_from is not None:
            result['GrantFrom'] = self.grant_from

        if self.owner_principal_id is not None:
            result['OwnerPrincipalId'] = self.owner_principal_id

        if self.owner_principal_type is not None:
            result['OwnerPrincipalType'] = self.owner_principal_type

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogUuid') is not None:
            self.catalog_uuid = m.get('CatalogUuid')

        if m.get('DatabaseQualifiedName') is not None:
            self.database_qualified_name = m.get('DatabaseQualifiedName')

        if m.get('DatabaseUuid') is not None:
            self.database_uuid = m.get('DatabaseUuid')

        if m.get('GrantBy') is not None:
            self.grant_by = m.get('GrantBy')

        if m.get('GrantFrom') is not None:
            self.grant_from = m.get('GrantFrom')

        if m.get('OwnerPrincipalId') is not None:
            self.owner_principal_id = m.get('OwnerPrincipalId')

        if m.get('OwnerPrincipalType') is not None:
            self.owner_principal_type = m.get('OwnerPrincipalType')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

