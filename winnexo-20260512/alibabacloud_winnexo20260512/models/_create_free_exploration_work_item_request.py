# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateFreeExplorationWorkItemRequest(DaraModel):
    def __init__(
        self,
        agent_names: List[str] = None,
        collaboration_group_id: str = None,
        member_user_ids: List[int] = None,
        tenant_id: str = None,
        title: str = None,
        visibility: str = None,
    ):
        # The technical names of the selected digital workers.
        # 
        # This parameter is required.
        self.agent_names = agent_names
        # The ID of the collaboration workspace to which the work item belongs.
        # 
        # This parameter is required.
        self.collaboration_group_id = collaboration_group_id
        # The actual members of the topic, including the creator. For public topics, members of the entire workspace are not enumerated.
        self.member_user_ids = member_user_ids
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
        if self.agent_names is not None:
            result['agentNames'] = self.agent_names

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.member_user_ids is not None:
            result['memberUserIds'] = self.member_user_ids

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
            self.agent_names = m.get('agentNames')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('memberUserIds') is not None:
            self.member_user_ids = m.get('memberUserIds')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('visibility') is not None:
            self.visibility = m.get('visibility')

        return self

