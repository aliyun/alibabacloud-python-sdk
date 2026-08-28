# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class ListAtiAgentRegisterInfosResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.ListAtiAgentRegisterInfosResponseBodyAccessDeniedDetail = None,
        agent_register_infos: main_models.ListAtiAgentRegisterInfosResponseBodyAgentRegisterInfos = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The details about the access denial. This field is returned only when RAM authentication fails.
        self.access_denied_detail = access_denied_detail
        self.agent_register_infos = agent_register_infos
        # The maximum number of records to return in this request.
        self.max_results = max_results
        # The token for the next query.
        self.next_token = next_token
        # The current page number. The start value is 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page in the Settings for the paging query. Maximum value: **100**. Default value: **20**.
        self.page_size = page_size
        # The unique request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_items = total_items
        # The total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.agent_register_infos:
            self.agent_register_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.agent_register_infos is not None:
            result['AgentRegisterInfos'] = self.agent_register_infos.to_map()

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
            temp_model = main_models.ListAtiAgentRegisterInfosResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('AgentRegisterInfos') is not None:
            temp_model = main_models.ListAtiAgentRegisterInfosResponseBodyAgentRegisterInfos()
            self.agent_register_infos = temp_model.from_map(m.get('AgentRegisterInfos'))

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

class ListAtiAgentRegisterInfosResponseBodyAgentRegisterInfos(DaraModel):
    def __init__(
        self,
        agent_register_info: List[main_models.ListAtiAgentRegisterInfosResponseBodyAgentRegisterInfosAgentRegisterInfo] = None,
    ):
        self.agent_register_info = agent_register_info

    def validate(self):
        if self.agent_register_info:
            for v1 in self.agent_register_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AgentRegisterInfo'] = []
        if self.agent_register_info is not None:
            for k1 in self.agent_register_info:
                result['AgentRegisterInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agent_register_info = []
        if m.get('AgentRegisterInfo') is not None:
            for k1 in m.get('AgentRegisterInfo'):
                temp_model = main_models.ListAtiAgentRegisterInfosResponseBodyAgentRegisterInfosAgentRegisterInfo()
                self.agent_register_info.append(temp_model.from_map(k1))

        return self

class ListAtiAgentRegisterInfosResponseBodyAgentRegisterInfosAgentRegisterInfo(DaraModel):
    def __init__(
        self,
        agent_display_name: str = None,
        agent_host: str = None,
        agent_id: str = None,
        agent_register_info_id: str = None,
        agent_version: str = None,
        ati_name: str = None,
        create_timestamp: str = None,
        endpoints: main_models.ListAtiAgentRegisterInfosResponseBodyAgentRegisterInfosAgentRegisterInfoEndpoints = None,
        status: str = None,
        trust_level: str = None,
        update_timestamp: str = None,
    ):
        self.agent_display_name = agent_display_name
        self.agent_host = agent_host
        self.agent_id = agent_id
        self.agent_register_info_id = agent_register_info_id
        self.agent_version = agent_version
        self.ati_name = ati_name
        self.create_timestamp = create_timestamp
        self.endpoints = endpoints
        self.status = status
        self.trust_level = trust_level
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.endpoints:
            self.endpoints.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_display_name is not None:
            result['AgentDisplayName'] = self.agent_display_name

        if self.agent_host is not None:
            result['AgentHost'] = self.agent_host

        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_register_info_id is not None:
            result['AgentRegisterInfoId'] = self.agent_register_info_id

        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

        if self.ati_name is not None:
            result['AtiName'] = self.ati_name

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.trust_level is not None:
            result['TrustLevel'] = self.trust_level

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentDisplayName') is not None:
            self.agent_display_name = m.get('AgentDisplayName')

        if m.get('AgentHost') is not None:
            self.agent_host = m.get('AgentHost')

        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentRegisterInfoId') is not None:
            self.agent_register_info_id = m.get('AgentRegisterInfoId')

        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

        if m.get('AtiName') is not None:
            self.ati_name = m.get('AtiName')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Endpoints') is not None:
            temp_model = main_models.ListAtiAgentRegisterInfosResponseBodyAgentRegisterInfosAgentRegisterInfoEndpoints()
            self.endpoints = temp_model.from_map(m.get('Endpoints'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TrustLevel') is not None:
            self.trust_level = m.get('TrustLevel')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        return self

class ListAtiAgentRegisterInfosResponseBodyAgentRegisterInfosAgentRegisterInfoEndpoints(DaraModel):
    def __init__(
        self,
        endpoint: List[main_models.ListAtiAgentRegisterInfosResponseBodyAgentRegisterInfosAgentRegisterInfoEndpointsEndpoint] = None,
    ):
        self.endpoint = endpoint

    def validate(self):
        if self.endpoint:
            for v1 in self.endpoint:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Endpoint'] = []
        if self.endpoint is not None:
            for k1 in self.endpoint:
                result['Endpoint'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.endpoint = []
        if m.get('Endpoint') is not None:
            for k1 in m.get('Endpoint'):
                temp_model = main_models.ListAtiAgentRegisterInfosResponseBodyAgentRegisterInfosAgentRegisterInfoEndpointsEndpoint()
                self.endpoint.append(temp_model.from_map(k1))

        return self

class ListAtiAgentRegisterInfosResponseBodyAgentRegisterInfosAgentRegisterInfoEndpointsEndpoint(DaraModel):
    def __init__(
        self,
        protocol: str = None,
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

class ListAtiAgentRegisterInfosResponseBodyAccessDeniedDetail(DaraModel):
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
        # The encrypted complete diagnostic message.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # The reason for the authentication failure. Valid values:
        # - ExplicitDeny: explicit denial.
        # - ImplicitDeny: implicit denial.
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

