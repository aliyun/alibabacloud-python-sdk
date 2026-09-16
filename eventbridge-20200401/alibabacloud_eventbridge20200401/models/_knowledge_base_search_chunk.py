# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class KnowledgeBaseSearchChunk(DaraModel):
    def __init__(
        self,
        chunk_seq: int = None,
        content: str = None,
        document_id: str = None,
        file_name: str = None,
        score: float = None,
        scores: main_models.KnowledgeBaseSearchChunkScores = None,
        source_location: str = None,
        title_path: str = None,
    ):
        # The sequence number of the chunk within the document.
        self.chunk_seq = chunk_seq
        # The body content of the hit chunk.
        self.content = content
        # The ID of the document to which the hit chunk belongs.
        self.document_id = document_id
        # The file name of the document to which the hit chunk belongs. This value has the same source as the FileName returned by GetDocument and can be used to render the reference source.
        self.file_name = file_name
        # The retrieval relevance score. A higher score indicates higher relevance.
        self.score = score
        # The score details for each stage. Score fields that are not involved in the calculation are not returned.
        self.scores = scores
        # The location of the chunk in the original document. p.N indicates page N (PDF). s.N indicates slide N (PPT/PPTX).
        self.source_location = source_location
        # The title path to which the chunk belongs, such as Chapter 1>1.1 Overview.
        self.title_path = title_path

    def validate(self):
        if self.scores:
            self.scores.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_seq is not None:
            result['ChunkSeq'] = self.chunk_seq

        if self.content is not None:
            result['Content'] = self.content

        if self.document_id is not None:
            result['DocumentId'] = self.document_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.score is not None:
            result['Score'] = self.score

        if self.scores is not None:
            result['Scores'] = self.scores.to_map()

        if self.source_location is not None:
            result['SourceLocation'] = self.source_location

        if self.title_path is not None:
            result['TitlePath'] = self.title_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkSeq') is not None:
            self.chunk_seq = m.get('ChunkSeq')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DocumentId') is not None:
            self.document_id = m.get('DocumentId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Scores') is not None:
            temp_model = main_models.KnowledgeBaseSearchChunkScores()
            self.scores = temp_model.from_map(m.get('Scores'))

        if m.get('SourceLocation') is not None:
            self.source_location = m.get('SourceLocation')

        if m.get('TitlePath') is not None:
            self.title_path = m.get('TitlePath')

        return self

class KnowledgeBaseSearchChunkScores(DaraModel):
    def __init__(
        self,
        fusion: float = None,
        keyword: float = None,
        rerank: float = None,
        vector: float = None,
    ):
        # The score after hybrid search fusion (reciprocal rank fusion or weighted normalization, depending on the active fusion algorithm). Value range: [0, 1].
        self.fusion = fusion
        # The normalized score of keyword (full-text) search. Value range: [0, 1].
        self.keyword = keyword
        # The score assigned by the rerank model. Value range: [0, 1].
        self.rerank = rerank
        # The similarity score of vector retrieval. Value range: [0, 1].
        self.vector = vector

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fusion is not None:
            result['Fusion'] = self.fusion

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.rerank is not None:
            result['Rerank'] = self.rerank

        if self.vector is not None:
            result['Vector'] = self.vector

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fusion') is not None:
            self.fusion = m.get('Fusion')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Rerank') is not None:
            self.rerank = m.get('Rerank')

        if m.get('Vector') is not None:
            self.vector = m.get('Vector')

        return self

