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
        evidence_next_token: str = None,
        evidence_results: List[main_models.SearchKnowledgeBaseResponseBodyEvidenceResults] = None,
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
        # The details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The returned status code.
        self.code = code
        # Optional or conditionally returned. Required when includeWiki is set to true. The cursor for the next page of evidence, which is null for the last page. Not used for legacy results pagination. Null is allowed and can be omitted. Constraints: {"minLength":1,"maxLength":4096}.
        self.evidence_next_token = evidence_next_token
        # Optional or conditionally returned. Returned only when includeWiki is set to true. The current page of unified and merged results. Constraints: {"minItems":0,"maxItems":100}.
        self.evidence_results = evidence_results
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The page number.
        self.page_number = page_number
        # The number of items per page.
        self.page_size = page_size
        # The query labels.
        self.query_labels = query_labels
        # The request ID.
        self.request_id = request_id
        # The list of search results.
        self.results = results
        # Indicates whether the request is successful.
        self.success = success
        # The total count.
        self.total_count = total_count

    def validate(self):
        if self.evidence_results:
            for v1 in self.evidence_results:
                 if v1:
                    v1.validate()
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

        if self.evidence_next_token is not None:
            result['evidenceNextToken'] = self.evidence_next_token

        result['evidenceResults'] = []
        if self.evidence_results is not None:
            for k1 in self.evidence_results:
                result['evidenceResults'].append(k1.to_map() if k1 else None)

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

        if m.get('evidenceNextToken') is not None:
            self.evidence_next_token = m.get('evidenceNextToken')

        self.evidence_results = []
        if m.get('evidenceResults') is not None:
            for k1 in m.get('evidenceResults'):
                temp_model = main_models.SearchKnowledgeBaseResponseBodyEvidenceResults()
                self.evidence_results.append(temp_model.from_map(k1))

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
        media_end_ms: int = None,
        media_start_ms: int = None,
        media_timeline: List[main_models.SearchKnowledgeBaseResponseBodyResultsMediaTimeline] = None,
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
        # The end time of the audio or video chunk in the original media, in milliseconds. This field is not returned for non-media chunks.
        self.media_end_ms = media_end_ms
        # The start time of the audio or video chunk in the original media, in milliseconds. This field is not returned for non-media chunks.
        self.media_start_ms = media_start_ms
        # The time ranges of sentence-by-sentence or paragraph-by-paragraph content within the chunk in the original media. This field is not returned for non-audio chunks.
        self.media_timeline = media_timeline
        # The parent chunk ID.
        self.parent_chunk_id = parent_chunk_id
        # The scalar fields of the structured knowledge base. These fields are returned by their original column names and are not used for retrieval.
        self.scalar_fields = scalar_fields
        # The overall relevance score.
        self.score = score
        # The relevance details.
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
        if self.media_timeline:
            for v1 in self.media_timeline:
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

        if self.media_end_ms is not None:
            result['mediaEndMs'] = self.media_end_ms

        if self.media_start_ms is not None:
            result['mediaStartMs'] = self.media_start_ms

        result['mediaTimeline'] = []
        if self.media_timeline is not None:
            for k1 in self.media_timeline:
                result['mediaTimeline'].append(k1.to_map() if k1 else None)

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

        if m.get('mediaEndMs') is not None:
            self.media_end_ms = m.get('mediaEndMs')

        if m.get('mediaStartMs') is not None:
            self.media_start_ms = m.get('mediaStartMs')

        self.media_timeline = []
        if m.get('mediaTimeline') is not None:
            for k1 in m.get('mediaTimeline'):
                temp_model = main_models.SearchKnowledgeBaseResponseBodyResultsMediaTimeline()
                self.media_timeline.append(temp_model.from_map(k1))

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

