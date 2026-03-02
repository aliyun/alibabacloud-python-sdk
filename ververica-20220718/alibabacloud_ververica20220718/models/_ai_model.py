# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class AiModel(DaraModel):
    def __init__(
        self,
        comment: str = None,
        input_schema: main_models.Schema = None,
        name: str = None,
        options: Dict[str, str] = None,
        output_schema: main_models.Schema = None,
    ):
        self.comment = comment
        self.input_schema = input_schema
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.options = options
        self.output_schema = output_schema

    def validate(self):
        if self.input_schema:
            self.input_schema.validate()
        if self.output_schema:
            self.output_schema.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        if self.input_schema is not None:
            result['inputSchema'] = self.input_schema.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.options is not None:
            result['options'] = self.options

        if self.output_schema is not None:
            result['outputSchema'] = self.output_schema.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('inputSchema') is not None:
            temp_model = main_models.Schema()
            self.input_schema = temp_model.from_map(m.get('inputSchema'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('options') is not None:
            self.options = m.get('options')

        if m.get('outputSchema') is not None:
            temp_model = main_models.Schema()
            self.output_schema = temp_model.from_map(m.get('outputSchema'))

        return self

