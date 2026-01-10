# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class CreateToolInput(DaraModel):
    def __init__(
        self,
        capconfig: main_models.CAPConfig = None,
        description: str = None,
        name: str = None,
        schema: str = None,
        source_type: str = None,
        tool_type: str = None,
    ):
        self.capconfig = capconfig
        self.description = description
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.schema = schema
        # This parameter is required.
        self.source_type = source_type
        # This parameter is required.
        self.tool_type = tool_type

    def validate(self):
        if self.capconfig:
            self.capconfig.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capconfig is not None:
            result['CAPConfig'] = self.capconfig.to_map()

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.schema is not None:
            result['schema'] = self.schema

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.tool_type is not None:
            result['toolType'] = self.tool_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CAPConfig') is not None:
            temp_model = main_models.CAPConfig()
            self.capconfig = temp_model.from_map(m.get('CAPConfig'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('schema') is not None:
            self.schema = m.get('schema')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('toolType') is not None:
            self.tool_type = m.get('toolType')

        return self

