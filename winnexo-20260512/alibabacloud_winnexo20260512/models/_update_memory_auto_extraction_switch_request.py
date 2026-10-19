# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMemoryAutoExtractionSwitchRequest(DaraModel):
    def __init__(
        self,
        clear_existing: bool = None,
        enabled: bool = None,
        group_id: str = None,
        owner_type: str = None,
        tenant_id: str = None,
    ):
        # 是否同时清空当前记忆范围内的全部自动记忆；开启或关闭时均可使用，不影响手动记忆；不传时为 false
        self.clear_existing = clear_existing
        # 目标开关状态；true 为开启自动记忆拾取，false 为关闭
        # 
        # This parameter is required.
        self.enabled = enabled
        # 写作协作空间 ID；ownerType 为 group 时必填，且当前鉴权用户须为该空间的活跃成员；ownerType 为 user 时不传
        self.group_id = group_id
        # 记忆归属范围；user 为当前鉴权用户的个人记忆，group 为指定写作协作空间的记忆；不传时默认为 user
        self.owner_type = owner_type
        # 租户 ID，查询参数；不传时使用调用方的默认租户
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clear_existing is not None:
            result['clearExisting'] = self.clear_existing

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.owner_type is not None:
            result['ownerType'] = self.owner_type

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clearExisting') is not None:
            self.clear_existing = m.get('clearExisting')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('ownerType') is not None:
            self.owner_type = m.get('ownerType')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

