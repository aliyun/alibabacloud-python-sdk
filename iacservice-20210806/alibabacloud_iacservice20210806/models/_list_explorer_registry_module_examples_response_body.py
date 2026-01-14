# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListExplorerRegistryModuleExamplesResponseBody(DaraModel):
    def __init__(
        self,
        explorer_registry_module_examples: List[main_models.ListExplorerRegistryModuleExamplesResponseBodyExplorerRegistryModuleExamples] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.explorer_registry_module_examples = explorer_registry_module_examples
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.explorer_registry_module_examples:
            for v1 in self.explorer_registry_module_examples:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['explorerRegistryModuleExamples'] = []
        if self.explorer_registry_module_examples is not None:
            for k1 in self.explorer_registry_module_examples:
                result['explorerRegistryModuleExamples'].append(k1.to_map() if k1 else None)

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
        self.explorer_registry_module_examples = []
        if m.get('explorerRegistryModuleExamples') is not None:
            for k1 in m.get('explorerRegistryModuleExamples'):
                temp_model = main_models.ListExplorerRegistryModuleExamplesResponseBodyExplorerRegistryModuleExamples()
                self.explorer_registry_module_examples.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListExplorerRegistryModuleExamplesResponseBodyExplorerRegistryModuleExamples(DaraModel):
    def __init__(
        self,
        example_name: str = None,
        example_path: str = None,
        example_schema: Dict[str, Any] = None,
        module_name: str = None,
        module_version: str = None,
        namespace_name: str = None,
        status: str = None,
    ):
        self.example_name = example_name
        self.example_path = example_path
        self.example_schema = example_schema
        self.module_name = module_name
        self.module_version = module_version
        self.namespace_name = namespace_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.example_name is not None:
            result['exampleName'] = self.example_name

        if self.example_path is not None:
            result['examplePath'] = self.example_path

        if self.example_schema is not None:
            result['exampleSchema'] = self.example_schema

        if self.module_name is not None:
            result['moduleName'] = self.module_name

        if self.module_version is not None:
            result['moduleVersion'] = self.module_version

        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exampleName') is not None:
            self.example_name = m.get('exampleName')

        if m.get('examplePath') is not None:
            self.example_path = m.get('examplePath')

        if m.get('exampleSchema') is not None:
            self.example_schema = m.get('exampleSchema')

        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')

        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')

        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

