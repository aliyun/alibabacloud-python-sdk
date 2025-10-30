# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDocumentResponseBody(DaraModel):
    def __init__(
        self,
        chunk_file_url: str = None,
        docs_count: int = None,
        document_loader: str = None,
        document_loader_result_file_url: str = None,
        file_ext: str = None,
        file_md_5: str = None,
        file_mtime: str = None,
        file_name: str = None,
        file_size: int = None,
        file_url: str = None,
        file_version: int = None,
        message: str = None,
        plain_chunk_file_url: str = None,
        request_id: str = None,
        source: str = None,
        status: str = None,
        text_splitter: str = None,
    ):
        # URL of the split file, valid for 2 hours. The file format is JSONL, with each line formatted as `{"page_content":"*****", "metadata": {"**":"***","**":"***"}`.
        self.chunk_file_url = chunk_file_url
        # Number of documents after splitting.
        self.docs_count = docs_count
        # Name of the document loader.
        self.document_loader = document_loader
        self.document_loader_result_file_url = document_loader_result_file_url
        # File extension.
        self.file_ext = file_ext
        # MD5 value of the file.
        self.file_md_5 = file_md_5
        # The last modified time of the document.
        self.file_mtime = file_mtime
        # File name.
        self.file_name = file_name
        # File size, in bytes.
        self.file_size = file_size
        # Download URL of the document, valid for 2 hours.
        self.file_url = file_url
        # Document version. This value increments by 1 each time the same document is updated and uploaded.
        self.file_version = file_version
        # Detailed information returned by the API.
        self.message = message
        # Download URL for the plain text (without metadata) after splitting, each line is a chunk, valid for 2 hours.
        self.plain_chunk_file_url = plain_chunk_file_url
        # Request ID.
        self.request_id = request_id
        # Source of the document.
        self.source = source
        # API execution status, with values as follows:
        # - **success**: Execution succeeded.
        # - **fail**: Execution failed.
        self.status = status
        # Name of the text splitter.
        self.text_splitter = text_splitter

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_file_url is not None:
            result['ChunkFileUrl'] = self.chunk_file_url

        if self.docs_count is not None:
            result['DocsCount'] = self.docs_count

        if self.document_loader is not None:
            result['DocumentLoader'] = self.document_loader

        if self.document_loader_result_file_url is not None:
            result['DocumentLoaderResultFileUrl'] = self.document_loader_result_file_url

        if self.file_ext is not None:
            result['FileExt'] = self.file_ext

        if self.file_md_5 is not None:
            result['FileMd5'] = self.file_md_5

        if self.file_mtime is not None:
            result['FileMtime'] = self.file_mtime

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.file_version is not None:
            result['FileVersion'] = self.file_version

        if self.message is not None:
            result['Message'] = self.message

        if self.plain_chunk_file_url is not None:
            result['PlainChunkFileUrl'] = self.plain_chunk_file_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.text_splitter is not None:
            result['TextSplitter'] = self.text_splitter

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkFileUrl') is not None:
            self.chunk_file_url = m.get('ChunkFileUrl')

        if m.get('DocsCount') is not None:
            self.docs_count = m.get('DocsCount')

        if m.get('DocumentLoader') is not None:
            self.document_loader = m.get('DocumentLoader')

        if m.get('DocumentLoaderResultFileUrl') is not None:
            self.document_loader_result_file_url = m.get('DocumentLoaderResultFileUrl')

        if m.get('FileExt') is not None:
            self.file_ext = m.get('FileExt')

        if m.get('FileMd5') is not None:
            self.file_md_5 = m.get('FileMd5')

        if m.get('FileMtime') is not None:
            self.file_mtime = m.get('FileMtime')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('FileVersion') is not None:
            self.file_version = m.get('FileVersion')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PlainChunkFileUrl') is not None:
            self.plain_chunk_file_url = m.get('PlainChunkFileUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TextSplitter') is not None:
            self.text_splitter = m.get('TextSplitter')

        return self

