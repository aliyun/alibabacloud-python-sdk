# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListSystemSecurityPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        security_policies: List[main_models.ListSystemSecurityPoliciesResponseBodySecurityPolicies] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The list of TLS security policies.
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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.security_policies = []
        if m.get('SecurityPolicies') is not None:
            for k1 in m.get('SecurityPolicies'):
                temp_model = main_models.ListSystemSecurityPoliciesResponseBodySecurityPolicies()
                self.security_policies.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSystemSecurityPoliciesResponseBodySecurityPolicies(DaraModel):
    def __init__(
        self,
        ciphers: List[str] = None,
        security_policy_id: str = None,
        tls_versions: List[str] = None,
    ):
        # The supported cipher suites. The value of this parameter is determined by the value of **TLSVersions**.
        # 
        # The specified cipher suites must be supported by at least one value of **TLSVersions**. For example, if you set TLSVersions to **TLSv1.3**, you must specify cipher suites that are supported by **TLSv1.3**.
        # 
        # *   Valid values when TLSVersions is set to **TLSv1.0** or **TLSv1.1**:
        # 
        #     *   ECDHE-ECDSA-AES128-SHA
        #     *   ECDHE-ECDSA-AES256-SHA
        #     *   ECDHE-RSA-AES128-SHA
        #     *   ECDHE-RSA-AES256-SHA
        #     *   AES128-SHA
        #     *   AES256-SHA
        #     *   DES-CBC3-SHA
        # 
        # *   Valid values when TLSVersions is set to **TLSv1.2**:
        # 
        #     *   ECDHE-ECDSA-AES128-SHA
        #     *   ECDHE-ECDSA-AES256-SHA
        #     *   ECDHE-RSA-AES128-SHA
        #     *   ECDHE-RSA-AES256-SHA
        #     *   AES128-SHA
        #     *   AES256-SHA
        #     *   DES-CBC3-SHA
        #     *   ECDHE-ECDSA-AES128-GCM-SHA256
        #     *   ECDHE-ECDSA-AES256-GCM-SHA384
        #     *   ECDHE-ECDSA-AES128-SHA256
        #     *   ECDHE-ECDSA-AES256-SHA384
        #     *   ECDHE-RSA-AES128-GCM-SHA256
        #     *   ECDHE-RSA-AES256-GCM-SHA384
        #     *   ECDHE-RSA-AES128-SHA256
        #     *   ECDHE-RSA-AES256-SHA384
        #     *   AES128-GCM-SHA256
        #     *   AES256-GCM-SHA384
        #     *   AES128-SHA256
        #     *   AES256-SHA256
        # 
        # *   Valid values when TLSVersions is set to **TLSv1.3**:
        # 
        #     *   TLS_AES_128_GCM_SHA256
        #     *   TLS_AES_256_GCM_SHA384
        #     *   TLS_CHACHA20_POLY1305_SHA256
        #     *   TLS_AES_128_CCM_SHA256
        #     *   TLS_AES_128_CCM_8_SHA256
        self.ciphers = ciphers
        # The ID of the TLS security policy.
        self.security_policy_id = security_policy_id
        # The supported TLS versions. Valid values: **TLSv1.0**, **TLSv1.1**, **TLSv1.2**, and **TLSv1.3**.
        self.tls_versions = tls_versions

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

        if self.tls_versions is not None:
            result['TlsVersions'] = self.tls_versions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')

        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')

        if m.get('TlsVersions') is not None:
            self.tls_versions = m.get('TlsVersions')

        return self

