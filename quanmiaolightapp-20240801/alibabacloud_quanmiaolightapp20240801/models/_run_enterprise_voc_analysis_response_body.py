# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quanmiaolightapp20240801 import models as main_models
from darabonba.model import DaraModel

class RunEnterpriseVocAnalysisResponseBody(DaraModel):
    def __init__(
        self,
        header: main_models.RunEnterpriseVocAnalysisResponseBodyHeader = None,
        payload: main_models.RunEnterpriseVocAnalysisResponseBodyPayload = None,
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
            temp_model = main_models.RunEnterpriseVocAnalysisResponseBodyHeader()
            self.header = temp_model.from_map(m.get('header'))

        if m.get('payload') is not None:
            temp_model = main_models.RunEnterpriseVocAnalysisResponseBodyPayload()
            self.payload = temp_model.from_map(m.get('payload'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class RunEnterpriseVocAnalysisResponseBodyPayload(DaraModel):
    def __init__(
        self,
        output: main_models.RunEnterpriseVocAnalysisResponseBodyPayloadOutput = None,
        usage: main_models.RunEnterpriseVocAnalysisResponseBodyPayloadUsage = None,
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
            temp_model = main_models.RunEnterpriseVocAnalysisResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m.get('output'))

        if m.get('usage') is not None:
            temp_model = main_models.RunEnterpriseVocAnalysisResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class RunEnterpriseVocAnalysisResponseBodyPayloadUsage(DaraModel):
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

class RunEnterpriseVocAnalysisResponseBodyPayloadOutput(DaraModel):
    def __init__(
        self,
        filter_result: main_models.RunEnterpriseVocAnalysisResponseBodyPayloadOutputFilterResult = None,
        reason_content: str = None,
        text: str = None,
    ):
        self.filter_result = filter_result
        self.reason_content = reason_content
        self.text = text

    def validate(self):
        if self.filter_result:
            self.filter_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_result is not None:
            result['filterResult'] = self.filter_result.to_map()

        if self.reason_content is not None:
            result['reasonContent'] = self.reason_content

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterResult') is not None:
            temp_model = main_models.RunEnterpriseVocAnalysisResponseBodyPayloadOutputFilterResult()
            self.filter_result = temp_model.from_map(m.get('filterResult'))

        if m.get('reasonContent') is not None:
            self.reason_content = m.get('reasonContent')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

class RunEnterpriseVocAnalysisResponseBodyPayloadOutputFilterResult(DaraModel):
    def __init__(
        self,
        filter_results: List[main_models.RunEnterpriseVocAnalysisResponseBodyPayloadOutputFilterResultFilterResults] = None,
    ):
        self.filter_results = filter_results

    def validate(self):
        if self.filter_results:
            for v1 in self.filter_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['filterResults'] = []
        if self.filter_results is not None:
            for k1 in self.filter_results:
                result['filterResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter_results = []
        if m.get('filterResults') is not None:
            for k1 in m.get('filterResults'):
                temp_model = main_models.RunEnterpriseVocAnalysisResponseBodyPayloadOutputFilterResultFilterResults()
                self.filter_results.append(temp_model.from_map(k1))

        return self

class RunEnterpriseVocAnalysisResponseBodyPayloadOutputFilterResultFilterResults(DaraModel):
    def __init__(
        self,
        hit: bool = None,
        tag_name: str = None,
        tag_value: str = None,
    ):
        self.hit = hit
        self.tag_name = tag_name
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hit is not None:
            result['hit'] = self.hit

        if self.tag_name is not None:
            result['tagName'] = self.tag_name

        if self.tag_value is not None:
            result['tagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hit') is not None:
            self.hit = m.get('hit')

        if m.get('tagName') is not None:
            self.tag_name = m.get('tagName')

        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')

        return self

class RunEnterpriseVocAnalysisResponseBodyHeader(DaraModel):
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

