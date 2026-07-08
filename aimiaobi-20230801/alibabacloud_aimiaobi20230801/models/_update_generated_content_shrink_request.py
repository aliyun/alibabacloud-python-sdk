# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGeneratedContentShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        content_text: str = None,
        id: int = None,
        keywords_shrink: str = None,
        prompt: str = None,
        title: str = None,
    ):
        # The unique identifier of the workspace. For more information, see [AgentKey](https://help.aliyun.com/document_detail/2587494.html).
        # 
        # This parameter is required.
        self.agent_key = agent_key
        # The body of the article in rich text format.
        self.content = content
        # The body of the article in plain text format.
        self.content_text = content_text
        # The unique identifier of the document.
        # 
        # This parameter is required.
        self.id = id
        # The keywords.
        self.keywords_shrink = keywords_shrink
        # The last prompt that was used to generate the content.
        self.prompt = prompt
        # The title.
        self.title = title

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

        if self.content_text is not None:
            result['ContentText'] = self.content_text

        if self.id is not None:
            result['Id'] = self.id

        if self.keywords_shrink is not None:
            result['Keywords'] = self.keywords_shrink

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentText') is not None:
            self.content_text = m.get('ContentText')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Keywords') is not None:
            self.keywords_shrink = m.get('Keywords')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

