# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateKnowledgeBaseChunkRequest(DaraModel):
    def __init__(
        self,
        chunk_content: str = None,
        chunk_status: str = None,
    ):
        self.chunk_content = chunk_content
        self.chunk_status = chunk_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_content is not None:
            result['ChunkContent'] = self.chunk_content

        if self.chunk_status is not None:
            result['ChunkStatus'] = self.chunk_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkContent') is not None:
            self.chunk_content = m.get('ChunkContent')

        if m.get('ChunkStatus') is not None:
            self.chunk_status = m.get('ChunkStatus')

        return self

