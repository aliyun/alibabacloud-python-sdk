# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHotTopicSummariesRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        hot_topic: str = None,
        hot_topic_version: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.category = category
        self.hot_topic = hot_topic
        self.hot_topic_version = hot_topic_version
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

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

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('hotTopic') is not None:
            self.hot_topic = m.get('hotTopic')

        if m.get('hotTopicVersion') is not None:
            self.hot_topic_version = m.get('hotTopicVersion')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

