# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

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
        types: List[str] = None,
    ):
        # Specifies whether to enable reranking. Default value: true.
        self.enable_rerank = enable_rerank
        # The string key-value metadata for exact matching. A maximum of 16 keys are supported. Each key can be up to 64 characters in length, and each value can be up to 1,024 characters in length.
        self.metadata = metadata
        # The minimum relevance score. Default value: 0.2. Valid values: 0 to 1. If both minScore and minSimilarity are specified, the results are filtered based on the AND logic.
        self.min_score = min_score
        # The minimum similarity score. Default value: 0.3. Valid values: 0 to 1. If both minSimilarity and minScore are specified, the results are filtered based on the AND logic.
        self.min_similarity = min_similarity
        # The query text for retrieval, up to 8,192 characters.
        # 
        # This parameter is required.
        self.query = query
        # The retrieval scope. UserId, AgentId, and SessionId are all optional.
        self.scope = scope
        # The number of results to return.
        self.top_k = top_k
        # The list of memory content types. Supported types include semantic, skill, user_profile, and session_summary. If omitted or left as an empty array, no type restriction is applied.
        self.types = types

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

        if self.types is not None:
            result['types'] = self.types

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

        if m.get('types') is not None:
            self.types = m.get('types')

        return self

class SearchMemoriesRequestBodyScope(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        session_id: str = None,
        team_id: str = None,
        user_id: str = None,
    ):
        # The agent ID. The length is limited to 1 to 128 UTF-8 bytes. The value cannot contain a forward slash (/) or an asterisk (*). This field is not returned if the memory is not associated with an agent ID.
        self.agent_id = agent_id
        # The session ID. The length is limited to 1 to 128 UTF-8 bytes. The value cannot contain a forward slash (/) or an asterisk (*). This field is not returned if the memory is not associated with a session ID.
        self.session_id = session_id
        # The business team ID defined by the caller. If provided, it cannot be empty and can be up to 128 UTF-8 bytes in length.
        self.team_id = team_id
        # The user ID. The length is limited to 1 to 128 UTF-8 bytes. The value cannot contain a forward slash (/) or an asterisk (*). This field is not returned if the memory is not associated with a user ID.
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

        if self.team_id is not None:
            result['teamId'] = self.team_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('teamId') is not None:
            self.team_id = m.get('teamId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

