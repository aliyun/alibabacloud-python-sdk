# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListExplorerRegistryModulesRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        module_name: str = None,
        next_token: str = None,
        sort: str = None,
    ):
        self.keyword = keyword
        self.max_results = max_results
        self.module_name = module_name
        self.next_token = next_token
        self.sort = sort

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.module_name is not None:
            result['moduleName'] = self.module_name

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.sort is not None:
            result['sort'] = self.sort

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('sort') is not None:
            self.sort = m.get('sort')

        return self

