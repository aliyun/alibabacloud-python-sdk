# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKnowledgeBaseBuildTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        content_locale: str = None,
        description: str = None,
        input_shrink: str = None,
        knowledge_base_id: str = None,
        llm_model: str = None,
        name: str = None,
        project_id: int = None,
        runtime_resource_shrink: str = None,
        trigger_shrink: str = None,
        type: str = None,
    ):
        # The idempotency token for the creation request.
        self.client_token = client_token
        # The language of the content.
        self.content_locale = content_locale
        # The description of the task. The description can be up to 1,024 characters in length. If this parameter is omitted, no description is set.
        self.description = description
        # Specifies the input scope by selecting projects, entities, sources, or files based on the type.
        # 
        # This parameter is required.
        self.input_shrink = input_shrink
        # The ID of the knowledge base to which the task belongs.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The specific model ID or AUTO.
        self.llm_model = llm_model
        # The name of the task.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the workspace where the task runs.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The resource group and Builder compute units (CUs).
        # 
        # This parameter is required.
        self.runtime_resource_shrink = runtime_resource_shrink
        # The manual or periodic trigger configuration.
        self.trigger_shrink = trigger_shrink
        # The available build types.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.content_locale is not None:
            result['ContentLocale'] = self.content_locale

        if self.description is not None:
            result['Description'] = self.description

        if self.input_shrink is not None:
            result['Input'] = self.input_shrink

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.llm_model is not None:
            result['LlmModel'] = self.llm_model

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.runtime_resource_shrink is not None:
            result['RuntimeResource'] = self.runtime_resource_shrink

        if self.trigger_shrink is not None:
            result['Trigger'] = self.trigger_shrink

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ContentLocale') is not None:
            self.content_locale = m.get('ContentLocale')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('LlmModel') is not None:
            self.llm_model = m.get('LlmModel')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RuntimeResource') is not None:
            self.runtime_resource_shrink = m.get('RuntimeResource')

        if m.get('Trigger') is not None:
            self.trigger_shrink = m.get('Trigger')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

