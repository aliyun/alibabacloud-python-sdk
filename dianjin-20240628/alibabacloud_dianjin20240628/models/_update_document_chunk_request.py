# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class UpdateDocumentChunkRequest(DaraModel):
    def __init__(
        self,
        chunks: List[main_models.UpdateDocumentChunkRequestChunks] = None,
        library_id: str = None,
    ):
        # This parameter is required.
        self.chunks = chunks
        # This parameter is required.
        self.library_id = library_id

    def validate(self):
        if self.chunks:
            for v1 in self.chunks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['chunks'] = []
        if self.chunks is not None:
            for k1 in self.chunks:
                result['chunks'].append(k1.to_map() if k1 else None)

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chunks = []
        if m.get('chunks') is not None:
            for k1 in m.get('chunks'):
                temp_model = main_models.UpdateDocumentChunkRequestChunks()
                self.chunks.append(temp_model.from_map(k1))

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        return self

class UpdateDocumentChunkRequestChunks(DaraModel):
    def __init__(
        self,
        chunk_id: str = None,
        chunk_text: str = None,
    ):
        # This parameter is required.
        self.chunk_id = chunk_id
        # This parameter is required.
        self.chunk_text = chunk_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_id is not None:
            result['chunkId'] = self.chunk_id

        if self.chunk_text is not None:
            result['chunkText'] = self.chunk_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkId') is not None:
            self.chunk_id = m.get('chunkId')

        if m.get('chunkText') is not None:
            self.chunk_text = m.get('chunkText')

        return self

