# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeDefaultHttpsResponseBody(DaraModel):
    def __init__(
        self,
        default_https: main_models.DescribeDefaultHttpsResponseBodyDefaultHttps = None,
        request_id: str = None,
    ):
        # The default SSL/TLS settings.
        self.default_https = default_https
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.default_https:
            self.default_https.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_https is not None:
            result['DefaultHttps'] = self.default_https.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultHttps') is not None:
            temp_model = main_models.DescribeDefaultHttpsResponseBodyDefaultHttps()
            self.default_https = temp_model.from_map(m.get('DefaultHttps'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDefaultHttpsResponseBodyDefaultHttps(DaraModel):
    def __init__(
        self,
        cert_id: str = None,
        cipher_suite: str = None,
        custom_ciphers: str = None,
        enable_tlsv_3: bool = None,
        tlsversion: str = None,
    ):
        # The ID of the certificate.
        self.cert_id = cert_id
        # The type of the cipher suite. Valid values:
        # 
        # - **1**: All cipher suites are added.
        # 
        # - **2**: Strong cipher suites are added. This value is available only when TLSVersion is set to tlsv1.2.
        # 
        # - **99**: Custom cipher suites are added. This value is available only when TLSVersion is not set to tlsv1.3.
        self.cipher_suite = cipher_suite
        # The custom cipher suites.
        self.custom_ciphers = custom_ciphers
        # Indicates whether TLS 1.3 is supported. Valid values:
        # 
        # - **true**: TLS 1.3 is supported.
        # 
        # - **false**: TLS 1.3 is not supported.
        # 
        # > This parameter takes effect only when HttpsPorts is not empty, which indicates that the domain name uses the HTTPS protocol. When TLSVersion is set to tlsv1.3, this value must be true.
        self.enable_tlsv_3 = enable_tlsv_3
        # The TLS version. Valid values:
        # 
        # - **tlsv1**: TLS 1.0 and later are supported. This value provides the highest compatibility and the lowest security.
        # 
        # - **tlsv1.1**: TLS 1.1 and later are supported. This value provides good compatibility and security.
        # 
        # - **tlsv1.2**: TLS 1.2 and later are supported. This value provides good compatibility and the highest security.
        # 
        # - **tlsv1.3**: Only TLS 1.3 is supported. This value provides the highest security and the lowest compatibility.
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

        if self.enable_tlsv_3 is not None:
            result['EnableTLSv3'] = self.enable_tlsv_3

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

        if m.get('EnableTLSv3') is not None:
            self.enable_tlsv_3 = m.get('EnableTLSv3')

        if m.get('TLSVersion') is not None:
            self.tlsversion = m.get('TLSVersion')

        return self

