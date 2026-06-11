# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadDocumentShrinkRequest(DaraModel):
    def __init__(
        self,
        chunk_overlap: int = None,
        chunk_size: int = None,
        description: str = None,
        document_loader_name: str = None,
        file_name: str = None,
        kb_uuid: str = None,
        location: str = None,
        separators_shrink: str = None,
        splitter_model: str = None,
        text_splitter_name: str = None,
        vl_enhance: bool = None,
        zh_title_enhance: bool = None,
    ):
        # The number of overlapping characters between adjacent chunks. This value cannot exceed `ChunkSize`. The default is 50.
        self.chunk_overlap = chunk_overlap
        # The size of each document chunk. The default is 250, and the maximum is 2,048.
        self.chunk_size = chunk_size
        # The description of the document.
        self.description = description
        # The name of the document loader. The default is `ADBPGLoader`.
        self.document_loader_name = document_loader_name
        # The name of the document.
        # 
        # This parameter is required.
        self.file_name = file_name
        # The ID of the knowledge base.
        # 
        # This parameter is required.
        self.kb_uuid = kb_uuid
        # The OSS location of the input file. Construct this path by appending the file name to the `UploadDir` value returned by the `DescribeKnowledgeBaseUploadSignature` operation.
        # 
        # This parameter is required.
        self.location = location
        # An array of strings used to split text.
        # 
        # > - This critical parameter affects data chunking results and is related to the splitter specified by `TextSplitterName`.
        # >
        # > - In most cases, you can omit this parameter. The service automatically assigns default separators based on `TextSplitterName`.
        self.separators_shrink = separators_shrink
        # The splitter model to use. The default is `qwen3-8b`.
        self.splitter_model = splitter_model
        # The name of the text splitter.
        self.text_splitter_name = text_splitter_name
        # Specifies whether to enable visual-linguistic (VL) enhanced content recognition for complex documents. The default is false.
        self.vl_enhance = vl_enhance
        # Specifies whether to enable title enhancement.
        self.zh_title_enhance = zh_title_enhance

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_overlap is not None:
            result['ChunkOverlap'] = self.chunk_overlap

        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size

        if self.description is not None:
            result['Description'] = self.description

        if self.document_loader_name is not None:
            result['DocumentLoaderName'] = self.document_loader_name

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.kb_uuid is not None:
            result['KbUuid'] = self.kb_uuid

        if self.location is not None:
            result['Location'] = self.location

        if self.separators_shrink is not None:
            result['Separators'] = self.separators_shrink

        if self.splitter_model is not None:
            result['SplitterModel'] = self.splitter_model

        if self.text_splitter_name is not None:
            result['TextSplitterName'] = self.text_splitter_name

        if self.vl_enhance is not None:
            result['VlEnhance'] = self.vl_enhance

        if self.zh_title_enhance is not None:
            result['ZhTitleEnhance'] = self.zh_title_enhance

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkOverlap') is not None:
            self.chunk_overlap = m.get('ChunkOverlap')

        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DocumentLoaderName') is not None:
            self.document_loader_name = m.get('DocumentLoaderName')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('KbUuid') is not None:
            self.kb_uuid = m.get('KbUuid')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Separators') is not None:
            self.separators_shrink = m.get('Separators')

        if m.get('SplitterModel') is not None:
            self.splitter_model = m.get('SplitterModel')

        if m.get('TextSplitterName') is not None:
            self.text_splitter_name = m.get('TextSplitterName')

        if m.get('VlEnhance') is not None:
            self.vl_enhance = m.get('VlEnhance')

        if m.get('ZhTitleEnhance') is not None:
            self.zh_title_enhance = m.get('ZhTitleEnhance')

        return self

