# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quanmiaolightapp20240801 import models as main_models
from darabonba.model import DaraModel

class GetTagMiningAnalysisTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetTagMiningAnalysisTaskResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # requestId
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
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetTagMiningAnalysisTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetTagMiningAnalysisTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        results: List[main_models.GetTagMiningAnalysisTaskResponseBodyDataResults] = None,
        status: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.results = results
        self.status = status

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        result['results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        self.results = []
        if m.get('results') is not None:
            for k1 in m.get('results'):
                temp_model = main_models.GetTagMiningAnalysisTaskResponseBodyDataResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class GetTagMiningAnalysisTaskResponseBodyDataResults(DaraModel):
    def __init__(
        self,
        custom_id: str = None,
        header: main_models.GetTagMiningAnalysisTaskResponseBodyDataResultsHeader = None,
        payload: main_models.GetTagMiningAnalysisTaskResponseBodyDataResultsPayload = None,
    ):
        self.custom_id = custom_id
        self.header = header
        self.payload = payload

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
        if self.custom_id is not None:
            result['customId'] = self.custom_id

        if self.header is not None:
            result['header'] = self.header.to_map()

        if self.payload is not None:
            result['payload'] = self.payload.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customId') is not None:
            self.custom_id = m.get('customId')

        if m.get('header') is not None:
            temp_model = main_models.GetTagMiningAnalysisTaskResponseBodyDataResultsHeader()
            self.header = temp_model.from_map(m.get('header'))

        if m.get('payload') is not None:
            temp_model = main_models.GetTagMiningAnalysisTaskResponseBodyDataResultsPayload()
            self.payload = temp_model.from_map(m.get('payload'))

        return self

class GetTagMiningAnalysisTaskResponseBodyDataResultsPayload(DaraModel):
    def __init__(
        self,
        output: main_models.GetTagMiningAnalysisTaskResponseBodyDataResultsPayloadOutput = None,
        usage: main_models.GetTagMiningAnalysisTaskResponseBodyDataResultsPayloadUsage = None,
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
            temp_model = main_models.GetTagMiningAnalysisTaskResponseBodyDataResultsPayloadOutput()
            self.output = temp_model.from_map(m.get('output'))

        if m.get('usage') is not None:
            temp_model = main_models.GetTagMiningAnalysisTaskResponseBodyDataResultsPayloadUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class GetTagMiningAnalysisTaskResponseBodyDataResultsPayloadUsage(DaraModel):
    def __init__(
        self,
        input_token: int = None,
        output_token: int = None,
        total_token: int = None,
    ):
        self.input_token = input_token
        self.output_token = output_token
        self.total_token = total_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_token is not None:
            result['inputToken'] = self.input_token

        if self.output_token is not None:
            result['outputToken'] = self.output_token

        if self.total_token is not None:
            result['totalToken'] = self.total_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputToken') is not None:
            self.input_token = m.get('inputToken')

        if m.get('outputToken') is not None:
            self.output_token = m.get('outputToken')

        if m.get('totalToken') is not None:
            self.total_token = m.get('totalToken')

        return self

class GetTagMiningAnalysisTaskResponseBodyDataResultsPayloadOutput(DaraModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')

        return self

class GetTagMiningAnalysisTaskResponseBodyDataResultsHeader(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        request_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.request_id = request_id

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

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('event') is not None:
            self.event = m.get('event')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

