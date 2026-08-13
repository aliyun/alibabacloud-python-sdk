# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePersonalDirectoryRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        operating_object_name: str = None,
        parent_directory_id: str = None,
        tenant_id: str = None,
    ):
        # 目录描述（可选）
        self.description = description
        # 目录名称
        # 
        # This parameter is required.
        self.name = name
        # 数字员工名称（已废弃：不再作为个人资源隔离条件，仅保留用于来源追溯）
        self.operating_object_name = operating_object_name
        # 父目录 ID；不传时新目录挂在用户的默认根目录下，传入时必须是当前用户的已有个人目录
        self.parent_directory_id = parent_directory_id
        # 租户ID，公共参数；winnexo-cli 通过 --tenant-id 显式传入
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.parent_directory_id is not None:
            result['parentDirectoryId'] = self.parent_directory_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('parentDirectoryId') is not None:
            self.parent_directory_id = m.get('parentDirectoryId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

