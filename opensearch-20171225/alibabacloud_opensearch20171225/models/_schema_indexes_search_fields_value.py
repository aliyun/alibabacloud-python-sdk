# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SchemaIndexesSearchFieldsValue(DaraModel):
    def __init__(
        self,
        analyzer: str = None,
        analyzer_type: str = None,
        analyzer_generation: str = None,
        fields: List[str] = None,
        label: str = None,
    ):
        self.analyzer = analyzer
        self.analyzer_type = analyzer_type
        self.analyzer_generation = analyzer_generation
        self.fields = fields
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analyzer is not None:
            result['analyzer'] = self.analyzer

        if self.analyzer_type is not None:
            result['analyzerType'] = self.analyzer_type

        if self.analyzer_generation is not None:
            result['analyzerGeneration'] = self.analyzer_generation

        if self.fields is not None:
            result['fields'] = self.fields

        if self.label is not None:
            result['label'] = self.label

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analyzer') is not None:
            self.analyzer = m.get('analyzer')

        if m.get('analyzerType') is not None:
            self.analyzer_type = m.get('analyzerType')

        if m.get('analyzerGeneration') is not None:
            self.analyzer_generation = m.get('analyzerGeneration')

        if m.get('fields') is not None:
            self.fields = m.get('fields')

        if m.get('label') is not None:
            self.label = m.get('label')

        return self

