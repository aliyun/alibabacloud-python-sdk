# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qweneduaisuite20261102 import models as main_models
from darabonba.model import DaraModel

class CreateEduProblemSolveResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateEduProblemSolveResponseBodyData = None,
        event: str = None,
    ):
        self.data = data
        self.event = event

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

        if self.event is not None:
            result['event'] = self.event

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.CreateEduProblemSolveResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('event') is not None:
            self.event = m.get('event')

        return self

class CreateEduProblemSolveResponseBodyData(DaraModel):
    def __init__(
        self,
        code: str = None,
        finished: bool = None,
        items: List[main_models.CreateEduProblemSolveResponseBodyDataItems] = None,
        message: str = None,
        request_id: str = None,
        result_type: str = None,
        retryable: bool = None,
        usage: main_models.CreateEduProblemSolveResponseBodyDataUsage = None,
    ):
        self.code = code
        self.finished = finished
        self.items = items
        self.message = message
        self.request_id = request_id
        self.result_type = result_type
        self.retryable = retryable
        self.usage = usage

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.finished is not None:
            result['finished'] = self.finished

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result_type is not None:
            result['resultType'] = self.result_type

        if self.retryable is not None:
            result['retryable'] = self.retryable

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('finished') is not None:
            self.finished = m.get('finished')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.CreateEduProblemSolveResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')

        if m.get('retryable') is not None:
            self.retryable = m.get('retryable')

        if m.get('usage') is not None:
            temp_model = main_models.CreateEduProblemSolveResponseBodyDataUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class CreateEduProblemSolveResponseBodyDataUsage(DaraModel):
    def __init__(
        self,
        completion_tokens: int = None,
        prompt_tokens: int = None,
    ):
        self.completion_tokens = completion_tokens
        self.prompt_tokens = prompt_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completion_tokens is not None:
            result['completionTokens'] = self.completion_tokens

        if self.prompt_tokens is not None:
            result['promptTokens'] = self.prompt_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('completionTokens') is not None:
            self.completion_tokens = m.get('completionTokens')

        if m.get('promptTokens') is not None:
            self.prompt_tokens = m.get('promptTokens')

        return self

class CreateEduProblemSolveResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        content: str = None,
        image_url: str = None,
        question_id: str = None,
        status: str = None,
        thinking: main_models.CreateEduProblemSolveResponseBodyDataItemsThinking = None,
    ):
        self.content = content
        self.image_url = image_url
        self.question_id = question_id
        self.status = status
        self.thinking = thinking

    def validate(self):
        if self.thinking:
            self.thinking.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.image_url is not None:
            result['imageUrl'] = self.image_url

        if self.question_id is not None:
            result['questionId'] = self.question_id

        if self.status is not None:
            result['status'] = self.status

        if self.thinking is not None:
            result['thinking'] = self.thinking.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')

        if m.get('questionId') is not None:
            self.question_id = m.get('questionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('thinking') is not None:
            temp_model = main_models.CreateEduProblemSolveResponseBodyDataItemsThinking()
            self.thinking = temp_model.from_map(m.get('thinking'))

        return self

class CreateEduProblemSolveResponseBodyDataItemsThinking(DaraModel):
    def __init__(
        self,
        content: str = None,
        status: str = None,
    ):
        self.content = content
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

