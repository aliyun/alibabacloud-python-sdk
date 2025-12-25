# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class UpdateDomainRequest(DaraModel):
    def __init__(
        self,
        ca_cert_identifier: str = None,
        cert_identifier: str = None,
        client_cacert: str = None,
        force_https: bool = None,
        http_2option: str = None,
        m_tlsenabled: bool = None,
        protocol: str = None,
        tls_cipher_suites_config: main_models.TlsCipherSuitesConfig = None,
        tls_max: str = None,
        tls_min: str = None,
    ):
        # The CA certificate ID.
        self.ca_cert_identifier = ca_cert_identifier
        # The certificate ID.
        self.cert_identifier = cert_identifier
        # The client CA certificate.
        self.client_cacert = client_cacert
        # Specifies whether to enable HTTPS redirection. If protocol is set to HTTPS, forceHttps is required.
        self.force_https = force_https
        # The HTTP/2 configuration.
        # 
        # Enumerated values:
        # 
        # *   GlobalConfig
        # *   Close
        # *   Open
        self.http_2option = http_2option
        # Specifies whether to enable mutual TLS (mTLS) authentication.
        self.m_tlsenabled = m_tlsenabled
        # The protocol type to be supported by the domain name. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        # 
        # This parameter is required.
        self.protocol = protocol
        # The cipher suite configuration.
        self.tls_cipher_suites_config = tls_cipher_suites_config
        # The maximum TLS version. Up to TLS 1.3 is supported.
        self.tls_max = tls_max
        # The minimum TLS version. Down to TLS 1.0 is supported.
        self.tls_min = tls_min

    def validate(self):
        if self.tls_cipher_suites_config:
            self.tls_cipher_suites_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ca_cert_identifier is not None:
            result['caCertIdentifier'] = self.ca_cert_identifier

        if self.cert_identifier is not None:
            result['certIdentifier'] = self.cert_identifier

        if self.client_cacert is not None:
            result['clientCACert'] = self.client_cacert

        if self.force_https is not None:
            result['forceHttps'] = self.force_https

        if self.http_2option is not None:
            result['http2Option'] = self.http_2option

        if self.m_tlsenabled is not None:
            result['mTLSEnabled'] = self.m_tlsenabled

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.tls_cipher_suites_config is not None:
            result['tlsCipherSuitesConfig'] = self.tls_cipher_suites_config.to_map()

        if self.tls_max is not None:
            result['tlsMax'] = self.tls_max

        if self.tls_min is not None:
            result['tlsMin'] = self.tls_min

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('caCertIdentifier') is not None:
            self.ca_cert_identifier = m.get('caCertIdentifier')

        if m.get('certIdentifier') is not None:
            self.cert_identifier = m.get('certIdentifier')

        if m.get('clientCACert') is not None:
            self.client_cacert = m.get('clientCACert')

        if m.get('forceHttps') is not None:
            self.force_https = m.get('forceHttps')

        if m.get('http2Option') is not None:
            self.http_2option = m.get('http2Option')

        if m.get('mTLSEnabled') is not None:
            self.m_tlsenabled = m.get('mTLSEnabled')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('tlsCipherSuitesConfig') is not None:
            temp_model = main_models.TlsCipherSuitesConfig()
            self.tls_cipher_suites_config = temp_model.from_map(m.get('tlsCipherSuitesConfig'))

        if m.get('tlsMax') is not None:
            self.tls_max = m.get('tlsMax')

        if m.get('tlsMin') is not None:
            self.tls_min = m.get('tlsMin')

        return self

