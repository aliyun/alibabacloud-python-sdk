# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class DeleteAppResourcePermissionsRequest(DaraModel):
    def __init__(
        self,
        items: List[main_models.DeleteAppResourcePermissionsRequestItems] = None,
        resource_tenant_id: str = None,
        tenant_id: str = None,
    ):
        # The scope of the permissions to be revoked.
        # 
        # This parameter is required.
        self.items = items
        # The ID of the tenant to which the resource belongs. If not specified, the current tenant of the caller is used.
        self.resource_tenant_id = resource_tenant_id
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.resource_tenant_id is not None:
            result['resourceTenantId'] = self.resource_tenant_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.DeleteAppResourcePermissionsRequestItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('resourceTenantId') is not None:
            self.resource_tenant_id = m.get('resourceTenantId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

class DeleteAppResourcePermissionsRequestItems(DaraModel):
    def __init__(
        self,
        grantee_ids: List[str] = None,
        grantee_tenant_id: str = None,
        grantee_type: str = None,
        include_descendants: bool = None,
        resource_key: str = None,
        resource_type: str = None,
        scope: str = None,
    ):
        # The list of grantee principal IDs.
        self.grantee_ids = grantee_ids
        # The ID of the tenant to which the grantee user belongs. This parameter is optional if the user and the resource belong to the same tenant, and is required for cross-tenant users.
        self.grantee_tenant_id = grantee_tenant_id
        # The grantee principal type.
        self.grantee_type = grantee_type
        # Specifies whether to include dot-separated descendant resources for the RESOURCE. Default value: false.
        self.include_descendants = include_descendants
        # The dot-separated resource key whose first segment is the application key of the APP.
        # 
        # This parameter is required.
        self.resource_key = resource_key
        # The resource type. Set the value to APP_RESOURCE.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The deletion scope: by resource or by principal.
        # 
        # This parameter is required.
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grantee_ids is not None:
            result['granteeIds'] = self.grantee_ids

        if self.grantee_tenant_id is not None:
            result['granteeTenantId'] = self.grantee_tenant_id

        if self.grantee_type is not None:
            result['granteeType'] = self.grantee_type

        if self.include_descendants is not None:
            result['includeDescendants'] = self.include_descendants

        if self.resource_key is not None:
            result['resourceKey'] = self.resource_key

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.scope is not None:
            result['scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('granteeIds') is not None:
            self.grantee_ids = m.get('granteeIds')

        if m.get('granteeTenantId') is not None:
            self.grantee_tenant_id = m.get('granteeTenantId')

        if m.get('granteeType') is not None:
            self.grantee_type = m.get('granteeType')

        if m.get('includeDescendants') is not None:
            self.include_descendants = m.get('includeDescendants')

        if m.get('resourceKey') is not None:
            self.resource_key = m.get('resourceKey')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        return self

