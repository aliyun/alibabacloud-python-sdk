# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListExplorerRegistryModuleVersionsRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        module_name: str = None,
        module_version: str = None,
        namespace_name: str = None,
        next_token: str = None,
    ):
        # The search keyword. Fuzzy match is supported based on the module name.
        self.keyword = keyword
        # The maximum number of entries per page.
        # 
        # Valid values: 0 to 200.
        # 
        # Default value: 100.
        self.max_results = max_results
        # The name of the module.
        self.module_name = module_name
        # The version of the module.
        self.module_version = module_version
        # The name of the workspace to which the module belongs.
        self.namespace_name = namespace_name
        # The pagination token for the next page of results.
        # 
        # If the total number of entries exceeds the maxResults limit, the data is truncated. You can use nextToken to query the next page of data.
        self.next_token = next_token

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

        if self.module_version is not None:
            result['moduleVersion'] = self.module_version

        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')

        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')

        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

