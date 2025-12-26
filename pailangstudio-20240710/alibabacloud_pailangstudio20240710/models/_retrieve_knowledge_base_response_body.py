# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pailangstudio20240710 import models as main_models
from darabonba.model import DaraModel

class RetrieveKnowledgeBaseResponseBody(DaraModel):
    def __init__(
        self,
        knowledge_base_file_chunks: List[main_models.KnowledgeBaseFileChunk] = None,
    ):
        self.knowledge_base_file_chunks = knowledge_base_file_chunks

    def validate(self):
        if self.knowledge_base_file_chunks:
            for v1 in self.knowledge_base_file_chunks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KnowledgeBaseFileChunks'] = []
        if self.knowledge_base_file_chunks is not None:
            for k1 in self.knowledge_base_file_chunks:
                result['KnowledgeBaseFileChunks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.knowledge_base_file_chunks = []
        if m.get('KnowledgeBaseFileChunks') is not None:
            for k1 in m.get('KnowledgeBaseFileChunks'):
                temp_model = main_models.KnowledgeBaseFileChunk()
                self.knowledge_base_file_chunks.append(temp_model.from_map(k1))

        return self

