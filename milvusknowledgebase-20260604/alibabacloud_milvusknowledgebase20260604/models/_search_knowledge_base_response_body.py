# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_milvusknowledgebase20260604 import models as main_models
from darabonba.model import DaraModel

class SearchKnowledgeBaseResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        query_labels: List[str] = None,
        request_id: str = None,
        results: List[main_models.SearchKnowledgeBaseResponseBodyResults] = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The details of the permission verification failure.
        self.access_denied_detail = access_denied_detail
        # The status code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The query labels.
        self.query_labels = query_labels
        # The request ID.
        self.request_id = request_id
        # The list of retrieval results.
        self.results = results
        # Indicates whether the request was successful.
        self.success = success
        # The total number of results.
        self.total_count = total_count

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
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['code'] = self.code

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.query_labels is not None:
            result['queryLabels'] = self.query_labels

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('queryLabels') is not None:
            self.query_labels = m.get('queryLabels')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.results = []
        if m.get('results') is not None:
            for k1 in m.get('results'):
                temp_model = main_models.SearchKnowledgeBaseResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class SearchKnowledgeBaseResponseBodyResults(DaraModel):
    def __init__(
        self,
        chunk_id: str = None,
        content: str = None,
        content_type: str = None,
        document_id: str = None,
        document_name: str = None,
        images: List[main_models.SearchKnowledgeBaseResponseBodyResultsImages] = None,
        knowledge_base_id: str = None,
        locations: List[main_models.SearchKnowledgeBaseResponseBodyResultsLocations] = None,
        parent_chunk_id: str = None,
        scalar_fields: Any = None,
        score: float = None,
        score_details: main_models.SearchKnowledgeBaseResponseBodyResultsScoreDetails = None,
        tags: List[str] = None,
    ):
        # The chunk ID.
        self.chunk_id = chunk_id
        # The chunk content.
        self.content = content
        # The content type.
        self.content_type = content_type
        # The document ID.
        self.document_id = document_id
        # The document name.
        self.document_name = document_name
        # The list of associated images.
        self.images = images
        # The knowledge base ID.
        self.knowledge_base_id = knowledge_base_id
        # The list of document locations.
        self.locations = locations
        # The parent chunk ID.
        self.parent_chunk_id = parent_chunk_id
        # The scalar columns of the structured knowledge base. The columns are returned by their original column names and are not used in retrieval.
        self.scalar_fields = scalar_fields
        # The overall relevance score.
        self.score = score
        # The relevance score details.
        self.score_details = score_details
        # The list of tags.
        self.tags = tags

    def validate(self):
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()
        if self.locations:
            for v1 in self.locations:
                 if v1:
                    v1.validate()
        if self.score_details:
            self.score_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_id is not None:
            result['chunkId'] = self.chunk_id

        if self.content is not None:
            result['content'] = self.content

        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.document_id is not None:
            result['documentId'] = self.document_id

        if self.document_name is not None:
            result['documentName'] = self.document_name

        result['images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['images'].append(k1.to_map() if k1 else None)

        if self.knowledge_base_id is not None:
            result['knowledgeBaseId'] = self.knowledge_base_id

        result['locations'] = []
        if self.locations is not None:
            for k1 in self.locations:
                result['locations'].append(k1.to_map() if k1 else None)

        if self.parent_chunk_id is not None:
            result['parentChunkId'] = self.parent_chunk_id

        if self.scalar_fields is not None:
            result['scalarFields'] = self.scalar_fields

        if self.score is not None:
            result['score'] = self.score

        if self.score_details is not None:
            result['scoreDetails'] = self.score_details.to_map()

        if self.tags is not None:
            result['tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkId') is not None:
            self.chunk_id = m.get('chunkId')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('documentId') is not None:
            self.document_id = m.get('documentId')

        if m.get('documentName') is not None:
            self.document_name = m.get('documentName')

        self.images = []
        if m.get('images') is not None:
            for k1 in m.get('images'):
                temp_model = main_models.SearchKnowledgeBaseResponseBodyResultsImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('knowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('knowledgeBaseId')

        self.locations = []
        if m.get('locations') is not None:
            for k1 in m.get('locations'):
                temp_model = main_models.SearchKnowledgeBaseResponseBodyResultsLocations()
                self.locations.append(temp_model.from_map(k1))

        if m.get('parentChunkId') is not None:
            self.parent_chunk_id = m.get('parentChunkId')

        if m.get('scalarFields') is not None:
            self.scalar_fields = m.get('scalarFields')

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('scoreDetails') is not None:
            temp_model = main_models.SearchKnowledgeBaseResponseBodyResultsScoreDetails()
            self.score_details = temp_model.from_map(m.get('scoreDetails'))

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        return self

class SearchKnowledgeBaseResponseBodyResultsScoreDetails(DaraModel):
    def __init__(
        self,
        keyword_score: float = None,
        semantic_score: float = None,
    ):
        # The keyword relevance score.
        self.keyword_score = keyword_score
        # The semantic relevance score.
        self.semantic_score = semantic_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword_score is not None:
            result['keywordScore'] = self.keyword_score

        if self.semantic_score is not None:
            result['semanticScore'] = self.semantic_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keywordScore') is not None:
            self.keyword_score = m.get('keywordScore')

        if m.get('semanticScore') is not None:
            self.semantic_score = m.get('semanticScore')

        return self

class SearchKnowledgeBaseResponseBodyResultsLocations(DaraModel):
    def __init__(
        self,
        bottom: int = None,
        left: int = None,
        page_number: int = None,
        right: int = None,
        top: int = None,
    ):
        # The bottom boundary.
        self.bottom = bottom
        # The left boundary.
        self.left = left
        # The page number.
        self.page_number = page_number
        # The right boundary.
        self.right = right
        # The top boundary.
        self.top = top

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bottom is not None:
            result['bottom'] = self.bottom

        if self.left is not None:
            result['left'] = self.left

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.right is not None:
            result['right'] = self.right

        if self.top is not None:
            result['top'] = self.top

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bottom') is not None:
            self.bottom = m.get('bottom')

        if m.get('left') is not None:
            self.left = m.get('left')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('right') is not None:
            self.right = m.get('right')

        if m.get('top') is not None:
            self.top = m.get('top')

        return self

class SearchKnowledgeBaseResponseBodyResultsImages(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        url: str = None,
    ):
        # The image ID.
        self.image_id = image_id
        # The temporary access URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['imageId'] = self.image_id

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

