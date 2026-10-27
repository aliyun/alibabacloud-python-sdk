# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class SearchMemoriesRequest(DaraModel):
    def __init__(
        self,
        body: main_models.SearchMemoriesRequestBody = None,
    ):
        # The semantic retrieval request.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.SearchMemoriesRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class SearchMemoriesRequestBody(DaraModel):
    def __init__(
        self,
        enable_rerank: bool = None,
        metadata: Dict[str, str] = None,
        min_score: float = None,
        min_similarity: float = None,
        query: str = None,
        scope: main_models.SearchMemoriesRequestBodyScope = None,
        top_k: int = None,
    ):
        # Specifies whether to enable reranking. Default value: true.
        self.enable_rerank = enable_rerank
        # The string key-value metadata for exact match. You can specify up to 16 keys. Each key can be up to 64 characters in length, and each value can be up to 1,024 characters in length.
        self.metadata = metadata
        # The minimum relevance score. Valid values: 0 to 1. Default value: 0.2. If both minScore and minSimilarity are specified, the AND logic is applied for filtering.
        self.min_score = min_score
        # The minimum similarity. Valid values: 0 to 1. Default value: 0.3. If both minScore and minSimilarity are specified, the AND logic is applied for filtering.
        self.min_similarity = min_similarity
        # The query text. The text can be up to 8,192 characters in length.
        # 
        # This parameter is required.
        self.query = query
        # The retrieval scope. UserId, AgentId, and SessionId are all optional.
        self.scope = scope
        # The number of results to return.
        self.top_k = top_k

    def validate(self):
        if self.scope:
            self.scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_rerank is not None:
            result['enableRerank'] = self.enable_rerank

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.min_score is not None:
            result['minScore'] = self.min_score

        if self.min_similarity is not None:
            result['minSimilarity'] = self.min_similarity

        if self.query is not None:
            result['query'] = self.query

        if self.scope is not None:
            result['scope'] = self.scope.to_map()

        if self.top_k is not None:
            result['topK'] = self.top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableRerank') is not None:
            self.enable_rerank = m.get('enableRerank')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('minScore') is not None:
            self.min_score = m.get('minScore')

        if m.get('minSimilarity') is not None:
            self.min_similarity = m.get('minSimilarity')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('scope') is not None:
            temp_model = main_models.SearchMemoriesRequestBodyScope()
            self.scope = temp_model.from_map(m.get('scope'))

        if m.get('topK') is not None:
            self.top_k = m.get('topK')

        return self

class SearchMemoriesRequestBodyScope(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        session_id: str = None,
        user_id: str = None,
    ):
        # The agent ID. The ID must be 1 to 128 bytes in length and encoded in UTF-8. The ID cannot contain a forward slash (/) or an asterisk (*). If the memory is not associated with an agent ID, this field is not returned.
        self.agent_id = agent_id
        # The session ID. The ID must be 1 to 128 bytes in length and encoded in UTF-8. The ID cannot contain a forward slash (/) or an asterisk (*). If the memory is not associated with a session ID, this field is not returned.
        self.session_id = session_id
        # The user ID. The ID must be 1 to 128 bytes in length and encoded in UTF-8. The ID cannot contain a forward slash (/) or an asterisk (*). If the memory is not associated with a user ID, this field is not returned.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

