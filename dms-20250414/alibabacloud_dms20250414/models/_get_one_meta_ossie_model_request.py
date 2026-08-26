# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOneMetaOssieModelRequest(DaraModel):
    def __init__(
        self,
        doc_format: str = None,
        knowledge_uuid: str = None,
    ):
        # The document type of the semantic model. Valid values: JSON and YAML.
        # 
        # This parameter is required.
        self.doc_format = doc_format
        # The UUID of the knowledge base.
        # 
        # This parameter is required.
        self.knowledge_uuid = knowledge_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_format is not None:
            result['DocFormat'] = self.doc_format

        if self.knowledge_uuid is not None:
            result['KnowledgeUuid'] = self.knowledge_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocFormat') is not None:
            self.doc_format = m.get('DocFormat')

        if m.get('KnowledgeUuid') is not None:
            self.knowledge_uuid = m.get('KnowledgeUuid')

        return self

