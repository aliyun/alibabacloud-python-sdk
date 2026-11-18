# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAiModelSourceModelsRequest(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        keyword: str = None,
        max_results: int = None,
        model_source_id: str = None,
        next_token: str = None,
    ):
        # The ID of the AI gateway instance to which the resource belongs.
        # 
        # This parameter is required.
        self.gateway_id = gateway_id
        # The query keyword used to match resources by name or identifier.
        self.keyword = keyword
        # The maximum number of results to return per page. Valid values: 1 to 100. This parameter is required. Token-based pagination does not use pageNumber or pageSize.
        # 
        # This parameter is required.
        self.max_results = max_results
        # The ID of the model source. Use the modelSourceId returned by CreateAiModelSource.
        self.model_source_id = model_source_id
        # The pagination token returned from the previous page. Omit this parameter for the first page. For the last page, this parameter is empty or omitted.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.model_source_id is not None:
            result['modelSourceId'] = self.model_source_id

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('modelSourceId') is not None:
            self.model_source_id = m.get('modelSourceId')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

