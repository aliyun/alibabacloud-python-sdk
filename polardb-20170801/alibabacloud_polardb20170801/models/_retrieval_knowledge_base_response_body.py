# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class RetrievalKnowledgeBaseResponseBody(DaraModel):
    def __init__(
        self,
        query_text: str = None,
        request_id: str = None,
        result_count: int = None,
        results: List[main_models.RetrievalKnowledgeBaseResponseBodyResults] = None,
    ):
        # The query text.
        self.query_text = query_text
        # Id of the request
        self.request_id = request_id
        # The number of results.
        self.result_count = result_count
        # The search results.
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query_text is not None:
            result['QueryText'] = self.query_text

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_count is not None:
            result['ResultCount'] = self.result_count

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryText') is not None:
            self.query_text = m.get('QueryText')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCount') is not None:
            self.result_count = m.get('ResultCount')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.RetrievalKnowledgeBaseResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self

class RetrievalKnowledgeBaseResponseBodyResults(DaraModel):
    def __init__(
        self,
        captions: List[str] = None,
        doc_items: List[str] = None,
        file_id: str = None,
        file_name: str = None,
        headings: List[str] = None,
        image_resources: List[main_models.RetrievalKnowledgeBaseResponseBodyResultsImageResources] = None,
        metadata: str = None,
        page_numbers: List[int] = None,
        shard_content: str = None,
        shard_index: int = None,
        similarity_score: float = None,
    ):
        # The list of figure or table captions associated with the chunk.
        self.captions = captions
        # The list of Docling source document structured element references associated with the chunk. You can use these references to precisely locate elements in the original document.
        self.doc_items = doc_items
        # The unique identifier of the file.
        self.file_id = file_id
        # The name of the file.
        self.file_name = file_name
        # The chain of section headings to which the chunk belongs.
        self.headings = headings
        # The list of image resources referenced by the chunk.
        self.image_resources = image_resources
        # The metadata.
        self.metadata = metadata
        # The list of page numbers to which the chunk belongs.
        self.page_numbers = page_numbers
        # The text content of the chunk.
        self.shard_content = shard_content
        # The index of the chunk.
        self.shard_index = shard_index
        # The similarity score.
        self.similarity_score = similarity_score

    def validate(self):
        if self.image_resources:
            for v1 in self.image_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.captions is not None:
            result['Captions'] = self.captions

        if self.doc_items is not None:
            result['DocItems'] = self.doc_items

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.headings is not None:
            result['Headings'] = self.headings

        result['ImageResources'] = []
        if self.image_resources is not None:
            for k1 in self.image_resources:
                result['ImageResources'].append(k1.to_map() if k1 else None)

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers

        if self.shard_content is not None:
            result['ShardContent'] = self.shard_content

        if self.shard_index is not None:
            result['ShardIndex'] = self.shard_index

        if self.similarity_score is not None:
            result['SimilarityScore'] = self.similarity_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Captions') is not None:
            self.captions = m.get('Captions')

        if m.get('DocItems') is not None:
            self.doc_items = m.get('DocItems')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Headings') is not None:
            self.headings = m.get('Headings')

        self.image_resources = []
        if m.get('ImageResources') is not None:
            for k1 in m.get('ImageResources'):
                temp_model = main_models.RetrievalKnowledgeBaseResponseBodyResultsImageResources()
                self.image_resources.append(temp_model.from_map(k1))

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')

        if m.get('ShardContent') is not None:
            self.shard_content = m.get('ShardContent')

        if m.get('ShardIndex') is not None:
            self.shard_index = m.get('ShardIndex')

        if m.get('SimilarityScore') is not None:
            self.similarity_score = m.get('SimilarityScore')

        return self

class RetrievalKnowledgeBaseResponseBodyResultsImageResources(DaraModel):
    def __init__(
        self,
        document_index: int = None,
        id: str = None,
        item_ref: str = None,
        mime_type: str = None,
        uri: str = None,
    ):
        # The index of the source document to which the image belongs, starting from 0.
        self.document_index = document_index
        # The unique identifier of the image resource.
        self.id = id
        # The element reference of the image in the Docling source document structure.
        self.item_ref = item_ref
        # The media type of the image resource.
        self.mime_type = mime_type
        # The OSS URI of the image resource.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document_index is not None:
            result['DocumentIndex'] = self.document_index

        if self.id is not None:
            result['Id'] = self.id

        if self.item_ref is not None:
            result['ItemRef'] = self.item_ref

        if self.mime_type is not None:
            result['MimeType'] = self.mime_type

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocumentIndex') is not None:
            self.document_index = m.get('DocumentIndex')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ItemRef') is not None:
            self.item_ref = m.get('ItemRef')

        if m.get('MimeType') is not None:
            self.mime_type = m.get('MimeType')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

