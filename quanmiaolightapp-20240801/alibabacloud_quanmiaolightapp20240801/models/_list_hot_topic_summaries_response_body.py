# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quanmiaolightapp20240801 import models as main_models
from darabonba.model import DaraModel

class ListHotTopicSummariesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListHotTopicSummariesResponseBodyData] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListHotTopicSummariesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListHotTopicSummariesResponseBodyData(DaraModel):
    def __init__(
        self,
        category: str = None,
        hot_topic: str = None,
        hot_topic_version: str = None,
        hot_value: float = None,
        id: str = None,
        news: List[main_models.ListHotTopicSummariesResponseBodyDataNews] = None,
        summary: main_models.ListHotTopicSummariesResponseBodyDataSummary = None,
        text_summary: str = None,
    ):
        self.category = category
        self.hot_topic = hot_topic
        self.hot_topic_version = hot_topic_version
        self.hot_value = hot_value
        self.id = id
        self.news = news
        self.summary = summary
        self.text_summary = text_summary

    def validate(self):
        if self.news:
            for v1 in self.news:
                 if v1:
                    v1.validate()
        if self.summary:
            self.summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.hot_topic is not None:
            result['hotTopic'] = self.hot_topic

        if self.hot_topic_version is not None:
            result['hotTopicVersion'] = self.hot_topic_version

        if self.hot_value is not None:
            result['hotValue'] = self.hot_value

        if self.id is not None:
            result['id'] = self.id

        result['news'] = []
        if self.news is not None:
            for k1 in self.news:
                result['news'].append(k1.to_map() if k1 else None)

        if self.summary is not None:
            result['summary'] = self.summary.to_map()

        if self.text_summary is not None:
            result['textSummary'] = self.text_summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('hotTopic') is not None:
            self.hot_topic = m.get('hotTopic')

        if m.get('hotTopicVersion') is not None:
            self.hot_topic_version = m.get('hotTopicVersion')

        if m.get('hotValue') is not None:
            self.hot_value = m.get('hotValue')

        if m.get('id') is not None:
            self.id = m.get('id')

        self.news = []
        if m.get('news') is not None:
            for k1 in m.get('news'):
                temp_model = main_models.ListHotTopicSummariesResponseBodyDataNews()
                self.news.append(temp_model.from_map(k1))

        if m.get('summary') is not None:
            temp_model = main_models.ListHotTopicSummariesResponseBodyDataSummary()
            self.summary = temp_model.from_map(m.get('summary'))

        if m.get('textSummary') is not None:
            self.text_summary = m.get('textSummary')

        return self

class ListHotTopicSummariesResponseBodyDataSummary(DaraModel):
    def __init__(
        self,
        summaries: List[main_models.ListHotTopicSummariesResponseBodyDataSummarySummaries] = None,
    ):
        self.summaries = summaries

    def validate(self):
        if self.summaries:
            for v1 in self.summaries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['summaries'] = []
        if self.summaries is not None:
            for k1 in self.summaries:
                result['summaries'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.summaries = []
        if m.get('summaries') is not None:
            for k1 in m.get('summaries'):
                temp_model = main_models.ListHotTopicSummariesResponseBodyDataSummarySummaries()
                self.summaries.append(temp_model.from_map(k1))

        return self

class ListHotTopicSummariesResponseBodyDataSummarySummaries(DaraModel):
    def __init__(
        self,
        summary: str = None,
        title: str = None,
    ):
        self.summary = summary
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.summary is not None:
            result['summary'] = self.summary

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class ListHotTopicSummariesResponseBodyDataNews(DaraModel):
    def __init__(
        self,
        comments: List[main_models.ListHotTopicSummariesResponseBodyDataNewsComments] = None,
        content: str = None,
        pub_time: str = None,
        title: str = None,
        url: str = None,
    ):
        self.comments = comments
        self.content = content
        self.pub_time = pub_time
        self.title = title
        # url
        self.url = url

    def validate(self):
        if self.comments:
            for v1 in self.comments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['comments'] = []
        if self.comments is not None:
            for k1 in self.comments:
                result['comments'].append(k1.to_map() if k1 else None)

        if self.content is not None:
            result['content'] = self.content

        if self.pub_time is not None:
            result['pubTime'] = self.pub_time

        if self.title is not None:
            result['title'] = self.title

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.comments = []
        if m.get('comments') is not None:
            for k1 in m.get('comments'):
                temp_model = main_models.ListHotTopicSummariesResponseBodyDataNewsComments()
                self.comments.append(temp_model.from_map(k1))

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('pubTime') is not None:
            self.pub_time = m.get('pubTime')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

class ListHotTopicSummariesResponseBodyDataNewsComments(DaraModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')

        return self

