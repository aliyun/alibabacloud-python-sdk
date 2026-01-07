# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_quanmiaolightapp20240801 import models as main_models
from darabonba.model import DaraModel

class RunVideoDetectShotResponseBody(DaraModel):
    def __init__(
        self,
        header: main_models.RunVideoDetectShotResponseBodyHeader = None,
        payload: main_models.RunVideoDetectShotResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.header = header
        self.payload = payload
        # Id of the request
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
            result['header'] = self.header.to_map()

        if self.payload is not None:
            result['payload'] = self.payload.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('header') is not None:
            temp_model = main_models.RunVideoDetectShotResponseBodyHeader()
            self.header = temp_model.from_map(m.get('header'))

        if m.get('payload') is not None:
            temp_model = main_models.RunVideoDetectShotResponseBodyPayload()
            self.payload = temp_model.from_map(m.get('payload'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class RunVideoDetectShotResponseBodyPayload(DaraModel):
    def __init__(
        self,
        output: main_models.RunVideoDetectShotResponseBodyPayloadOutput = None,
        usage: main_models.RunVideoDetectShotResponseBodyPayloadUsage = None,
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
            result['output'] = self.output.to_map()

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('output') is not None:
            temp_model = main_models.RunVideoDetectShotResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m.get('output'))

        if m.get('usage') is not None:
            temp_model = main_models.RunVideoDetectShotResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class RunVideoDetectShotResponseBodyPayloadUsage(DaraModel):
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
            result['inputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')

        return self

class RunVideoDetectShotResponseBodyPayloadOutput(DaraModel):
    def __init__(
        self,
        video_split_result: main_models.RunVideoDetectShotResponseBodyPayloadOutputVideoSplitResult = None,
    ):
        self.video_split_result = video_split_result

    def validate(self):
        if self.video_split_result:
            self.video_split_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.video_split_result is not None:
            result['videoSplitResult'] = self.video_split_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('videoSplitResult') is not None:
            temp_model = main_models.RunVideoDetectShotResponseBodyPayloadOutputVideoSplitResult()
            self.video_split_result = temp_model.from_map(m.get('videoSplitResult'))

        return self

class RunVideoDetectShotResponseBodyPayloadOutputVideoSplitResult(DaraModel):
    def __init__(
        self,
        reason_text: str = None,
        text: str = None,
        video_parts: List[Dict[str, str]] = None,
        video_recognition_result: List[main_models.RunVideoDetectShotResponseBodyPayloadOutputVideoSplitResultVideoRecognitionResult] = None,
    ):
        self.reason_text = reason_text
        self.text = text
        self.video_parts = video_parts
        self.video_recognition_result = video_recognition_result

    def validate(self):
        if self.video_recognition_result:
            for v1 in self.video_recognition_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason_text is not None:
            result['reasonText'] = self.reason_text

        if self.text is not None:
            result['text'] = self.text

        if self.video_parts is not None:
            result['videoParts'] = self.video_parts

        result['videoRecognitionResult'] = []
        if self.video_recognition_result is not None:
            for k1 in self.video_recognition_result:
                result['videoRecognitionResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reasonText') is not None:
            self.reason_text = m.get('reasonText')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('videoParts') is not None:
            self.video_parts = m.get('videoParts')

        self.video_recognition_result = []
        if m.get('videoRecognitionResult') is not None:
            for k1 in m.get('videoRecognitionResult'):
                temp_model = main_models.RunVideoDetectShotResponseBodyPayloadOutputVideoSplitResultVideoRecognitionResult()
                self.video_recognition_result.append(temp_model.from_map(k1))

        return self

class RunVideoDetectShotResponseBodyPayloadOutputVideoSplitResultVideoRecognitionResult(DaraModel):
    def __init__(
        self,
        asr: str = None,
        end_time: int = None,
        ocr: str = None,
        start_time: int = None,
        vl: str = None,
    ):
        self.asr = asr
        self.end_time = end_time
        self.ocr = ocr
        self.start_time = start_time
        self.vl = vl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asr is not None:
            result['asr'] = self.asr

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.ocr is not None:
            result['ocr'] = self.ocr

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.vl is not None:
            result['vl'] = self.vl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asr') is not None:
            self.asr = m.get('asr')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('ocr') is not None:
            self.ocr = m.get('ocr')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('vl') is not None:
            self.vl = m.get('vl')

        return self

class RunVideoDetectShotResponseBodyHeader(DaraModel):
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
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.event is not None:
            result['event'] = self.event

        if self.event_info is not None:
            result['eventInfo'] = self.event_info

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('event') is not None:
            self.event = m.get('event')

        if m.get('eventInfo') is not None:
            self.event_info = m.get('eventInfo')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

