# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetResourceServerScopeResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_server_scope: main_models.GetResourceServerScopeResponseBodyResourceServerScope = None,
    ):
        self.request_id = request_id
        self.resource_server_scope = resource_server_scope

    def validate(self):
        if self.resource_server_scope:
            self.resource_server_scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_server_scope is not None:
            result['ResourceServerScope'] = self.resource_server_scope.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceServerScope') is not None:
            temp_model = main_models.GetResourceServerScopeResponseBodyResourceServerScope()
            self.resource_server_scope = temp_model.from_map(m.get('ResourceServerScope'))

        return self

class GetResourceServerScopeResponseBodyResourceServerScope(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        authorization_type: str = None,
        instance_id: str = None,
        resource_server_scope_id: str = None,
        resource_server_scope_name: str = None,
        resource_server_scope_type: str = None,
        resource_server_scope_value: str = None,
    ):
        # IDaaS EIAM 应用Id
        self.application_id = application_id
        self.authorization_type = authorization_type
        # IDaaS EIAM 实例Id
        self.instance_id = instance_id
        # IDaaS EIAM ResourceServer下权限Id
        self.resource_server_scope_id = resource_server_scope_id
        # IDaaS EIAM ResourceServer下权限名称
        self.resource_server_scope_name = resource_server_scope_name
        # IDaaS EIAM ResourceServer下权限类型
        self.resource_server_scope_type = resource_server_scope_type
        # IDaaS EIAM ResourceServer下权限值
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

        if self.resource_server_scope_id is not None:
            result['ResourceServerScopeId'] = self.resource_server_scope_id

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

        if m.get('ResourceServerScopeId') is not None:
            self.resource_server_scope_id = m.get('ResourceServerScopeId')

        if m.get('ResourceServerScopeName') is not None:
            self.resource_server_scope_name = m.get('ResourceServerScopeName')

        if m.get('ResourceServerScopeType') is not None:
            self.resource_server_scope_type = m.get('ResourceServerScopeType')

        if m.get('ResourceServerScopeValue') is not None:
            self.resource_server_scope_value = m.get('ResourceServerScopeValue')

        return self

