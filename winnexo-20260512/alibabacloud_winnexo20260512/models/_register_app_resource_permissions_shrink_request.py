# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterAppResourcePermissionsShrinkRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        items_shrink: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        resource_tenant_id: str = None,
        tenant_id: str = None,
    ):
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The batch authorization item.
        # 
        # This parameter is required.
        self.items_shrink = items_shrink
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The batch authorization item.
        self.resource_tenant_id = resource_tenant_id
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

        if self.items_shrink is not None:
            result['items'] = self.items_shrink

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.resource_tenant_id is not None:
            result['resourceTenantId'] = self.resource_tenant_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('items') is not None:
            self.items_shrink = m.get('items')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('resourceTenantId') is not None:
            self.resource_tenant_id = m.get('resourceTenantId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

