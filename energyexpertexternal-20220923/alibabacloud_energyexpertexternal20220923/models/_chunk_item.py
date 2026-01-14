# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ChunkItem(DaraModel):
    def __init__(
        self,
        chunk_content: str = None,
        chunk_id: str = None,
        doc_els_ids: List[str] = None,
        doc_id: str = None,
        doc_name: str = None,
        doc_url: str = None,
        rerank_score: float = None,
        score: float = None,
        weighted_score: float = None,
    ):
        self.chunk_content = chunk_content
        self.chunk_id = chunk_id
        self.doc_els_ids = doc_els_ids
        self.doc_id = doc_id
        self.doc_name = doc_name
        self.doc_url = doc_url
        self.rerank_score = rerank_score
        self.score = score
        self.weighted_score = weighted_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_content is not None:
            result['chunkContent'] = self.chunk_content

        if self.chunk_id is not None:
            result['chunkId'] = self.chunk_id

        if self.doc_els_ids is not None:
            result['docElsIds'] = self.doc_els_ids

        if self.doc_id is not None:
            result['docId'] = self.doc_id

        if self.doc_name is not None:
            result['docName'] = self.doc_name

        if self.doc_url is not None:
            result['docUrl'] = self.doc_url

        if self.rerank_score is not None:
            result['rerankScore'] = self.rerank_score

        if self.score is not None:
            result['score'] = self.score

        if self.weighted_score is not None:
            result['weightedScore'] = self.weighted_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkContent') is not None:
            self.chunk_content = m.get('chunkContent')

        if m.get('chunkId') is not None:
            self.chunk_id = m.get('chunkId')

        if m.get('docElsIds') is not None:
            self.doc_els_ids = m.get('docElsIds')

        if m.get('docId') is not None:
            self.doc_id = m.get('docId')

        if m.get('docName') is not None:
            self.doc_name = m.get('docName')

        if m.get('docUrl') is not None:
            self.doc_url = m.get('docUrl')

        if m.get('rerankScore') is not None:
            self.rerank_score = m.get('rerankScore')

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('weightedScore') is not None:
            self.weighted_score = m.get('weightedScore')

        return self

