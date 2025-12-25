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
        # The default SSL and TLS settings.
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
        # The certificate ID.
        self.cert_id = cert_id
        # The type of the cipher suites. Valid values:
        # 
        # *   **1**: all cipher suites.
        # *   **2**: strong cipher suites.
        # *   **99**: custom cipher suites.
        self.cipher_suite = cipher_suite
        # The custom cipher suite.
        self.custom_ciphers = custom_ciphers
        # Indicates whether TLS 1.3 is supported. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable_tlsv_3 = enable_tlsv_3
        # The version of the TLS protocol. Valid values:
        # 
        # *   **tlsv1**
        # *   **tlsv1.1**
        # *   **tlsv1.2**
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

