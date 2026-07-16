# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListHotTopicsRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        create_time_end: str = None,
        create_time_start: str = None,
        custom_field: str = None,
        max_results: int = None,
        next_token: str = None,
        topic_ids: List[str] = None,
        topic_query: str = None,
        topic_source: str = None,
        topic_version: str = None,
        topics: List[str] = None,
        with_news: bool = None,
    ):
        # The unique identifier of the business space.
        # 
        # This parameter is required.
        self.agent_key = agent_key
        # The end of the creation time filter range (inclusive). The value must be in the `yyyy-MM-dd HH:mm:ss` format.
        self.create_time_end = create_time_end
        # The start of the creation time filter range (inclusive). The value must be in the `yyyy-MM-dd HH:mm:ss` format.
        self.create_time_start = create_time_start
        # Filters the results by a custom business field. The service performs an exact keyword match on this field. The value can be up to 255 characters long.
        self.custom_field = custom_field
        # The maximum number of results to return for a single request. If this parameter is not specified, the service uses a default value.
        self.max_results = max_results
        # The token used to retrieve the next page of results. If you do not specify this parameter, the service returns the first page of results. You can get this token from the `NextToken` response parameter of the previous request.
        self.next_token = next_token
        # A list of topic IDs.
        self.topic_ids = topic_ids
        # The keywords for a full-text search on hot topics.
        self.topic_query = topic_query
        # Filters the results by hot topic source. For a list of supported hot topic sources, call the `ListHotSources` operation.
        # 
        # `Aggregation`: represents the aggregated list of national hot topics.
        self.topic_source = topic_source
        # Filters the results by data version.
        self.topic_version = topic_version
        # Filters the results by hot topic.
        self.topics = topics
        # Specifies whether to include news in the response.
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

        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end

        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start

        if self.custom_field is not None:
            result['CustomField'] = self.custom_field

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.topic_ids is not None:
            result['TopicIds'] = self.topic_ids

        if self.topic_query is not None:
            result['TopicQuery'] = self.topic_query

        if self.topic_source is not None:
            result['TopicSource'] = self.topic_source

        if self.topic_version is not None:
            result['TopicVersion'] = self.topic_version

        if self.topics is not None:
            result['Topics'] = self.topics

        if self.with_news is not None:
            result['WithNews'] = self.with_news

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')

        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')

        if m.get('CustomField') is not None:
            self.custom_field = m.get('CustomField')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TopicIds') is not None:
            self.topic_ids = m.get('TopicIds')

        if m.get('TopicQuery') is not None:
            self.topic_query = m.get('TopicQuery')

        if m.get('TopicSource') is not None:
            self.topic_source = m.get('TopicSource')

        if m.get('TopicVersion') is not None:
            self.topic_version = m.get('TopicVersion')

        if m.get('Topics') is not None:
            self.topics = m.get('Topics')

        if m.get('WithNews') is not None:
            self.with_news = m.get('WithNews')

        return self

