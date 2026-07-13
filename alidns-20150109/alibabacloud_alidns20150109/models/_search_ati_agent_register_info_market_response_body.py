# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class SearchAtiAgentRegisterInfoMarketResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.SearchAtiAgentRegisterInfoMarketResponseBodyAccessDeniedDetail = None,
        agents: main_models.SearchAtiAgentRegisterInfoMarketResponseBodyAgents = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The details of the access denial. This field is returned only when RAM authentication fails.
        self.access_denied_detail = access_denied_detail
        self.agents = agents
        # The number of entries per batch query.
        self.max_results = max_results
        # The pagination token for the next query.
        self.next_token = next_token
        # The current page number. Minimum value: **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page for the paged query. Settings: maximum value: **100**. Default value: **20**. This parameter controls paging behavior.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_items = total_items
        # The total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.agents:
            self.agents.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.agents is not None:
            result['Agents'] = self.agents.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.SearchAtiAgentRegisterInfoMarketResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Agents') is not None:
            temp_model = main_models.SearchAtiAgentRegisterInfoMarketResponseBodyAgents()
            self.agents = temp_model.from_map(m.get('Agents'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class SearchAtiAgentRegisterInfoMarketResponseBodyAgents(DaraModel):
    def __init__(
        self,
        agent: List[main_models.SearchAtiAgentRegisterInfoMarketResponseBodyAgentsAgent] = None,
    ):
        self.agent = agent

    def validate(self):
        if self.agent:
            for v1 in self.agent:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Agent'] = []
        if self.agent is not None:
            for k1 in self.agent:
                result['Agent'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agent = []
        if m.get('Agent') is not None:
            for k1 in m.get('Agent'):
                temp_model = main_models.SearchAtiAgentRegisterInfoMarketResponseBodyAgentsAgent()
                self.agent.append(temp_model.from_map(k1))

        return self

class SearchAtiAgentRegisterInfoMarketResponseBodyAgentsAgent(DaraModel):
    def __init__(
        self,
        agent_description: str = None,
        agent_display_name: str = None,
        agent_host: str = None,
        agent_id: str = None,
        agent_version: str = None,
        create_timestamp: int = None,
        protocols: main_models.SearchAtiAgentRegisterInfoMarketResponseBodyAgentsAgentProtocols = None,
        status: str = None,
        trust_card_url: str = None,
        trust_level: str = None,
        update_timestamp: int = None,
    ):
        self.agent_description = agent_description
        self.agent_display_name = agent_display_name
        self.agent_host = agent_host
        self.agent_id = agent_id
        self.agent_version = agent_version
        self.create_timestamp = create_timestamp
        self.protocols = protocols
        self.status = status
        self.trust_card_url = trust_card_url
        self.trust_level = trust_level
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.protocols:
            self.protocols.validate()

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

        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.protocols is not None:
            result['Protocols'] = self.protocols.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.trust_card_url is not None:
            result['TrustCardUrl'] = self.trust_card_url

        if self.trust_level is not None:
            result['TrustLevel'] = self.trust_level

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentDescription') is not None:
            self.agent_description = m.get('AgentDescription')

        if m.get('AgentDisplayName') is not None:
            self.agent_display_name = m.get('AgentDisplayName')

        if m.get('AgentHost') is not None:
            self.agent_host = m.get('AgentHost')

        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Protocols') is not None:
            temp_model = main_models.SearchAtiAgentRegisterInfoMarketResponseBodyAgentsAgentProtocols()
            self.protocols = temp_model.from_map(m.get('Protocols'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TrustCardUrl') is not None:
            self.trust_card_url = m.get('TrustCardUrl')

        if m.get('TrustLevel') is not None:
            self.trust_level = m.get('TrustLevel')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        return self

class SearchAtiAgentRegisterInfoMarketResponseBodyAgentsAgentProtocols(DaraModel):
    def __init__(
        self,
        protocol: List[str] = None,
    ):
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

class SearchAtiAgentRegisterInfoMarketResponseBodyAccessDeniedDetail(DaraModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        # The unauthorized operation that was attempted.
        self.auth_action = auth_action
        # The display name of the authorization principal.
        self.auth_principal_display_name = auth_principal_display_name
        # The owner ID of the authorization principal.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The identity type.
        self.auth_principal_type = auth_principal_type
        # The encrypted diagnostic message.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # The reason for the authentication failure. Valid values:
        # - ExplicitDeny: explicit deny.
        # - ImplicitDeny: implicit deny.
        self.no_permission_type = no_permission_type
        # The policy type.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action

        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name

        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id

        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type

        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message

        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')

        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')

        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')

        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')

        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')

        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

