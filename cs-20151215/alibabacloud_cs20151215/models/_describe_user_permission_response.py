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
        # The cluster access configuration. The format varies based on the authorization scope:
        # 
        # - Cluster-level authorization: `{cluster_id}`.
        # - Namespace-level authorization: `{cluster_id}/{namespace}`.
        # - All-cluster authorization: `all-clusters`.
        self.resource_id = resource_id
        # The authorization type. Valid values:
        # 
        # - `cluster`: cluster-level.
        # - `namespace`: namespace-level.
        # - `console`: all-cluster-level authorization.
        self.resource_type = resource_type
        # The custom role name. When a custom role is authorized, this field specifies the name of the custom cluster management role.
        self.role_name = role_name
        # The preset role type. Valid values:
        # 
        # - `admin`: Administrator.
        # - `ops`: O&M engineer.
        # - `dev`: Developer.
        # - `restricted`: Restricted user.
        # - `custom`: Custom cluster management role.
        self.role_type = role_type
        # Indicates whether the authorization belongs to the cluster creator. Valid values:
        # 
        # - `0`: The authorization record does not belong to the cluster creator.
        # - `1`: The authorization record represents the administrator permissions of the cluster creator.
        self.is_owner = is_owner
        # Indicates whether the authorization is for a RAM role. Valid values:
        # 
        # - `0`: The record is not a RAM role authorization.
        # - `1`: The record is a RAM role authorization.
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

