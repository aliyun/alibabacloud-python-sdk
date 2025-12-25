# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunCustomHotTopicViewPointAnalysisRequest(DaraModel):
    def __init__(
        self,
        ask_user: str = None,
        prompt: str = None,
        search_query: str = None,
        skip_ask_user: bool = None,
        topic: str = None,
        topic_id: str = None,
        topic_source: str = None,
        topic_version: str = None,
        user_back: str = None,
        workspace_id: str = None,
    ):
        self.ask_user = ask_user
        # This parameter is required.
        self.prompt = prompt
        self.search_query = search_query
        self.skip_ask_user = skip_ask_user
        self.topic = topic
        self.topic_id = topic_id
        self.topic_source = topic_source
        self.topic_version = topic_version
        self.user_back = user_back
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ask_user is not None:
            result['AskUser'] = self.ask_user

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.search_query is not None:
            result['SearchQuery'] = self.search_query

        if self.skip_ask_user is not None:
            result['SkipAskUser'] = self.skip_ask_user

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.topic_id is not None:
            result['TopicId'] = self.topic_id

        if self.topic_source is not None:
            result['TopicSource'] = self.topic_source

        if self.topic_version is not None:
            result['TopicVersion'] = self.topic_version

        if self.user_back is not None:
            result['UserBack'] = self.user_back

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AskUser') is not None:
            self.ask_user = m.get('AskUser')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('SearchQuery') is not None:
            self.search_query = m.get('SearchQuery')

        if m.get('SkipAskUser') is not None:
            self.skip_ask_user = m.get('SkipAskUser')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')

        if m.get('TopicSource') is not None:
            self.topic_source = m.get('TopicSource')

        if m.get('TopicVersion') is not None:
            self.topic_version = m.get('TopicVersion')

        if m.get('UserBack') is not None:
            self.user_back = m.get('UserBack')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

