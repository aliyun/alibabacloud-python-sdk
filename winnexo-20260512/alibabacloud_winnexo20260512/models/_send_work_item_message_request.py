# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendWorkItemMessageRequest(DaraModel):
    def __init__(
        self,
        collaboration_group_id: str = None,
        content: str = None,
        conversation_id: str = None,
        tenant_id: str = None,
        work_item_id: str = None,
    ):
        # 目标会话所属的协作空间ID，必填，长度1至64，不能为空白。调用者须具有目标话题的查看和发送权限。
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # 用户发送的文本正文，必填，长度1至32768，不能全为空白；保留原有文本格式。
        # 
        # This parameter is required.
        self.content = content
        # 已有自由探索话题的会话ID，长度1至128，可使用创建自由探索接口返回的conversation_id。与workItemId至少传一个，同时传入时须指向同一会话。
        self.conversation_id = conversation_id
        # 业务租户ID，可选。必须属于当前调用身份的可访问租户；无权访问时拒绝请求。未传时按现有鉴权规则解析租户，多租户用户无法唯一确定时需显式指定。
        self.tenant_id = tenant_id
        # 自由探索工作项ID，长度1至256；兼容legacy-topic:<conversationId>形式。与conversationId至少传一个，同时传入时须指向同一会话。普通工作项必须为FREE_EXPLORATION类型。
        self.work_item_id = work_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.content is not None:
            result['content'] = self.content

        if self.conversation_id is not None:
            result['conversationId'] = self.conversation_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.work_item_id is not None:
            result['workItemId'] = self.work_item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('conversationId') is not None:
            self.conversation_id = m.get('conversationId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('workItemId') is not None:
            self.work_item_id = m.get('workItemId')

        return self

