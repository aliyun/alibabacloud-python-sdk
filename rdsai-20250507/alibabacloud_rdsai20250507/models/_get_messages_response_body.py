# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class GetMessagesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetMessagesResponseBodyData] = None,
        has_more: bool = None,
        limit: int = None,
        request_id: str = None,
    ):
        self.data = data
        self.has_more = has_more
        self.limit = limit
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.has_more is not None:
            result['HasMore'] = self.has_more

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetMessagesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMessagesResponseBodyData(DaraModel):
    def __init__(
        self,
        answer: str = None,
        conversation_id: str = None,
        created_at: str = None,
        feedback: str = None,
        id: str = None,
        query: str = None,
        retriever_resources: List[Any] = None,
    ):
        self.answer = answer
        self.conversation_id = conversation_id
        self.created_at = created_at
        self.feedback = feedback
        self.id = id
        self.query = query
        self.retriever_resources = retriever_resources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['Answer'] = self.answer

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.feedback is not None:
            result['Feedback'] = self.feedback

        if self.id is not None:
            result['Id'] = self.id

        if self.query is not None:
            result['Query'] = self.query

        if self.retriever_resources is not None:
            result['RetrieverResources'] = self.retriever_resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('RetrieverResources') is not None:
            self.retriever_resources = m.get('RetrieverResources')

        return self

