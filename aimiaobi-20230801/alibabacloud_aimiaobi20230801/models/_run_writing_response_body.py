# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class RunWritingResponseBody(DaraModel):
    def __init__(
        self,
        end: bool = None,
        header: main_models.RunWritingResponseBodyHeader = None,
        payload: main_models.RunWritingResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.end = end
        self.header = header
        self.payload = payload
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
        if self.end is not None:
            result['End'] = self.end

        if self.header is not None:
            result['Header'] = self.header.to_map()

        if self.payload is not None:
            result['Payload'] = self.payload.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Header') is not None:
            temp_model = main_models.RunWritingResponseBodyHeader()
            self.header = temp_model.from_map(m.get('Header'))

        if m.get('Payload') is not None:
            temp_model = main_models.RunWritingResponseBodyPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RunWritingResponseBodyPayload(DaraModel):
    def __init__(
        self,
        output: main_models.RunWritingResponseBodyPayloadOutput = None,
        usage: main_models.RunWritingResponseBodyPayloadUsage = None,
    ):
        self.output = output
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
            temp_model = main_models.RunWritingResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('Usage') is not None:
            temp_model = main_models.RunWritingResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        return self

class RunWritingResponseBodyPayloadUsage(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        token_map: Dict[str, int] = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.token_map = token_map
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

        if self.token_map is not None:
            result['TokenMap'] = self.token_map

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('TokenMap') is not None:
            self.token_map = m.get('TokenMap')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        return self

class RunWritingResponseBodyPayloadOutput(DaraModel):
    def __init__(
        self,
        articles: List[main_models.RunWritingResponseBodyPayloadOutputArticles] = None,
        mini_doc: List[str] = None,
        search_query: str = None,
        text: str = None,
    ):
        self.articles = articles
        self.mini_doc = mini_doc
        self.search_query = search_query
        self.text = text

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

        if self.mini_doc is not None:
            result['MiniDoc'] = self.mini_doc

        if self.search_query is not None:
            result['SearchQuery'] = self.search_query

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.articles = []
        if m.get('Articles') is not None:
            for k1 in m.get('Articles'):
                temp_model = main_models.RunWritingResponseBodyPayloadOutputArticles()
                self.articles.append(temp_model.from_map(k1))

        if m.get('MiniDoc') is not None:
            self.mini_doc = m.get('MiniDoc')

        if m.get('SearchQuery') is not None:
            self.search_query = m.get('SearchQuery')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

class RunWritingResponseBodyPayloadOutputArticles(DaraModel):
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
        self.author = author
        self.content = content
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.pub_time = pub_time
        self.source = source
        self.summary = summary
        self.tag = tag
        self.title = title
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

class RunWritingResponseBodyHeader(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        origin_session_id: str = None,
        session_id: str = None,
        status_code: int = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.origin_session_id = origin_session_id
        self.session_id = session_id
        self.status_code = status_code
        self.task_id = task_id
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

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

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

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

