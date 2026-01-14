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
        result: str = None,
        score: int = None,
        usage: main_models.ModelUsage = None,
    ):
        # xxx
        self.custom_id = custom_id
        self.result = result
        self.score = score
        self.usage = usage

    def validate(self):
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_id is not None:
            result['customId'] = self.custom_id

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

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('usage') is not None:
            temp_model = main_models.ModelUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

