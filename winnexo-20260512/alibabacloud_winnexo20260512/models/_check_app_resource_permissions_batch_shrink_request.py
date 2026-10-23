# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckAppResourcePermissionsBatchShrinkRequest(DaraModel):
    def __init__(
        self,
        checks_shrink: str = None,
        resource_tenant_id: str = None,
        target_user_id: int = None,
        target_user_tenant_id: str = None,
        tenant_id: str = None,
    ):
        # The check items.
        # 
        # This parameter is required.
        self.checks_shrink = checks_shrink
        # The ID of the tenant to which the resource belongs. If not specified, the current tenant of the caller is used.
        self.resource_tenant_id = resource_tenant_id
        # The ID of the target platform user.
        self.target_user_id = target_user_id
        # The tenant to which the target user belongs. This parameter is required for cross-tenant targets.
        self.target_user_tenant_id = target_user_tenant_id
        # The tenant ID. This is a common parameter. If not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checks_shrink is not None:
            result['checks'] = self.checks_shrink

        if self.resource_tenant_id is not None:
            result['resourceTenantId'] = self.resource_tenant_id

        if self.target_user_id is not None:
            result['targetUserId'] = self.target_user_id

        if self.target_user_tenant_id is not None:
            result['targetUserTenantId'] = self.target_user_tenant_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checks') is not None:
            self.checks_shrink = m.get('checks')

        if m.get('resourceTenantId') is not None:
            self.resource_tenant_id = m.get('resourceTenantId')

        if m.get('targetUserId') is not None:
            self.target_user_id = m.get('targetUserId')

        if m.get('targetUserTenantId') is not None:
            self.target_user_tenant_id = m.get('targetUserTenantId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

