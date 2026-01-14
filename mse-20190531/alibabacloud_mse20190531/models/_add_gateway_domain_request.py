# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class AddGatewayDomainRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        cert_identifier: str = None,
        gateway_unique_id: str = None,
        http_2: str = None,
        must_https: bool = None,
        name: str = None,
        protocol: str = None,
        tls_cipher_suites_config_json: main_models.AddGatewayDomainRequestTlsCipherSuitesConfigJSON = None,
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
        self.tls_cipher_suites_config_json = tls_cipher_suites_config_json
        # The maximum version of Transport Layer Security (TLS).
        self.tls_max = tls_max
        # The minimum version of TLS.
        self.tls_min = tls_min

    def validate(self):
        if self.tls_cipher_suites_config_json:
            self.tls_cipher_suites_config_json.validate()

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

        if self.tls_cipher_suites_config_json is not None:
            result['TlsCipherSuitesConfigJSON'] = self.tls_cipher_suites_config_json.to_map()

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
            temp_model = main_models.AddGatewayDomainRequestTlsCipherSuitesConfigJSON()
            self.tls_cipher_suites_config_json = temp_model.from_map(m.get('TlsCipherSuitesConfigJSON'))

        if m.get('TlsMax') is not None:
            self.tls_max = m.get('TlsMax')

        if m.get('TlsMin') is not None:
            self.tls_min = m.get('TlsMin')

        return self

class AddGatewayDomainRequestTlsCipherSuitesConfigJSON(DaraModel):
    def __init__(
        self,
        config_type: str = None,
        tls_cipher_suites: List[str] = None,
    ):
        self.config_type = config_type
        self.tls_cipher_suites = tls_cipher_suites

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_type is not None:
            result['ConfigType'] = self.config_type

        if self.tls_cipher_suites is not None:
            result['TlsCipherSuites'] = self.tls_cipher_suites

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')

        if m.get('TlsCipherSuites') is not None:
            self.tls_cipher_suites = m.get('TlsCipherSuites')

        return self

