# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateSecurityPolicyAttributeRequest(DaraModel):
    def __init__(
        self,
        ciphers: List[str] = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        security_policy_id: str = None,
        security_policy_name: str = None,
        tls_versions: List[str] = None,
    ):
        # The cipher suites supported by the security policy. Valid values of this parameter vary based on the value of TlsVersions. You can specify up to 32 cipher suites.
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
        # The client token used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token. Ensure that the token is unique among different requests. Only ASCII characters are allowed.
        # 
        # >  If you do not set this parameter, the value of **RequestId** is used.**** The value of **RequestId** is different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: validates the request without performing the operation. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the validation, the corresponding error message is returned. If the request passes the validation, the `DryRunOperation` error code is returned.
        # *   **false** (default): validates the request and performs the operation. If the request passes the validation, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the TLS security policy.
        # 
        # This parameter is required.
        self.security_policy_id = security_policy_id
        # The name of the security policy.
        # 
        # The name must be 1 to 200 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        self.security_policy_name = security_policy_name
        # The supported TLS versions. Valid values: **TLSv1.0**, **TLSv1.1**, **TLSv1.2**, and **TLSv1.3**. You can specify up to four TLS versions.
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id

        if self.security_policy_name is not None:
            result['SecurityPolicyName'] = self.security_policy_name

        if self.tls_versions is not None:
            result['TlsVersions'] = self.tls_versions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')

        if m.get('SecurityPolicyName') is not None:
            self.security_policy_name = m.get('SecurityPolicyName')

        if m.get('TlsVersions') is not None:
            self.tls_versions = m.get('TlsVersions')

        return self

