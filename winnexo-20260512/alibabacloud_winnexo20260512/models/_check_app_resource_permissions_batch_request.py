# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class CheckAppResourcePermissionsBatchRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        checks: List[main_models.CheckAppResourcePermissionsBatchRequestChecks] = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        resource_tenant_id: str = None,
        target_user_id: int = None,
        target_user_tenant_id: str = None,
        tenant_id: str = None,
    ):
        # The platform application token issued by the console. If specified, the operation is performed as the user specified by opsUserId or opsUserCode.
        self.app_token = app_token
        # The check item.
        # 
        # This parameter is required.
        self.checks = checks
        # The proxy user code, which is unique within the tenant. This parameter is used only when the application credential is configured as source_uid.
        self.ops_user_code = ops_user_code
        # The proxy user ID, which is the WINNEXO platform user ID. This parameter is used only when the application credential is configured as winnexo_uid.
        self.ops_user_id = ops_user_id
        # The ID of the target platform user.
        self.resource_tenant_id = resource_tenant_id
        # The tenant to which the target user belongs. This parameter is required for cross-tenant targets.
        self.target_user_id = target_user_id
        # The check item.
        self.target_user_tenant_id = target_user_tenant_id
        # The ID of the tenant to which the resource belongs. If not specified, the current tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        if self.checks:
            for v1 in self.checks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        result['checks'] = []
        if self.checks is not None:
            for k1 in self.checks:
                result['checks'].append(k1.to_map() if k1 else None)

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

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
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        self.checks = []
        if m.get('checks') is not None:
            for k1 in m.get('checks'):
                temp_model = main_models.CheckAppResourcePermissionsBatchRequestChecks()
                self.checks.append(temp_model.from_map(k1))

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('resourceTenantId') is not None:
            self.resource_tenant_id = m.get('resourceTenantId')

        if m.get('targetUserId') is not None:
            self.target_user_id = m.get('targetUserId')

        if m.get('targetUserTenantId') is not None:
            self.target_user_tenant_id = m.get('targetUserTenantId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

class CheckAppResourcePermissionsBatchRequestChecks(DaraModel):
    def __init__(
        self,
        permission: str = None,
        resource_key: str = None,
        resource_type: str = None,
    ):
        # The target permission.
        # 
        # This parameter is required.
        self.permission = permission
        # The dot-separated resource key. The first segment is the APP application key.
        # 
        # This parameter is required.
        self.resource_key = resource_key
        # The resource type. Set the value to APP_RESOURCE.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.permission is not None:
            result['permission'] = self.permission

        if self.resource_key is not None:
            result['resourceKey'] = self.resource_key

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('permission') is not None:
            self.permission = m.get('permission')

        if m.get('resourceKey') is not None:
            self.resource_key = m.get('resourceKey')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

