# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentrun20250910 import models as main_models
from darabonba.model import DaraModel

class ToolInfo(DaraModel):
    def __init__(
        self,
        capconfig: main_models.CAPConfig = None,
        created_at: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        schema: str = None,
        source_type: str = None,
        tool_type: str = None,
        updated_at: str = None,
    ):
        self.capconfig = capconfig
        self.created_at = created_at
        self.description = description
        self.id = id
        self.name = name
        self.schema = schema
        self.source_type = source_type
        self.tool_type = tool_type
        self.updated_at = updated_at

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

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.schema is not None:
            result['schema'] = self.schema

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.tool_type is not None:
            result['toolType'] = self.tool_type

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CAPConfig') is not None:
            temp_model = main_models.CAPConfig()
            self.capconfig = temp_model.from_map(m.get('CAPConfig'))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('schema') is not None:
            self.schema = m.get('schema')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('toolType') is not None:
            self.tool_type = m.get('toolType')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

