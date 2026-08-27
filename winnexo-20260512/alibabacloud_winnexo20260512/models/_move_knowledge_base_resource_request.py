# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MoveKnowledgeBaseResourceRequest(DaraModel):
    def __init__(
        self,
        knowledge_id: str = None,
        source_directory_id: str = None,
        source_id: str = None,
        target_directory_id: str = None,
        tenant_id: str = None,
    ):
        # Not supported. This parameter is ignored.
        # 
        # This parameter is required.
        self.knowledge_id = knowledge_id
        # The source directory ID. This is the enterprise knowledge base directory where the resource currently resides.
        # 
        # This parameter is required.
        self.source_directory_id = source_directory_id
        # The data source ID.
        # 
        # This parameter is required.
        self.source_id = source_id
        # The target directory ID.
        # 
        # This parameter is required.
        self.target_directory_id = target_directory_id
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.knowledge_id is not None:
            result['knowledgeId'] = self.knowledge_id

        if self.source_directory_id is not None:
            result['sourceDirectoryId'] = self.source_directory_id

        if self.source_id is not None:
            result['sourceId'] = self.source_id

        if self.target_directory_id is not None:
            result['targetDirectoryId'] = self.target_directory_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('knowledgeId') is not None:
            self.knowledge_id = m.get('knowledgeId')

        if m.get('sourceDirectoryId') is not None:
            self.source_directory_id = m.get('sourceDirectoryId')

        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')

        if m.get('targetDirectoryId') is not None:
            self.target_directory_id = m.get('targetDirectoryId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

