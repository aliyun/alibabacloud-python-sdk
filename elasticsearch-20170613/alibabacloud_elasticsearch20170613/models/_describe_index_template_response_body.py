# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class DescribeIndexTemplateResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.DescribeIndexTemplateResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.DescribeIndexTemplateResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class DescribeIndexTemplateResponseBodyResult(DaraModel):
    def __init__(
        self,
        data_stream: bool = None,
        ilm_policy: str = None,
        index_patterns: List[str] = None,
        index_template: str = None,
        priority: int = None,
        template: main_models.DescribeIndexTemplateResponseBodyResultTemplate = None,
    ):
        self.data_stream = data_stream
        self.ilm_policy = ilm_policy
        self.index_patterns = index_patterns
        self.index_template = index_template
        self.priority = priority
        self.template = template

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

        if self.ilm_policy is not None:
            result['ilmPolicy'] = self.ilm_policy

        if self.index_patterns is not None:
            result['indexPatterns'] = self.index_patterns

        if self.index_template is not None:
            result['indexTemplate'] = self.index_template

        if self.priority is not None:
            result['priority'] = self.priority

        if self.template is not None:
            result['template'] = self.template.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataStream') is not None:
            self.data_stream = m.get('dataStream')

        if m.get('ilmPolicy') is not None:
            self.ilm_policy = m.get('ilmPolicy')

        if m.get('indexPatterns') is not None:
            self.index_patterns = m.get('indexPatterns')

        if m.get('indexTemplate') is not None:
            self.index_template = m.get('indexTemplate')

        if m.get('priority') is not None:
            self.priority = m.get('priority')

        if m.get('template') is not None:
            temp_model = main_models.DescribeIndexTemplateResponseBodyResultTemplate()
            self.template = temp_model.from_map(m.get('template'))

        return self

class DescribeIndexTemplateResponseBodyResultTemplate(DaraModel):
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

