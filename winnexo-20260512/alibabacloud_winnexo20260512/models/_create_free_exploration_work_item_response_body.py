# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateFreeExplorationWorkItemResponseBody(DaraModel):
    def __init__(
        self,
        agent_names: List[str] = None,
        code: str = None,
        collaboration_group_id: str = None,
        conversation_id: str = None,
        created_by_user_id: int = None,
        item_type: str = None,
        member_user_ids: List[int] = None,
        message: str = None,
        request_id: str = None,
        title: str = None,
        visibility: str = None,
    ):
        # The technical names of the selected digital workers.
        self.agent_names = agent_names
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The ID of the collaboration workspace to which the work item belongs.
        self.collaboration_group_id = collaboration_group_id
        # The actual group topic ID, which can be associated in queryWorkItemFeed. It cannot be used as a workItemId in Workflow.
        self.conversation_id = conversation_id
        # The user ID of the creator on the platform.
        self.created_by_user_id = created_by_user_id
        # The work item mode. The value is fixed to FREE_EXPLORATION.
        self.item_type = item_type
        # The actual members of the topic, including the creator. For public topics, members of the entire workspace are not enumerated.
        self.member_user_ids = member_user_ids
        # The error description.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The title of the work item.
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

        if self.code is not None:
            result['code'] = self.code

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.conversation_id is not None:
            result['conversationId'] = self.conversation_id

        if self.created_by_user_id is not None:
            result['createdByUserId'] = self.created_by_user_id

        if self.item_type is not None:
            result['itemType'] = self.item_type

        if self.member_user_ids is not None:
            result['memberUserIds'] = self.member_user_ids

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.title is not None:
            result['title'] = self.title

        if self.visibility is not None:
            result['visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentNames') is not None:
            self.agent_names = m.get('agentNames')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('conversationId') is not None:
            self.conversation_id = m.get('conversationId')

        if m.get('createdByUserId') is not None:
            self.created_by_user_id = m.get('createdByUserId')

        if m.get('itemType') is not None:
            self.item_type = m.get('itemType')

        if m.get('memberUserIds') is not None:
            self.member_user_ids = m.get('memberUserIds')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('visibility') is not None:
            self.visibility = m.get('visibility')

        return self

