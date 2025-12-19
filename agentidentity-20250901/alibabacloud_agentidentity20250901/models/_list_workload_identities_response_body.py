# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class ListWorkloadIdentitiesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        workload_identities: List[main_models.ListWorkloadIdentitiesResponseBodyWorkloadIdentities] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count
        self.workload_identities = workload_identities

    def validate(self):
        if self.workload_identities:
            for v1 in self.workload_identities:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['WorkloadIdentities'] = []
        if self.workload_identities is not None:
            for k1 in self.workload_identities:
                result['WorkloadIdentities'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.workload_identities = []
        if m.get('WorkloadIdentities') is not None:
            for k1 in m.get('WorkloadIdentities'):
                temp_model = main_models.ListWorkloadIdentitiesResponseBodyWorkloadIdentities()
                self.workload_identities.append(temp_model.from_map(k1))

        return self

class ListWorkloadIdentitiesResponseBodyWorkloadIdentities(DaraModel):
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

