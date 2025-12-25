# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GenerateImageTaskRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        article_task_id: str = None,
        paragraph_list: List[main_models.GenerateImageTaskRequestParagraphList] = None,
        size: str = None,
        style: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.article_task_id = article_task_id
        # This parameter is required.
        self.paragraph_list = paragraph_list
        # This parameter is required.
        self.size = size
        # This parameter is required.
        self.style = style

    def validate(self):
        if self.paragraph_list:
            for v1 in self.paragraph_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.article_task_id is not None:
            result['ArticleTaskId'] = self.article_task_id

        result['ParagraphList'] = []
        if self.paragraph_list is not None:
            for k1 in self.paragraph_list:
                result['ParagraphList'].append(k1.to_map() if k1 else None)

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

        self.paragraph_list = []
        if m.get('ParagraphList') is not None:
            for k1 in m.get('ParagraphList'):
                temp_model = main_models.GenerateImageTaskRequestParagraphList()
                self.paragraph_list.append(temp_model.from_map(k1))

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Style') is not None:
            self.style = m.get('Style')

        return self

class GenerateImageTaskRequestParagraphList(DaraModel):
    def __init__(
        self,
        content: str = None,
        id: int = None,
        task_id: str = None,
        task_status: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.id = id
        self.task_id = task_id
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.id is not None:
            result['Id'] = self.id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        return self

