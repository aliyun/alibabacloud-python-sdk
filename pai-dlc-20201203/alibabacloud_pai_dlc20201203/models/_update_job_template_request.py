# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class UpdateJobTemplateRequest(DaraModel):
    def __init__(
        self,
        constraints: Dict[str, Any] = None,
        content: str = None,
        description: str = None,
        metadata: Dict[str, Any] = None,
        set_as_default: bool = None,
        template_name: str = None,
        version: int = None,
    ):
        # The field constraints. The key is a JSONPath expression and the value is the constraint type. Valid values are `locked`, `overridable`, and `required`. This parameter must be specified with `Content` and cannot be updated on its own.
        self.constraints = constraints
        # The configuration content of the job template. This parameter supports all fields from the `CreateJob` operation and must be in JSON format. Specifying this parameter creates a new version.
        self.content = content
        # The description of the job template.
        self.description = description
        # User-defined key-value pairs.
        self.metadata = metadata
        # If `true`, the new version becomes the default version.
        self.set_as_default = set_as_default
        # The name of the job template.
        self.template_name = template_name
        # This field is not supported.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.constraints is not None:
            result['Constraints'] = self.constraints

        if self.content is not None:
            result['Content'] = self.content

        if self.description is not None:
            result['Description'] = self.description

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.set_as_default is not None:
            result['SetAsDefault'] = self.set_as_default

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Constraints') is not None:
            self.constraints = m.get('Constraints')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('SetAsDefault') is not None:
            self.set_as_default = m.get('SetAsDefault')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

