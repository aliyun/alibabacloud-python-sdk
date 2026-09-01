# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateKnowledgeSpaceResponseBody(DaraModel):
    def __init__(
        self,
        knowledge_space_id: str = None,
        request_id: str = None,
        task_id: int = None,
    ):
        self.knowledge_space_id = knowledge_space_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.knowledge_space_id is not None:
            result['KnowledgeSpaceId'] = self.knowledge_space_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeSpaceId') is not None:
            self.knowledge_space_id = m.get('KnowledgeSpaceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

