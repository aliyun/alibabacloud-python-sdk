# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListAIAgentDialoguesResponseBody(DaraModel):
    def __init__(
        self,
        dialogues: List[main_models.ListAIAgentDialoguesResponseBodyDialogues] = None,
        request_id: str = None,
    ):
        # A list of dialogues.
        self.dialogues = dialogues
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.dialogues:
            for v1 in self.dialogues:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Dialogues'] = []
        if self.dialogues is not None:
            for k1 in self.dialogues:
                result['Dialogues'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dialogues = []
        if m.get('Dialogues') is not None:
            for k1 in m.get('Dialogues'):
                temp_model = main_models.ListAIAgentDialoguesResponseBodyDialogues()
                self.dialogues.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAIAgentDialoguesResponseBodyDialogues(DaraModel):
    def __init__(
        self,
        attached_file_list: List[main_models.ListAIAgentDialoguesResponseBodyDialoguesAttachedFileList] = None,
        dialogue_id: str = None,
        extend: str = None,
        node_id: str = None,
        producer: str = None,
        reasoning_text: str = None,
        round_id: str = None,
        source: str = None,
        text: str = None,
        time: int = None,
        type: str = None,
    ):
        # A list of file attachments referenced in the dialogue.
        self.attached_file_list = attached_file_list
        # The unique ID of the dialogue.
        self.dialogue_id = dialogue_id
        # A JSON-formatted string for extended information. Use this field to store custom data, such as sentiment labels or intent recognition results.
        self.extend = extend
        # The ID of the workflow node that generated the dialogue entry, which you can use for tracing.
        self.node_id = node_id
        # The producer of this message.
        # 
        # - user: A message from the user.
        # 
        # - agent: A message from the agent.
        self.producer = producer
        # The agent\\"s reasoning text, which can reveal its thought process.
        self.reasoning_text = reasoning_text
        # The ID of the dialogue round.
        self.round_id = round_id
        # The source channel of the message. Valid values:
        # 
        # chat: The message is from a text chat.
        # 
        # call: The message is from a voice call.
        self.source = source
        # The text content of the dialogue entry.
        self.text = text
        # The Unix timestamp (in milliseconds) when the dialogue entry was created.
        self.time = time
        # The type of the message. Valid values include:
        # 
        # For a call:
        # 
        # 1. greeting: A welcome message.
        # 
        # 2. normal: A standard voice response.
        # 
        # 3. speech: A proactive voice broadcast.
        # 
        # For a chat:
        # 
        # 1. normal: A standard text response.
        # 
        # 2. announcement: A proactive text push.
        # 
        # 3. custom: A custom message.
        self.type = type

    def validate(self):
        if self.attached_file_list:
            for v1 in self.attached_file_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttachedFileList'] = []
        if self.attached_file_list is not None:
            for k1 in self.attached_file_list:
                result['AttachedFileList'].append(k1.to_map() if k1 else None)

        if self.dialogue_id is not None:
            result['DialogueId'] = self.dialogue_id

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.producer is not None:
            result['Producer'] = self.producer

        if self.reasoning_text is not None:
            result['ReasoningText'] = self.reasoning_text

        if self.round_id is not None:
            result['RoundId'] = self.round_id

        if self.source is not None:
            result['Source'] = self.source

        if self.text is not None:
            result['Text'] = self.text

        if self.time is not None:
            result['Time'] = self.time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attached_file_list = []
        if m.get('AttachedFileList') is not None:
            for k1 in m.get('AttachedFileList'):
                temp_model = main_models.ListAIAgentDialoguesResponseBodyDialoguesAttachedFileList()
                self.attached_file_list.append(temp_model.from_map(k1))

        if m.get('DialogueId') is not None:
            self.dialogue_id = m.get('DialogueId')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Producer') is not None:
            self.producer = m.get('Producer')

        if m.get('ReasoningText') is not None:
            self.reasoning_text = m.get('ReasoningText')

        if m.get('RoundId') is not None:
            self.round_id = m.get('RoundId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListAIAgentDialoguesResponseBodyDialoguesAttachedFileList(DaraModel):
    def __init__(
        self,
        format: str = None,
        id: str = None,
        name: str = None,
        type: int = None,
        url: str = None,
    ):
        # The format of the attachment, such as mp3, wav, or pdf.
        self.format = format
        # The unique identifier of the attachment.
        self.id = id
        # The file name of the attachment.
        self.name = name
        # The attachment type, represented by a numeric value. The meaning of this value is defined by your business logic.
        self.type = type
        # The URL of the attachment.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format is not None:
            result['Format'] = self.format

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

