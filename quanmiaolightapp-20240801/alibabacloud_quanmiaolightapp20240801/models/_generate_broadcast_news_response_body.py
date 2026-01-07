# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quanmiaolightapp20240801 import models as main_models
from darabonba.model import DaraModel

class GenerateBroadcastNewsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GenerateBroadcastNewsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GenerateBroadcastNewsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GenerateBroadcastNewsResponseBodyData(DaraModel):
    def __init__(
        self,
        hot_topic_summaries: List[main_models.GenerateBroadcastNewsResponseBodyDataHotTopicSummaries] = None,
        session_id: str = None,
        task_id: str = None,
        text: str = None,
        usage: main_models.GenerateBroadcastNewsResponseBodyDataUsage = None,
    ):
        self.hot_topic_summaries = hot_topic_summaries
        self.session_id = session_id
        self.task_id = task_id
        self.text = text
        self.usage = usage

    def validate(self):
        if self.hot_topic_summaries:
            for v1 in self.hot_topic_summaries:
                 if v1:
                    v1.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['hotTopicSummaries'] = []
        if self.hot_topic_summaries is not None:
            for k1 in self.hot_topic_summaries:
                result['hotTopicSummaries'].append(k1.to_map() if k1 else None)

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.text is not None:
            result['text'] = self.text

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hot_topic_summaries = []
        if m.get('hotTopicSummaries') is not None:
            for k1 in m.get('hotTopicSummaries'):
                temp_model = main_models.GenerateBroadcastNewsResponseBodyDataHotTopicSummaries()
                self.hot_topic_summaries.append(temp_model.from_map(k1))

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('text') is not None:
            self.text = m.get('text')

        if m.get('usage') is not None:
            temp_model = main_models.GenerateBroadcastNewsResponseBodyDataUsage()
            self.usage = temp_model.from_map(m.get('usage'))

        return self

class GenerateBroadcastNewsResponseBodyDataUsage(DaraModel):
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

class GenerateBroadcastNewsResponseBodyDataHotTopicSummaries(DaraModel):
    def __init__(
        self,
        category: str = None,
        hot_topic: str = None,
        hot_topic_version: str = None,
        hot_value: float = None,
        id: str = None,
        images: List[main_models.GenerateBroadcastNewsResponseBodyDataHotTopicSummariesImages] = None,
        text_summary: str = None,
    ):
        self.category = category
        self.hot_topic = hot_topic
        self.hot_topic_version = hot_topic_version
        self.hot_value = hot_value
        self.id = id
        self.images = images
        self.text_summary = text_summary

    def validate(self):
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()

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

        result['images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['images'].append(k1.to_map() if k1 else None)

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

        self.images = []
        if m.get('images') is not None:
            for k1 in m.get('images'):
                temp_model = main_models.GenerateBroadcastNewsResponseBodyDataHotTopicSummariesImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('textSummary') is not None:
            self.text_summary = m.get('textSummary')

        return self



class GenerateBroadcastNewsResponseBodyDataHotTopicSummariesImages(DaraModel):
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

