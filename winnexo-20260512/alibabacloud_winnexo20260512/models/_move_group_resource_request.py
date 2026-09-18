# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MoveGroupResourceRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        source_directory_id: str = None,
        source_id: str = None,
        target_directory_id: str = None,
        tenant_id: str = None,
    ):
        # 协作空间 ID
        # 
        # This parameter is required.
        self.group_id = group_id
        # 资料当前所在的空间物理目录真实 ID，不支持 root 哨兵
        # 
        # This parameter is required.
        self.source_directory_id = source_directory_id
        # 待移动的物理 GROUP 资料 ID；引用资料只读
        # 
        # This parameter is required.
        self.source_id = source_id
        # 同一空间目标物理目录真实 ID，必须与源目录不同
        # 
        # This parameter is required.
        self.target_directory_id = target_directory_id
        # 租户ID，公共参数；缺省时使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.source_directory_id is not None:
            result['sourceDirectoryId'] = self.source_directory_id

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.target_directory_id is not None:
            result['targetDirectoryId'] = self.target_directory_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('sourceDirectoryId') is not None:
            self.source_directory_id = m.get('sourceDirectoryId')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('targetDirectoryId') is not None:
            self.target_directory_id = m.get('targetDirectoryId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

