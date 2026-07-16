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
        # 集群访问配置，格式为：
        # 
        # - 当是集群维度授权时，格式为：`{cluster_id}`。
        # - 当是命名空间维度授权时，格式为：`{cluster_id}/{namespace}`。
        # - 当是所有集群授权时，值固定为：`all-clusters`。
        self.resource_id = resource_id
        # 授权类型，取值：
        # 
        # - `cluster`：集群维度。
        # - `namespace`：命名空间维度。
        # - `console`：所有集群维度的授权。
        self.resource_type = resource_type
        # 自定义角色名称，当授权自定义角色时，该字段为指定的自定义集群管理角色名称。
        self.role_name = role_name
        # 预置的角色类型，取值：
        # 
        # - `admin`：管理员。
        # - `ops`：运维人员。
        # - `dev`：开发人员。
        # - `restricted`：受限用户。
        # - `custom`：使用自定义的集群管理角色。
        self.role_type = role_type
        # 是否为集群创建者的授权，取值：
        # 
        # - `0`：代表不是集群创建者的授权记录。
        # - `1`：代表该授权记录为集群创建者的管理员权限。
        self.is_owner = is_owner
        # 是否为RAM角色授权，取值：
        # 
        # - `0`：代表当前记录不是RAM角色授权。
        # - `1`：代表当前记录是RAM角色授权。
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

