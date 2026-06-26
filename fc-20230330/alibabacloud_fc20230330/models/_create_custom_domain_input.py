# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class CreateCustomDomainInput(DaraModel):
    def __init__(
        self,
        auth_config: main_models.AuthConfig = None,
        cert_config: main_models.CertConfig = None,
        cors_config: main_models.CORSConfig = None,
        domain_name: str = None,
        is_e2b: bool = None,
        protocol: str = None,
        route_config: main_models.RouteConfig = None,
        tls_config: main_models.TLSConfig = None,
        waf_config: main_models.WAFConfig = None,
    ):
        # Permission authentication configuration.
        self.auth_config = auth_config
        # HTTPS certificate information.
        self.cert_config = cert_config
        self.cors_config = cors_config
        # Domain name. Enter a custom domain name that has an ICP filing with Alibaba Cloud or has added Alibaba Cloud to the ICP filing information as a service provider.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.is_e2b = is_e2b
        # Protocol type supported by the domain. HTTP: supports HTTP only. HTTPS: supports HTTPS only. HTTP,HTTPS: supports both HTTP and HTTPS.
        self.protocol = protocol
        # Route table: maps PATHs to functions when accessing the custom domain.
        self.route_config = route_config
        # TLS configuration information.
        self.tls_config = tls_config
        # Web Application Firewall configuration information.
        self.waf_config = waf_config

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.cert_config:
            self.cert_config.validate()
        if self.cors_config:
            self.cors_config.validate()
        if self.route_config:
            self.route_config.validate()
        if self.tls_config:
            self.tls_config.validate()
        if self.waf_config:
            self.waf_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()

        if self.cert_config is not None:
            result['certConfig'] = self.cert_config.to_map()

        if self.cors_config is not None:
            result['corsConfig'] = self.cors_config.to_map()

        if self.domain_name is not None:
            result['domainName'] = self.domain_name

        if self.is_e2b is not None:
            result['isE2B'] = self.is_e2b

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.route_config is not None:
            result['routeConfig'] = self.route_config.to_map()

        if self.tls_config is not None:
            result['tlsConfig'] = self.tls_config.to_map()

        if self.waf_config is not None:
            result['wafConfig'] = self.waf_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authConfig') is not None:
            temp_model = main_models.AuthConfig()
            self.auth_config = temp_model.from_map(m.get('authConfig'))

        if m.get('certConfig') is not None:
            temp_model = main_models.CertConfig()
            self.cert_config = temp_model.from_map(m.get('certConfig'))

        if m.get('corsConfig') is not None:
            temp_model = main_models.CORSConfig()
            self.cors_config = temp_model.from_map(m.get('corsConfig'))

        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')

        if m.get('isE2B') is not None:
            self.is_e2b = m.get('isE2B')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('routeConfig') is not None:
            temp_model = main_models.RouteConfig()
            self.route_config = temp_model.from_map(m.get('routeConfig'))

        if m.get('tlsConfig') is not None:
            temp_model = main_models.TLSConfig()
            self.tls_config = temp_model.from_map(m.get('tlsConfig'))

        if m.get('wafConfig') is not None:
            temp_model = main_models.WAFConfig()
            self.waf_config = temp_model.from_map(m.get('wafConfig'))

        return self

