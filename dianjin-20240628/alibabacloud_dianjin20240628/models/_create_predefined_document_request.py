# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class CreatePredefinedDocumentRequest(DaraModel):
    def __init__(
        self,
        chunks: List[main_models.CreatePredefinedDocumentRequestChunks] = None,
        library_id: str = None,
        metadata: Dict[str, Any] = None,
        title: str = None,
    ):
        self.chunks = chunks
        self.library_id = library_id
        self.metadata = metadata
        self.title = title

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

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chunks = []
        if m.get('chunks') is not None:
            for k1 in m.get('chunks'):
                temp_model = main_models.CreatePredefinedDocumentRequestChunks()
                self.chunks.append(temp_model.from_map(k1))

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class CreatePredefinedDocumentRequestChunks(DaraModel):
    def __init__(
        self,
        chunk_meta: Dict[str, Any] = None,
        chunk_order: int = None,
        chunk_text: str = None,
        chunk_type: str = None,
    ):
        self.chunk_meta = chunk_meta
        self.chunk_order = chunk_order
        self.chunk_text = chunk_text
        self.chunk_type = chunk_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_meta is not None:
            result['chunkMeta'] = self.chunk_meta

        if self.chunk_order is not None:
            result['chunkOrder'] = self.chunk_order

        if self.chunk_text is not None:
            result['chunkText'] = self.chunk_text

        if self.chunk_type is not None:
            result['chunkType'] = self.chunk_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkMeta') is not None:
            self.chunk_meta = m.get('chunkMeta')

        if m.get('chunkOrder') is not None:
            self.chunk_order = m.get('chunkOrder')

        if m.get('chunkText') is not None:
            self.chunk_text = m.get('chunkText')

        if m.get('chunkType') is not None:
            self.chunk_type = m.get('chunkType')

        return self

