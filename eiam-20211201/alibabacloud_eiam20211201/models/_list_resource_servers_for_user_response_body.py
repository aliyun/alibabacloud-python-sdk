# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListResourceServersForUserResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resource_servers: List[main_models.ListResourceServersForUserResponseBodyResourceServers] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        # 本次调用返回的查询凭证（Token）值，用于下一次翻页查询。
        self.next_token = next_token
        self.request_id = request_id
        self.resource_servers = resource_servers
        self.total_count = total_count

    def validate(self):
        if self.resource_servers:
            for v1 in self.resource_servers:
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourceServers'] = []
        if self.resource_servers is not None:
            for k1 in self.resource_servers:
                result['ResourceServers'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_servers = []
        if m.get('ResourceServers') is not None:
            for k1 in m.get('ResourceServers'):
                temp_model = main_models.ListResourceServersForUserResponseBodyResourceServers()
                self.resource_servers.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListResourceServersForUserResponseBodyResourceServers(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        instance_id: str = None,
        resource_server_identifier: str = None,
        resource_server_scopes: List[main_models.ListResourceServersForUserResponseBodyResourceServersResourceServerScopes] = None,
    ):
        # 资源服务应用的唯一标识
        self.application_id = application_id
        # 实例唯一标识
        self.instance_id = instance_id
        self.resource_server_identifier = resource_server_identifier
        # 资源服务Scope权限集合
        self.resource_server_scopes = resource_server_scopes

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
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.resource_server_identifier is not None:
            result['ResourceServerIdentifier'] = self.resource_server_identifier

        result['ResourceServerScopes'] = []
        if self.resource_server_scopes is not None:
            for k1 in self.resource_server_scopes:
                result['ResourceServerScopes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ResourceServerIdentifier') is not None:
            self.resource_server_identifier = m.get('ResourceServerIdentifier')

        self.resource_server_scopes = []
        if m.get('ResourceServerScopes') is not None:
            for k1 in m.get('ResourceServerScopes'):
                temp_model = main_models.ListResourceServersForUserResponseBodyResourceServersResourceServerScopes()
                self.resource_server_scopes.append(temp_model.from_map(k1))

        return self

class ListResourceServersForUserResponseBodyResourceServersResourceServerScopes(DaraModel):
    def __init__(
        self,
        has_direct_authorization: bool = None,
        has_inherit_authorization: bool = None,
        resource_server_scope_id: str = None,
        resource_server_scope_name: str = None,
    ):
        # 直接分配给当前用户的权限，视为直接授权。
        self.has_direct_authorization = has_direct_authorization
        # 通过用户隶属的组织、组获取的权限，视为继承权限。
        self.has_inherit_authorization = has_inherit_authorization
        # ResourceServerScope唯一标识
        self.resource_server_scope_id = resource_server_scope_id
        # ResourceServerScope名称
        self.resource_server_scope_name = resource_server_scope_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_direct_authorization is not None:
            result['HasDirectAuthorization'] = self.has_direct_authorization

        if self.has_inherit_authorization is not None:
            result['HasInheritAuthorization'] = self.has_inherit_authorization

        if self.resource_server_scope_id is not None:
            result['ResourceServerScopeId'] = self.resource_server_scope_id

        if self.resource_server_scope_name is not None:
            result['ResourceServerScopeName'] = self.resource_server_scope_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasDirectAuthorization') is not None:
            self.has_direct_authorization = m.get('HasDirectAuthorization')

        if m.get('HasInheritAuthorization') is not None:
            self.has_inherit_authorization = m.get('HasInheritAuthorization')

        if m.get('ResourceServerScopeId') is not None:
            self.resource_server_scope_id = m.get('ResourceServerScopeId')

        if m.get('ResourceServerScopeName') is not None:
            self.resource_server_scope_name = m.get('ResourceServerScopeName')

        return self

