# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class SearchContextRequest(DaraModel):
    def __init__(
        self,
        filter: Dict[str, Any] = None,
        formatted: bool = None,
        include_inactive: bool = None,
        limit: int = None,
        query: str = None,
        retrieval_option: str = None,
        scope: main_models.SearchContextRequestScope = None,
        threshold: float = None,
    ):
        # The structured filter conditions. The key is the field name, and the value is the expected matching value.
        self.filter = filter
        # Specifies whether to apply structured formatting to the returned results.
        self.formatted = formatted
        self.include_inactive = include_inactive
        # The maximum number of returned results (similarity Top-N).
        self.limit = limit
        # The retrieval query text. Natural language is supported.
        # 
        # This parameter is required.
        self.query = query
        # The retrieval options that control the retrieval strategy.
        self.retrieval_option = retrieval_option
        self.scope = scope
        # The similarity threshold. Results with a similarity score lower than this value are filtered out. Valid values: 0 to 1.
        self.threshold = threshold

    def validate(self):
        if self.scope:
            self.scope.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['filter'] = self.filter

        if self.formatted is not None:
            result['formatted'] = self.formatted

        if self.include_inactive is not None:
            result['includeInactive'] = self.include_inactive

        if self.limit is not None:
            result['limit'] = self.limit

        if self.query is not None:
            result['query'] = self.query

        if self.retrieval_option is not None:
            result['retrievalOption'] = self.retrieval_option

        if self.scope is not None:
            result['scope'] = self.scope.to_map()

        if self.threshold is not None:
            result['threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filter') is not None:
            self.filter = m.get('filter')

        if m.get('formatted') is not None:
            self.formatted = m.get('formatted')

        if m.get('includeInactive') is not None:
            self.include_inactive = m.get('includeInactive')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('retrievalOption') is not None:
            self.retrieval_option = m.get('retrievalOption')

        if m.get('scope') is not None:
            temp_model = main_models.SearchContextRequestScope()
            self.scope = temp_model.from_map(m.get('scope'))

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        return self

class SearchContextRequestScope(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        app_id: str = None,
        run_id: str = None,
        user_id: str = None,
    ):
        self.agent_id = agent_id
        self.app_id = app_id
        self.run_id = run_id
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

        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

