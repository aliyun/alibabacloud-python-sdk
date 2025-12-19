# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWorkloadIdentityShrinkRequest(DaraModel):
    def __init__(
        self,
        allowed_resource_oauth2_return_urls_shrink: str = None,
        description: str = None,
        identity_provider_name: str = None,
        role_arn: str = None,
        workload_identity_name: str = None,
    ):
        self.allowed_resource_oauth2_return_urls_shrink = allowed_resource_oauth2_return_urls_shrink
        self.description = description
        self.identity_provider_name = identity_provider_name
        self.role_arn = role_arn
        self.workload_identity_name = workload_identity_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_resource_oauth2_return_urls_shrink is not None:
            result['AllowedResourceOAuth2ReturnURLs'] = self.allowed_resource_oauth2_return_urls_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.identity_provider_name is not None:
            result['IdentityProviderName'] = self.identity_provider_name

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.workload_identity_name is not None:
            result['WorkloadIdentityName'] = self.workload_identity_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedResourceOAuth2ReturnURLs') is not None:
            self.allowed_resource_oauth2_return_urls_shrink = m.get('AllowedResourceOAuth2ReturnURLs')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IdentityProviderName') is not None:
            self.identity_provider_name = m.get('IdentityProviderName')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('WorkloadIdentityName') is not None:
            self.workload_identity_name = m.get('WorkloadIdentityName')

        return self

