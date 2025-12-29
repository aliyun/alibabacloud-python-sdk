# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class UpdateUserPermissionsRequest(DaraModel):
    def __init__(
        self,
        body: List[main_models.UpdateUserPermissionsRequestBody] = None,
        mode: str = None,
    ):
        # The request body.
        self.body = body
        # The authorization method. Valid values:
        # 
        # *   `apply`: The global update mode. Overwrites all existing permissions of the RAM user or RAM role on the cluster. You must specify all the permissions you want to grant to the RAM user or RAM role in the request parameters when you call this operation.
        # *   `delete`: The deletion mode. Revokes only the cluster permissions specified in the request, preserving other existing permissions of the RAM user or RAM role.
        # *   `patch`: The incremental mode. Adds only the cluster permissions specified in the request, preserving other existing permissions of the RAM user or RAM role.
        # 
        # Default value: `apply`.
        self.mode = mode

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
        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        if self.mode is not None:
            result['mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.UpdateUserPermissionsRequestBody()
                self.body.append(temp_model.from_map(k1))

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        return self

class UpdateUserPermissionsRequestBody(DaraModel):
    def __init__(
        self,
        cluster: str = None,
        is_custom: bool = None,
        is_ram_role: bool = None,
        namespace: str = None,
        role_name: str = None,
        role_type: str = None,
    ):
        # The ID of the cluster on which you want to grant permissions to the RAM role or RAM role.
        # 
        # *   Set this parameter to an empty string if `role_type` is set to `all-clusters`.
        self.cluster = cluster
        # Specifies whether to assign a custom role to the RAM user or RAM role. If you want to assign a custom role to the RAM user or RAM role, set `role_name` to the name of the custom role.
        self.is_custom = is_custom
        # Specifies whether to use a RAM role to grant permissions.
        self.is_ram_role = is_ram_role
        # The namespace that you want to authorize the RAM user or RAM role to manage. This parameter is required only if you set role_type to namespace.
        self.namespace = namespace
        # The predefined role name. Valid values:
        # 
        # *   `admin`: administrator
        # *   `admin-view`: read-only administrator
        # *   `ops`: O\\&M engineer
        # *   `dev`: developer
        # *   `restricted`: restricted user
        # *   Custom role
        # 
        # Note:
        # 
        # *   You cannot grant **namespace-level** permissions to the `admin`, `admin-view`, and `ops` roles.
        # *   You cannot grant **all cluster-level** permissions to the `admin-view` role.
        self.role_name = role_name
        # The authorization type. Valid values:
        # 
        # *   `cluster`: authorizes the RAM user or RAM role to manage the specified clusters.
        # *   `namespace`: authorizes the RAM user or RAM role to manage the specified namespaces.
        # *   `all-clusters`: authorizes the RAM user or RAM role to manage all clusters.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster is not None:
            result['cluster'] = self.cluster

        if self.is_custom is not None:
            result['is_custom'] = self.is_custom

        if self.is_ram_role is not None:
            result['is_ram_role'] = self.is_ram_role

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.role_name is not None:
            result['role_name'] = self.role_name

        if self.role_type is not None:
            result['role_type'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')

        if m.get('is_custom') is not None:
            self.is_custom = m.get('is_custom')

        if m.get('is_ram_role') is not None:
            self.is_ram_role = m.get('is_ram_role')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('role_name') is not None:
            self.role_name = m.get('role_name')

        if m.get('role_type') is not None:
            self.role_type = m.get('role_type')

        return self

