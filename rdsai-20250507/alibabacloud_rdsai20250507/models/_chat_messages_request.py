# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class ChatMessagesRequest(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        inputs: main_models.ChatMessagesRequestInputs = None,
        parent_message_id: str = None,
        query: str = None,
    ):
        self.conversation_id = conversation_id
        self.inputs = inputs
        self.parent_message_id = parent_message_id
        # This parameter is required.
        self.query = query

    def validate(self):
        if self.inputs:
            self.inputs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.inputs is not None:
            result['Inputs'] = self.inputs.to_map()

        if self.parent_message_id is not None:
            result['ParentMessageId'] = self.parent_message_id

        if self.query is not None:
            result['Query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('Inputs') is not None:
            temp_model = main_models.ChatMessagesRequestInputs()
            self.inputs = temp_model.from_map(m.get('Inputs'))

        if m.get('ParentMessageId') is not None:
            self.parent_message_id = m.get('ParentMessageId')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        return self



class ChatMessagesRequestInputs(DaraModel):
    def __init__(
        self,
        custom_agent_id: str = None,
        language: str = None,
        region_id: str = None,
        timezone: str = None,
    ):
        self.custom_agent_id = custom_agent_id
        self.language = language
        self.region_id = region_id
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_agent_id is not None:
            result['CustomAgentId'] = self.custom_agent_id

        if self.language is not None:
            result['Language'] = self.language

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        return self

