# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListExplorerRegistryModulesResponseBody(DaraModel):
    def __init__(
        self,
        explorer_registry_modules: List[main_models.ListExplorerRegistryModulesResponseBodyExplorerRegistryModules] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.explorer_registry_modules = explorer_registry_modules
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.explorer_registry_modules:
            for v1 in self.explorer_registry_modules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['explorerRegistryModules'] = []
        if self.explorer_registry_modules is not None:
            for k1 in self.explorer_registry_modules:
                result['explorerRegistryModules'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.explorer_registry_modules = []
        if m.get('explorerRegistryModules') is not None:
            for k1 in m.get('explorerRegistryModules'):
                temp_model = main_models.ListExplorerRegistryModulesResponseBodyExplorerRegistryModules()
                self.explorer_registry_modules.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListExplorerRegistryModulesResponseBodyExplorerRegistryModules(DaraModel):
    def __init__(
        self,
        description: str = None,
        downloads: int = None,
        latest_version: str = None,
        module_name: str = None,
        namespace_name: str = None,
        source: str = None,
        status: str = None,
    ):
        self.description = description
        self.downloads = downloads
        self.latest_version = latest_version
        self.module_name = module_name
        self.namespace_name = namespace_name
        self.source = source
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.downloads is not None:
            result['downloads'] = self.downloads

        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version

        if self.module_name is not None:
            result['moduleName'] = self.module_name

        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name

        if self.source is not None:
            result['source'] = self.source

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('downloads') is not None:
            self.downloads = m.get('downloads')

        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')

        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')

        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

