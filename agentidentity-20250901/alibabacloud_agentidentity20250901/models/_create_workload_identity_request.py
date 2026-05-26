# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateWorkloadIdentityRequest(DaraModel):
    def __init__(
        self,
        allowed_resource_oauth2_return_urls: List[str] = None,
        create_ramrole: bool = None,
        description: str = None,
        identity_provider_name: str = None,
        role_arn: str = None,
        session_binding_enabled: bool = None,
        source_agent_arn: str = None,
        source_platform: str = None,
        workload_identity_name: str = None,
    ):
        self.allowed_resource_oauth2_return_urls = allowed_resource_oauth2_return_urls
        self.create_ramrole = create_ramrole
        self.description = description
        self.identity_provider_name = identity_provider_name
        self.role_arn = role_arn
        self.session_binding_enabled = session_binding_enabled
        self.source_agent_arn = source_agent_arn
        self.source_platform = source_platform
        self.workload_identity_name = workload_identity_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_resource_oauth2_return_urls is not None:
            result['AllowedResourceOAuth2ReturnURLs'] = self.allowed_resource_oauth2_return_urls

        if self.create_ramrole is not None:
            result['CreateRAMRole'] = self.create_ramrole

        if self.description is not None:
            result['Description'] = self.description

        if self.identity_provider_name is not None:
            result['IdentityProviderName'] = self.identity_provider_name

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.session_binding_enabled is not None:
            result['SessionBindingEnabled'] = self.session_binding_enabled

        if self.source_agent_arn is not None:
            result['SourceAgentArn'] = self.source_agent_arn

        if self.source_platform is not None:
            result['SourcePlatform'] = self.source_platform

        if self.workload_identity_name is not None:
            result['WorkloadIdentityName'] = self.workload_identity_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedResourceOAuth2ReturnURLs') is not None:
            self.allowed_resource_oauth2_return_urls = m.get('AllowedResourceOAuth2ReturnURLs')

        if m.get('CreateRAMRole') is not None:
            self.create_ramrole = m.get('CreateRAMRole')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IdentityProviderName') is not None:
            self.identity_provider_name = m.get('IdentityProviderName')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('SessionBindingEnabled') is not None:
            self.session_binding_enabled = m.get('SessionBindingEnabled')

        if m.get('SourceAgentArn') is not None:
            self.source_agent_arn = m.get('SourceAgentArn')

        if m.get('SourcePlatform') is not None:
            self.source_platform = m.get('SourcePlatform')

        if m.get('WorkloadIdentityName') is not None:
            self.workload_identity_name = m.get('WorkloadIdentityName')

        return self

