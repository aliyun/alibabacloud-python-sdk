# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListModelsRequest(DaraModel):
    def __init__(
        self,
        connection_id: str = None,
        max_results: int = None,
        model_name: str = None,
        next_token: str = None,
    ):
        # The model connection ID used to filter models.
        self.connection_id = connection_id
        # The number of results per page. Valid values: 0 to 100. If this parameter is not set or set to 0, the default value 10 is used.
        self.max_results = max_results
        # The upstream model name.
        self.model_name = model_name
        # The pagination token. Pass the token returned from the previous query. An empty response indicates that no more pages are available.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_id is not None:
            result['connectionId'] = self.connection_id

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('connectionId') is not None:
            self.connection_id = m.get('connectionId')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

