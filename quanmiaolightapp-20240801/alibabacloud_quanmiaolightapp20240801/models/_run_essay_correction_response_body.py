# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quanmiaolightapp20240801 import models as main_models
from darabonba.model import DaraModel

class RunEssayCorrectionResponseBody(DaraModel):
    def __init__(
        self,
        header: main_models.RunEssayCorrectionResponseBodyHeader = None,
        payload: main_models.RunEssayCorrectionResponseBodyPayload = None,
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
            temp_model = main_models.RunEssayCorrectionResponseBodyHeader()
            self.header = temp_model.from_map(m.get('header'))

        if m.get('payload') is not None:
            temp_model = main_models.RunEssayCorrectionResponseBodyPayload()
            self.payload = temp_model.from_map(m.get('payload'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class RunEssayCorrectionResponseBodyPayload(DaraModel):
    def __init__(
        self,
        output: main_models.RunEssayCorrectionResponseBodyPayloadOutput = None,
        usage: main_models.RunEssayCorrectionResponseBodyPayloadUsage = None,
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
            temp_model = main_models.RunEssayCorrectionResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m.get('output'))

        if m.get('usage') is not None:
            temp_model = main_models.RunEssayCorrectionResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class RunEssayCorrectionResponseBodyPayloadUsage(DaraModel):
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

class RunEssayCorrectionResponseBodyPayloadOutput(DaraModel):
    def __init__(
        self,
        dimension_results: List[main_models.RunEssayCorrectionResponseBodyPayloadOutputDimensionResults] = None,
        overall_comment: str = None,
        reasoning_content: str = None,
        score: int = None,
        text: str = None,
    ):
        self.dimension_results = dimension_results
        self.overall_comment = overall_comment
        self.reasoning_content = reasoning_content
        self.score = score
        self.text = text

    def validate(self):
        if self.dimension_results:
            for v1 in self.dimension_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['dimensionResults'] = []
        if self.dimension_results is not None:
            for k1 in self.dimension_results:
                result['dimensionResults'].append(k1.to_map() if k1 else None)

        if self.overall_comment is not None:
            result['overallComment'] = self.overall_comment

        if self.reasoning_content is not None:
            result['reasoningContent'] = self.reasoning_content

        if self.score is not None:
            result['score'] = self.score

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dimension_results = []
        if m.get('dimensionResults') is not None:
            for k1 in m.get('dimensionResults'):
                temp_model = main_models.RunEssayCorrectionResponseBodyPayloadOutputDimensionResults()
                self.dimension_results.append(temp_model.from_map(k1))

        if m.get('overallComment') is not None:
            self.overall_comment = m.get('overallComment')

        if m.get('reasoningContent') is not None:
            self.reasoning_content = m.get('reasoningContent')

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

class RunEssayCorrectionResponseBodyPayloadOutputDimensionResults(DaraModel):
    def __init__(
        self,
        analysis: str = None,
        max_score: float = None,
        name: str = None,
        score: float = None,
    ):
        self.analysis = analysis
        self.max_score = max_score
        self.name = name
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis is not None:
            result['analysis'] = self.analysis

        if self.max_score is not None:
            result['maxScore'] = self.max_score

        if self.name is not None:
            result['name'] = self.name

        if self.score is not None:
            result['score'] = self.score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysis') is not None:
            self.analysis = m.get('analysis')

        if m.get('maxScore') is not None:
            self.max_score = m.get('maxScore')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('score') is not None:
            self.score = m.get('score')

        return self

class RunEssayCorrectionResponseBodyHeader(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
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

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

