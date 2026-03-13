# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_searchplat20240529 import models as main_models
from darabonba.model import DaraModel

class GetImageAnalyzeTaskStatusResponseBody(DaraModel):
    def __init__(
        self,
        latency: int = None,
        request_id: str = None,
        result: main_models.GetImageAnalyzeTaskStatusResponseBodyResult = None,
        usage: main_models.GetImageAnalyzeTaskStatusResponseBodyUsage = None,
    ):
        self.latency = latency
        self.request_id = request_id
        self.result = result
        self.usage = usage

    def validate(self):
        if self.result:
            self.result.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.latency is not None:
            result['latency'] = self.latency

        if self.request_id is not None:
            result['request_id'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('latency') is not None:
            self.latency = m.get('latency')

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        if m.get('result') is not None:
            temp_model = main_models.GetImageAnalyzeTaskStatusResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('usage') is not None:
            temp_model = main_models.GetImageAnalyzeTaskStatusResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class GetImageAnalyzeTaskStatusResponseBodyUsage(DaraModel):
    def __init__(
        self,
        pv_count: int = None,
        token_count: int = None,
    ):
        self.pv_count = pv_count
        self.token_count = token_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pv_count is not None:
            result['pv_count'] = self.pv_count

        if self.token_count is not None:
            result['token_count'] = self.token_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pv_count') is not None:
            self.pv_count = m.get('pv_count')

        if m.get('token_count') is not None:
            self.token_count = m.get('token_count')

        return self

class GetImageAnalyzeTaskStatusResponseBodyResult(DaraModel):
    def __init__(
        self,
        data: main_models.GetImageAnalyzeTaskStatusResponseBodyResultData = None,
        error: str = None,
        status: str = None,
        task_id: str = None,
    ):
        self.data = data
        self.error = error
        self.status = status
        self.task_id = task_id

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

        if self.error is not None:
            result['error'] = self.error

        if self.status is not None:
            result['status'] = self.status

        if self.task_id is not None:
            result['task_id'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetImageAnalyzeTaskStatusResponseBodyResultData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('error') is not None:
            self.error = m.get('error')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')

        return self

class GetImageAnalyzeTaskStatusResponseBodyResultData(DaraModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        page_num: int = None,
    ):
        self.content = content
        self.content_type = content_type
        self.page_num = page_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.content_type is not None:
            result['content_type'] = self.content_type

        if self.page_num is not None:
            result['page_num'] = self.page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')

        if m.get('page_num') is not None:
            self.page_num = m.get('page_num')

        return self

