# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListRegistryModuleVersionsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        max_results: int = None,
        module_versions: List[main_models.ListRegistryModuleVersionsResponseBodyModuleVersions] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.count = count
        self.max_results = max_results
        self.module_versions = module_versions
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.module_versions:
            for v1 in self.module_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        result['moduleVersions'] = []
        if self.module_versions is not None:
            for k1 in self.module_versions:
                result['moduleVersions'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        self.module_versions = []
        if m.get('moduleVersions') is not None:
            for k1 in m.get('moduleVersions'):
                temp_model = main_models.ListRegistryModuleVersionsResponseBodyModuleVersions()
                self.module_versions.append(temp_model.from_map(k1))

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListRegistryModuleVersionsResponseBodyModuleVersions(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        module_name: str = None,
        namespace_name: str = None,
        provider: str = None,
        source: str = None,
        source_url: str = None,
        version: str = None,
    ):
        self.create_time = create_time
        self.module_name = module_name
        self.namespace_name = namespace_name
        self.provider = provider
        self.source = source
        self.source_url = source_url
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.module_name is not None:
            result['moduleName'] = self.module_name

        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name

        if self.provider is not None:
            result['provider'] = self.provider

        if self.source is not None:
            result['source'] = self.source

        if self.source_url is not None:
            result['sourceUrl'] = self.source_url

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')

        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('sourceUrl') is not None:
            self.source_url = m.get('sourceUrl')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

