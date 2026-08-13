# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MoveResourceRequest(DaraModel):
    def __init__(
        self,
        source_directory_id: str = None,
        source_id: str = None,
        target_directory_id: str = None,
        tenant_id: str = None,
    ):
        # 源目录 ID（资源当前所在的个人目录）
        # 
        # This parameter is required.
        self.source_directory_id = source_directory_id
        # 待移动的资源 ID
        # 
        # This parameter is required.
        self.source_id = source_id
        # 目标目录 ID（资源即将移动到的个人目录）
        # 
        # This parameter is required.
        self.target_directory_id = target_directory_id
        # 租户ID，公共参数；winnexo-cli 通过 --tenant-id 显式传入
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('sourceDirectoryId') is not None:
            self.source_directory_id = m.get('sourceDirectoryId')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('targetDirectoryId') is not None:
            self.target_directory_id = m.get('targetDirectoryId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

