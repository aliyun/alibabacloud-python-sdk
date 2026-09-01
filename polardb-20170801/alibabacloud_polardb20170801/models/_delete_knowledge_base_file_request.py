# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteKnowledgeBaseFileRequest(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        knowledge_base_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.file_id = file_id
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

