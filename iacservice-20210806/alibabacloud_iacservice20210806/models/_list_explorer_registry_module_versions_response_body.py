# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListExplorerRegistryModuleVersionsResponseBody(DaraModel):
    def __init__(
        self,
        explorer_registry_module_versions: List[main_models.ListExplorerRegistryModuleVersionsResponseBodyExplorerRegistryModuleVersions] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.explorer_registry_module_versions = explorer_registry_module_versions
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.explorer_registry_module_versions:
            for v1 in self.explorer_registry_module_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['explorerRegistryModuleVersions'] = []
        if self.explorer_registry_module_versions is not None:
            for k1 in self.explorer_registry_module_versions:
                result['explorerRegistryModuleVersions'].append(k1.to_map() if k1 else None)

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
        self.explorer_registry_module_versions = []
        if m.get('explorerRegistryModuleVersions') is not None:
            for k1 in m.get('explorerRegistryModuleVersions'):
                temp_model = main_models.ListExplorerRegistryModuleVersionsResponseBodyExplorerRegistryModuleVersions()
                self.explorer_registry_module_versions.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListExplorerRegistryModuleVersionsResponseBodyExplorerRegistryModuleVersions(DaraModel):
    def __init__(
        self,
        module_detail: Dict[str, Any] = None,
        module_file: Dict[str, Any] = None,
        module_name: str = None,
        namespace_name: str = None,
        properties: Dict[str, Any] = None,
        source: str = None,
        version: str = None,
    ):
        self.module_detail = module_detail
        self.module_file = module_file
        self.module_name = module_name
        self.namespace_name = namespace_name
        self.properties = properties
        self.source = source
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_detail is not None:
            result['moduleDetail'] = self.module_detail

        if self.module_file is not None:
            result['moduleFile'] = self.module_file

        if self.module_name is not None:
            result['moduleName'] = self.module_name

        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name

        if self.properties is not None:
            result['properties'] = self.properties

        if self.source is not None:
            result['source'] = self.source

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('moduleDetail') is not None:
            self.module_detail = m.get('moduleDetail')

        if m.get('moduleFile') is not None:
            self.module_file = m.get('moduleFile')

        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')

        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')

        if m.get('properties') is not None:
            self.properties = m.get('properties')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

