# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddGatewayDomainShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        cert_identifier: str = None,
        gateway_unique_id: str = None,
        http_2: str = None,
        must_https: bool = None,
        name: str = None,
        protocol: str = None,
        tls_cipher_suites_config_jsonshrink: str = None,
        tls_max: str = None,
        tls_min: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the certificate.
        self.cert_identifier = cert_identifier
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # Specifies whether to enable `HTTP/2`.
        # 
        # *   `open`: enables `HTTP/2`
        # *   `close`: disables `HTTP/2`
        # *   `globalConfig`: uses global configurations
        self.http_2 = http_2
        # Specifies whether to enable HTTPS.
        self.must_https = must_https
        # The domain name.
        self.name = name
        # The type of the protocol. Valid values:
        # 
        # *   `HTTP`
        # *   `HTTPS`
        self.protocol = protocol
        self.tls_cipher_suites_config_jsonshrink = tls_cipher_suites_config_jsonshrink
        # The maximum version of Transport Layer Security (TLS).
        self.tls_max = tls_max
        # The minimum version of TLS.
        self.tls_min = tls_min

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.http_2 is not None:
            result['Http2'] = self.http_2

        if self.must_https is not None:
            result['MustHttps'] = self.must_https

        if self.name is not None:
            result['Name'] = self.name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.tls_cipher_suites_config_jsonshrink is not None:
            result['TlsCipherSuitesConfigJSON'] = self.tls_cipher_suites_config_jsonshrink

        if self.tls_max is not None:
            result['TlsMax'] = self.tls_max

        if self.tls_min is not None:
            result['TlsMin'] = self.tls_min

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Http2') is not None:
            self.http_2 = m.get('Http2')

        if m.get('MustHttps') is not None:
            self.must_https = m.get('MustHttps')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('TlsCipherSuitesConfigJSON') is not None:
            self.tls_cipher_suites_config_jsonshrink = m.get('TlsCipherSuitesConfigJSON')

        if m.get('TlsMax') is not None:
            self.tls_max = m.get('TlsMax')

        if m.get('TlsMin') is not None:
            self.tls_min = m.get('TlsMin')

        return self

