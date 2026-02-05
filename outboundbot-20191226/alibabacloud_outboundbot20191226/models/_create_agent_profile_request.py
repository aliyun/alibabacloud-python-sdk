# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAgentProfileRequest(DaraModel):
    def __init__(
        self,
        agent_profile_template_id: str = None,
        app_ip: str = None,
        description: str = None,
        faq_category_ids: str = None,
        instance_id: str = None,
        instruction_json: str = None,
        labels_json: str = None,
        model: str = None,
        model_config: str = None,
        prompt: str = None,
        prompt_json: str = None,
        scenario: str = None,
        script_id: str = None,
        variables_json: str = None,
    ):
        # This parameter is required.
        self.agent_profile_template_id = agent_profile_template_id
        self.app_ip = app_ip
        self.description = description
        self.faq_category_ids = faq_category_ids
        # This parameter is required.
        self.instance_id = instance_id
        self.instruction_json = instruction_json
        self.labels_json = labels_json
        # This parameter is required.
        self.model = model
        self.model_config = model_config
        self.prompt = prompt
        self.prompt_json = prompt_json
        self.scenario = scenario
        # This parameter is required.
        self.script_id = script_id
        self.variables_json = variables_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_profile_template_id is not None:
            result['AgentProfileTemplateId'] = self.agent_profile_template_id

        if self.app_ip is not None:
            result['AppIp'] = self.app_ip

        if self.description is not None:
            result['Description'] = self.description

        if self.faq_category_ids is not None:
            result['FaqCategoryIds'] = self.faq_category_ids

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

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.variables_json is not None:
            result['VariablesJson'] = self.variables_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentProfileTemplateId') is not None:
            self.agent_profile_template_id = m.get('AgentProfileTemplateId')

        if m.get('AppIp') is not None:
            self.app_ip = m.get('AppIp')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FaqCategoryIds') is not None:
            self.faq_category_ids = m.get('FaqCategoryIds')

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

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('VariablesJson') is not None:
            self.variables_json = m.get('VariablesJson')

        return self

