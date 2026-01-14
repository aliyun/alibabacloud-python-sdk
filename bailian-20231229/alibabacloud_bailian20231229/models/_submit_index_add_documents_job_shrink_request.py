# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitIndexAddDocumentsJobShrinkRequest(DaraModel):
    def __init__(
        self,
        category_ids_shrink: str = None,
        chunk_mode: str = None,
        chunk_size: int = None,
        document_ids_shrink: str = None,
        enable_headers: bool = None,
        index_id: str = None,
        overlap_size: int = None,
        separator: str = None,
        source_type: str = None,
    ):
        # The list of primary key IDs of the category.
        self.category_ids_shrink = category_ids_shrink
        self.chunk_mode = chunk_mode
        self.chunk_size = chunk_size
        # The list of the primary key IDs of the documents.
        self.document_ids_shrink = document_ids_shrink
        self.enable_headers = enable_headers
        # The primary key ID of the knowledge base, which is the `Data.Id` parameter returned by the [CreateIndex](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-createindex) operation.
        # 
        # This parameter is required.
        self.index_id = index_id
        self.overlap_size = overlap_size
        self.separator = separator
        # The data type of [Data Management](https://bailian.console.aliyun.com/#/data-center). For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values:
        # 
        # *   DATA_CENTER_CATEGORY: The category type. Import all documents from one or more categories in Data Center.
        # *   DATA_CENTER_FILE: The document type. Import one or more documents from Data Center.
        # 
        # >  If this parameter is set to DATA_CENTER_CATEGORY, you must specify the `CategoryIds` parameter. If this parameter is set to DATA_CENTER_FILE, you must specify the `DocumentIds` parameter.
        # 
        # This parameter is required.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_ids_shrink is not None:
            result['CategoryIds'] = self.category_ids_shrink

        if self.chunk_mode is not None:
            result['ChunkMode'] = self.chunk_mode

        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size

        if self.document_ids_shrink is not None:
            result['DocumentIds'] = self.document_ids_shrink

        if self.enable_headers is not None:
            result['EnableHeaders'] = self.enable_headers

        if self.index_id is not None:
            result['IndexId'] = self.index_id

        if self.overlap_size is not None:
            result['OverlapSize'] = self.overlap_size

        if self.separator is not None:
            result['Separator'] = self.separator

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryIds') is not None:
            self.category_ids_shrink = m.get('CategoryIds')

        if m.get('ChunkMode') is not None:
            self.chunk_mode = m.get('ChunkMode')

        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')

        if m.get('DocumentIds') is not None:
            self.document_ids_shrink = m.get('DocumentIds')

        if m.get('EnableHeaders') is not None:
            self.enable_headers = m.get('EnableHeaders')

        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')

        if m.get('OverlapSize') is not None:
            self.overlap_size = m.get('OverlapSize')

        if m.get('Separator') is not None:
            self.separator = m.get('Separator')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

