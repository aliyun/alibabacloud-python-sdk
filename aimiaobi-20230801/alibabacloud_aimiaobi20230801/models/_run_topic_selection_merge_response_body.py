# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class RunTopicSelectionMergeResponseBody(DaraModel):
    def __init__(
        self,
        end: bool = None,
        header: main_models.RunTopicSelectionMergeResponseBodyHeader = None,
        payload: main_models.RunTopicSelectionMergeResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.end = end
        self.header = header
        self.payload = payload
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end

        if self.header is not None:
            result['Header'] = self.header.to_map()

        if self.payload is not None:
            result['Payload'] = self.payload.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Header') is not None:
            temp_model = main_models.RunTopicSelectionMergeResponseBodyHeader()
            self.header = temp_model.from_map(m.get('Header'))

        if m.get('Payload') is not None:
            temp_model = main_models.RunTopicSelectionMergeResponseBodyPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RunTopicSelectionMergeResponseBodyPayload(DaraModel):
    def __init__(
        self,
        output: main_models.RunTopicSelectionMergeResponseBodyPayloadOutput = None,
        usage: main_models.RunTopicSelectionMergeResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output is not None:
            result['Output'] = self.output.to_map()

        if self.usage is not None:
            result['Usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            temp_model = main_models.RunTopicSelectionMergeResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('Usage') is not None:
            temp_model = main_models.RunTopicSelectionMergeResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        return self

class RunTopicSelectionMergeResponseBodyPayloadUsage(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        token_map: Dict[str, int] = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.token_map = token_map
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens

        if self.token_map is not None:
            result['TokenMap'] = self.token_map

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('TokenMap') is not None:
            self.token_map = m.get('TokenMap')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        return self

class RunTopicSelectionMergeResponseBodyPayloadOutput(DaraModel):
    def __init__(
        self,
        text: str = None,
        topic: main_models.TopicSelection = None,
    ):
        self.text = text
        self.topic = topic

    def validate(self):
        if self.topic:
            self.topic.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['Text'] = self.text

        if self.topic is not None:
            result['Topic'] = self.topic.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Topic') is not None:
            temp_model = main_models.TopicSelection()
            self.topic = temp_model.from_map(m.get('Topic'))

        return self

class RunTopicSelectionMergeResponseBodyHeader(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        origin_session_id: str = None,
        session_id: str = None,
        status_code: int = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.origin_session_id = origin_session_id
        self.session_id = session_id
        self.status_code = status_code
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.event is not None:
            result['Event'] = self.event

        if self.origin_session_id is not None:
            result['OriginSessionId'] = self.origin_session_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('OriginSessionId') is not None:
            self.origin_session_id = m.get('OriginSessionId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

