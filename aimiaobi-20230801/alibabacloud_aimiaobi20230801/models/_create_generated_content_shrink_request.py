# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGeneratedContentShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        content_domain: str = None,
        content_text: str = None,
        keywords_shrink: str = None,
        prompt: str = None,
        task_id: str = None,
        title: str = None,
        uuid: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.content = content
        self.content_domain = content_domain
        self.content_text = content_text
        self.keywords_shrink = keywords_shrink
        self.prompt = prompt
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.title = title
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.content is not None:
            result['Content'] = self.content

        if self.content_domain is not None:
            result['ContentDomain'] = self.content_domain

        if self.content_text is not None:
            result['ContentText'] = self.content_text

        if self.keywords_shrink is not None:
            result['Keywords'] = self.keywords_shrink

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.title is not None:
            result['Title'] = self.title

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentDomain') is not None:
            self.content_domain = m.get('ContentDomain')

        if m.get('ContentText') is not None:
            self.content_text = m.get('ContentText')

        if m.get('Keywords') is not None:
            self.keywords_shrink = m.get('Keywords')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

