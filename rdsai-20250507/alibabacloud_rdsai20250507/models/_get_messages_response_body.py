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
        # The returned results.
        self.data = data
        # Indicates whether the current page is followed by a page.
        self.has_more = has_more
        # The maximum number of entries to return.
        self.limit = limit
        # The request ID.
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
        events: List[main_models.GetMessagesResponseBodyDataEvents] = None,
        feedback: str = None,
        generation_finished_at: str = None,
        generation_started_at: str = None,
        generation_status: str = None,
        id: str = None,
        last_sent_entry_id: str = None,
        query: str = None,
        retriever_resources: List[Any] = None,
        stream_key: str = None,
    ):
        # The response to the query.
        self.answer = answer
        # The ID of the conversation.
        self.conversation_id = conversation_id
        # The creation time of the conversation.
        self.created_at = created_at
        self.events = events
        # The feedback.
        self.feedback = feedback
        self.generation_finished_at = generation_finished_at
        self.generation_started_at = generation_started_at
        self.generation_status = generation_status
        # The message ID.
        self.id = id
        self.last_sent_entry_id = last_sent_entry_id
        # The query statement.
        self.query = query
        # The retriever resources.
        self.retriever_resources = retriever_resources
        self.stream_key = stream_key

    def validate(self):
        if self.events:
            for v1 in self.events:
                 if v1:
                    v1.validate()

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

        result['Events'] = []
        if self.events is not None:
            for k1 in self.events:
                result['Events'].append(k1.to_map() if k1 else None)

        if self.feedback is not None:
            result['Feedback'] = self.feedback

        if self.generation_finished_at is not None:
            result['GenerationFinishedAt'] = self.generation_finished_at

        if self.generation_started_at is not None:
            result['GenerationStartedAt'] = self.generation_started_at

        if self.generation_status is not None:
            result['GenerationStatus'] = self.generation_status

        if self.id is not None:
            result['Id'] = self.id

        if self.last_sent_entry_id is not None:
            result['LastSentEntryId'] = self.last_sent_entry_id

        if self.query is not None:
            result['Query'] = self.query

        if self.retriever_resources is not None:
            result['RetrieverResources'] = self.retriever_resources

        if self.stream_key is not None:
            result['StreamKey'] = self.stream_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        self.events = []
        if m.get('Events') is not None:
            for k1 in m.get('Events'):
                temp_model = main_models.GetMessagesResponseBodyDataEvents()
                self.events.append(temp_model.from_map(k1))

        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')

        if m.get('GenerationFinishedAt') is not None:
            self.generation_finished_at = m.get('GenerationFinishedAt')

        if m.get('GenerationStartedAt') is not None:
            self.generation_started_at = m.get('GenerationStartedAt')

        if m.get('GenerationStatus') is not None:
            self.generation_status = m.get('GenerationStatus')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastSentEntryId') is not None:
            self.last_sent_entry_id = m.get('LastSentEntryId')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('RetrieverResources') is not None:
            self.retriever_resources = m.get('RetrieverResources')

        if m.get('StreamKey') is not None:
            self.stream_key = m.get('StreamKey')

        return self

class GetMessagesResponseBodyDataEvents(DaraModel):
    def __init__(
        self,
        answer: str = None,
        event: str = None,
    ):
        self.answer = answer
        self.event = event

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['answer'] = self.answer

        if self.event is not None:
            result['event'] = self.event

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answer') is not None:
            self.answer = m.get('answer')

        if m.get('event') is not None:
            self.event = m.get('event')

        return self

