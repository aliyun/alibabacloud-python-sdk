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
        self.include_models = include_models
        self.max_results = max_results
        self.name = name
        self.next_token = next_token
        self.protocol = protocol
        self.provider_type = provider_type
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

