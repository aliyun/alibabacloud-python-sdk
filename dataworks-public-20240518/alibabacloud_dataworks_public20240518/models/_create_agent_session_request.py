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
        # The request ID provided by the client. This ID is returned in the response without modification.
        self.id = id
        # The JSON-RPC version. The value is fixed at `2.0`.
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
        # The extended metadata, which includes information such as agent binding, session source, and session tags.
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
        # The agent configuration for this session. The value must be one of the agents returned by the `ListAgents` API.
        self.agent = agent
        # The configuration parameters for the session, such as filters based on session source and session tags.
        self.config = config
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
    ):
        self.execution_lane = execution_lane
        self.mode = mode

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionLane') is not None:
            self.execution_lane = m.get('ExecutionLane')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        return self

class CreateAgentSessionRequestParamsMetaConfig(DaraModel):
    def __init__(
        self,
        session_source: str = None,
        session_tags: List[main_models.CreateAgentSessionRequestParamsMetaConfigSessionTags] = None,
    ):
        # The identifier for the session source. This allows you to search for sessions by their source. For example, if you use an agent on multiple pages, such as Page A and Page B, you can use this parameter to filter and display only the sessions created on Page A. The identifier can be up to 128 characters and can contain letters, digits, hyphens (-), and underscores (_).
        self.session_source = session_source
        # A list of session tags. You can use these tags to search and filter sessions.
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
        # The session tag. You can use session tags to filter sessions. For example, if your application calls the API with a fixed RAM sub-account but maintains its own user account system, you can pass a user\\"s account ID as a tag. This allows you to filter the session list by your internal account IDs. The tag can be up to 128 characters and can contain letters, digits, hyphens (-), and underscores (_).
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
        # The agent name to bind to the session. This parameter is required.
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

