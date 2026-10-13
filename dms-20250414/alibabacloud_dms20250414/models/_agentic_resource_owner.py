# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AgenticResourceOwner(DaraModel):
    def __init__(
        self,
        catalog_alias: str = None,
        catalog_data_source_type: str = None,
        catalog_env_type: str = None,
        catalog_host: str = None,
        catalog_port: str = None,
        catalog_uuid: str = None,
        data_source_uuid: str = None,
        database_qualified_name: str = None,
        database_uuid: str = None,
        grant_by: str = None,
        grant_from: str = None,
        owner_principal_id: str = None,
        owner_principal_type: str = None,
        resource_type: str = None,
    ):
        # The instance alias. This display property comes from the catalog to which the resource belongs and is used only for frontend display to align with the data permission list. It is populated only in the My Assets or Managed Resources query scenarios and is null in other scenarios.
        self.catalog_alias = catalog_alias
        # The instance data source type, used only for frontend display. It is populated only in the My Assets or Managed Resources query scenarios and is null in other scenarios.
        self.catalog_data_source_type = catalog_data_source_type
        # The instance environment type, used only for frontend display. It is populated only in the My Assets or Managed Resources query scenarios and is null in other scenarios.
        self.catalog_env_type = catalog_env_type
        # The instance host, used only for frontend display. Built-in sample data sources are masked as ******. It is populated only in the My Assets or Managed Resources query scenarios and is null in other scenarios.
        self.catalog_host = catalog_host
        # The instance port, used only for frontend display. Built-in sample data sources are masked as ******. It is populated only in the My Assets or Managed Resources query scenarios and is null in other scenarios.
        self.catalog_port = catalog_port
        # The UUID of the catalog to which the resource belongs.
        self.catalog_uuid = catalog_uuid
        # The UUID of the instance data source to which the resource belongs. It is used only for frontend display and instance locating. Non-sensitive connection information is not masked. It is populated only in the My Assets or Managed Resources query scenarios and is null in other scenarios.
        self.data_source_uuid = data_source_uuid
        # The fully qualified name of the database. It has a value only when ResourceType is DATABASE and is populated by the downstream service, which facilitates direct frontend display. For MySQL, it is the database name itself. For PostgreSQL or SQL Server, it is in the format of DatabaseName.SchemaName.
        self.database_qualified_name = database_qualified_name
        # The UUID of the database. It has a value only when ResourceType is DATABASE.
        self.database_uuid = database_uuid
        # The principal ID of the operator who registered the ownership relationship. The downstream service does not return this field in the My Assets query scenario, and the value is null.
        self.grant_by = grant_by
        # The source channel of the ownership. CONSOLE indicates manual registration in the console. Other values indicate that the ownership is written by the built-in system. The downstream service does not return this field in the My Assets query scenario, and the value is null.
        self.grant_from = grant_from
        # The principal ID of the owner. This is the internal principal ID of the gateway with a usr_ or agt_ prefix, not the Alibaba Cloud UID.
        self.owner_principal_id = owner_principal_id
        # The principal type of the owner. Valid values:
        # - USER: Human user.
        # - AGENT: Managed agent.
        self.owner_principal_type = owner_principal_type
        # The ownership level. Valid values:
        # - INSTANCE: Instance-level ownership. The coordinate includes only CatalogUuid.
        # - DATABASE: Database-level ownership. The coordinate includes CatalogUuid and DatabaseUuid.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_alias is not None:
            result['CatalogAlias'] = self.catalog_alias

        if self.catalog_data_source_type is not None:
            result['CatalogDataSourceType'] = self.catalog_data_source_type

        if self.catalog_env_type is not None:
            result['CatalogEnvType'] = self.catalog_env_type

        if self.catalog_host is not None:
            result['CatalogHost'] = self.catalog_host

        if self.catalog_port is not None:
            result['CatalogPort'] = self.catalog_port

        if self.catalog_uuid is not None:
            result['CatalogUuid'] = self.catalog_uuid

        if self.data_source_uuid is not None:
            result['DataSourceUuid'] = self.data_source_uuid

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
        if m.get('CatalogAlias') is not None:
            self.catalog_alias = m.get('CatalogAlias')

        if m.get('CatalogDataSourceType') is not None:
            self.catalog_data_source_type = m.get('CatalogDataSourceType')

        if m.get('CatalogEnvType') is not None:
            self.catalog_env_type = m.get('CatalogEnvType')

        if m.get('CatalogHost') is not None:
            self.catalog_host = m.get('CatalogHost')

        if m.get('CatalogPort') is not None:
            self.catalog_port = m.get('CatalogPort')

        if m.get('CatalogUuid') is not None:
            self.catalog_uuid = m.get('CatalogUuid')

        if m.get('DataSourceUuid') is not None:
            self.data_source_uuid = m.get('DataSourceUuid')

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

