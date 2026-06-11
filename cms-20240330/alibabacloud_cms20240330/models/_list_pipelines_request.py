# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPipelinesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        pipeline_name: str = None,
    ):
        # The maximum number of results to return. The service may return fewer results than the specified value.
        self.max_results = max_results
        # The pagination token. If this parameter is not empty, use it in a subsequent request to get the next page of results.
        self.next_token = next_token
        # The pipeline name.
        self.pipeline_name = pipeline_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.pipeline_name is not None:
            result['pipelineName'] = self.pipeline_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('pipelineName') is not None:
            self.pipeline_name = m.get('pipelineName')

        return self

