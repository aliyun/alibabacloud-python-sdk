# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class ListSecurityPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        security_policies: List[main_models.ListSecurityPoliciesResponseBodySecurityPolicies] = None,
        total_count: int = None,
    ):
        # The number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value is returned for **NextToken**, the value is the token that determines the start point of the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The supported security policies.
        self.security_policies = security_policies
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.security_policies:
            for v1 in self.security_policies:
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

        result['SecurityPolicies'] = []
        if self.security_policies is not None:
            for k1 in self.security_policies:
                result['SecurityPolicies'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.security_policies = []
        if m.get('SecurityPolicies') is not None:
            for k1 in m.get('SecurityPolicies'):
                temp_model = main_models.ListSecurityPoliciesResponseBodySecurityPolicies()
                self.security_policies.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSecurityPoliciesResponseBodySecurityPolicies(DaraModel):
    def __init__(
        self,
        ciphers: List[str] = None,
        create_time: str = None,
        resource_group_id: str = None,
        security_policy_id: str = None,
        security_policy_name: str = None,
        security_policy_status: str = None,
        tlsversions: List[str] = None,
        tags: List[main_models.ListSecurityPoliciesResponseBodySecurityPoliciesTags] = None,
    ):
        # The supported cipher suites.
        self.ciphers = ciphers
        # The time when the ACL was created. The time follows the `YYYY-MM-DDThh:mm:ssZ` format.
        self.create_time = create_time
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the security policy.
        self.security_policy_id = security_policy_id
        # The name of the security policy.
        self.security_policy_name = security_policy_name
        # The status of the security policy. Valid values:
        # 
        # *   **Configuring**
        # *   **Available**
        self.security_policy_status = security_policy_status
        # The supported TLS protocol versions.
        self.tlsversions = tlsversions
        # The tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ciphers is not None:
            result['Ciphers'] = self.ciphers

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id

        if self.security_policy_name is not None:
            result['SecurityPolicyName'] = self.security_policy_name

        if self.security_policy_status is not None:
            result['SecurityPolicyStatus'] = self.security_policy_status

        if self.tlsversions is not None:
            result['TLSVersions'] = self.tlsversions

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')

        if m.get('SecurityPolicyName') is not None:
            self.security_policy_name = m.get('SecurityPolicyName')

        if m.get('SecurityPolicyStatus') is not None:
            self.security_policy_status = m.get('SecurityPolicyStatus')

        if m.get('TLSVersions') is not None:
            self.tlsversions = m.get('TLSVersions')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListSecurityPoliciesResponseBodySecurityPoliciesTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListSecurityPoliciesResponseBodySecurityPoliciesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The tag key can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https://.
        self.key = key
        # The tag value. The tag value can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https://.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

