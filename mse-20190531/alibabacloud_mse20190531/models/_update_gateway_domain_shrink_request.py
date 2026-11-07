# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGatewayDomainShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        ca_cert_identifier: str = None,
        cert_identifier: str = None,
        enable_waf: bool = None,
        gateway_unique_id: str = None,
        http_2: str = None,
        id: int = None,
        mtls_enabled: bool = None,
        must_https: bool = None,
        protocol: str = None,
        tls_cipher_suites_config_jsonshrink: str = None,
        tls_max: str = None,
        tls_min: str = None,
    ):
        # The language of the returned information. Valid values:
        # - zh: Chinese (default).
        # - en: English.
        self.accept_language = accept_language
        # The CA certificate content.
        self.ca_cert_identifier = ca_cert_identifier
        # The certificate ID.
        self.cert_identifier = cert_identifier
        # Specifies whether to enable Web Application Firewall (WAF) for the gateway domain name.
        self.enable_waf = enable_waf
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # Specifies whether to enable HTTP/2. Valid values:
        # - `open`: enables HTTP/2.
        # - `close`: disables HTTP/2.
        # - `globalConfig`: uses the global configuration.
        self.http_2 = http_2
        # The ID of the domain name to be updated.
        self.id = id
        # Specifies whether to enable mTLS.
        self.mtls_enabled = mtls_enabled
        # Specifies whether to force HTTPS.
        self.must_https = must_https
        # The protocol type. Valid values:
        # - HTTPS
        # - HTTP
        self.protocol = protocol
        # The TLS cipher suite configuration.
        self.tls_cipher_suites_config_jsonshrink = tls_cipher_suites_config_jsonshrink
        # The maximum TLS version.
        self.tls_max = tls_max
        # The minimum TLS version.
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

        if self.ca_cert_identifier is not None:
            result['CaCertIdentifier'] = self.ca_cert_identifier

        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.enable_waf is not None:
            result['EnableWaf'] = self.enable_waf

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.http_2 is not None:
            result['Http2'] = self.http_2

        if self.id is not None:
            result['Id'] = self.id

        if self.mtls_enabled is not None:
            result['MtlsEnabled'] = self.mtls_enabled

        if self.must_https is not None:
            result['MustHttps'] = self.must_https

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

        if m.get('CaCertIdentifier') is not None:
            self.ca_cert_identifier = m.get('CaCertIdentifier')

        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('EnableWaf') is not None:
            self.enable_waf = m.get('EnableWaf')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Http2') is not None:
            self.http_2 = m.get('Http2')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MtlsEnabled') is not None:
            self.mtls_enabled = m.get('MtlsEnabled')

        if m.get('MustHttps') is not None:
            self.must_https = m.get('MustHttps')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('TlsCipherSuitesConfigJSON') is not None:
            self.tls_cipher_suites_config_jsonshrink = m.get('TlsCipherSuitesConfigJSON')

        if m.get('TlsMax') is not None:
            self.tls_max = m.get('TlsMax')

        if m.get('TlsMin') is not None:
            self.tls_min = m.get('TlsMin')

        return self

