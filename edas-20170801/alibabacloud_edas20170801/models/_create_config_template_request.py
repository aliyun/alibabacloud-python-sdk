# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateConfigTemplateRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        description: str = None,
        format: str = None,
        name: str = None,
    ):
        # The content of the configuration template. The value must be in the format that is specified by the Format parameter.
        self.content = content
        # The description of the configuration template. The description can be up to 255 characters in length.
        self.description = description
        # The data format of the configuration template. Valid values:
        # 
        # - JSON: JSON format
        # 
        # - XML: XML format
        # 
        # - YAML: YAML format
        # 
        # - Properties: .properties format
        # 
        # - KeyValue: key-value pairs
        # 
        # - Custom: custom format
        self.format = format
        # The name of the configuration template. The name can be up to 64 characters in length.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.description is not None:
            result['Description'] = self.description

        if self.format is not None:
            result['Format'] = self.format

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

