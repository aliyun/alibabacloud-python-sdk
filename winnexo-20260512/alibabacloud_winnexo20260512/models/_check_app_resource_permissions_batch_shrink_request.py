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
        # 检查项
        # 
        # This parameter is required.
        self.checks_shrink = checks_shrink
        # 资源所属租户 ID；省略为调用人当前租户
        self.resource_tenant_id = resource_tenant_id
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

