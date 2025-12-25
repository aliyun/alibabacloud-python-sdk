# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateImageTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        article_task_id: str = None,
        paragraph_list_shrink: str = None,
        size: str = None,
        style: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.article_task_id = article_task_id
        # This parameter is required.
        self.paragraph_list_shrink = paragraph_list_shrink
        # This parameter is required.
        self.size = size
        # This parameter is required.
        self.style = style

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.article_task_id is not None:
            result['ArticleTaskId'] = self.article_task_id

        if self.paragraph_list_shrink is not None:
            result['ParagraphList'] = self.paragraph_list_shrink

        if self.size is not None:
            result['Size'] = self.size

        if self.style is not None:
            result['Style'] = self.style

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('ArticleTaskId') is not None:
            self.article_task_id = m.get('ArticleTaskId')

        if m.get('ParagraphList') is not None:
            self.paragraph_list_shrink = m.get('ParagraphList')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Style') is not None:
            self.style = m.get('Style')

        return self

