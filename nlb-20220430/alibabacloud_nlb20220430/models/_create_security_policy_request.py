# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nlb20220430 import models as main_models
from darabonba.model import DaraModel

class CreateSecurityPolicyRequest(DaraModel):
    def __init__(
        self,
        ciphers: List[str] = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_policy_name: str = None,
        tag: List[main_models.CreateSecurityPolicyRequestTag] = None,
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
        # 
        # This parameter is required.
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
        # The ID of the resource group to which the security policy belongs.
        self.resource_group_id = resource_group_id
        # The name of the security policy.
        # 
        # It must be 1 to 200 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        self.security_policy_name = security_policy_name
        # The tags.
        self.tag = tag
        # The Transport Layer Security (TLS) versions supported by the security policy. Valid values: **TLSv1.0**, **TLSv1.1**, **TLSv1.2**, and **TLSv1.3**.
        # 
        # This parameter is required.
        self.tls_versions = tls_versions

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

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

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_policy_name is not None:
            result['SecurityPolicyName'] = self.security_policy_name

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

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

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityPolicyName') is not None:
            self.security_policy_name = m.get('SecurityPolicyName')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateSecurityPolicyRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TlsVersions') is not None:
            self.tls_versions = m.get('TlsVersions')

        return self

class CreateSecurityPolicyRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. It must be 1 to 64 characters in length, cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`. It can contain letters, digits, underscores (_), periods (.), colons (:), forward slashes (/), equal signs (=), plus signs (+), minus signs (-), and at signs (@).
        # 
        # You can add up to 20 tags for the security policy in each call.
        self.key = key
        # The value of the tag. It must be 1 to 128 characters in length, cannot start with `acs:` or `aliyun`, and cannot contain `http://` or `https://`. It can contain letters, digits, underscores (_), periods (.), colons (:), forward slashes (/), equal signs (=), plus signs (+), minus signs (-), and at signs (@).
        # 
        # You can add up to 20 tags for the security policy in each call.
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

