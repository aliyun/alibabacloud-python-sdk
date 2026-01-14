# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteChunkRequest(DaraModel):
    def __init__(
        self,
        chunk_ids: List[str] = None,
        pipeline_id: str = None,
    ):
        # The list of text chunks to be deleted. You can specify up to 10 chunk IDs at a time.
        # 
        # This parameter is required.
        self.chunk_ids = chunk_ids
        # The knowledge base ID, which is the `Data.Id` parameter returned by **CreateIndex**.
        # 
        # This parameter is required.
        self.pipeline_id = pipeline_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_ids is not None:
            result['ChunkIds'] = self.chunk_ids

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkIds') is not None:
            self.chunk_ids = m.get('ChunkIds')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        return self

