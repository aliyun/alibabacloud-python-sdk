# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nlb20220430 import models as main_models
from darabonba.model import DaraModel

class ListSecurityPolicyResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        security_policies: List[main_models.ListSecurityPolicyResponseBodySecurityPolicies] = None,
        total_count: int = None,
    ):
        # The number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If NextToken is empty, no next page exists.
        # *   If a value is returned for NextToken, specify the value in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The TLS security policies.
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
                temp_model = main_models.ListSecurityPolicyResponseBodySecurityPolicies()
                self.security_policies.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSecurityPolicyResponseBodySecurityPolicies(DaraModel):
    def __init__(
        self,
        ciphers: str = None,
        region_id: str = None,
        related_listeners: List[main_models.ListSecurityPolicyResponseBodySecurityPoliciesRelatedListeners] = None,
        resource_group_id: str = None,
        security_policy_id: str = None,
        security_policy_name: str = None,
        security_policy_status: str = None,
        tags: List[main_models.ListSecurityPolicyResponseBodySecurityPoliciesTags] = None,
        tls_version: str = None,
    ):
        # The cipher suites supported by the security policy. Valid values of this parameter vary based on the value of TlsVersions. A security policy supports up to 32 cipher suites.
        # 
        # TLSv1.0 and TLSv1.1 support the following cipher suites:
        # 
        # *   **ECDHE-ECDSA-AES128-SHA**
        # *   **ECDHE-ECDSA-AES256-SHA**
        # *   **ECDHE-RSA-AES128-SHA**
        # *   **ECDHE-RSA-AES256-SHA**
        # *   **AES128-SHA**
        # *   **AES256-SHA**
        # *   **DES-CBC3-SHA**
        # 
        # TLSv1.2 supports the following cipher suites:
        # 
        # *   **ECDHE-ECDSA-AES128-SHA**
        # *   **ECDHE-ECDSA-AES256-SHA**
        # *   **ECDHE-RSA-AES128-SHA**
        # *   **ECDHE-RSA-AES256-SHA**
        # *   **AES128-SHA**
        # *   **AES256-SHA**
        # *   **DES-CBC3-SHA**
        # *   **ECDHE-ECDSA-AES128-GCM-SHA256**
        # *   **ECDHE-ECDSA-AES256-GCM-SHA384**
        # *   **ECDHE-ECDSA-AES128-SHA256**
        # *   **ECDHE-ECDSA-AES256-SHA384**
        # *   **ECDHE-RSA-AES128-GCM-SHA256**
        # *   **ECDHE-RSA-AES256-GCM-SHA384**
        # *   **ECDHE-RSA-AES128-SHA256**
        # *   **ECDHE-RSA-AES256-SHA384**
        # *   **AES128-GCM-SHA256**
        # *   **AES256-GCM-SHA384**
        # *   **AES128-SHA256**
        # *   **AES256-SHA256**
        # 
        # TLSv1.3 supports the following cipher suites:
        # 
        # *   **TLS_AES_128_GCM_SHA256**
        # *   **TLS_AES_256_GCM_SHA384**
        # *   **TLS_CHACHA20_POLY1305_SHA256**
        # *   **TLS_AES_128_CCM_SHA256**
        # *   **TLS_AES_128_CCM_8_SHA256**
        self.ciphers = ciphers
        # The region ID of the NLB instance.
        self.region_id = region_id
        # The listeners that are associated with the NLB instance.
        self.related_listeners = related_listeners
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The ID of the TLS security policy.
        self.security_policy_id = security_policy_id
        # The name of the TLS security policy.
        self.security_policy_name = security_policy_name
        # The status of the TLS security policy. Valid values:
        # 
        # *   **Configuring**
        # *   **Available**
        self.security_policy_status = security_policy_status
        # The tags.
        self.tags = tags
        # The supported versions of the TLS protocol. Valid values: **TLSv1.0**, **TLSv1.1**, **TLSv1.2**, and **TLSv1.3**.
        self.tls_version = tls_version

    def validate(self):
        if self.related_listeners:
            for v1 in self.related_listeners:
                 if v1:
                    v1.validate()
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['RelatedListeners'] = []
        if self.related_listeners is not None:
            for k1 in self.related_listeners:
                result['RelatedListeners'].append(k1.to_map() if k1 else None)

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id

        if self.security_policy_name is not None:
            result['SecurityPolicyName'] = self.security_policy_name

        if self.security_policy_status is not None:
            result['SecurityPolicyStatus'] = self.security_policy_status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.tls_version is not None:
            result['TlsVersion'] = self.tls_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.related_listeners = []
        if m.get('RelatedListeners') is not None:
            for k1 in m.get('RelatedListeners'):
                temp_model = main_models.ListSecurityPolicyResponseBodySecurityPoliciesRelatedListeners()
                self.related_listeners.append(temp_model.from_map(k1))

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')

        if m.get('SecurityPolicyName') is not None:
            self.security_policy_name = m.get('SecurityPolicyName')

        if m.get('SecurityPolicyStatus') is not None:
            self.security_policy_status = m.get('SecurityPolicyStatus')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListSecurityPolicyResponseBodySecurityPoliciesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TlsVersion') is not None:
            self.tls_version = m.get('TlsVersion')

        return self

class ListSecurityPolicyResponseBodySecurityPoliciesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. You can specify up to 10 tag keys.
        # 
        # The tag key can be up to 64 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        self.key = key
        # The tag value. You can specify up to 10 tag values.
        # 
        # The tag value can be up to 128 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
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

class ListSecurityPolicyResponseBodySecurityPoliciesRelatedListeners(DaraModel):
    def __init__(
        self,
        listener_id: str = None,
        listener_port: int = None,
        listener_protocol: str = None,
        load_balancer_id: str = None,
    ):
        # The listener ID.
        self.listener_id = listener_id
        # The listener port.
        self.listener_port = listener_port
        # The listener protocol. Valid value: **TCPSSL**.
        self.listener_protocol = listener_protocol
        # The NLB instance ID.
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        return self

