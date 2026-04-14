# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OneMetaKnowledgeBaseDocument(DaraModel):
    def __init__(
        self,
        description: str = None,
        docs_count: int = None,
        document_loader_name: str = None,
        file_ext: str = None,
        file_size: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        kb_uuid: str = None,
        keywords: str = None,
        name: str = None,
        state: int = None,
        summary: str = None,
        text_splitter_name: str = None,
    ):
        self.description = description
        self.docs_count = docs_count
        self.document_loader_name = document_loader_name
        self.file_ext = file_ext
        self.file_size = file_size
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.kb_uuid = kb_uuid
        self.keywords = keywords
        self.name = name
        self.state = state
        self.summary = summary
        self.text_splitter_name = text_splitter_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.docs_count is not None:
            result['DocsCount'] = self.docs_count

        if self.document_loader_name is not None:
            result['DocumentLoaderName'] = self.document_loader_name

        if self.file_ext is not None:
            result['FileExt'] = self.file_ext

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.kb_uuid is not None:
            result['KbUuid'] = self.kb_uuid

        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.name is not None:
            result['Name'] = self.name

        if self.state is not None:
            result['State'] = self.state

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.text_splitter_name is not None:
            result['TextSplitterName'] = self.text_splitter_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DocsCount') is not None:
            self.docs_count = m.get('DocsCount')

        if m.get('DocumentLoaderName') is not None:
            self.document_loader_name = m.get('DocumentLoaderName')

        if m.get('FileExt') is not None:
            self.file_ext = m.get('FileExt')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('KbUuid') is not None:
            self.kb_uuid = m.get('KbUuid')

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('TextSplitterName') is not None:
            self.text_splitter_name = m.get('TextSplitterName')

        return self

