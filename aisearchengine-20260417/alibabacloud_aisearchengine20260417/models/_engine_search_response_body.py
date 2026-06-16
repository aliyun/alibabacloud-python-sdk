# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_aisearchengine20260417 import models as main_models
from darabonba.model import DaraModel

class EngineSearchResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.EngineSearchResponseBodyData = None,
        message: str = None,
    ):
        # The status code. A value of 200 indicates success.
        self.code = code
        # The business data body.
        self.data = data
        # The response message.
        self.message = message

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

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.EngineSearchResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

class EngineSearchResponseBodyData(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        extra: Dict[str, Any] = None,
        items: List[main_models.EngineSearchResponseBodyDataItems] = None,
        page: int = None,
        request_id: str = None,
        size: int = None,
        status: str = None,
        total: int = None,
        trace_info: Dict[str, Any] = None,
    ):
        # The error message.
        self.error_message = error_message
        # The additional metadata. 
        # 
        # > Contains the exclude_ids field, which represents the list of IDs that were actually excluded. The format is `Array[String]`.
        # > - Example: ["id_1", "id_2"].
        self.extra = extra
        # 搜索结果列表
        self.items = items
        # The search page number.
        self.page = page
        # The response ID of this request.
        self.request_id = request_id
        # The number of results returned on the current page.
        self.size = size
        # The execution status.
        # 200: succeeded.
        # 500: failed.
        self.status = status
        # The total number of records.
        self.total = total
        # The Tracing Analysis information.
        self.trace_info = trace_info

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.extra is not None:
            result['extra'] = self.extra

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['page'] = self.page

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.size is not None:
            result['size'] = self.size

        if self.status is not None:
            result['status'] = self.status

        if self.total is not None:
            result['total'] = self.total

        if self.trace_info is not None:
            result['traceInfo'] = self.trace_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.EngineSearchResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('total') is not None:
            self.total = m.get('total')

        if m.get('traceInfo') is not None:
            self.trace_info = m.get('traceInfo')

        return self

class EngineSearchResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        algorithm: Dict[str, Any] = None,
        content: Dict[str, Any] = None,
        id: str = None,
        score: float = None,
        trace_info: Dict[str, Any] = None,
    ):
        # 算法内容
        self.algorithm = algorithm
        # 内容详情对象（详细结构见下文）
        self.content = content
        # 权益绑定 ID
        self.id = id
        # 相关性得分
        self.score = score
        # 回传日志时使用。
        # 
        # 取值：
        # 
        # trace_id=ali。
        self.trace_info = trace_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm

        if self.content is not None:
            result['content'] = self.content

        if self.id is not None:
            result['id'] = self.id

        if self.score is not None:
            result['score'] = self.score

        if self.trace_info is not None:
            result['traceInfo'] = self.trace_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('traceInfo') is not None:
            self.trace_info = m.get('traceInfo')

        return self

