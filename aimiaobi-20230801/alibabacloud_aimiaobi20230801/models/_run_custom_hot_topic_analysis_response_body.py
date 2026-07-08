# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class RunCustomHotTopicAnalysisResponseBody(DaraModel):
    def __init__(
        self,
        header: main_models.RunCustomHotTopicAnalysisResponseBodyHeader = None,
        payload: main_models.RunCustomHotTopicAnalysisResponseBodyPayload = None,
        request_id: str = None,
    ):
        # The response header.
        self.header = header
        # The response body.
        self.payload = payload
        # The request ID.
        self.request_id = request_id

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
        if self.header is not None:
            result['Header'] = self.header.to_map()

        if self.payload is not None:
            result['Payload'] = self.payload.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Header') is not None:
            temp_model = main_models.RunCustomHotTopicAnalysisResponseBodyHeader()
            self.header = temp_model.from_map(m.get('Header'))

        if m.get('Payload') is not None:
            temp_model = main_models.RunCustomHotTopicAnalysisResponseBodyPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RunCustomHotTopicAnalysisResponseBodyPayload(DaraModel):
    def __init__(
        self,
        output: main_models.RunCustomHotTopicAnalysisResponseBodyPayloadOutput = None,
        usage: main_models.RunCustomHotTopicAnalysisResponseBodyPayloadUsage = None,
    ):
        # The output.
        self.output = output
        # The token usage.
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
            result['Output'] = self.output.to_map()

        if self.usage is not None:
            result['Usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            temp_model = main_models.RunCustomHotTopicAnalysisResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('Usage') is not None:
            temp_model = main_models.RunCustomHotTopicAnalysisResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        return self

class RunCustomHotTopicAnalysisResponseBodyPayloadUsage(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        # The number of tokens used for the input.
        self.input_tokens = input_tokens
        # The number of tokens for the output.
        self.output_tokens = output_tokens
        # The total number of tokens.
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        return self

class RunCustomHotTopicAnalysisResponseBodyPayloadOutput(DaraModel):
    def __init__(
        self,
        articles: List[main_models.RunCustomHotTopicAnalysisResponseBodyPayloadOutputArticles] = None,
        ask_user: List[str] = None,
        async_task_id: str = None,
        attitude: str = None,
        search_query: str = None,
        text: str = None,
        topic_id: str = None,
    ):
        # The reference articles.
        self.articles = articles
        # The list of follow-up questions.
        self.ask_user = ask_user
        # The ID of the asynchronous task.
        self.async_task_id = async_task_id
        # The custom perspective for topic selection.
        self.attitude = attitude
        # The rewritten query.
        self.search_query = search_query
        # The text generation result.
        self.text = text
        # The topic ID.
        self.topic_id = topic_id

    def validate(self):
        if self.articles:
            for v1 in self.articles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Articles'] = []
        if self.articles is not None:
            for k1 in self.articles:
                result['Articles'].append(k1.to_map() if k1 else None)

        if self.ask_user is not None:
            result['AskUser'] = self.ask_user

        if self.async_task_id is not None:
            result['AsyncTaskId'] = self.async_task_id

        if self.attitude is not None:
            result['Attitude'] = self.attitude

        if self.search_query is not None:
            result['SearchQuery'] = self.search_query

        if self.text is not None:
            result['Text'] = self.text

        if self.topic_id is not None:
            result['TopicId'] = self.topic_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.articles = []
        if m.get('Articles') is not None:
            for k1 in m.get('Articles'):
                temp_model = main_models.RunCustomHotTopicAnalysisResponseBodyPayloadOutputArticles()
                self.articles.append(temp_model.from_map(k1))

        if m.get('AskUser') is not None:
            self.ask_user = m.get('AskUser')

        if m.get('AsyncTaskId') is not None:
            self.async_task_id = m.get('AsyncTaskId')

        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')

        if m.get('SearchQuery') is not None:
            self.search_query = m.get('SearchQuery')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')

        return self

class RunCustomHotTopicAnalysisResponseBodyPayloadOutputArticles(DaraModel):
    def __init__(
        self,
        author: str = None,
        content: str = None,
        doc_id: str = None,
        doc_uuid: str = None,
        pub_time: str = None,
        source: str = None,
        summary: str = None,
        tag: str = None,
        title: str = None,
        url: str = None,
    ):
        # The author.
        self.author = author
        # The content.
        self.content = content
        # The custom unique ID of the document.
        self.doc_id = doc_id
        # The internal unique ID of the document.
        self.doc_uuid = doc_uuid
        # The publication time.
        self.pub_time = pub_time
        # The source.
        self.source = source
        # The article summary.
        self.summary = summary
        # The tag.
        self.tag = tag
        # The title.
        self.title = title
        # The URL of the article.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.author is not None:
            result['Author'] = self.author

        if self.content is not None:
            result['Content'] = self.content

        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.source is not None:
            result['Source'] = self.source

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunCustomHotTopicAnalysisResponseBodyHeader(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        origin_session_id: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The Server-Sent Events (SSE) event. Valid values: task-started: The task starts. task-finished: The task is complete. task-failed: The task failed.
        self.event = event
        # The parent session ID.
        self.origin_session_id = origin_session_id
        # The session ID.
        self.session_id = session_id
        # The task ID.
        self.task_id = task_id
        # The trace ID.
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.event is not None:
            result['Event'] = self.event

        if self.origin_session_id is not None:
            result['OriginSessionId'] = self.origin_session_id

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('OriginSessionId') is not None:
            self.origin_session_id = m.get('OriginSessionId')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

