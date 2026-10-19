# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReplaceManualMemoryRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        group_id: str = None,
        owner_type: str = None,
        tenant_id: str = None,
    ):
        # 手动记忆 profile.md 的完整新内容，将覆盖原内容；传空字符串表示清空，字段必须传入
        # 
        # This parameter is required.
        self.content = content
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
        if self.content is not None:
            result['content'] = self.content

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.owner_type is not None:
            result['ownerType'] = self.owner_type

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('ownerType') is not None:
            self.owner_type = m.get('ownerType')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

