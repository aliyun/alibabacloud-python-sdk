# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nlb20220430 import models as main_models
from darabonba.model import DaraModel

class ListSystemSecurityPolicyResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        security_policies: List[main_models.ListSystemSecurityPolicyResponseBodySecurityPolicies] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # A list of TLS security policies.
        self.security_policies = security_policies

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SecurityPolicies'] = []
        if self.security_policies is not None:
            for k1 in self.security_policies:
                result['SecurityPolicies'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.security_policies = []
        if m.get('SecurityPolicies') is not None:
            for k1 in m.get('SecurityPolicies'):
                temp_model = main_models.ListSystemSecurityPolicyResponseBodySecurityPolicies()
                self.security_policies.append(temp_model.from_map(k1))

        return self

class ListSystemSecurityPolicyResponseBodySecurityPolicies(DaraModel):
    def __init__(
        self,
        ciphers: str = None,
        security_policy_id: str = None,
        security_policy_name: str = None,
        tls_version: str = None,
    ):
        # The cipher suite.
        self.ciphers = ciphers
        # The ID of the TLS security policy.
        self.security_policy_id = security_policy_id
        # The name of the TLS security policy.
        self.security_policy_name = security_policy_name
        # The TLS version.
        self.tls_version = tls_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ciphers is not None:
            result['Ciphers'] = self.ciphers

        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id

        if self.security_policy_name is not None:
            result['SecurityPolicyName'] = self.security_policy_name

        if self.tls_version is not None:
            result['TlsVersion'] = self.tls_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')

        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')

        if m.get('SecurityPolicyName') is not None:
            self.security_policy_name = m.get('SecurityPolicyName')

        if m.get('TlsVersion') is not None:
            self.tls_version = m.get('TlsVersion')

        return self

