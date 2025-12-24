# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetTLSCipherPolicyAttributeRequest(DaraModel):
    def __init__(
        self,
        ciphers: List[str] = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        tlscipher_policy_id: str = None,
        tlsversions: List[str] = None,
    ):
        # The cipher suites supported by the TLS version.
        # 
        # The specified cipher suites must be supported by at least one TLS protocol version that you specify. For example, if you set the TLSVersions parameter to TLSv1.3, you must specify cipher suites that are supported by this protocol version.
        # 
        # TLS 1.0 and TLS 1.1 support the following cipher suites:
        # 
        # *   ECDHE-ECDSA-AES128-SHA
        # *   ECDHE-ECDSA-AES256-SHA
        # *   ECDHE-RSA-AES128-SHA
        # *   ECDHE-RSA-AES256-SHA
        # *   AES128-SHA AES256-SHA
        # *   DES-CBC3-SHA
        # 
        # TLS 1.2 supports the following cipher suites:
        # 
        # *   ECDHE-ECDSA-AES128-SHA
        # *   ECDHE-ECDSA-AES256-SHA
        # *   ECDHE-RSA-AES128-SHA
        # *   ECDHE-RSA-AES256-SHA
        # *   AES128-SHA AES256-SHA
        # *   DES-CBC3-SHA
        # *   ECDHE-ECDSA-AES128-GCM-SHA256
        # *   ECDHE-ECDSA-AES256-GCM-SHA384
        # *   ECDHE-ECDSA-AES128-SHA256
        # *   ECDHE-ECDSA-AES256-SHA384
        # *   ECDHE-RSA-AES128-GCM-SHA256
        # *   ECDHE-RSA-AES256-GCM-SHA384
        # *   ECDHE-RSA-AES128-SHA256
        # *   ECDHE-RSA-AES256-SHA384
        # *   AES128-GCM-SHA256
        # *   AES256-GCM-SHA384
        # *   AES128-SHA256 AES256-SHA256
        # 
        # TLS 1.3 supports the following cipher suites:
        # 
        # *   TLS_AES_128_GCM_SHA256
        # *   TLS_AES_256_GCM_SHA384
        # *   TLS_CHACHA20_POLY1305_SHA256
        # *   TLS_AES_128_CCM_SHA256
        # *   TLS_AES_128_CCM_8_SHA256
        # 
        # This parameter is required.
        self.ciphers = ciphers
        # The name of the TLS policy. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        # 
        # This parameter is required.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the Server Load Balancer (SLB) instance is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the TLS policy.
        # 
        # This parameter is required.
        self.tlscipher_policy_id = tlscipher_policy_id
        # The version of the TLS protocol. Valid values: **TLSv1.0**, **TLSv1.1**, **TLSv1.2**, and **TLSv1.3**.
        # 
        # This parameter is required.
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

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.tlscipher_policy_id is not None:
            result['TLSCipherPolicyId'] = self.tlscipher_policy_id

        if self.tlsversions is not None:
            result['TLSVersions'] = self.tlsversions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TLSCipherPolicyId') is not None:
            self.tlscipher_policy_id = m.get('TLSCipherPolicyId')

        if m.get('TLSVersions') is not None:
            self.tlsversions = m.get('TLSVersions')

        return self

