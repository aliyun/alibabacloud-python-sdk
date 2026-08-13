# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReplaceObjectBindingsShrinkRequest(DaraModel):
    def __init__(
        self,
        object_bindings_shrink: str = None,
        source_id: str = None,
        tenant_id: str = None,
    ):
        # 新的对象绑定列表（全量替换；传空列表表示清空所有绑定）
        # 
        # This parameter is required.
        self.object_bindings_shrink = object_bindings_shrink
        # 数据源 ID（租户内唯一）
        # 
        # This parameter is required.
        self.source_id = source_id
        # 租户ID，公共参数；winnexo-cli 通过 --tenant-id 显式传入
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.object_bindings_shrink is not None:
            result['objectBindings'] = self.object_bindings_shrink

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('objectBindings') is not None:
            self.object_bindings_shrink = m.get('objectBindings')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

