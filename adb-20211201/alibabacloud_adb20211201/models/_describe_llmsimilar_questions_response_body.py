# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeLLMSimilarQuestionsResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeLLMSimilarQuestionsResponseBodyItems] = None,
        request_id: str = None,
        session_id: str = None,
    ):
        # The queried similar questions.
        self.items = items
        # The request ID.
        self.request_id = request_id
        # The session ID.
        self.session_id = session_id

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
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeLLMSimilarQuestionsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

class DescribeLLMSimilarQuestionsResponseBodyItems(DaraModel):
    def __init__(
        self,
        answer: str = None,
        id: str = None,
        score: float = None,
        source: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        # The answer to the similar question.
        self.answer = answer
        # The ID of the similar question.
        self.id = id
        # The similarity of the similar question.
        self.score = score
        # The source of the similar question.
        self.source = source
        # The summary of the similar question.
        self.summary = summary
        # The content of the similar question.
        self.title = title
        # The URL of the answer to the similar question.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['Answer'] = self.answer

        if self.id is not None:
            result['Id'] = self.id

        if self.score is not None:
            result['Score'] = self.score

        if self.source is not None:
            result['Source'] = self.source

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

