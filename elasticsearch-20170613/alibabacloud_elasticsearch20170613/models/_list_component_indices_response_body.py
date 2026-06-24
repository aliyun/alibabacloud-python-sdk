# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListComponentIndicesResponseBody(DaraModel):
    def __init__(
        self,
        headers: main_models.ListComponentIndicesResponseBodyHeaders = None,
        request_id: str = None,
        result: List[main_models.ListComponentIndicesResponseBodyResult] = None,
    ):
        # The response headers.
        self.headers = headers
        # The request ID.
        self.request_id = request_id
        # The details of the returned results.
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
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
            result['Headers'] = self.headers.to_map()

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
            temp_model = main_models.ListComponentIndicesResponseBodyHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListComponentIndicesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListComponentIndicesResponseBodyResult(DaraModel):
    def __init__(
        self,
        composed: List[str] = None,
        content: main_models.ListComponentIndicesResponseBodyResultContent = None,
        name: str = None,
    ):
        # The information about the index templates that reference this composable template.
        self.composed = composed
        # The content of the composable template.
        self.content = content
        # The name of the composable template.
        self.name = name

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.composed is not None:
            result['composed'] = self.composed

        if self.content is not None:
            result['content'] = self.content.to_map()

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('composed') is not None:
            self.composed = m.get('composed')

        if m.get('content') is not None:
            temp_model = main_models.ListComponentIndicesResponseBodyResultContent()
            self.content = temp_model.from_map(m.get('content'))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ListComponentIndicesResponseBodyResultContent(DaraModel):
    def __init__(
        self,
        meta: Dict[str, Any] = None,
        template: main_models.ListComponentIndicesResponseBodyResultContentTemplate = None,
        version: int = None,
    ):
        # The metadata, which is used to store information such as remarks.
        self.meta = meta
        # The composable template object.
        self.template = template
        # The version of the composable template.
        self.version = version

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.meta is not None:
            result['_meta'] = self.meta

        if self.template is not None:
            result['template'] = self.template.to_map()

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('_meta') is not None:
            self.meta = m.get('_meta')

        if m.get('template') is not None:
            temp_model = main_models.ListComponentIndicesResponseBodyResultContentTemplate()
            self.template = temp_model.from_map(m.get('template'))

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ListComponentIndicesResponseBodyResultContentTemplate(DaraModel):
    def __init__(
        self,
        settings: main_models.ListComponentIndicesResponseBodyResultContentTemplateSettings = None,
    ):
        # The settings configuration of the template.
        self.settings = settings

    def validate(self):
        if self.settings:
            self.settings.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.settings is not None:
            result['settings'] = self.settings.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('settings') is not None:
            temp_model = main_models.ListComponentIndicesResponseBodyResultContentTemplateSettings()
            self.settings = temp_model.from_map(m.get('settings'))

        return self

class ListComponentIndicesResponseBodyResultContentTemplateSettings(DaraModel):
    def __init__(
        self,
        index: main_models.ListComponentIndicesResponseBodyResultContentTemplateSettingsIndex = None,
    ):
        # The index information.
        self.index = index

    def validate(self):
        if self.index:
            self.index.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['index'] = self.index.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('index') is not None:
            temp_model = main_models.ListComponentIndicesResponseBodyResultContentTemplateSettingsIndex()
            self.index = temp_model.from_map(m.get('index'))

        return self

class ListComponentIndicesResponseBodyResultContentTemplateSettingsIndex(DaraModel):
    def __init__(
        self,
        codec: str = None,
        lifecycle: main_models.ListComponentIndicesResponseBodyResultContentTemplateSettingsIndexLifecycle = None,
    ):
        # The index compression method. Valid values:
        # 
        # - LZ4: the default compression algorithm of Elasticsearch. It provides fast compression and decompression but a relatively lower compression ratio.
        # - best_compression: uses the best_compression algorithm for compression, which provides a higher compression ratio.
        self.codec = codec
        # The index lifecycle configuration.
        self.lifecycle = lifecycle

    def validate(self):
        if self.lifecycle:
            self.lifecycle.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.codec is not None:
            result['codec'] = self.codec

        if self.lifecycle is not None:
            result['lifecycle'] = self.lifecycle.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codec') is not None:
            self.codec = m.get('codec')

        if m.get('lifecycle') is not None:
            temp_model = main_models.ListComponentIndicesResponseBodyResultContentTemplateSettingsIndexLifecycle()
            self.lifecycle = temp_model.from_map(m.get('lifecycle'))

        return self

class ListComponentIndicesResponseBodyResultContentTemplateSettingsIndexLifecycle(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the lifecycle policy.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ListComponentIndicesResponseBodyHeaders(DaraModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        # The total number of entries returned.
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')

        return self

