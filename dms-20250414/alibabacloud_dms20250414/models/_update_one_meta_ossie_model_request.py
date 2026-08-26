# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateOneMetaOssieModelRequest(DaraModel):
    def __init__(
        self,
        catalog_uuid: str = None,
        database_uuid: str = None,
        description: str = None,
        doc_format: str = None,
        document: str = None,
        knowledge_uuid: str = None,
        tag: str = None,
        title: str = None,
    ):
        # The UUID of the associated folder.
        self.catalog_uuid = catalog_uuid
        # The UUID of the associated database.
        self.database_uuid = database_uuid
        # The semantic description.
        self.description = description
        # The document type of the semantic model. Valid values:
        # 
        # - JSON
        # - YAML
        self.doc_format = doc_format
        # The document definition of the semantic model.
        self.document = document
        # The UUID of the knowledge.
        # 
        # This parameter is required.
        self.knowledge_uuid = knowledge_uuid
        # The tag of the semantic model.
        self.tag = tag
        # The semantic title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_uuid is not None:
            result['CatalogUuid'] = self.catalog_uuid

        if self.database_uuid is not None:
            result['DatabaseUuid'] = self.database_uuid

        if self.description is not None:
            result['Description'] = self.description

        if self.doc_format is not None:
            result['DocFormat'] = self.doc_format

        if self.document is not None:
            result['Document'] = self.document

        if self.knowledge_uuid is not None:
            result['KnowledgeUuid'] = self.knowledge_uuid

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogUuid') is not None:
            self.catalog_uuid = m.get('CatalogUuid')

        if m.get('DatabaseUuid') is not None:
            self.database_uuid = m.get('DatabaseUuid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DocFormat') is not None:
            self.doc_format = m.get('DocFormat')

        if m.get('Document') is not None:
            self.document = m.get('Document')

        if m.get('KnowledgeUuid') is not None:
            self.knowledge_uuid = m.get('KnowledgeUuid')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

