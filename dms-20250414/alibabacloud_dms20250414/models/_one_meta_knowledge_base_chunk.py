# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OneMetaKnowledgeBaseChunk(DaraModel):
    def __init__(
        self,
        chunk_mtime: str = None,
        chunk_title: str = None,
        content: str = None,
        doc_name: str = None,
        id: str = None,
    ):
        self.chunk_mtime = chunk_mtime
        self.chunk_title = chunk_title
        self.content = content
        self.doc_name = doc_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_mtime is not None:
            result['ChunkMtime'] = self.chunk_mtime

        if self.chunk_title is not None:
            result['ChunkTitle'] = self.chunk_title

        if self.content is not None:
            result['Content'] = self.content

        if self.doc_name is not None:
            result['DocName'] = self.doc_name

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkMtime') is not None:
            self.chunk_mtime = m.get('ChunkMtime')

        if m.get('ChunkTitle') is not None:
            self.chunk_title = m.get('ChunkTitle')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

