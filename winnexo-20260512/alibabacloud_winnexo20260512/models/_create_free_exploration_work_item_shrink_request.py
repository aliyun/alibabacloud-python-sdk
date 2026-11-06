# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFreeExplorationWorkItemShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_names_shrink: str = None,
        collaboration_group_id: str = None,
        member_user_ids_shrink: str = None,
        tenant_id: str = None,
        title: str = None,
        visibility: str = None,
    ):
        # 空间内数字员工技术名称，1–5 个，不可重复
        # 
        # This parameter is required.
        self.agent_names_shrink = agent_names_shrink
        # 协作空间 ID；调用者须为有效成员
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # 协作档至少一个创建人以外的有效空间成员；最多 1000 人；私密和公开档忽略；创建人始终加入
        self.member_user_ids_shrink = member_user_ids_shrink
        # 租户ID，公共参数；缺省时使用调用方默认租户
        self.tenant_id = tenant_id
        # 自由探索工作项标题，去首尾空格后 1–200 字符
        # 
        # This parameter is required.
        self.title = title
        # 可见范围：PRIVATE 私密；COLLABORATIVE 指定成员协作；PUBLIC 空间内公开
        self.visibility = visibility

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_names_shrink is not None:
            result['agentNames'] = self.agent_names_shrink

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.member_user_ids_shrink is not None:
            result['memberUserIds'] = self.member_user_ids_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.title is not None:
            result['title'] = self.title

        if self.visibility is not None:
            result['visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentNames') is not None:
            self.agent_names_shrink = m.get('agentNames')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('memberUserIds') is not None:
            self.member_user_ids_shrink = m.get('memberUserIds')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('visibility') is not None:
            self.visibility = m.get('visibility')

        return self

