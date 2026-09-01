# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeKnowledgeBaseAnswerResponseBody(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        answer: str = None,
        completion_tokens: int = None,
        error_message: str = None,
        error_type: str = None,
        llmmodel_id: str = None,
        prompt_tokens: int = None,
        query_id: str = None,
        request_id: str = None,
        sources: List[main_models.DescribeKnowledgeBaseAnswerResponseBodySources] = None,
        status: str = None,
    ):
        self.agent_id = agent_id
        self.answer = answer
        self.completion_tokens = completion_tokens
        self.error_message = error_message
        self.error_type = error_type
        self.llmmodel_id = llmmodel_id
        self.prompt_tokens = prompt_tokens
        self.query_id = query_id
        self.request_id = request_id
        self.sources = sources
        self.status = status

    def validate(self):
        if self.sources:
            for v1 in self.sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.answer is not None:
            result['Answer'] = self.answer

        if self.completion_tokens is not None:
            result['CompletionTokens'] = self.completion_tokens

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.error_type is not None:
            result['ErrorType'] = self.error_type

        if self.llmmodel_id is not None:
            result['LLMModelId'] = self.llmmodel_id

        if self.prompt_tokens is not None:
            result['PromptTokens'] = self.prompt_tokens

        if self.query_id is not None:
            result['QueryId'] = self.query_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Sources'] = []
        if self.sources is not None:
            for k1 in self.sources:
                result['Sources'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('Answer') is not None:
            self.answer = m.get('Answer')

        if m.get('CompletionTokens') is not None:
            self.completion_tokens = m.get('CompletionTokens')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('ErrorType') is not None:
            self.error_type = m.get('ErrorType')

        if m.get('LLMModelId') is not None:
            self.llmmodel_id = m.get('LLMModelId')

        if m.get('PromptTokens') is not None:
            self.prompt_tokens = m.get('PromptTokens')

        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sources = []
        if m.get('Sources') is not None:
            for k1 in m.get('Sources'):
                temp_model = main_models.DescribeKnowledgeBaseAnswerResponseBodySources()
                self.sources.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeKnowledgeBaseAnswerResponseBodySources(DaraModel):
    def __init__(
        self,
        chunk_metadata: Dict[str, Any] = None,
        file_id: str = None,
        file_name: str = None,
        knowledge_base_id: str = None,
        metadata: Dict[str, Any] = None,
        page_numbers: List[int] = None,
        shard_content: str = None,
        shard_index: int = None,
        similarity_score: float = None,
        source_id: int = None,
    ):
        self.chunk_metadata = chunk_metadata
        self.file_id = file_id
        self.file_name = file_name
        self.knowledge_base_id = knowledge_base_id
        self.metadata = metadata
        self.page_numbers = page_numbers
        self.shard_content = shard_content
        self.shard_index = shard_index
        self.similarity_score = similarity_score
        self.source_id = source_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_metadata is not None:
            result['ChunkMetadata'] = self.chunk_metadata

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

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

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkMetadata') is not None:
            self.chunk_metadata = m.get('ChunkMetadata')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

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

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        return self

