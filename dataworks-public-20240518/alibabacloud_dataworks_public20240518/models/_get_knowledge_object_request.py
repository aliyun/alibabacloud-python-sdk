# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetKnowledgeObjectRequest(DaraModel):
    def __init__(
        self,
        knowledge_base_id: str = None,
        knowledge_object_id: str = None,
        version_no: int = None,
    ):
        # The ID of the knowledge base.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The ID of the long-term business object.
        # 
        # This parameter is required.
        self.knowledge_object_id = knowledge_object_id
        # Applies only to semantic models. Specifies the version to read. If omitted, the operation returns the published version if available, or the latest version otherwise.
        self.version_no = version_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.knowledge_object_id is not None:
            result['KnowledgeObjectId'] = self.knowledge_object_id

        if self.version_no is not None:
            result['VersionNo'] = self.version_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('KnowledgeObjectId') is not None:
            self.knowledge_object_id = m.get('KnowledgeObjectId')

        if m.get('VersionNo') is not None:
            self.version_no = m.get('VersionNo')

        return self

