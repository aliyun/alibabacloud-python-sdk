# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTemplateRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        tags: str = None,
        template: str = None,
        template_type: str = None,
    ):
        # The description of the template.
        self.description = description
        # The name of the orchestration template.
        # 
        # The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen (-).
        # 
        # This parameter is required.
        self.name = name
        # The label of the template.
        self.tags = tags
        # The template content in the YAML format.
        # 
        # This parameter is required.
        self.template = template
        # The template type.
        # 
        # *   If the parameter is set to `kubernetes`, the template is displayed on the Templates page in the console.
        # *   If this parameter is not specified or the value is set to another value, the template is not displayed on the Orchestration Template page in the console.
        # 
        # We recommend that you set the parameter to `kubernetes`.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.tags is not None:
            result['tags'] = self.tags

        if self.template is not None:
            result['template'] = self.template

        if self.template_type is not None:
            result['template_type'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('template') is not None:
            self.template = m.get('template')

        if m.get('template_type') is not None:
            self.template_type = m.get('template_type')

        return self

