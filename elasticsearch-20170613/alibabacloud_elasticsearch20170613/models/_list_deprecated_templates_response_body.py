# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListDeprecatedTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        headers: main_models.ListDeprecatedTemplatesResponseBodyHeaders = None,
        request_id: str = None,
        result: List[main_models.ListDeprecatedTemplatesResponseBodyResult] = None,
    ):
        self.headers = headers
        self.request_id = request_id
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
            temp_model = main_models.ListDeprecatedTemplatesResponseBodyHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListDeprecatedTemplatesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListDeprecatedTemplatesResponseBodyResult(DaraModel):
    def __init__(
        self,
        data_stream: bool = None,
        index_patterns: List[str] = None,
        index_template: str = None,
        order: int = None,
        template: main_models.ListDeprecatedTemplatesResponseBodyResultTemplate = None,
        version: str = None,
    ):
        self.data_stream = data_stream
        self.index_patterns = index_patterns
        self.index_template = index_template
        self.order = order
        self.template = template
        self.version = version

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_stream is not None:
            result['dataStream'] = self.data_stream

        if self.index_patterns is not None:
            result['indexPatterns'] = self.index_patterns

        if self.index_template is not None:
            result['indexTemplate'] = self.index_template

        if self.order is not None:
            result['order'] = self.order

        if self.template is not None:
            result['template'] = self.template.to_map()

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataStream') is not None:
            self.data_stream = m.get('dataStream')

        if m.get('indexPatterns') is not None:
            self.index_patterns = m.get('indexPatterns')

        if m.get('indexTemplate') is not None:
            self.index_template = m.get('indexTemplate')

        if m.get('order') is not None:
            self.order = m.get('order')

        if m.get('template') is not None:
            temp_model = main_models.ListDeprecatedTemplatesResponseBodyResultTemplate()
            self.template = temp_model.from_map(m.get('template'))

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ListDeprecatedTemplatesResponseBodyResultTemplate(DaraModel):
    def __init__(
        self,
        aliases: str = None,
        mappings: str = None,
        settings: str = None,
    ):
        self.aliases = aliases
        self.mappings = mappings
        self.settings = settings

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliases is not None:
            result['aliases'] = self.aliases

        if self.mappings is not None:
            result['mappings'] = self.mappings

        if self.settings is not None:
            result['settings'] = self.settings

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliases') is not None:
            self.aliases = m.get('aliases')

        if m.get('mappings') is not None:
            self.mappings = m.get('mappings')

        if m.get('settings') is not None:
            self.settings = m.get('settings')

        return self

class ListDeprecatedTemplatesResponseBodyHeaders(DaraModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
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

