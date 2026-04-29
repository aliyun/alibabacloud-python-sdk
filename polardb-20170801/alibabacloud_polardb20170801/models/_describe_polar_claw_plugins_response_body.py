# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarClawPluginsResponseBody(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        code: int = None,
        diagnostics: List[main_models.DescribePolarClawPluginsResponseBodyDiagnostics] = None,
        message: str = None,
        plugins: List[main_models.DescribePolarClawPluginsResponseBodyPlugins] = None,
        request_id: str = None,
    ):
        self.application_id = application_id
        self.code = code
        self.diagnostics = diagnostics
        self.message = message
        self.plugins = plugins
        self.request_id = request_id

    def validate(self):
        if self.diagnostics:
            for v1 in self.diagnostics:
                 if v1:
                    v1.validate()
        if self.plugins:
            for v1 in self.plugins:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        result['Diagnostics'] = []
        if self.diagnostics is not None:
            for k1 in self.diagnostics:
                result['Diagnostics'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        result['Plugins'] = []
        if self.plugins is not None:
            for k1 in self.plugins:
                result['Plugins'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.diagnostics = []
        if m.get('Diagnostics') is not None:
            for k1 in m.get('Diagnostics'):
                temp_model = main_models.DescribePolarClawPluginsResponseBodyDiagnostics()
                self.diagnostics.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.plugins = []
        if m.get('Plugins') is not None:
            for k1 in m.get('Plugins'):
                temp_model = main_models.DescribePolarClawPluginsResponseBodyPlugins()
                self.plugins.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePolarClawPluginsResponseBodyPlugins(DaraModel):
    def __init__(
        self,
        channel_ids: List[str] = None,
        description: str = None,
        error: str = None,
        format: str = None,
        id: str = None,
        name: str = None,
        origin: str = None,
        provider_ids: List[str] = None,
        source: str = None,
        status: str = None,
        version: str = None,
    ):
        self.channel_ids = channel_ids
        self.description = description
        self.error = error
        self.format = format
        self.id = id
        self.name = name
        self.origin = origin
        self.provider_ids = provider_ids
        self.source = source
        self.status = status
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_ids is not None:
            result['ChannelIds'] = self.channel_ids

        if self.description is not None:
            result['Description'] = self.description

        if self.error is not None:
            result['Error'] = self.error

        if self.format is not None:
            result['Format'] = self.format

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.provider_ids is not None:
            result['ProviderIds'] = self.provider_ids

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelIds') is not None:
            self.channel_ids = m.get('ChannelIds')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('ProviderIds') is not None:
            self.provider_ids = m.get('ProviderIds')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribePolarClawPluginsResponseBodyDiagnostics(DaraModel):
    def __init__(
        self,
        level: str = None,
        message: str = None,
        plugin_id: str = None,
        source: str = None,
    ):
        self.level = level
        self.message = message
        self.plugin_id = plugin_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level is not None:
            result['Level'] = self.level

        if self.message is not None:
            result['Message'] = self.message

        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self

