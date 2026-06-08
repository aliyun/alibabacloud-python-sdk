# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListResourceServerScopesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        previous_token: str = None,
        request_id: str = None,
        resource_server_scopes: List[main_models.ListResourceServerScopesResponseBodyResourceServerScopes] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        # 本次调用返回的查询凭证（Token）值，用于下一次翻页查询。
        self.next_token = next_token
        self.previous_token = previous_token
        self.request_id = request_id
        self.resource_server_scopes = resource_server_scopes
        self.total_count = total_count

    def validate(self):
        if self.resource_server_scopes:
            for v1 in self.resource_server_scopes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.previous_token is not None:
            result['PreviousToken'] = self.previous_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceServerScopes'] = []
        if self.resource_server_scopes is not None:
            for k1 in self.resource_server_scopes:
                result['ResourceServerScopes'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PreviousToken') is not None:
            self.previous_token = m.get('PreviousToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_server_scopes = []
        if m.get('ResourceServerScopes') is not None:
            for k1 in m.get('ResourceServerScopes'):
                temp_model = main_models.ListResourceServerScopesResponseBodyResourceServerScopes()
                self.resource_server_scopes.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListResourceServerScopesResponseBodyResourceServerScopes(DaraModel):
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

