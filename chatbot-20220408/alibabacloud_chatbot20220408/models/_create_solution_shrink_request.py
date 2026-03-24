# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateSolutionShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        content_type: int = None,
        knowledge_id: int = None,
        perspective_codes: List[str] = None,
        tag_id_list_shrink: str = None,
    ):
        self.agent_key = agent_key
        # This parameter is required.
        self.content = content
        self.content_type = content_type
        # This parameter is required.
        self.knowledge_id = knowledge_id
        # This parameter is required.
        self.perspective_codes = perspective_codes
        self.tag_id_list_shrink = tag_id_list_shrink

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

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id

        if self.perspective_codes is not None:
            result['PerspectiveCodes'] = self.perspective_codes

        if self.tag_id_list_shrink is not None:
            result['TagIdList'] = self.tag_id_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')

        if m.get('PerspectiveCodes') is not None:
            self.perspective_codes = m.get('PerspectiveCodes')

        if m.get('TagIdList') is not None:
            self.tag_id_list_shrink = m.get('TagIdList')

        return self

