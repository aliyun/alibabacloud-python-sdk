# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateFaqShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        category_id: int = None,
        end_date: str = None,
        knowledge_id: int = None,
        start_date: str = None,
        tag_id_list_shrink: str = None,
        title: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.category_id = category_id
        self.end_date = end_date
        # This parameter is required.
        self.knowledge_id = knowledge_id
        self.start_date = start_date
        self.tag_id_list_shrink = tag_id_list_shrink
        # This parameter is required.
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

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.tag_id_list_shrink is not None:
            result['TagIdList'] = self.tag_id_list_shrink

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('TagIdList') is not None:
            self.tag_id_list_shrink = m.get('TagIdList')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

