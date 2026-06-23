# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class GrantPermissionsRequest(DaraModel):
    def __init__(
        self,
        body: List[main_models.GrantPermissionsRequestBody] = None,
    ):
        # The request body parameters.
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
        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.GrantPermissionsRequestBody()
                self.body.append(temp_model.from_map(k1))

        return self

class GrantPermissionsRequestBody(DaraModel):
    def __init__(
        self,
        cluster: str = None,
        is_custom: bool = None,
        is_ram_role: bool = None,
        namespace: str = None,
        role_name: str = None,
        role_type: str = None,
    ):
        # The ID of the cluster to be authorized.
        # 
        # - If the value of the `role_type` parameter is `all-clusters`, set this parameter to an empty string.
        # 
        # This parameter is required.
        self.cluster = cluster
        # Specifies whether the authorization is a custom authorization, which means `role_name` uses a custom ClusterRole name.
        self.is_custom = is_custom
        # Specifies whether the authorization is for a RAM role.
        self.is_ram_role = is_ram_role
        # The namespace name. This parameter is empty by default for cluster-level authorization.
        self.namespace = namespace
        # The name of the preset role. Valid values:
        # 
        # - `admin`: administrator.
        # - `admin-view`: read-only administrator.
        # - `ops`: O&M engineer.
        # - `dev`: developer.
        # - `restricted`: restricted user.
        # - Custom ClusterRole name.
        # 
        # >Notice: 
        # 
        # - `admin`, `admin-view`, `ops`: cannot be granted at the namespace level.
        # - `admin-view`: cannot be granted at the all-clusters level.
        # .
        # 
        # This parameter is required.
        self.role_name = role_name
        # The authorization type. Valid values:
        # 
        # - `cluster`: cluster level.
        # - `namespace`: namespace level.
        # - `all-clusters`: all-clusters level.
        # 
        # This parameter is required.
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

