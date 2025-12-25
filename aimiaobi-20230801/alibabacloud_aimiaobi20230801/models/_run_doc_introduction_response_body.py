# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class RunDocIntroductionResponseBody(DaraModel):
    def __init__(
        self,
        header: main_models.RunDocIntroductionResponseBodyHeader = None,
        payload: main_models.RunDocIntroductionResponseBodyPayload = None,
        request_id: str = None,
    ):
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
        if self.header is not None:
            result['Header'] = self.header.to_map()

        if self.payload is not None:
            result['Payload'] = self.payload.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Header') is not None:
            temp_model = main_models.RunDocIntroductionResponseBodyHeader()
            self.header = temp_model.from_map(m.get('Header'))

        if m.get('Payload') is not None:
            temp_model = main_models.RunDocIntroductionResponseBodyPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RunDocIntroductionResponseBodyPayload(DaraModel):
    def __init__(
        self,
        output: main_models.RunDocIntroductionResponseBodyPayloadOutput = None,
        usage: main_models.RunDocIntroductionResponseBodyPayloadUsage = None,
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
            temp_model = main_models.RunDocIntroductionResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('Usage') is not None:
            temp_model = main_models.RunDocIntroductionResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        return self

class RunDocIntroductionResponseBodyPayloadUsage(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
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

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        return self

class RunDocIntroductionResponseBodyPayloadOutput(DaraModel):
    def __init__(
        self,
        introductions: List[main_models.RunDocIntroductionResponseBodyPayloadOutputIntroductions] = None,
        key_point: str = None,
        summary: str = None,
    ):
        self.introductions = introductions
        self.key_point = key_point
        self.summary = summary

    def validate(self):
        if self.introductions:
            for v1 in self.introductions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Introductions'] = []
        if self.introductions is not None:
            for k1 in self.introductions:
                result['Introductions'].append(k1.to_map() if k1 else None)

        if self.key_point is not None:
            result['KeyPoint'] = self.key_point

        if self.summary is not None:
            result['Summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.introductions = []
        if m.get('Introductions') is not None:
            for k1 in m.get('Introductions'):
                temp_model = main_models.RunDocIntroductionResponseBodyPayloadOutputIntroductions()
                self.introductions.append(temp_model.from_map(k1))

        if m.get('KeyPoint') is not None:
            self.key_point = m.get('KeyPoint')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        return self

class RunDocIntroductionResponseBodyPayloadOutputIntroductions(DaraModel):
    def __init__(
        self,
        blocks: List[main_models.RunDocIntroductionResponseBodyPayloadOutputIntroductionsBlocks] = None,
        start_page_id: int = None,
        summary: str = None,
        title: str = None,
    ):
        self.blocks = blocks
        self.start_page_id = start_page_id
        self.summary = summary
        self.title = title

    def validate(self):
        if self.blocks:
            for v1 in self.blocks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Blocks'] = []
        if self.blocks is not None:
            for k1 in self.blocks:
                result['Blocks'].append(k1.to_map() if k1 else None)

        if self.start_page_id is not None:
            result['StartPageId'] = self.start_page_id

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.blocks = []
        if m.get('Blocks') is not None:
            for k1 in m.get('Blocks'):
                temp_model = main_models.RunDocIntroductionResponseBodyPayloadOutputIntroductionsBlocks()
                self.blocks.append(temp_model.from_map(k1))

        if m.get('StartPageId') is not None:
            self.start_page_id = m.get('StartPageId')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class RunDocIntroductionResponseBodyPayloadOutputIntroductionsBlocks(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        height: int = None,
        page_id: int = None,
        width: int = None,
        x: int = None,
        y: int = None,
    ):
        self.begin_time = begin_time
        self.end_time = end_time
        self.height = height
        self.page_id = page_id
        self.width = width
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.height is not None:
            result['Height'] = self.height

        if self.page_id is not None:
            result['PageId'] = self.page_id

        if self.width is not None:
            result['Width'] = self.width

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('PageId') is not None:
            self.page_id = m.get('PageId')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class RunDocIntroductionResponseBodyHeader(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        event_info: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.event_info = event_info
        self.session_id = session_id
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

        if self.event_info is not None:
            result['EventInfo'] = self.event_info

        if self.session_id is not None:
            result['SessionId'] = self.session_id

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

        if m.get('EventInfo') is not None:
            self.event_info = m.get('EventInfo')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

