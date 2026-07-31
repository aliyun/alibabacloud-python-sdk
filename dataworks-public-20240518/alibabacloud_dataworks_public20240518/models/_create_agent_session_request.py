# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateAgentSessionRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        jsonrpc: str = None,
        params: main_models.CreateAgentSessionRequestParams = None,
    ):
        # The request ID passed by the caller. The value is returned as-is.
        self.id = id
        # The JSON-RPC version. Fixed value: 2.0.
        self.jsonrpc = jsonrpc
        # The business parameters.
        self.params = params

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.jsonrpc is not None:
            result['Jsonrpc'] = self.jsonrpc

        if self.params is not None:
            result['Params'] = self.params.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Jsonrpc') is not None:
            self.jsonrpc = m.get('Jsonrpc')

        if m.get('Params') is not None:
            temp_model = main_models.CreateAgentSessionRequestParams()
            self.params = temp_model.from_map(m.get('Params'))

        return self

class CreateAgentSessionRequestParams(DaraModel):
    def __init__(
        self,
        meta: main_models.CreateAgentSessionRequestParamsMeta = None,
    ):
        # The extended metadata that carries agent binding, session source, tags, and other information.
        self.meta = meta

    def validate(self):
        if self.meta:
            self.meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.meta is not None:
            result['Meta'] = self.meta.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Meta') is not None:
            temp_model = main_models.CreateAgentSessionRequestParamsMeta()
            self.meta = temp_model.from_map(m.get('Meta'))

        return self

class CreateAgentSessionRequestParamsMeta(DaraModel):
    def __init__(
        self,
        agent: main_models.CreateAgentSessionRequestParamsMetaAgent = None,
        config: main_models.CreateAgentSessionRequestParamsMetaConfig = None,
        initial_config_options: main_models.CreateAgentSessionRequestParamsMetaInitialConfigOptions = None,
    ):
        # The agent configuration for the session. Valid values are the results returned by the ListAgents operation.
        self.agent = agent
        # The session parameter settings, such as filtering parameter settings based on session source and session tags.
        self.config = config
        # The advanced parameter settings for the agent execution environment.
        self.initial_config_options = initial_config_options

    def validate(self):
        if self.agent:
            self.agent.validate()
        if self.config:
            self.config.validate()
        if self.initial_config_options:
            self.initial_config_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent is not None:
            result['Agent'] = self.agent.to_map()

        if self.config is not None:
            result['Config'] = self.config.to_map()

        if self.initial_config_options is not None:
            result['InitialConfigOptions'] = self.initial_config_options.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Agent') is not None:
            temp_model = main_models.CreateAgentSessionRequestParamsMetaAgent()
            self.agent = temp_model.from_map(m.get('Agent'))

        if m.get('Config') is not None:
            temp_model = main_models.CreateAgentSessionRequestParamsMetaConfig()
            self.config = temp_model.from_map(m.get('Config'))

        if m.get('InitialConfigOptions') is not None:
            temp_model = main_models.CreateAgentSessionRequestParamsMetaInitialConfigOptions()
            self.initial_config_options = temp_model.from_map(m.get('InitialConfigOptions'))

        return self

class CreateAgentSessionRequestParamsMetaInitialConfigOptions(DaraModel):
    def __init__(
        self,
        execution_lane: str = None,
        mode: str = None,
        resource_group_id: str = None,
        skills: str = None,
    ):
        # The exec mode. Valid values:
        # * chat: conversation mode only. Suitable for simple Q&A scenarios. Advantages: fast response and low token consumption. Disadvantages: cannot handle complex problems.
        # * cli: sandbox mode. Suitable for complex data analytics, data processing, and code writing scenarios. Advantages: can handle complex problems with the model autonomously performing analysis and problem resolution. Disadvantages: slower processing speed and higher token consumption compared to chat mode.
        self.execution_lane = execution_lane
        # The authorization mode for script execution. OpenAPI currently supports only the yolo mode. Valid values:
        # * yolo: automatic authorization. No human intervention is required, and the model can process tasks automatically.
        self.mode = mode
        # The ID of the resource group used for initialization.
        self.resource_group_id = resource_group_id
        # The names of custom skills to load. Separate multiple names with commas (,).
        self.skills = skills

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execution_lane is not None:
            result['ExecutionLane'] = self.execution_lane

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.skills is not None:
            result['Skills'] = self.skills

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionLane') is not None:
            self.execution_lane = m.get('ExecutionLane')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Skills') is not None:
            self.skills = m.get('Skills')

        return self

class CreateAgentSessionRequestParamsMetaConfig(DaraModel):
    def __init__(
        self,
        session_source: str = None,
        session_tags: List[main_models.CreateAgentSessionRequestParamsMetaConfigSessionTags] = None,
    ):
        # The session source identifier for retrieval by source. For example, if an agent is used on both page A and page B, and you want page A to display only sessions created from page A, you can filter based on this parameter. The value can be up to 128 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        self.session_source = session_source
        # The list of session tags. You can use session tags for search and filtering.
        self.session_tags = session_tags

    def validate(self):
        if self.session_tags:
            for v1 in self.session_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_source is not None:
            result['SessionSource'] = self.session_source

        result['SessionTags'] = []
        if self.session_tags is not None:
            for k1 in self.session_tags:
                result['SessionTags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionSource') is not None:
            self.session_source = m.get('SessionSource')

        self.session_tags = []
        if m.get('SessionTags') is not None:
            for k1 in m.get('SessionTags'):
                temp_model = main_models.CreateAgentSessionRequestParamsMetaConfigSessionTags()
                self.session_tags.append(temp_model.from_map(k1))

        return self

class CreateAgentSessionRequestParamsMetaConfigSessionTags(DaraModel):
    def __init__(
        self,
        session_tag_code: str = None,
    ):
        # The session tag. You can filter sessions based on session tags. For example, if you use a fixed RAM user to call OpenAPI operations but your calling system has its own account system, you can pass the account ID of your calling system as this tag to filter the session list by account ID. The value can be up to 128 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        self.session_tag_code = session_tag_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_tag_code is not None:
            result['SessionTagCode'] = self.session_tag_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionTagCode') is not None:
            self.session_tag_code = m.get('SessionTagCode')

        return self

class CreateAgentSessionRequestParamsMetaAgent(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
    ):
        # The name of the agent bound to the session. This parameter is required.
        # * dataworks_data_agent: DataWorks built-in agent — Data Agent, which provides intelligent data development AI capabilities covering the entire workflow of data integration, development, O&M, governance, and analytics.
        # * dataworks_chatbi_agent: DataWorks built-in agent — ChatBI, which uses natural language processing and intelligent analytics technologies to automate the entire analysis workflow from requirement parsing, data extraction, and automatic code generation to visualization report output through conversational interaction.
        # * dataworks_ai_assistant_agent: DataWorks built-in agent — AI Assistant Service, which is a DataWorks enterprise-grade dedicated AI assistant built on open source frameworks such as OpenClaw and Hermes Agent.
        self.agent_name = agent_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        return self

