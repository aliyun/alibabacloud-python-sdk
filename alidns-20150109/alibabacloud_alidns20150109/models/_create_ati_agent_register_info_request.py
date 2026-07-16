# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class CreateAtiAgentRegisterInfoRequest(DaraModel):
    def __init__(
        self,
        agent_description: str = None,
        agent_display_name: str = None,
        agent_host: str = None,
        agent_version: str = None,
        client_token: str = None,
        endpoints: List[main_models.CreateAtiAgentRegisterInfoRequestEndpoints] = None,
        registrant_id: str = None,
    ):
        # The description of the agent capabilities.
        self.agent_description = agent_description
        # The display name of the agent.
        # 
        # This parameter is required.
        self.agent_display_name = agent_display_name
        # The endpoint domain name through which the agent provides services.
        # 
        # This parameter is required.
        self.agent_host = agent_host
        # The version of the agent.
        # 
        # This parameter is required.
        self.agent_version = agent_version
        # Provides idempotency. Within 3 minutes, the same value takes effect only once.
        self.client_token = client_token
        # The endpoint information of the agent.
        # 
        # This parameter is required.
        self.endpoints = endpoints
        # The ID of the verified registrant. Obtain this ID by invoking the identity verification API operation or from the ATS console.
        # 
        # This parameter is required.
        self.registrant_id = registrant_id

    def validate(self):
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_description is not None:
            result['AgentDescription'] = self.agent_description

        if self.agent_display_name is not None:
            result['AgentDisplayName'] = self.agent_display_name

        if self.agent_host is not None:
            result['AgentHost'] = self.agent_host

        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

        if self.registrant_id is not None:
            result['RegistrantId'] = self.registrant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentDescription') is not None:
            self.agent_description = m.get('AgentDescription')

        if m.get('AgentDisplayName') is not None:
            self.agent_display_name = m.get('AgentDisplayName')

        if m.get('AgentHost') is not None:
            self.agent_host = m.get('AgentHost')

        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.CreateAtiAgentRegisterInfoRequestEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('RegistrantId') is not None:
            self.registrant_id = m.get('RegistrantId')

        return self

class CreateAtiAgentRegisterInfoRequestEndpoints(DaraModel):
    def __init__(
        self,
        agent_url: str = None,
        metadata_url: str = None,
        protocol: str = None,
        transports: List[str] = None,
    ):
        # The actual service address of the agent endpoint, which is the HTTPS entry point where the agent runs online. This is a required field with a maximum of 500 characters.
        # 
        # Example: https://my-agent.example.com/mcp
        # 
        # After a caller discovers this agent through DNS, it can use this URL to initiate a connection directly. This is the address where the agent is actually online.
        self.agent_url = agent_url
        # An optional URL that points to the metadata description file of the agent (typically in JSON format). This allows other agents or clients to automatically discover the agent capabilities before connecting, including:
        # - Functions supported by the agent
        # - Input/output formats
        # - Version information
        # - Other capability declarations
        self.metadata_url = metadata_url
        # The communication protocol standard that the agent endpoint follows. This determines how the invoker interacts with the agent.
        # 
        # Valid values:
        # - MCP: Model Context Protocol, an agent tool invocation protocol developed by Anthropic.
        # - A2A: Agent-to-Agent Protocol, a cross-agent communication protocol developed by Google.
        # - OpenAPI: Standard RESTful API specification (Swagger/OpenAPI).
        # 
        # When other agents or clients see this protocol identity, they know which method to use to communicate with the agent. For example, MCP uses the MCP SDK, A2A uses the A2A SDK, and OpenAPI uses standard HTTP requests.
        self.protocol = protocol
        # The transport methods.
        self.transports = transports

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_url is not None:
            result['AgentUrl'] = self.agent_url

        if self.metadata_url is not None:
            result['MetadataUrl'] = self.metadata_url

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.transports is not None:
            result['Transports'] = self.transports

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentUrl') is not None:
            self.agent_url = m.get('AgentUrl')

        if m.get('MetadataUrl') is not None:
            self.metadata_url = m.get('MetadataUrl')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('Transports') is not None:
            self.transports = m.get('Transports')

        return self

