# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReparseGroupSourceRequest(DaraModel):
    def __init__(
        self,
        force_sync: bool = None,
        group_id: str = None,
        source_id: str = None,
        tenant_id: str = None,
    ):
        # 是否等待解析完成；默认 false 异步受理，true 同步等待，网关超时 300000ms
        self.force_sync = force_sync
        # 资料所属协作空间 ID
        # 
        # This parameter is required.
        self.group_id = group_id
        # 当前空间物理 GROUP 资料 ID；引用资料只读
        # 
        # This parameter is required.
        self.source_id = source_id
        # 租户ID，公共参数；缺省时使用调用方默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.force_sync is not None:
            result['forceSync'] = self.force_sync

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('forceSync') is not None:
            self.force_sync = m.get('forceSync')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

