# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qweneduaisuite20261102 import models as main_models
from darabonba.model import DaraModel

class CreateEduProblemSolveResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        finished: bool = None,
        items: List[main_models.CreateEduProblemSolveResponseBodyItems] = None,
        message: str = None,
        request_id: str = None,
        result_type: str = None,
        retryable: bool = None,
        usage: main_models.CreateEduProblemSolveResponseBodyUsage = None,
    ):
        # The API data identifier.
        self.code = code
        # Specifies whether this is the final full snapshot. The value is fixed to true in the complete event.
        self.finished = finished
        # The current list of complete question results.
        self.items = items
        # The actual response message of the request.
        self.message = message
        # Echo request ID echoed from echo request.
        self.request_id = request_id
        # The type of the question resolution result. Valid values:
        # * single: Single question.
        # * multiple: Multiple questions.
        self.result_type = result_type
        # Specifies whether the error is retryable. Default value: true.
        self.retryable = retryable
        # The token usage. Only the complete event carries the final value. The message event does not return this field.
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
                temp_model = main_models.CreateEduProblemSolveResponseBodyItems()
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
            temp_model = main_models.CreateEduProblemSolveResponseBodyUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class CreateEduProblemSolveResponseBodyUsage(DaraModel):
    def __init__(
        self,
        completion_tokens: int = None,
        prompt_tokens: int = None,
    ):
        # The number of output tokens.
        self.completion_tokens = completion_tokens
        # The number of input tokens.
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

class CreateEduProblemSolveResponseBodyItems(DaraModel):
    def __init__(
        self,
        content: str = None,
        image_url: str = None,
        question_id: str = None,
        status: str = None,
        thinking: main_models.CreateEduProblemSolveResponseBodyItemsThinking = None,
    ):
        # The complete Markdown content of the question resolution, including the deduction process and the final result.
        self.content = content
        # The URL of the unique image for the current question. The URL may be time-sensitive. If the question is not associated with an image resource and no request URL is available for fallback, an empty string is returned.
        self.image_url = image_url
        # The question identifier. The value is the question title, such as Question 1. The server does not return a separate title field. If the downstream service does not provide a question title, which is always the case for single-question scenarios, titles such as Question 1 and Question 2 are generated in the order of the questions.
        self.question_id = question_id
        # The current question status. Valid values:
        # * processing: Processing.
        # * complete: Complete.
        self.status = status
        # The thinking process. This field is returned only when result_type is single, and is not returned for multiple questions.
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
            temp_model = main_models.CreateEduProblemSolveResponseBodyItemsThinking()
            self.thinking = temp_model.from_map(m.get('thinking'))

        return self

class CreateEduProblemSolveResponseBodyItemsThinking(DaraModel):
    def __init__(
        self,
        content: str = None,
        status: str = None,
    ):
        # The current thinking content.
        self.content = content
        # The thinking status. Valid values:
        # * processing: Processing.
        # * complete: Complete.
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

