# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateKnowledgeBaseBuildTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        content_locale: str = None,
        description: str = None,
        input_shrink: str = None,
        knowledge_base_id: str = None,
        llm_model: str = None,
        name: str = None,
        project_id: int = None,
        runtime_resource_shrink: str = None,
        task_id: str = None,
        trigger_shrink: str = None,
    ):
        # The content language.
        self.content_locale = content_locale
        # The new description.
        self.description = description
        # The input configuration that completely replaces the original input.
        self.input_shrink = input_shrink
        # The associated knowledge base.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The specific model ID or AUTO.
        self.llm_model = llm_model
        # The new task name.
        self.name = name
        # The workspace used for future runs.
        self.project_id = project_id
        # Updates the runtime resources based on the submitted fields. If ResourceGroupId or Cu is not provided, the original value is retained.
        self.runtime_resource_shrink = runtime_resource_shrink
        # The task ID.
        # 
        # This parameter is required.
        self.task_id = task_id
        # The trigger configuration that completely replaces the original trigger.
        self.trigger_shrink = trigger_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.trigger_shrink is not None:
            result['Trigger'] = self.trigger_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Trigger') is not None:
            self.trigger_shrink = m.get('Trigger')

        return self

