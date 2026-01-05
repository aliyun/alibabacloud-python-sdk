# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class ListSystemSecurityPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        security_policies: List[main_models.ListSystemSecurityPoliciesResponseBodySecurityPolicies] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The security policies.
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
                temp_model = main_models.ListSystemSecurityPoliciesResponseBodySecurityPolicies()
                self.security_policies.append(temp_model.from_map(k1))

        return self

class ListSystemSecurityPoliciesResponseBodySecurityPolicies(DaraModel):
    def __init__(
        self,
        ciphers: List[str] = None,
        security_policy_id: str = None,
        tlsversions: List[str] = None,
    ):
        # The supported cipher suite.
        self.ciphers = ciphers
        # The ID of the security policy.
        self.security_policy_id = security_policy_id
        # The supported TLS protocol versions.
        self.tlsversions = tlsversions

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

        if self.tlsversions is not None:
            result['TLSVersions'] = self.tlsversions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')

        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')

        if m.get('TLSVersions') is not None:
            self.tlsversions = m.get('TLSVersions')

        return self

