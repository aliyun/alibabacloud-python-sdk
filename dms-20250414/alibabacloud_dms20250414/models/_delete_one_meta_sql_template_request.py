# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteOneMetaSqlTemplateRequest(DaraModel):
    def __init__(
        self,
        knowledge_uuid: str = None,
    ):
        # The UUID of the knowledge base.
        # 
        # This parameter is required.
        self.knowledge_uuid = knowledge_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.knowledge_uuid is not None:
            result['KnowledgeUuid'] = self.knowledge_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeUuid') is not None:
            self.knowledge_uuid = m.get('KnowledgeUuid')

        return self

