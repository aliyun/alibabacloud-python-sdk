# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class CheckAppResourcePermissionsBatchRequest(DaraModel):
    def __init__(
        self,
        checks: List[main_models.CheckAppResourcePermissionsBatchRequestChecks] = None,
        resource_tenant_id: str = None,
        target_user_id: int = None,
        target_user_tenant_id: str = None,
        tenant_id: str = None,
    ):
        # 检查项
        # 
        # This parameter is required.
        self.checks = checks
        # 资源所属租户 ID；省略为调用人当前租户
        self.resource_tenant_id = resource_tenant_id
        # 目标平台用户 ID
        self.target_user_id = target_user_id
        # 目标用户所属租户；跨租户目标必填
        self.target_user_tenant_id = target_user_tenant_id
        # 租户ID，公共参数，缺省时使用调用方默认租户
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
        result['checks'] = []
        if self.checks is not None:
            for k1 in self.checks:
                result['checks'].append(k1.to_map() if k1 else None)

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
        self.checks = []
        if m.get('checks') is not None:
            for k1 in m.get('checks'):
                temp_model = main_models.CheckAppResourcePermissionsBatchRequestChecks()
                self.checks.append(temp_model.from_map(k1))

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
        # 目标权限点
        # 
        # This parameter is required.
        self.permission = permission
        # 首段为 APP 应用键的点分资源键
        # 
        # This parameter is required.
        self.resource_key = resource_key
        # 固定为 APP_RESOURCE
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

