# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDocResponseBody(DaraModel):
    def __init__(
        self,
        knowledge_id: int = None,
        request_id: str = None,
    ):
        self.knowledge_id = knowledge_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.knowledge_id is not None:
            result['KnowledgeId'] = self.knowledge_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeId') is not None:
            self.knowledge_id = m.get('KnowledgeId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

