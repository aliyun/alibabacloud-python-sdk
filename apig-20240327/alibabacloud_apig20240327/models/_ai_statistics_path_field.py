# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AiStatisticsPathField(DaraModel):
    def __init__(
        self,
        category: str = None,
        description: str = None,
        field_key: str = None,
        io: str = None,
        json_path: str = None,
        name: str = None,
        record_enabled: bool = None,
        rule: str = None,
        sensitive: bool = None,
        source: str = None,
    ):
        self.category = category
        self.description = description
        self.field_key = field_key
        self.io = io
        self.json_path = json_path
        self.name = name
        self.record_enabled = record_enabled
        self.rule = rule
        self.sensitive = sensitive
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.description is not None:
            result['description'] = self.description

        if self.field_key is not None:
            result['fieldKey'] = self.field_key

        if self.io is not None:
            result['io'] = self.io

        if self.json_path is not None:
            result['jsonPath'] = self.json_path

        if self.name is not None:
            result['name'] = self.name

        if self.record_enabled is not None:
            result['recordEnabled'] = self.record_enabled

        if self.rule is not None:
            result['rule'] = self.rule

        if self.sensitive is not None:
            result['sensitive'] = self.sensitive

        if self.source is not None:
            result['source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('fieldKey') is not None:
            self.field_key = m.get('fieldKey')

        if m.get('io') is not None:
            self.io = m.get('io')

        if m.get('jsonPath') is not None:
            self.json_path = m.get('jsonPath')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('recordEnabled') is not None:
            self.record_enabled = m.get('recordEnabled')

        if m.get('rule') is not None:
            self.rule = m.get('rule')

        if m.get('sensitive') is not None:
            self.sensitive = m.get('sensitive')

        if m.get('source') is not None:
            self.source = m.get('source')

        return self

