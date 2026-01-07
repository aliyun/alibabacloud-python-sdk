# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quanmiaolightapp20240801 import models as main_models
from darabonba.model import DaraModel

class RunHotTopicChatResponseBody(DaraModel):
    def __init__(
        self,
        header: main_models.RunHotTopicChatResponseBodyHeader = None,
        payload: main_models.RunHotTopicChatResponseBodyPayload = None,
        request_id: str = None,
    ):
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
        if self.header is not None:
            result['header'] = self.header.to_map()

        if self.payload is not None:
            result['payload'] = self.payload.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('header') is not None:
            temp_model = main_models.RunHotTopicChatResponseBodyHeader()
            self.header = temp_model.from_map(m.get('header'))

        if m.get('payload') is not None:
            temp_model = main_models.RunHotTopicChatResponseBodyPayload()
            self.payload = temp_model.from_map(m.get('payload'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class RunHotTopicChatResponseBodyPayload(DaraModel):
    def __init__(
        self,
        output: main_models.RunHotTopicChatResponseBodyPayloadOutput = None,
        usage: main_models.RunHotTopicChatResponseBodyPayloadUsage = None,
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
            result['output'] = self.output.to_map()

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('output') is not None:
            temp_model = main_models.RunHotTopicChatResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m.get('output'))

        if m.get('usage') is not None:
            temp_model = main_models.RunHotTopicChatResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class RunHotTopicChatResponseBodyPayloadUsage(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')

        return self

class RunHotTopicChatResponseBodyPayloadOutput(DaraModel):
    def __init__(
        self,
        articles: List[main_models.RunHotTopicChatResponseBodyPayloadOutputArticles] = None,
        category: str = None,
        hot_topic_summaries: List[main_models.RunHotTopicChatResponseBodyPayloadOutputHotTopicSummaries] = None,
        keyword: str = None,
        location: str = None,
        multimodal_medias: List[main_models.RunHotTopicChatResponseBodyPayloadOutputMultimodalMedias] = None,
        recommend_queries: List[str] = None,
        search_query: str = None,
        text: str = None,
    ):
        self.articles = articles
        self.category = category
        self.hot_topic_summaries = hot_topic_summaries
        self.keyword = keyword
        self.location = location
        self.multimodal_medias = multimodal_medias
        self.recommend_queries = recommend_queries
        self.search_query = search_query
        self.text = text

    def validate(self):
        if self.articles:
            for v1 in self.articles:
                 if v1:
                    v1.validate()
        if self.hot_topic_summaries:
            for v1 in self.hot_topic_summaries:
                 if v1:
                    v1.validate()
        if self.multimodal_medias:
            for v1 in self.multimodal_medias:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['articles'] = []
        if self.articles is not None:
            for k1 in self.articles:
                result['articles'].append(k1.to_map() if k1 else None)

        if self.category is not None:
            result['category'] = self.category

        result['hotTopicSummaries'] = []
        if self.hot_topic_summaries is not None:
            for k1 in self.hot_topic_summaries:
                result['hotTopicSummaries'].append(k1.to_map() if k1 else None)

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.location is not None:
            result['location'] = self.location

        result['multimodalMedias'] = []
        if self.multimodal_medias is not None:
            for k1 in self.multimodal_medias:
                result['multimodalMedias'].append(k1.to_map() if k1 else None)

        if self.recommend_queries is not None:
            result['recommendQueries'] = self.recommend_queries

        if self.search_query is not None:
            result['searchQuery'] = self.search_query

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.articles = []
        if m.get('articles') is not None:
            for k1 in m.get('articles'):
                temp_model = main_models.RunHotTopicChatResponseBodyPayloadOutputArticles()
                self.articles.append(temp_model.from_map(k1))

        if m.get('category') is not None:
            self.category = m.get('category')

        self.hot_topic_summaries = []
        if m.get('hotTopicSummaries') is not None:
            for k1 in m.get('hotTopicSummaries'):
                temp_model = main_models.RunHotTopicChatResponseBodyPayloadOutputHotTopicSummaries()
                self.hot_topic_summaries.append(temp_model.from_map(k1))

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('location') is not None:
            self.location = m.get('location')

        self.multimodal_medias = []
        if m.get('multimodalMedias') is not None:
            for k1 in m.get('multimodalMedias'):
                temp_model = main_models.RunHotTopicChatResponseBodyPayloadOutputMultimodalMedias()
                self.multimodal_medias.append(temp_model.from_map(k1))

        if m.get('recommendQueries') is not None:
            self.recommend_queries = m.get('recommendQueries')

        if m.get('searchQuery') is not None:
            self.search_query = m.get('searchQuery')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

class RunHotTopicChatResponseBodyPayloadOutputMultimodalMedias(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        media_type: str = None,
        sort_score: float = None,
    ):
        self.file_url = file_url
        self.media_type = media_type
        self.sort_score = sort_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_url is not None:
            result['fileUrl'] = self.file_url

        if self.media_type is not None:
            result['mediaType'] = self.media_type

        if self.sort_score is not None:
            result['sortScore'] = self.sort_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')

        if m.get('mediaType') is not None:
            self.media_type = m.get('mediaType')

        if m.get('sortScore') is not None:
            self.sort_score = m.get('sortScore')

        return self

class RunHotTopicChatResponseBodyPayloadOutputHotTopicSummaries(DaraModel):
    def __init__(
        self,
        custom_hot_value: float = None,
        custom_text_summary: str = None,
        hot_topic: str = None,
        hot_topic_version: str = None,
        hot_value: float = None,
        images: List[main_models.RunHotTopicChatResponseBodyPayloadOutputHotTopicSummariesImages] = None,
        news: List[main_models.RunHotTopicChatResponseBodyPayloadOutputHotTopicSummariesNews] = None,
        pub_time: str = None,
        text_summary: str = None,
        url: str = None,
    ):
        self.custom_hot_value = custom_hot_value
        self.custom_text_summary = custom_text_summary
        self.hot_topic = hot_topic
        self.hot_topic_version = hot_topic_version
        self.hot_value = hot_value
        self.images = images
        self.news = news
        self.pub_time = pub_time
        self.text_summary = text_summary
        self.url = url

    def validate(self):
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()
        if self.news:
            for v1 in self.news:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_hot_value is not None:
            result['customHotValue'] = self.custom_hot_value

        if self.custom_text_summary is not None:
            result['customTextSummary'] = self.custom_text_summary

        if self.hot_topic is not None:
            result['hotTopic'] = self.hot_topic

        if self.hot_topic_version is not None:
            result['hotTopicVersion'] = self.hot_topic_version

        if self.hot_value is not None:
            result['hotValue'] = self.hot_value

        result['images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['images'].append(k1.to_map() if k1 else None)

        result['news'] = []
        if self.news is not None:
            for k1 in self.news:
                result['news'].append(k1.to_map() if k1 else None)

        if self.pub_time is not None:
            result['pubTime'] = self.pub_time

        if self.text_summary is not None:
            result['textSummary'] = self.text_summary

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customHotValue') is not None:
            self.custom_hot_value = m.get('customHotValue')

        if m.get('customTextSummary') is not None:
            self.custom_text_summary = m.get('customTextSummary')

        if m.get('hotTopic') is not None:
            self.hot_topic = m.get('hotTopic')

        if m.get('hotTopicVersion') is not None:
            self.hot_topic_version = m.get('hotTopicVersion')

        if m.get('hotValue') is not None:
            self.hot_value = m.get('hotValue')

        self.images = []
        if m.get('images') is not None:
            for k1 in m.get('images'):
                temp_model = main_models.RunHotTopicChatResponseBodyPayloadOutputHotTopicSummariesImages()
                self.images.append(temp_model.from_map(k1))

        self.news = []
        if m.get('news') is not None:
            for k1 in m.get('news'):
                temp_model = main_models.RunHotTopicChatResponseBodyPayloadOutputHotTopicSummariesNews()
                self.news.append(temp_model.from_map(k1))

        if m.get('pubTime') is not None:
            self.pub_time = m.get('pubTime')

        if m.get('textSummary') is not None:
            self.text_summary = m.get('textSummary')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class RunHotTopicChatResponseBodyPayloadOutputHotTopicSummariesNews(DaraModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.title is not None:
            result['title'] = self.title

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class RunHotTopicChatResponseBodyPayloadOutputHotTopicSummariesImages(DaraModel):
    def __init__(
        self,
        url: str = None,
    ):
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class RunHotTopicChatResponseBodyPayloadOutputArticles(DaraModel):
    def __init__(
        self,
        content: str = None,
        pub_time: str = None,
        score: float = None,
        search_source_name: str = None,
        select: bool = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.content = content
        self.pub_time = pub_time
        self.score = score
        self.search_source_name = search_source_name
        self.select = select
        self.summary = summary
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.pub_time is not None:
            result['pubTime'] = self.pub_time

        if self.score is not None:
            result['score'] = self.score

        if self.search_source_name is not None:
            result['searchSourceName'] = self.search_source_name

        if self.select is not None:
            result['select'] = self.select

        if self.summary is not None:
            result['summary'] = self.summary

        if self.title is not None:
            result['title'] = self.title

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('pubTime') is not None:
            self.pub_time = m.get('pubTime')

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('searchSourceName') is not None:
            self.search_source_name = m.get('searchSourceName')

        if m.get('select') is not None:
            self.select = m.get('select')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class RunHotTopicChatResponseBodyHeader(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        event_info: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.event_info = event_info
        self.session_id = session_id
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
            result['errorCode'] = self.error_code

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.event is not None:
            result['event'] = self.event

        if self.event_info is not None:
            result['eventInfo'] = self.event_info

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('event') is not None:
            self.event = m.get('event')

        if m.get('eventInfo') is not None:
            self.event_info = m.get('eventInfo')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

