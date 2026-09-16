# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class KnowledgeBaseChunk(DaraModel):
    def __init__(
        self,
        chunk_seq: int = None,
        chunk_size: int = None,
        content: str = None,
        created_at: str = None,
        document_id: str = None,
        enabled: bool = None,
        file_name: str = None,
        source_location: str = None,
        title_path: str = None,
        updated_at: str = None,
    ):
        # The sequence number of the chunk within the document, starting from 1 and numbered consecutively.
        self.chunk_seq = chunk_seq
        # The number of characters in the chunk content, measured in UTF-16 code units, consistent with MaxChunkSize. You can use this value to evaluate chunk saturation against the chunking configuration.
        self.chunk_size = chunk_size
        # The content of the chunk.
        self.content = content
        # The time when the chunk was created.
        self.created_at = created_at
        # The ID of the document to which the chunk belongs.
        self.document_id = document_id
        # Indicates whether the chunk is enabled. Disabled chunks are excluded from retrieval.
        self.enabled = enabled
        # The file name of the document to which the chunk belongs. This value is from the same source as the FileName returned by GetDocument.
        self.file_name = file_name
        # The location of the chunk in the original document. The format varies by document type: for PDF, the value is p.PageNumber (such as p.3). For PPT/PPTX, the value is s.SlideNumber (such as s.2). For XLS/XLSX, the value is the sheet name. For other formats (such as txt, md, html, doc, or docx), this field is not returned if no source location is available.
        self.source_location = source_location
        # The hierarchical title path of the chunk, connected by >. If no recognizable title exists in the original document, the value falls back to a summary of the first paragraph content (such as CONTENT). This field is for display purposes only.
        self.title_path = title_path
        # The time when the chunk was last updated.
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_seq is not None:
            result['ChunkSeq'] = self.chunk_seq

        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size

        if self.content is not None:
            result['Content'] = self.content

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.document_id is not None:
            result['DocumentId'] = self.document_id

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.source_location is not None:
            result['SourceLocation'] = self.source_location

        if self.title_path is not None:
            result['TitlePath'] = self.title_path

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkSeq') is not None:
            self.chunk_seq = m.get('ChunkSeq')

        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('DocumentId') is not None:
            self.document_id = m.get('DocumentId')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('SourceLocation') is not None:
            self.source_location = m.get('SourceLocation')

        if m.get('TitlePath') is not None:
            self.title_path = m.get('TitlePath')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

