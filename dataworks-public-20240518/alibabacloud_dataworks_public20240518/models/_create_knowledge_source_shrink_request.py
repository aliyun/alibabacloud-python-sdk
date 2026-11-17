# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKnowledgeSourceShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        data_source_shrink: str = None,
        description: str = None,
        document_shrink: str = None,
        knowledge_base_id: str = None,
        name: str = None,
        project_shrink: str = None,
        type: str = None,
    ):
        # The client token used to ensure idempotence.
        self.client_token = client_token
        # The data source configuration. This parameter is required when Type is set to DATA_SOURCE.
        self.data_source_shrink = data_source_shrink
        # The description.
        self.description = description
        # The document configuration. This parameter is required when Type is set to DOCUMENT.
        self.document_shrink = document_shrink
        # The ID of the knowledge base.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The name of the source.
        # 
        # This parameter is required.
        self.name = name
        # The project configuration. This parameter is required when Type is set to PROJECT.
        self.project_shrink = project_shrink
        # The type of the knowledge source. Valid values: PROJECT, DATA_SOURCE, and DOCUMENT.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

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

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

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

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

