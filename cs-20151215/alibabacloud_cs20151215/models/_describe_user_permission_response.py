# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeUserPermissionResponse(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[main_models.DescribeUserPermissionResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.DescribeUserPermissionResponseBody()
                self.body.append(temp_model.from_map(k1))

        return self

class DescribeUserPermissionResponseBody(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        role_name: str = None,
        role_type: str = None,
        is_owner: int = None,
        is_ram_role: int = None,
    ):
        # The authorization setting. Valid values:
        # 
        # *   `{cluster_id}` is returned if the permissions are scoped to a cluster.
        # *   `{cluster_id}/{namespace}` is returned if the permissions are scoped to a namespace of a cluster.
        # *   `all-clusters` is returned if the permissions are scoped to all clusters.
        self.resource_id = resource_id
        # The authorization type. Valid values:
        # 
        # *   `cluster`: indicates that the permissions are scoped to a cluster.
        # *   `namespace`: indicates that the permissions are scoped to a namespace of a cluster.
        # *   `console`: indicates that the permissions are scoped to all clusters.
        self.resource_type = resource_type
        # The name of the custom role. If a custom role is assigned, the value is the name of the assigned custom role.
        self.role_name = role_name
        # The type of predefined role. Valid values:
        # 
        # *   `admin`: administrator
        # *   `ops`: O\\&M engineer
        # *   `dev`: developer
        # *   `restricted`: restricted user
        # *   `custom`: custom role
        self.role_type = role_type
        # Indicates whether the permissions are granted to the cluster owner.
        # 
        # *   `0`: indicates that the permissions are not granted to the cluster owner.
        # *   `1`: indicates that the permissions are granted to the cluster owner. The cluster owner is the administrator.
        self.is_owner = is_owner
        # Indicates whether the permissions are granted to the RAM role. Valid values:
        # 
        # *   `0`: indicates that the permissions are not granted to the RAM role.
        # *   `1`: indicates that the permissions are granted to the RAM role.
        self.is_ram_role = is_ram_role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['resource_id'] = self.resource_id

        if self.resource_type is not None:
            result['resource_type'] = self.resource_type

        if self.role_name is not None:
            result['role_name'] = self.role_name

        if self.role_type is not None:
            result['role_type'] = self.role_type

        if self.is_owner is not None:
            result['is_owner'] = self.is_owner

        if self.is_ram_role is not None:
            result['is_ram_role'] = self.is_ram_role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resource_id') is not None:
            self.resource_id = m.get('resource_id')

        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')

        if m.get('role_name') is not None:
            self.role_name = m.get('role_name')

        if m.get('role_type') is not None:
            self.role_type = m.get('role_type')

        if m.get('is_owner') is not None:
            self.is_owner = m.get('is_owner')

        if m.get('is_ram_role') is not None:
            self.is_ram_role = m.get('is_ram_role')

        return self

