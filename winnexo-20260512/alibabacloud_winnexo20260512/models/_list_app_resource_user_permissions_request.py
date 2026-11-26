# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAppResourceUserPermissionsRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        page: int = None,
        page_size: int = None,
        permissions: List[str] = None,
        resource_key_prefix: str = None,
        resource_tenant_id: str = None,
        resource_type: str = None,
        target_user_id: int = None,
        target_user_tenant_id: str = None,
        tenant_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The number of entries per page.
        self.page = page
        # The permission filter.
        self.page_size = page_size
        # The permission filter.
        self.permissions = permissions
        # The page number.
        # 
        # This parameter is required.
        self.resource_key_prefix = resource_key_prefix
        # The ID of the target platform user.
        self.resource_tenant_id = resource_tenant_id
        # The application key or its subpath.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tenant to which the target user belongs. This parameter is required for cross-tenant targets.
        self.target_user_id = target_user_id
        # The fixed value APP_RESOURCE.
        self.target_user_tenant_id = target_user_tenant_id
        # The ID of the tenant to which the resource belongs. If omitted, the current tenant of the caller is used.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.permissions is not None:
            result['permissions'] = self.permissions

        if self.resource_key_prefix is not None:
            result['resourceKeyPrefix'] = self.resource_key_prefix

        if self.resource_tenant_id is not None:
            result['resourceTenantId'] = self.resource_tenant_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

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

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')

        if m.get('resourceKeyPrefix') is not None:
            self.resource_key_prefix = m.get('resourceKeyPrefix')

        if m.get('resourceTenantId') is not None:
            self.resource_tenant_id = m.get('resourceTenantId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('targetUserId') is not None:
            self.target_user_id = m.get('targetUserId')

        if m.get('targetUserTenantId') is not None:
            self.target_user_tenant_id = m.get('targetUserTenantId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

