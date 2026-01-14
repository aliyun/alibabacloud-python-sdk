# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRegistryModuleVersionsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        module_name: str = None,
        namespace_name: str = None,
        next_token: str = None,
    ):
        self.max_results = max_results
        # This parameter is required.
        self.module_name = module_name
        # This parameter is required.
        self.namespace_name = namespace_name
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.module_name is not None:
            result['moduleName'] = self.module_name

        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')

        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        return self

