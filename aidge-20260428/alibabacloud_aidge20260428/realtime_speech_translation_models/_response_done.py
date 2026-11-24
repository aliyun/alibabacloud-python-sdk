# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aidge20260428 import realtime_speech_translation_models as main_models
from darabonba.model import DaraModel

class ResponseDone(DaraModel):
    def __init__(
        self,
        type: str = None,
        event_id: str = None,
        response: main_models.ResponseDoneResponse = None,
    ):
        self.type = type
        self.event_id = event_id
        self.response = response

    def validate(self):
        if self.response:
            self.response.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.event_id is not None:
            result['event_id'] = self.event_id

        if self.response is not None:
            result['response'] = self.response.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')

        if m.get('response') is not None:
            temp_model = main_models.ResponseDoneResponse()
            self.response = temp_model.from_map(m.get('response'))

        return self

class ResponseDoneResponse(DaraModel):
    def __init__(
        self,
        id: str = None,
        object: str = None,
        conversation_id: str = None,
        status: str = None,
        modalities: List[str] = None,
        voice: str = None,
        output_audio_format: str = None,
        output: List[main_models.ResponseDoneResponseOutput] = None,
        usage: main_models.ResponseDoneResponseUsage = None,
    ):
        self.id = id
        self.object = object
        self.conversation_id = conversation_id
        self.status = status
        self.modalities = modalities
        self.voice = voice
        self.output_audio_format = output_audio_format
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            for v1 in self.output:
                 if v1:
                    v1.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.object is not None:
            result['object'] = self.object

        if self.conversation_id is not None:
            result['conversation_id'] = self.conversation_id

        if self.status is not None:
            result['status'] = self.status

        if self.modalities is not None:
            result['modalities'] = self.modalities

        if self.voice is not None:
            result['voice'] = self.voice

        if self.output_audio_format is not None:
            result['output_audio_format'] = self.output_audio_format

        result['output'] = []
        if self.output is not None:
            for k1 in self.output:
                result['output'].append(k1.to_map() if k1 else None)

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('object') is not None:
            self.object = m.get('object')

        if m.get('conversation_id') is not None:
            self.conversation_id = m.get('conversation_id')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('modalities') is not None:
            self.modalities = m.get('modalities')

        if m.get('voice') is not None:
            self.voice = m.get('voice')

        if m.get('output_audio_format') is not None:
            self.output_audio_format = m.get('output_audio_format')

        self.output = []
        if m.get('output') is not None:
            for k1 in m.get('output'):
                temp_model = main_models.ResponseDoneResponseOutput()
                self.output.append(temp_model.from_map(k1))

        if m.get('usage') is not None:
            temp_model = main_models.ResponseDoneResponseUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class ResponseDoneResponseUsage(DaraModel):
    def __init__(
        self,
        total_tokens: int = None,
        input_tokens: int = None,
        output_tokens: int = None,
        input_tokens_details: main_models.ResponseDoneResponseUsageInputTokensDetails = None,
        output_tokens_details: main_models.ResponseDoneResponseUsageOutputTokensDetails = None,
    ):
        self.total_tokens = total_tokens
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.input_tokens_details = input_tokens_details
        self.output_tokens_details = output_tokens_details

    def validate(self):
        if self.input_tokens_details:
            self.input_tokens_details.validate()
        if self.output_tokens_details:
            self.output_tokens_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total_tokens is not None:
            result['total_tokens'] = self.total_tokens

        if self.input_tokens is not None:
            result['input_tokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['output_tokens'] = self.output_tokens

        if self.input_tokens_details is not None:
            result['input_tokens_details'] = self.input_tokens_details.to_map()

        if self.output_tokens_details is not None:
            result['output_tokens_details'] = self.output_tokens_details.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total_tokens') is not None:
            self.total_tokens = m.get('total_tokens')

        if m.get('input_tokens') is not None:
            self.input_tokens = m.get('input_tokens')

        if m.get('output_tokens') is not None:
            self.output_tokens = m.get('output_tokens')

        if m.get('input_tokens_details') is not None:
            temp_model = main_models.ResponseDoneResponseUsageInputTokensDetails()
            self.input_tokens_details = temp_model.from_map(m.get('input_tokens_details'))

        if m.get('output_tokens_details') is not None:
            temp_model = main_models.ResponseDoneResponseUsageOutputTokensDetails()
            self.output_tokens_details = temp_model.from_map(m.get('output_tokens_details'))

        return self

class ResponseDoneResponseUsageOutputTokensDetails(DaraModel):
    def __init__(
        self,
        text_tokens: int = None,
        audio_tokens: int = None,
    ):
        self.text_tokens = text_tokens
        self.audio_tokens = audio_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text_tokens is not None:
            result['text_tokens'] = self.text_tokens

        if self.audio_tokens is not None:
            result['audio_tokens'] = self.audio_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text_tokens') is not None:
            self.text_tokens = m.get('text_tokens')

        if m.get('audio_tokens') is not None:
            self.audio_tokens = m.get('audio_tokens')

        return self

class ResponseDoneResponseUsageInputTokensDetails(DaraModel):
    def __init__(
        self,
        text_tokens: int = None,
        audio_tokens: int = None,
    ):
        self.text_tokens = text_tokens
        self.audio_tokens = audio_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text_tokens is not None:
            result['text_tokens'] = self.text_tokens

        if self.audio_tokens is not None:
            result['audio_tokens'] = self.audio_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text_tokens') is not None:
            self.text_tokens = m.get('text_tokens')

        if m.get('audio_tokens') is not None:
            self.audio_tokens = m.get('audio_tokens')

        return self

class ResponseDoneResponseOutput(DaraModel):
    def __init__(
        self,
        id: str = None,
        object: str = None,
        type: str = None,
        status: str = None,
        role: str = None,
        content: List[main_models.ResponseDoneResponseOutputContent] = None,
    ):
        self.id = id
        self.object = object
        self.type = type
        self.status = status
        self.role = role
        self.content = content

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.object is not None:
            result['object'] = self.object

        if self.type is not None:
            result['type'] = self.type

        if self.status is not None:
            result['status'] = self.status

        if self.role is not None:
            result['role'] = self.role

        result['content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['content'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('object') is not None:
            self.object = m.get('object')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('role') is not None:
            self.role = m.get('role')

        self.content = []
        if m.get('content') is not None:
            for k1 in m.get('content'):
                temp_model = main_models.ResponseDoneResponseOutputContent()
                self.content.append(temp_model.from_map(k1))

        return self

class ResponseDoneResponseOutputContent(DaraModel):
    def __init__(
        self,
        type: str = None,
        text: str = None,
        transcript: str = None,
    ):
        self.type = type
        self.text = text
        self.transcript = transcript

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.text is not None:
            result['text'] = self.text

        if self.transcript is not None:
            result['transcript'] = self.transcript

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('transcript') is not None:
            self.transcript = m.get('transcript')

        return self

