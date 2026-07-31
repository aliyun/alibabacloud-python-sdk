# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyDomainCertRequest(DaraModel):
    def __init__(
        self,
        cert_id: str = None,
        cipher_suite: str = None,
        custom_ciphers: List[str] = None,
        domain: str = None,
        enable_tlsv_3: bool = None,
        instance_id: str = None,
        region_id: str = None,
        tlsversion: str = None,
    ):
        # The ID of the certificate.
        # 
        # This parameter is required.
        self.cert_id = cert_id
        # The type of the cipher suite.
        self.cipher_suite = cipher_suite
        # The specific custom cipher suites to add. This parameter is used only when **CipherSuite** is set to **99**.
        self.custom_ciphers = custom_ciphers
        # The domain name that you want to manage.
        # 
        # This parameter is required.
        self.domain = domain
        # Specifies whether TLS 1.3 is supported. Valid values:
        # 
        # - **true**: TLS 1.3 is supported.
        # 
        # - **false**: TLS 1.3 is not supported.
        # 
        # > This parameter is used only when HttpsPorts is not empty, which indicates that the domain name uses the HTTPS protocol. When TLSVersion is set to tlsv1.3, this value must be true.
        self.enable_tlsv_3 = enable_tlsv_3
        # The ID of the WAF instance.
        # 
        # > You can call [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) to query the ID of the current WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region where the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The TLS version.
        self.tlsversion = tlsversion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.cipher_suite is not None:
            result['CipherSuite'] = self.cipher_suite

        if self.custom_ciphers is not None:
            result['CustomCiphers'] = self.custom_ciphers

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.enable_tlsv_3 is not None:
            result['EnableTLSv3'] = self.enable_tlsv_3

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tlsversion is not None:
            result['TLSVersion'] = self.tlsversion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CipherSuite') is not None:
            self.cipher_suite = m.get('CipherSuite')

        if m.get('CustomCiphers') is not None:
            self.custom_ciphers = m.get('CustomCiphers')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EnableTLSv3') is not None:
            self.enable_tlsv_3 = m.get('EnableTLSv3')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TLSVersion') is not None:
            self.tlsversion = m.get('TLSVersion')

        return self

