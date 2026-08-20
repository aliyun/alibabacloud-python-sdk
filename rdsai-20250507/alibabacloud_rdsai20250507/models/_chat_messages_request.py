# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class ChatMessagesRequest(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        event_mode: str = None,
        files: List[main_models.ChatMessagesRequestFiles] = None,
        inputs: main_models.ChatMessagesRequestInputs = None,
        parent_message_id: str = None,
        query: str = None,
    ):
        # The conversation ID.
        self.conversation_id = conversation_id
        # The event output type. Valid values: inline and separate. Default value: inline. When set to inline, tool invocation events, sub-node events, and document events are included in the answer field of event = message. When set to separate, tool invocation events, sub-node events, and document events each have their own event.
        self.event_mode = event_mode
        self.files = files
        # The task input.
        self.inputs = inputs
        # The parent message ID.
        self.parent_message_id = parent_message_id
        # The query content.
        # 
        # This parameter is required.
        self.query = query

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()
        if self.inputs:
            self.inputs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.event_mode is not None:
            result['EventMode'] = self.event_mode

        result['Files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['Files'].append(k1.to_map() if k1 else None)

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

        if m.get('EventMode') is not None:
            self.event_mode = m.get('EventMode')

        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.ChatMessagesRequestFiles()
                self.files.append(temp_model.from_map(k1))

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
        enable_thinking: str = None,
        language: str = None,
        model_id: str = None,
        region_id: str = None,
        think_effort: str = None,
        timezone: str = None,
    ):
        # The custom agent ID for the user.
        self.custom_agent_id = custom_agent_id
        # Specifies whether to enable deep thinking mode.
        self.enable_thinking = enable_thinking
        # The conversation language.
        self.language = language
        # The model ID.
        self.model_id = model_id
        # The region ID.
        self.region_id = region_id
        # The thinking depth.
        self.think_effort = think_effort
        # The time zone. Default value: **Asia/Shanghai**.
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

        if self.enable_thinking is not None:
            result['EnableThinking'] = self.enable_thinking

        if self.language is not None:
            result['Language'] = self.language

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.think_effort is not None:
            result['ThinkEffort'] = self.think_effort

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')

        if m.get('EnableThinking') is not None:
            self.enable_thinking = m.get('EnableThinking')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ThinkEffort') is not None:
            self.think_effort = m.get('ThinkEffort')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        return self



class ChatMessagesRequestFiles(DaraModel):
    def __init__(
        self,
        transfer_method: str = None,
        type: str = None,
        upload_file_id: str = None,
    ):
        self.transfer_method = transfer_method
        self.type = type
        self.upload_file_id = upload_file_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.transfer_method is not None:
            result['TransferMethod'] = self.transfer_method

        if self.type is not None:
            result['Type'] = self.type

        if self.upload_file_id is not None:
            result['UploadFileId'] = self.upload_file_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TransferMethod') is not None:
            self.transfer_method = m.get('TransferMethod')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UploadFileId') is not None:
            self.upload_file_id = m.get('UploadFileId')

        return self

