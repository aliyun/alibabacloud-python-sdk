# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFreeExplorationWorkItemShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_names_shrink: str = None,
        app_token: str = None,
        collaboration_group_id: str = None,
        member_user_ids_shrink: str = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        tenant_id: str = None,
        title: str = None,
        visibility: str = None,
    ):
        # The technical names of the selected digital workers.
        # 
        # This parameter is required.
        self.agent_names_shrink = agent_names_shrink
        # 平台应用 Token（控制台签发）。传入后将以 opsUserId 或 opsUserCode 指定的用户身份执行
        self.app_token = app_token
        # The ID of the collaboration workspace to which the work item belongs.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The actual members of the topic, including the creator. For public topics, members of the entire workspace are not enumerated.
        self.member_user_ids_shrink = member_user_ids_shrink
        # 代理用户编码（租户内唯一），仅当应用凭证配置为 source_uid 时使用
        self.ops_user_code = ops_user_code
        # 代理用户ID（WINNEXO 平台用户ID），仅当应用凭证配置为 winnexo_uid 时使用
        self.ops_user_id = ops_user_id
        # The tenant ID. This is a common parameter. If this parameter is not specified, the default tenant of the caller is used.
        self.tenant_id = tenant_id
        # The title of the work item.
        # 
        # This parameter is required.
        self.title = title
        # The actual visibility scope. Valid values: PRIVATE, COLLABORATIVE, and PUBLIC.
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

        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.member_user_ids_shrink is not None:
            result['memberUserIds'] = self.member_user_ids_shrink

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

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

        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('memberUserIds') is not None:
            self.member_user_ids_shrink = m.get('memberUserIds')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('visibility') is not None:
            self.visibility = m.get('visibility')

        return self

