# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class ListPromptTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        prompt_templates: List[main_models.ListPromptTemplatesResponseBodyPromptTemplates] = None,
        request_id: str = None,
        total_count: int = None,
        workspace_id: str = None,
    ):
        # The maximum number of returned entries.
        self.max_results = max_results
        # The token that determines the start position of the next query.
        self.next_token = next_token
        # The templates.
        self.prompt_templates = prompt_templates
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.prompt_templates:
            for v1 in self.prompt_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['promptTemplates'] = []
        if self.prompt_templates is not None:
            for k1 in self.prompt_templates:
                result['promptTemplates'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.prompt_templates = []
        if m.get('promptTemplates') is not None:
            for k1 in m.get('promptTemplates'):
                temp_model = main_models.ListPromptTemplatesResponseBodyPromptTemplates()
                self.prompt_templates.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class ListPromptTemplatesResponseBodyPromptTemplates(DaraModel):
    def __init__(
        self,
        content: str = None,
        name: str = None,
        prompt_template_id: str = None,
        type: str = None,
        variables: List[str] = None,
    ):
        # The template content
        self.content = content
        # The template name.
        self.name = name
        # The template ID.
        self.prompt_template_id = prompt_template_id
        # The template type.
        self.type = type
        # The variables of the template.
        self.variables = variables

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

        if self.type is not None:
            result['type'] = self.type

        if self.variables is not None:
            result['variables'] = self.variables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('promptTemplateId') is not None:
            self.prompt_template_id = m.get('promptTemplateId')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('variables') is not None:
            self.variables = m.get('variables')

        return self

