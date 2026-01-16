# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class UpdateComponentIndexRequest(DaraModel):
    def __init__(
        self,
        meta: Dict[str, Any] = None,
        template: main_models.UpdateComponentIndexRequestTemplate = None,
    ):
        self.meta = meta
        self.template = template

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('_meta') is not None:
            self.meta = m.get('_meta')

        if m.get('template') is not None:
            temp_model = main_models.UpdateComponentIndexRequestTemplate()
            self.template = temp_model.from_map(m.get('template'))

        return self

class UpdateComponentIndexRequestTemplate(DaraModel):
    def __init__(
        self,
        aliases: Dict[str, Any] = None,
        mappings: Dict[str, Any] = None,
        settings: Dict[str, Any] = None,
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

