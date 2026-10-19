# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAppResourceUserPermissionsRequest(DaraModel):
    def __init__(
        self,
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
        # 页码
        self.page = page
        # 每页条数
        self.page_size = page_size
        # 权限点筛选
        self.permissions = permissions
        # 应用键或其子路径
        # 
        # This parameter is required.
        self.resource_key_prefix = resource_key_prefix
        # 资源所属租户 ID；省略为调用人当前租户
        self.resource_tenant_id = resource_tenant_id
        # 固定为 APP_RESOURCE
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # 目标平台用户 ID
        self.target_user_id = target_user_id
        # 目标用户所属租户；跨租户目标必填
        self.target_user_tenant_id = target_user_tenant_id
        # 租户ID，公共参数，缺省时使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

