# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetPromptTemplateResponseBody(DaraModel):
    def __init__(
        self,
        content: str = None,
        name: str = None,
        prompt_template_id: str = None,
        request_id: str = None,
        variables: List[str] = None,
        workspace_id: str = None,
    ):
        # The template content.
        self.content = content
        # The template name.
        self.name = name
        # The template ID.
        self.prompt_template_id = prompt_template_id
        # The request ID.
        self.request_id = request_id
        # The variables of the template.
        self.variables = variables
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.name is not None:
            result['name'] = self.name

        if self.prompt_template_id is not None:
            result['promptTemplateId'] = self.prompt_template_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.variables is not None:
            result['variables'] = self.variables

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('promptTemplateId') is not None:
            self.prompt_template_id = m.get('promptTemplateId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('variables') is not None:
            self.variables = m.get('variables')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

