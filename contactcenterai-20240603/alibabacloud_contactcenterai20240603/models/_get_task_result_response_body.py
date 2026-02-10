# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_contactcenterai20240603 import models as main_models
from darabonba.model import DaraModel

class GetTaskResultResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetTaskResultResponseBodyData = None,
        request_id: str = None,
        success: str = None,
    ):
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetTaskResultResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetTaskResultResponseBodyData(DaraModel):
    def __init__(
        self,
        asr_result: List[main_models.GetTaskResultResponseBodyDataAsrResult] = None,
        extra: str = None,
        rag_error_message: str = None,
        rag_result: str = None,
        rag_status: str = None,
        task_error_message: str = None,
        task_id: str = None,
        task_status: str = None,
        text: str = None,
        usage: main_models.GetTaskResultResponseBodyDataUsage = None,
    ):
        self.asr_result = asr_result
        self.extra = extra
        self.rag_error_message = rag_error_message
        self.rag_result = rag_result
        self.rag_status = rag_status
        self.task_error_message = task_error_message
        self.task_id = task_id
        self.task_status = task_status
        self.text = text
        self.usage = usage

    def validate(self):
        if self.asr_result:
            for v1 in self.asr_result:
                 if v1:
                    v1.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['asrResult'] = []
        if self.asr_result is not None:
            for k1 in self.asr_result:
                result['asrResult'].append(k1.to_map() if k1 else None)

        if self.extra is not None:
            result['extra'] = self.extra

        if self.rag_error_message is not None:
            result['ragErrorMessage'] = self.rag_error_message

        if self.rag_result is not None:
            result['ragResult'] = self.rag_result

        if self.rag_status is not None:
            result['ragStatus'] = self.rag_status

        if self.task_error_message is not None:
            result['taskErrorMessage'] = self.task_error_message

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_status is not None:
            result['taskStatus'] = self.task_status

        if self.text is not None:
            result['text'] = self.text

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asr_result = []
        if m.get('asrResult') is not None:
            for k1 in m.get('asrResult'):
                temp_model = main_models.GetTaskResultResponseBodyDataAsrResult()
                self.asr_result.append(temp_model.from_map(k1))

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('ragErrorMessage') is not None:
            self.rag_error_message = m.get('ragErrorMessage')

        if m.get('ragResult') is not None:
            self.rag_result = m.get('ragResult')

        if m.get('ragStatus') is not None:
            self.rag_status = m.get('ragStatus')

        if m.get('taskErrorMessage') is not None:
            self.task_error_message = m.get('taskErrorMessage')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('usage') is not None:
            temp_model = main_models.GetTaskResultResponseBodyDataUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class GetTaskResultResponseBodyDataUsage(DaraModel):
    def __init__(
        self,
        rag: main_models.GetTaskResultResponseBodyDataUsageRag = None,
    ):
        self.rag = rag

    def validate(self):
        if self.rag:
            self.rag.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rag is not None:
            result['rag'] = self.rag.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rag') is not None:
            temp_model = main_models.GetTaskResultResponseBodyDataUsageRag()
            self.rag = temp_model.from_map(m.get('rag'))

        return self

class GetTaskResultResponseBodyDataUsageRag(DaraModel):
    def __init__(
        self,
        adaptive: main_models.GetTaskResultResponseBodyDataUsageRagAdaptive = None,
        dialog_summary: main_models.GetTaskResultResponseBodyDataUsageRagDialogSummary = None,
    ):
        self.adaptive = adaptive
        self.dialog_summary = dialog_summary

    def validate(self):
        if self.adaptive:
            self.adaptive.validate()
        if self.dialog_summary:
            self.dialog_summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adaptive is not None:
            result['adaptive'] = self.adaptive.to_map()

        if self.dialog_summary is not None:
            result['dialogSummary'] = self.dialog_summary.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('adaptive') is not None:
            temp_model = main_models.GetTaskResultResponseBodyDataUsageRagAdaptive()
            self.adaptive = temp_model.from_map(m.get('adaptive'))

        if m.get('dialogSummary') is not None:
            temp_model = main_models.GetTaskResultResponseBodyDataUsageRagDialogSummary()
            self.dialog_summary = temp_model.from_map(m.get('dialogSummary'))

        return self

class GetTaskResultResponseBodyDataUsageRagDialogSummary(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        invoke_count: int = None,
        output_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.invoke_count = invoke_count
        self.output_tokens = output_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.invoke_count is not None:
            result['invokeCount'] = self.invoke_count

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('invokeCount') is not None:
            self.invoke_count = m.get('invokeCount')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        return self

class GetTaskResultResponseBodyDataUsageRagAdaptive(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        invoke_count: int = None,
        output_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.invoke_count = invoke_count
        self.output_tokens = output_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.invoke_count is not None:
            result['invokeCount'] = self.invoke_count

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('invokeCount') is not None:
            self.invoke_count = m.get('invokeCount')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        return self

class GetTaskResultResponseBodyDataAsrResult(DaraModel):
    def __init__(
        self,
        begin: int = None,
        emotion_value: int = None,
        end: int = None,
        role: str = None,
        role_name: str = None,
        speech_rate: int = None,
        words: str = None,
    ):
        self.begin = begin
        self.emotion_value = emotion_value
        self.end = end
        self.role = role
        self.role_name = role_name
        self.speech_rate = speech_rate
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin is not None:
            result['begin'] = self.begin

        if self.emotion_value is not None:
            result['emotionValue'] = self.emotion_value

        if self.end is not None:
            result['end'] = self.end

        if self.role is not None:
            result['role'] = self.role

        if self.role_name is not None:
            result['roleName'] = self.role_name

        if self.speech_rate is not None:
            result['speechRate'] = self.speech_rate

        if self.words is not None:
            result['words'] = self.words

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('begin') is not None:
            self.begin = m.get('begin')

        if m.get('emotionValue') is not None:
            self.emotion_value = m.get('emotionValue')

        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')

        if m.get('speechRate') is not None:
            self.speech_rate = m.get('speechRate')

        if m.get('words') is not None:
            self.words = m.get('words')

        return self

