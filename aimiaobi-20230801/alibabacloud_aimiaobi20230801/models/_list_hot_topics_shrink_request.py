# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHotTopicsShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        max_results: int = None,
        next_token: str = None,
        topic_ids_shrink: str = None,
        topic_query: str = None,
        topic_source: str = None,
        topic_version: str = None,
        topics_shrink: str = None,
        with_news: bool = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.max_results = max_results
        self.next_token = next_token
        self.topic_ids_shrink = topic_ids_shrink
        self.topic_query = topic_query
        self.topic_source = topic_source
        self.topic_version = topic_version
        self.topics_shrink = topics_shrink
        self.with_news = with_news

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.topic_ids_shrink is not None:
            result['TopicIds'] = self.topic_ids_shrink

        if self.topic_query is not None:
            result['TopicQuery'] = self.topic_query

        if self.topic_source is not None:
            result['TopicSource'] = self.topic_source

        if self.topic_version is not None:
            result['TopicVersion'] = self.topic_version

        if self.topics_shrink is not None:
            result['Topics'] = self.topics_shrink

        if self.with_news is not None:
            result['WithNews'] = self.with_news

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TopicIds') is not None:
            self.topic_ids_shrink = m.get('TopicIds')

        if m.get('TopicQuery') is not None:
            self.topic_query = m.get('TopicQuery')

        if m.get('TopicSource') is not None:
            self.topic_source = m.get('TopicSource')

        if m.get('TopicVersion') is not None:
            self.topic_version = m.get('TopicVersion')

        if m.get('Topics') is not None:
            self.topics_shrink = m.get('Topics')

        if m.get('WithNews') is not None:
            self.with_news = m.get('WithNews')

        return self

