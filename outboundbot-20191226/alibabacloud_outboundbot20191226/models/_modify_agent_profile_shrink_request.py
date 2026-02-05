# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAgentProfileShrinkRequest(DaraModel):
    def __init__(
        self,
        agent_profile_id: str = None,
        api_plugin_json: str = None,
        description: str = None,
        faq_category_ids_shrink: str = None,
        instance_id: str = None,
        instruction_json: str = None,
        labels_json: str = None,
        model: str = None,
        model_config: str = None,
        prompt: str = None,
        prompt_json: str = None,
        scenario: str = None,
        variables_json: str = None,
    ):
        # This parameter is required.
        self.agent_profile_id = agent_profile_id
        self.api_plugin_json = api_plugin_json
        self.description = description
        self.faq_category_ids_shrink = faq_category_ids_shrink
        # This parameter is required.
        self.instance_id = instance_id
        self.instruction_json = instruction_json
        self.labels_json = labels_json
        self.model = model
        self.model_config = model_config
        self.prompt = prompt
        self.prompt_json = prompt_json
        self.scenario = scenario
        self.variables_json = variables_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_profile_id is not None:
            result['AgentProfileId'] = self.agent_profile_id

        if self.api_plugin_json is not None:
            result['ApiPluginJson'] = self.api_plugin_json

        if self.description is not None:
            result['Description'] = self.description

        if self.faq_category_ids_shrink is not None:
            result['FaqCategoryIds'] = self.faq_category_ids_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instruction_json is not None:
            result['InstructionJson'] = self.instruction_json

        if self.labels_json is not None:
            result['LabelsJson'] = self.labels_json

        if self.model is not None:
            result['Model'] = self.model

        if self.model_config is not None:
            result['ModelConfig'] = self.model_config

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.prompt_json is not None:
            result['PromptJson'] = self.prompt_json

        if self.scenario is not None:
            result['Scenario'] = self.scenario

        if self.variables_json is not None:
            result['VariablesJson'] = self.variables_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentProfileId') is not None:
            self.agent_profile_id = m.get('AgentProfileId')

        if m.get('ApiPluginJson') is not None:
            self.api_plugin_json = m.get('ApiPluginJson')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FaqCategoryIds') is not None:
            self.faq_category_ids_shrink = m.get('FaqCategoryIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstructionJson') is not None:
            self.instruction_json = m.get('InstructionJson')

        if m.get('LabelsJson') is not None:
            self.labels_json = m.get('LabelsJson')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('ModelConfig') is not None:
            self.model_config = m.get('ModelConfig')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('PromptJson') is not None:
            self.prompt_json = m.get('PromptJson')

        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')

        if m.get('VariablesJson') is not None:
            self.variables_json = m.get('VariablesJson')

        return self

