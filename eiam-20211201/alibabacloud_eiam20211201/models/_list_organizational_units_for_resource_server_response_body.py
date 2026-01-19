# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListOrganizationalUnitsForResourceServerResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        organizational_units: List[main_models.ListOrganizationalUnitsForResourceServerResponseBodyOrganizationalUnits] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        # 本次调用返回的查询凭证（Token）值，用于下一次翻页查询。
        self.next_token = next_token
        self.organizational_units = organizational_units
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.organizational_units:
            for v1 in self.organizational_units:
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

        result['OrganizationalUnits'] = []
        if self.organizational_units is not None:
            for k1 in self.organizational_units:
                result['OrganizationalUnits'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.organizational_units = []
        if m.get('OrganizationalUnits') is not None:
            for k1 in m.get('OrganizationalUnits'):
                temp_model = main_models.ListOrganizationalUnitsForResourceServerResponseBodyOrganizationalUnits()
                self.organizational_units.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOrganizationalUnitsForResourceServerResponseBodyOrganizationalUnits(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        organizational_unit_id: str = None,
        resource_server_scopes: List[main_models.ListOrganizationalUnitsForResourceServerResponseBodyOrganizationalUnitsResourceServerScopes] = None,
    ):
        # 实例唯一标识
        self.instance_id = instance_id
        # 组织的唯一标识
        self.organizational_unit_id = organizational_unit_id
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id

        result['ResourceServerScopes'] = []
        if self.resource_server_scopes is not None:
            for k1 in self.resource_server_scopes:
                result['ResourceServerScopes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')

        self.resource_server_scopes = []
        if m.get('ResourceServerScopes') is not None:
            for k1 in m.get('ResourceServerScopes'):
                temp_model = main_models.ListOrganizationalUnitsForResourceServerResponseBodyOrganizationalUnitsResourceServerScopes()
                self.resource_server_scopes.append(temp_model.from_map(k1))

        return self

class ListOrganizationalUnitsForResourceServerResponseBodyOrganizationalUnitsResourceServerScopes(DaraModel):
    def __init__(
        self,
        resource_server_scope_id: str = None,
        resource_server_scope_name: str = None,
    ):
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
        if self.resource_server_scope_id is not None:
            result['ResourceServerScopeId'] = self.resource_server_scope_id

        if self.resource_server_scope_name is not None:
            result['ResourceServerScopeName'] = self.resource_server_scope_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceServerScopeId') is not None:
            self.resource_server_scope_id = m.get('ResourceServerScopeId')

        if m.get('ResourceServerScopeName') is not None:
            self.resource_server_scope_name = m.get('ResourceServerScopeName')

        return self

