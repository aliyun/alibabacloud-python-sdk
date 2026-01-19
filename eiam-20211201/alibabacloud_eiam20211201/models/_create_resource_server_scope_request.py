# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateResourceServerScopeRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        authorization_type: str = None,
        instance_id: str = None,
        resource_server_scope_name: str = None,
        resource_server_scope_type: str = None,
        resource_server_scope_value: str = None,
    ):
        # IDaaS的应用资源ID。
        # 
        # This parameter is required.
        self.application_id = application_id
        self.authorization_type = authorization_type
        # IDaaS EIAM实例的ID。
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # 权限名称
        # 
        # This parameter is required.
        self.resource_server_scope_name = resource_server_scope_name
        # 权限类型
        # 
        # This parameter is required.
        self.resource_server_scope_type = resource_server_scope_type
        # 权限值，大小写不敏感，格式(${ResourceType}:${ResourceOption}:${ResourceRestrict})
        # 
        # This parameter is required.
        self.resource_server_scope_value = resource_server_scope_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.authorization_type is not None:
            result['AuthorizationType'] = self.authorization_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.resource_server_scope_name is not None:
            result['ResourceServerScopeName'] = self.resource_server_scope_name

        if self.resource_server_scope_type is not None:
            result['ResourceServerScopeType'] = self.resource_server_scope_type

        if self.resource_server_scope_value is not None:
            result['ResourceServerScopeValue'] = self.resource_server_scope_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('AuthorizationType') is not None:
            self.authorization_type = m.get('AuthorizationType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ResourceServerScopeName') is not None:
            self.resource_server_scope_name = m.get('ResourceServerScopeName')

        if m.get('ResourceServerScopeType') is not None:
            self.resource_server_scope_type = m.get('ResourceServerScopeType')

        if m.get('ResourceServerScopeValue') is not None:
            self.resource_server_scope_value = m.get('ResourceServerScopeValue')

        return self

