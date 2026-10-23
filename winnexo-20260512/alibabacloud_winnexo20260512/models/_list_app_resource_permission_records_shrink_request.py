# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAppResourcePermissionRecordsShrinkRequest(DaraModel):
    def __init__(
        self,
        grantee_id: str = None,
        grantee_tenant_id: str = None,
        grantee_type: str = None,
        page: int = None,
        page_size: int = None,
        permissions_shrink: str = None,
        resource_key_prefix: str = None,
        resource_tenant_id: str = None,
        resource_type: str = None,
        tenant_id: str = None,
    ):
        # The grantee ID filter.
        self.grantee_id = grantee_id
        # The tenant ID filter for cross-tenant users.
        self.grantee_tenant_id = grantee_tenant_id
        # The grantee type filter.
        self.grantee_type = grantee_type
        # The page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The permission filter.
        self.permissions_shrink = permissions_shrink
        # The application key or its subpath.
        # 
        # This parameter is required.
        self.resource_key_prefix = resource_key_prefix
        # The ID of the tenant to which the resource belongs. If not specified, the current tenant of the caller is used.
        self.resource_tenant_id = resource_tenant_id
        # The resource type. Set this parameter to APP_RESOURCE.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grantee_id is not None:
            result['granteeId'] = self.grantee_id

        if self.grantee_tenant_id is not None:
            result['granteeTenantId'] = self.grantee_tenant_id

        if self.grantee_type is not None:
            result['granteeType'] = self.grantee_type

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.permissions_shrink is not None:
            result['permissions'] = self.permissions_shrink

        if self.resource_key_prefix is not None:
            result['resourceKeyPrefix'] = self.resource_key_prefix

        if self.resource_tenant_id is not None:
            result['resourceTenantId'] = self.resource_tenant_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('granteeId') is not None:
            self.grantee_id = m.get('granteeId')

        if m.get('granteeTenantId') is not None:
            self.grantee_tenant_id = m.get('granteeTenantId')

        if m.get('granteeType') is not None:
            self.grantee_type = m.get('granteeType')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('permissions') is not None:
            self.permissions_shrink = m.get('permissions')

        if m.get('resourceKeyPrefix') is not None:
            self.resource_key_prefix = m.get('resourceKeyPrefix')

        if m.get('resourceTenantId') is not None:
            self.resource_tenant_id = m.get('resourceTenantId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

