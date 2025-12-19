# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class GetWorkloadIdentityResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        workload_identity: main_models.GetWorkloadIdentityResponseBodyWorkloadIdentity = None,
    ):
        self.request_id = request_id
        self.workload_identity = workload_identity

    def validate(self):
        if self.workload_identity:
            self.workload_identity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.workload_identity is not None:
            result['WorkloadIdentity'] = self.workload_identity.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WorkloadIdentity') is not None:
            temp_model = main_models.GetWorkloadIdentityResponseBodyWorkloadIdentity()
            self.workload_identity = temp_model.from_map(m.get('WorkloadIdentity'))

        return self

class GetWorkloadIdentityResponseBodyWorkloadIdentity(DaraModel):
    def __init__(
        self,
        allowed_resource_oauth2_return_urls: List[str] = None,
        create_time: str = None,
        description: str = None,
        identity_provider_name: str = None,
        role_arn: str = None,
        update_time: str = None,
        workload_identity_arn: str = None,
        workload_identity_name: str = None,
    ):
        self.allowed_resource_oauth2_return_urls = allowed_resource_oauth2_return_urls
        self.create_time = create_time
        self.description = description
        self.identity_provider_name = identity_provider_name
        self.role_arn = role_arn
        self.update_time = update_time
        self.workload_identity_arn = workload_identity_arn
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.identity_provider_name is not None:
            result['IdentityProviderName'] = self.identity_provider_name

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.workload_identity_arn is not None:
            result['WorkloadIdentityArn'] = self.workload_identity_arn

        if self.workload_identity_name is not None:
            result['WorkloadIdentityName'] = self.workload_identity_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedResourceOAuth2ReturnURLs') is not None:
            self.allowed_resource_oauth2_return_urls = m.get('AllowedResourceOAuth2ReturnURLs')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IdentityProviderName') is not None:
            self.identity_provider_name = m.get('IdentityProviderName')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('WorkloadIdentityArn') is not None:
            self.workload_identity_arn = m.get('WorkloadIdentityArn')

        if m.get('WorkloadIdentityName') is not None:
            self.workload_identity_name = m.get('WorkloadIdentityName')

        return self

