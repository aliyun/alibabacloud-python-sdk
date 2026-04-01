# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListUserPluginResponseBody(DaraModel):
    def __init__(
        self,
        headers: Dict[str, Any] = None,
        request_id: str = None,
        result: List[main_models.ListUserPluginResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['Headers'] = self.headers

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListUserPluginResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListUserPluginResponseBodyResult(DaraModel):
    def __init__(
        self,
        bingo_plugins: List[main_models.ListUserPluginResponseBodyResultBingoPlugins] = None,
        name: str = None,
        source: str = None,
        state: str = None,
        version: str = None,
    ):
        self.bingo_plugins = bingo_plugins
        self.name = name
        self.source = source
        self.state = state
        self.version = version

    def validate(self):
        if self.bingo_plugins:
            for v1 in self.bingo_plugins:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['bingoPlugins'] = []
        if self.bingo_plugins is not None:
            for k1 in self.bingo_plugins:
                result['bingoPlugins'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.source is not None:
            result['source'] = self.source

        if self.state is not None:
            result['state'] = self.state

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bingo_plugins = []
        if m.get('bingoPlugins') is not None:
            for k1 in m.get('bingoPlugins'):
                temp_model = main_models.ListUserPluginResponseBodyResultBingoPlugins()
                self.bingo_plugins.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ListUserPluginResponseBodyResultBingoPlugins(DaraModel):
    def __init__(
        self,
        description: str = None,
        elasticsearch_version: str = None,
        file_version: str = None,
        name: str = None,
        source: str = None,
        state: str = None,
        version: str = None,
    ):
        self.description = description
        self.elasticsearch_version = elasticsearch_version
        self.file_version = file_version
        self.name = name
        self.source = source
        self.state = state
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.elasticsearch_version is not None:
            result['elasticsearchVersion'] = self.elasticsearch_version

        if self.file_version is not None:
            result['fileVersion'] = self.file_version

        if self.name is not None:
            result['name'] = self.name

        if self.source is not None:
            result['source'] = self.source

        if self.state is not None:
            result['state'] = self.state

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('elasticsearchVersion') is not None:
            self.elasticsearch_version = m.get('elasticsearchVersion')

        if m.get('fileVersion') is not None:
            self.file_version = m.get('fileVersion')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

