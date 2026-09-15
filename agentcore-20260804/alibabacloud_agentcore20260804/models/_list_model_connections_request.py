# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListModelConnectionsRequest(DaraModel):
    def __init__(
        self,
        include_models: bool = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        protocol: str = None,
        provider_type: str = None,
        search_type: str = None,
    ):
        # Specifies whether to return associated model summaries for each model connection. By default, model summaries are not returned.
        self.include_models = include_models
        # The number of records per page. Valid values: 0 to 100. If this parameter is not set or is set to 0, the default value 10 is used.
        self.max_results = max_results
        # The model connection name. The name must be 1 to 128 non-whitespace characters in length.
        self.name = name
        # The pagination token. Pass the token returned in the previous query. An empty response indicates that no more pages are available.
        self.next_token = next_token
        # The invocation protocol used to filter model connections.
        self.protocol = protocol
        # The model provider type used to filter model connections.
        self.provider_type = provider_type
        # The name matching mode. Takes effect only when Name is set. Valid values: accurate (exact match), blur (fuzzy match). Default value: blur.
        self.search_type = search_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_models is not None:
            result['includeModels'] = self.include_models

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.name is not None:
            result['name'] = self.name

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.provider_type is not None:
            result['providerType'] = self.provider_type

        if self.search_type is not None:
            result['searchType'] = self.search_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('includeModels') is not None:
            self.include_models = m.get('includeModels')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('providerType') is not None:
            self.provider_type = m.get('providerType')

        if m.get('searchType') is not None:
            self.search_type = m.get('searchType')

        return self

