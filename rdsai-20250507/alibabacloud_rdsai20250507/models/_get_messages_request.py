# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMessagesRequest(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        event_mode: str = None,
        first_id: str = None,
        flow_id: str = None,
        limit: int = None,
        workspace_id: str = None,
    ):
        # The conversation ID.
        self.conversation_id = conversation_id
        # The event output type. Valid values: inline and separate. Default value: inline. In inline mode, tool invocation events, child node events, and document events are unified into the answer field of the event where event = message. In separate mode, tool invocation events, child node events, and document events have their own respective events.
        self.event_mode = event_mode
        # The ID of the first message.
        self.first_id = first_id
        # The flow instance ID.
        self.flow_id = flow_id
        # The number of rows per page for paging. Valid values: 1 to 100. Default value: 100.
        self.limit = limit
        # The ContextDB workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.event_mode is not None:
            result['EventMode'] = self.event_mode

        if self.first_id is not None:
            result['FirstId'] = self.first_id

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('EventMode') is not None:
            self.event_mode = m.get('EventMode')

        if m.get('FirstId') is not None:
            self.first_id = m.get('FirstId')

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

