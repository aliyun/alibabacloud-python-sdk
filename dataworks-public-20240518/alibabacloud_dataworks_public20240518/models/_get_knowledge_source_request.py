# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetKnowledgeSourceRequest(DaraModel):
    def __init__(
        self,
        knowledge_base_id: str = None,
        source_id: str = None,
    ):
        # The ID of the knowledge base to which the source belongs.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The source ID.
        # 
        # This parameter is required.
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        return self

