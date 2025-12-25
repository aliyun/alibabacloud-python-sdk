# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class FetchImageTaskRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        article_task_id: str = None,
        task_id_list: List[str] = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.article_task_id = article_task_id
        # This parameter is required.
        self.task_id_list = task_id_list

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

        if self.task_id_list is not None:
            result['TaskIdList'] = self.task_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('ArticleTaskId') is not None:
            self.article_task_id = m.get('ArticleTaskId')

        if m.get('TaskIdList') is not None:
            self.task_id_list = m.get('TaskIdList')

        return self

