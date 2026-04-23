# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfirmInventoryKnowledgeRequest(DaraModel):
    def __init__(
        self,
        entity_id: int = None,
        job_id: int = None,
        knowledge_type: str = None,
    ):
        # This parameter is required.
        self.entity_id = entity_id
        # This parameter is required.
        self.job_id = job_id
        # This parameter is required.
        self.knowledge_type = knowledge_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.knowledge_type is not None:
            result['KnowledgeType'] = self.knowledge_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('KnowledgeType') is not None:
            self.knowledge_type = m.get('KnowledgeType')

        return self

