# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatMessagesShrinkRequest(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        event_mode: str = None,
        files_shrink: str = None,
        inputs_shrink: str = None,
        parent_message_id: str = None,
        query: str = None,
    ):
        # The conversation ID.
        self.conversation_id = conversation_id
        # The event output type. Valid values: inline and separate. Default value: inline. When set to inline, tool invocation events, sub-node events, and document events are included in the answer field of event = message. When set to separate, tool invocation events, sub-node events, and document events each have their own event.
        self.event_mode = event_mode
        self.files_shrink = files_shrink
        # The task input.
        self.inputs_shrink = inputs_shrink
        # The parent message ID.
        self.parent_message_id = parent_message_id
        # The query content.
        # 
        # This parameter is required.
        self.query = query

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

        if self.files_shrink is not None:
            result['Files'] = self.files_shrink

        if self.inputs_shrink is not None:
            result['Inputs'] = self.inputs_shrink

        if self.parent_message_id is not None:
            result['ParentMessageId'] = self.parent_message_id

        if self.query is not None:
            result['Query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('EventMode') is not None:
            self.event_mode = m.get('EventMode')

        if m.get('Files') is not None:
            self.files_shrink = m.get('Files')

        if m.get('Inputs') is not None:
            self.inputs_shrink = m.get('Inputs')

        if m.get('ParentMessageId') is not None:
            self.parent_message_id = m.get('ParentMessageId')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        return self

