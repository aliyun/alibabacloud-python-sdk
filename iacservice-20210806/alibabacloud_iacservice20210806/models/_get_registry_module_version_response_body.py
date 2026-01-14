# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class GetRegistryModuleVersionResponseBody(DaraModel):
    def __init__(
        self,
        module_version: main_models.GetRegistryModuleVersionResponseBodyModuleVersion = None,
        request_id: str = None,
    ):
        self.module_version = module_version
        self.request_id = request_id

    def validate(self):
        if self.module_version:
            self.module_version.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('moduleVersion') is not None:
            temp_model = main_models.GetRegistryModuleVersionResponseBodyModuleVersion()
            self.module_version = temp_model.from_map(m.get('moduleVersion'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetRegistryModuleVersionResponseBodyModuleVersion(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        detail_url: str = None,
        downloads: str = None,
        module_name: str = None,
        namespace_name: str = None,
        provider: str = None,
        source: str = None,
        source_url: str = None,
        version: str = None,
    ):
        self.create_time = create_time
        self.detail_url = detail_url
        self.downloads = downloads
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

        if self.detail_url is not None:
            result['detailUrl'] = self.detail_url

        if self.downloads is not None:
            result['downloads'] = self.downloads

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

        if m.get('detailUrl') is not None:
            self.detail_url = m.get('detailUrl')

        if m.get('downloads') is not None:
            self.downloads = m.get('downloads')

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