class SearchKnowledgeBaseResponseBodyResultsMediaTimeline(DaraModel):
    def __init__(
        self,
        end_ms: int = None,
        start_ms: int = None,
        text: str = None,
    ):
        # The end time of the segment.
        self.end_ms = end_ms
        # The start time of the segment.
        self.start_ms = start_ms
        # The segment text.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_ms is not None:
            result['endMs'] = self.end_ms

        if self.start_ms is not None:
            result['startMs'] = self.start_ms

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endMs') is not None:
            self.end_ms = m.get('endMs')

        if m.get('startMs') is not None:
            self.start_ms = m.get('startMs')

        if m.get('text') is not None:
            self.text = m.get('text')

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

class SearchKnowledgeBaseResponseBodyEvidenceResults(DaraModel):
    def __init__(
        self,
        batch_id: str = None,
        chunk_id: str = None,
        content: str = None,
        document_id: str = None,
        entity_id: str = None,
        evidence_id: str = None,
        kind: str = None,
        knowledge_base_id: str = None,
        page_id: str = None,
        relation_id: str = None,
        revision_id: str = None,
        score: float = None,
        section_id: str = None,
        source_ref_count: int = None,
        source_refs: List[main_models.SearchKnowledgeBaseResponseBodyEvidenceResultsSourceRefs] = None,
        source_refs_truncated: bool = None,
        source_task_id: str = None,
        title: str = None,
    ):
        # Required and always returned. Null is allowed. The semantics of null values follow the field description. Null is allowed and can be omitted. Constraints: {"minLength":1,"maxLength":128,"pattern":"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$"}.
        # 
        # This parameter is required.
        self.batch_id = batch_id
        # Required and always returned. Null is allowed. The semantics of null values follow the field description. Null is allowed and can be omitted. Constraints: {"minLength":1,"maxLength":128,"pattern":"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$"}.
        # 
        # This parameter is required.
        self.chunk_id = chunk_id
        # Required and always returned. The readable evidence text. Constraints: {"maxLength":65535}.
        # 
        # This parameter is required.
        self.content = content
        # Required and always returned. Null is allowed. The semantics of null values follow the field description. Null is allowed and can be omitted. Constraints: {"minLength":1,"maxLength":128,"pattern":"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$"}.
        # 
        # This parameter is required.
        self.document_id = document_id
        # Required and always returned. Null is allowed. The semantics of null values follow the field description. Null is allowed and can be omitted. Constraints: {"minLength":1,"maxLength":128,"pattern":"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$"}.
        # 
        # This parameter is required.
        self.entity_id = entity_id
        # Required and always returned. An opaque business ID generated by the server. Ownership is validated, and arbitrary paths are not accepted. Constraints: {"minLength":1,"maxLength":128,"pattern":"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$"}.
        # 
        # This parameter is required.
        self.evidence_id = evidence_id
        # Required and always returned. The actual evidence object type. Constraints: {"enum":["raw","wiki_page","wiki_section","graph_fact"],"maxLength":64}.
        # 
        # This parameter is required.
        self.kind = kind
        # Required and always returned. An opaque business ID generated by the server. Ownership is validated, and arbitrary paths are not accepted. Constraints: {"minLength":1,"maxLength":128,"pattern":"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$"}.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # Required and always returned. Null is allowed. The semantics of null values follow the field description. Null is allowed and can be omitted. Constraints: {"minLength":1,"maxLength":128,"pattern":"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$"}.
        # 
        # This parameter is required.
        self.page_id = page_id
        # Required and always returned. Null is allowed. The semantics of null values follow the field description. Null is allowed and can be omitted. Constraints: {"minLength":1,"maxLength":128,"pattern":"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$"}.
        # 
        # This parameter is required.
        self.relation_id = relation_id
        # Required and always returned. An opaque business ID generated by the server. Ownership is validated, and arbitrary paths are not accepted. Constraints: {"minLength":1,"maxLength":128,"pattern":"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$"}.
        # 
        # This parameter is required.
        self.revision_id = revision_id
        # Required and always returned. A finite numerical value used for unified ranking. For hybrid, it is the relevance of the existing Dealer.rerank. For rerank, it is the text and model hybrid relevance of the existing Dealer.rerank_by_model, along semanticWeight and rank features, and is not a relevance probability. minScore is applied according to the existing unified scoring rules. Can be null for non-ranked factual evidence. Null is allowed and can be omitted.
        # 
        # This parameter is required.
        self.score = score
        # Required and always returned. Null is allowed. The semantics of null values follow the field description. Null is allowed and can be omitted. Constraints: {"minLength":1,"maxLength":128,"pattern":"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$"}.
        # 
        # This parameter is required.
        self.section_id = section_id
        # Required and always returned. The total number of source chunk references. Authentication is performed on the full set. Constraints: {"minimum":1,"maximum":9223372036854775807}.
        # 
        # This parameter is required.
        self.source_ref_count = source_ref_count
        # Required and always returned. The actually supported sources. Constraints: {"minItems":1,"maxItems":1000}.
        # 
        # This parameter is required.
        self.source_refs = source_refs
        # Required and always returned. True when a single sourceRefs contains only the first 1,000 items. You can paginate and verify by using sourceTaskId.
        # 
        # This parameter is required.
        self.source_refs_truncated = source_refs_truncated
        # Required and always returned. The entry for complete sources. Must be a non-null locator when sourceRefsTruncated is true. Source operation references held by artifacts or revisions remain readable, and archiving task details does not delete the source manifest. Null is allowed and can be omitted. Constraints: {"minLength":32,"maxLength":32,"pattern":"^[0-9a-f]{32}$"}.
        # 
        # This parameter is required.
        self.source_task_id = source_task_id
        # Required and always returned. The display title after authorization. Constraints: {"maxLength":1024}.
        # 
        # This parameter is required.
        self.title = title

    def validate(self):
        if self.source_refs:
            for v1 in self.source_refs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['batchId'] = self.batch_id

        if self.chunk_id is not None:
            result['chunkId'] = self.chunk_id

        if self.content is not None:
            result['content'] = self.content

        if self.document_id is not None:
            result['documentId'] = self.document_id

        if self.entity_id is not None:
            result['entityId'] = self.entity_id

        if self.evidence_id is not None:
            result['evidenceId'] = self.evidence_id

        if self.kind is not None:
            result['kind'] = self.kind

        if self.knowledge_base_id is not None:
            result['knowledgeBaseId'] = self.knowledge_base_id

        if self.page_id is not None:
            result['pageId'] = self.page_id

        if self.relation_id is not None:
            result['relationId'] = self.relation_id

        if self.revision_id is not None:
            result['revisionId'] = self.revision_id

        if self.score is not None:
            result['score'] = self.score

        if self.section_id is not None:
            result['sectionId'] = self.section_id

        if self.source_ref_count is not None:
            result['sourceRefCount'] = self.source_ref_count

        result['sourceRefs'] = []
        if self.source_refs is not None:
            for k1 in self.source_refs:
                result['sourceRefs'].append(k1.to_map() if k1 else None)

        if self.source_refs_truncated is not None:
            result['sourceRefsTruncated'] = self.source_refs_truncated

        if self.source_task_id is not None:
            result['sourceTaskId'] = self.source_task_id

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchId') is not None:
            self.batch_id = m.get('batchId')

        if m.get('chunkId') is not None:
            self.chunk_id = m.get('chunkId')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('documentId') is not None:
            self.document_id = m.get('documentId')

        if m.get('entityId') is not None:
            self.entity_id = m.get('entityId')

        if m.get('evidenceId') is not None:
            self.evidence_id = m.get('evidenceId')

        if m.get('kind') is not None:
            self.kind = m.get('kind')

        if m.get('knowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('knowledgeBaseId')

        if m.get('pageId') is not None:
            self.page_id = m.get('pageId')

        if m.get('relationId') is not None:
            self.relation_id = m.get('relationId')

        if m.get('revisionId') is not None:
            self.revision_id = m.get('revisionId')

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('sectionId') is not None:
            self.section_id = m.get('sectionId')

        if m.get('sourceRefCount') is not None:
            self.source_ref_count = m.get('sourceRefCount')

        self.source_refs = []
        if m.get('sourceRefs') is not None:
            for k1 in m.get('sourceRefs'):
                temp_model = main_models.SearchKnowledgeBaseResponseBodyEvidenceResultsSourceRefs()
                self.source_refs.append(temp_model.from_map(k1))

        if m.get('sourceRefsTruncated') is not None:
            self.source_refs_truncated = m.get('sourceRefsTruncated')

        if m.get('sourceTaskId') is not None:
            self.source_task_id = m.get('sourceTaskId')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class SearchKnowledgeBaseResponseBodyEvidenceResultsSourceRefs(DaraModel):
    def __init__(
        self,
        chunk_id: str = None,
        document_id: str = None,
        document_name: str = None,
        media_end_ms: int = None,
        media_start_ms: int = None,
        page_number: int = None,
        source_revision_id: str = None,
        version: str = None,
    ):
        # Required and always returned. An opaque business ID generated by the server. Ownership is validated, and arbitrary paths are not accepted. Constraints: {"minLength":1,"maxLength":128,"pattern":"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$"}.
        # 
        # This parameter is required.
        self.chunk_id = chunk_id
        # Required and always returned. An opaque business ID generated by the server. Ownership is validated, and arbitrary paths are not accepted. Constraints: {"minLength":1,"maxLength":128,"pattern":"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$"}.
        # 
        # This parameter is required.
        self.document_id = document_id
        # Optional or conditionally returned. The document name that can be returned only after authorization. Constraints: {"maxLength":1024}.
        self.document_name = document_name
        # Optional or conditionally returned. Null is allowed. The semantics of null values follow the field description. Null is allowed and can be omitted. Constraints: {"minimum":0,"maximum":9223372036854775807}.
        self.media_end_ms = media_end_ms
        # Optional or conditionally returned. Null is allowed. The semantics of null values follow the field description. Null is allowed and can be omitted. Constraints: {"minimum":0,"maximum":9223372036854775807}.
        self.media_start_ms = media_start_ms
        # Optional or conditionally returned. Null is allowed. The semantics of null values follow the field description. Null is allowed and can be omitted. Constraints: {"minimum":1,"maximum":9223372036854775807}.
        self.page_number = page_number
        # Required and always returned. An opaque business ID generated by the server. Ownership is validated, and arbitrary paths are not accepted. Constraints: {"minLength":1,"maxLength":128,"pattern":"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$"}.
        # 
        # This parameter is required.
        self.source_revision_id = source_revision_id
        # Required and always returned. The display name of the version. Does not fall back to draft if invalid or unavailable. Constraints: {"maxLength":64,"pattern":"^(DRAFT|LATEST_PUBLISHED|v[1-9][0-9]*)$","default":"DRAFT"}.
        # 
        # This parameter is required.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_id is not None:
            result['chunkId'] = self.chunk_id

        if self.document_id is not None:
            result['documentId'] = self.document_id

        if self.document_name is not None:
            result['documentName'] = self.document_name

        if self.media_end_ms is not None:
            result['mediaEndMs'] = self.media_end_ms

        if self.media_start_ms is not None:
            result['mediaStartMs'] = self.media_start_ms

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.source_revision_id is not None:
            result['sourceRevisionId'] = self.source_revision_id

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkId') is not None:
            self.chunk_id = m.get('chunkId')

        if m.get('documentId') is not None:
            self.document_id = m.get('documentId')

        if m.get('documentName') is not None:
            self.document_name = m.get('documentName')

        if m.get('mediaEndMs') is not None:
            self.media_end_ms = m.get('mediaEndMs')

        if m.get('mediaStartMs') is not None:
            self.media_start_ms = m.get('mediaStartMs')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('sourceRevisionId') is not None:
            self.source_revision_id = m.get('sourceRevisionId')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

