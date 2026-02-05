# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class GetAgentProfileResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAgentProfileResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetAgentProfileResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAgentProfileResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_profile_id: str = None,
        agent_profile_template_id: str = None,
        agent_type: str = None,
        api_plugin_json: str = None,
        create_time: str = None,
        description: str = None,
        instance_id: str = None,
        instruction_json: str = None,
        labels_json: str = None,
        model: str = None,
        model_config: str = None,
        nlu_config_json: str = None,
        prompt: str = None,
        prompt_json: str = None,
        scenario: str = None,
        script_id: str = None,
        system: bool = None,
        update_time: str = None,
        variables_json: str = None,
    ):
        self.agent_profile_id = agent_profile_id
        self.agent_profile_template_id = agent_profile_template_id
        # agent type
        self.agent_type = agent_type
        self.api_plugin_json = api_plugin_json
        self.create_time = create_time
        self.description = description
        self.instance_id = instance_id
        self.instruction_json = instruction_json
        self.labels_json = labels_json
        self.model = model
        self.model_config = model_config
        self.nlu_config_json = nlu_config_json
        self.prompt = prompt
        self.prompt_json = prompt_json
        self.scenario = scenario
        self.script_id = script_id
        self.system = system
        self.update_time = update_time
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

        if self.agent_profile_template_id is not None:
            result['AgentProfileTemplateId'] = self.agent_profile_template_id

        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

        if self.api_plugin_json is not None:
            result['ApiPluginJson'] = self.api_plugin_json

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

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

        if self.nlu_config_json is not None:
            result['NluConfigJson'] = self.nlu_config_json

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.prompt_json is not None:
            result['PromptJson'] = self.prompt_json

        if self.scenario is not None:
            result['Scenario'] = self.scenario

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.system is not None:
            result['System'] = self.system

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.variables_json is not None:
            result['VariablesJson'] = self.variables_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentProfileId') is not None:
            self.agent_profile_id = m.get('AgentProfileId')

        if m.get('AgentProfileTemplateId') is not None:
            self.agent_profile_template_id = m.get('AgentProfileTemplateId')

        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('ApiPluginJson') is not None:
            self.api_plugin_json = m.get('ApiPluginJson')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

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

        if m.get('NluConfigJson') is not None:
            self.nlu_config_json = m.get('NluConfigJson')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('PromptJson') is not None:
            self.prompt_json = m.get('PromptJson')

        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('System') is not None:
            self.system = m.get('System')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VariablesJson') is not None:
            self.variables_json = m.get('VariablesJson')

        return self

