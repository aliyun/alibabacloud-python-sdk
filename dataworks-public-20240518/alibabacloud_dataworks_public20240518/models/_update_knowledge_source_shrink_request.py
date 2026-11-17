# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateKnowledgeSourceShrinkRequest(DaraModel):
    def __init__(
        self,
        data_source_shrink: str = None,
        description: str = None,
        document_shrink: str = None,
        knowledge_base_id: str = None,
        name: str = None,
        project_shrink: str = None,
        source_id: str = None,
    ):
        # The complete configuration for Type=DATA_SOURCE.
        self.data_source_shrink = data_source_shrink
        # The new description.
        self.description = description
        # The complete configuration for Type=DOCUMENT. Credentials are not returned after they are written.
        self.document_shrink = document_shrink
        # The ID of the knowledge base to which the source belongs.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The new name.
        self.name = name
        # The complete configuration for Type=PROJECT.
        self.project_shrink = project_shrink
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
        if self.data_source_shrink is not None:
            result['DataSource'] = self.data_source_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.document_shrink is not None:
            result['Document'] = self.document_shrink

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.name is not None:
            result['Name'] = self.name

        if self.project_shrink is not None:
            result['Project'] = self.project_shrink

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSource') is not None:
            self.data_source_shrink = m.get('DataSource')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Document') is not None:
            self.document_shrink = m.get('Document')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Project') is not None:
            self.project_shrink = m.get('Project')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        return self

