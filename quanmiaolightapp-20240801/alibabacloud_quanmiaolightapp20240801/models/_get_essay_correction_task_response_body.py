# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quanmiaolightapp20240801 import models as main_models
from darabonba.model import DaraModel

class GetEssayCorrectionTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetEssayCorrectionTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
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
            temp_model = main_models.GetEssayCorrectionTaskResponseBodyData()
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

class GetEssayCorrectionTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        results: List[main_models.GetEssayCorrectionTaskResponseBodyDataResults] = None,
        status: str = None,
        total_usage: main_models.ModelUsage = None,
    ):
        self.error_message = error_message
        self.results = results
        self.status = status
        self.total_usage = total_usage

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()
        if self.total_usage:
            self.total_usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        result['results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        if self.total_usage is not None:
            result['totalUsage'] = self.total_usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        self.results = []
        if m.get('results') is not None:
            for k1 in m.get('results'):
                temp_model = main_models.GetEssayCorrectionTaskResponseBodyDataResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('totalUsage') is not None:
            temp_model = main_models.ModelUsage()
            self.total_usage = temp_model.from_map(m.get('totalUsage'))

        return self

class GetEssayCorrectionTaskResponseBodyDataResults(DaraModel):
    def __init__(
        self,
        custom_id: str = None,
        dimension_results: List[main_models.GetEssayCorrectionTaskResponseBodyDataResultsDimensionResults] = None,
        error_code: str = None,
        error_message: str = None,
        overall_comment: str = None,
        result: str = None,
        score: int = None,
        usage: main_models.ModelUsage = None,
    ):
        # xxx
        self.custom_id = custom_id
        self.dimension_results = dimension_results
        self.error_code = error_code
        self.error_message = error_message
        self.overall_comment = overall_comment
        self.result = result
        self.score = score
        self.usage = usage

    def validate(self):
        if self.dimension_results:
            for v1 in self.dimension_results:
                 if v1:
                    v1.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_id is not None:
            result['customId'] = self.custom_id

        result['dimensionResults'] = []
        if self.dimension_results is not None:
            for k1 in self.dimension_results:
                result['dimensionResults'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.overall_comment is not None:
            result['overallComment'] = self.overall_comment

        if self.result is not None:
            result['result'] = self.result

        if self.score is not None:
            result['score'] = self.score

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customId') is not None:
            self.custom_id = m.get('customId')

        self.dimension_results = []
        if m.get('dimensionResults') is not None:
            for k1 in m.get('dimensionResults'):
                temp_model = main_models.GetEssayCorrectionTaskResponseBodyDataResultsDimensionResults()
                self.dimension_results.append(temp_model.from_map(k1))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('overallComment') is not None:
            self.overall_comment = m.get('overallComment')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('usage') is not None:
            temp_model = main_models.ModelUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class GetEssayCorrectionTaskResponseBodyDataResultsDimensionResults(DaraModel):
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

