# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListRegistryModulesResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        max_results: int = None,
        next_token: str = None,
        registry_modules: List[main_models.ListRegistryModulesResponseBodyRegistryModules] = None,
        request_id: str = None,
    ):
        self.count = count
        self.max_results = max_results
        self.next_token = next_token
        self.registry_modules = registry_modules
        self.request_id = request_id

    def validate(self):
        if self.registry_modules:
            for v1 in self.registry_modules:
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

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['registryModules'] = []
        if self.registry_modules is not None:
            for k1 in self.registry_modules:
                result['registryModules'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.registry_modules = []
        if m.get('registryModules') is not None:
            for k1 in m.get('registryModules'):
                temp_model = main_models.ListRegistryModulesResponseBodyRegistryModules()
                self.registry_modules.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListRegistryModulesResponseBodyRegistryModules(DaraModel):
    def __init__(
        self,
        acl: str = None,
        create_time: str = None,
        description: str = None,
        downloads: int = None,
        module_name: str = None,
        namespace_name: str = None,
        provider: str = None,
        shared_accounts: List[int] = None,
        source: str = None,
        source_url: str = None,
        type: str = None,
        version: str = None,
    ):
        self.acl = acl
        self.create_time = create_time
        self.description = description
        self.downloads = downloads
        self.module_name = module_name
        self.namespace_name = namespace_name
        self.provider = provider
        self.shared_accounts = shared_accounts
        self.source = source
        self.source_url = source_url
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl is not None:
            result['acl'] = self.acl

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.downloads is not None:
            result['downloads'] = self.downloads

        if self.module_name is not None:
            result['moduleName'] = self.module_name

        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name

        if self.provider is not None:
            result['provider'] = self.provider

        if self.shared_accounts is not None:
            result['sharedAccounts'] = self.shared_accounts

        if self.source is not None:
            result['source'] = self.source

        if self.source_url is not None:
            result['sourceUrl'] = self.source_url

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('downloads') is not None:
            self.downloads = m.get('downloads')

        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')

        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('sharedAccounts') is not None:
            self.shared_accounts = m.get('sharedAccounts')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('sourceUrl') is not None:
            self.source_url = m.get('sourceUrl')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

