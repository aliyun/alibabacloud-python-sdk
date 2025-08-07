# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 


class ListIcebergNamespaceDetailsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        namespace_name_pattern: str = None,
        page_token: str = None,
    ):
        self.max_results = max_results
        self.namespace_name_pattern = namespace_name_pattern
        self.page_token = page_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.namespace_name_pattern is not None:
            result['namespaceNamePattern'] = self.namespace_name_pattern

        if self.page_token is not None:
            result['pageToken'] = self.page_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('namespaceNamePattern') is not None:
            self.namespace_name_pattern = m.get('namespaceNamePattern')

        if m.get('pageToken') is not None:
            self.page_token = m.get('pageToken')

        return self

