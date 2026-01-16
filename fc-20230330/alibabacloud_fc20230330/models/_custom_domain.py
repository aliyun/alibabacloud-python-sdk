# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class CustomDomain(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        api_version: str = None,
        auth_config: main_models.AuthConfig = None,
        cert_config: main_models.CertConfig = None,
        created_time: str = None,
        domain_name: str = None,
        last_modified_time: str = None,
        protocol: str = None,
        route_config: main_models.RouteConfig = None,
        subdomain_count: str = None,
        tls_config: main_models.TLSConfig = None,
        waf_config: main_models.WAFConfig = None,
    ):
        self.account_id = account_id
        self.api_version = api_version
        self.auth_config = auth_config
        self.cert_config = cert_config
        self.created_time = created_time
        self.domain_name = domain_name
        self.last_modified_time = last_modified_time
        self.protocol = protocol
        self.route_config = route_config
        self.subdomain_count = subdomain_count
        self.tls_config = tls_config
        self.waf_config = waf_config

    def validate(self):
        if self.auth_config:
            self.auth_config.validate()
        if self.cert_config:
            self.cert_config.validate()
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
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.api_version is not None:
            result['apiVersion'] = self.api_version

        if self.auth_config is not None:
            result['authConfig'] = self.auth_config.to_map()

        if self.cert_config is not None:
            result['certConfig'] = self.cert_config.to_map()

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.domain_name is not None:
            result['domainName'] = self.domain_name

        if self.last_modified_time is not None:
            result['lastModifiedTime'] = self.last_modified_time

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.route_config is not None:
            result['routeConfig'] = self.route_config.to_map()

        if self.subdomain_count is not None:
            result['subdomainCount'] = self.subdomain_count

        if self.tls_config is not None:
            result['tlsConfig'] = self.tls_config.to_map()

        if self.waf_config is not None:
            result['wafConfig'] = self.waf_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')

        if m.get('authConfig') is not None:
            temp_model = main_models.AuthConfig()
            self.auth_config = temp_model.from_map(m.get('authConfig'))

        if m.get('certConfig') is not None:
            temp_model = main_models.CertConfig()
            self.cert_config = temp_model.from_map(m.get('certConfig'))

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')

        if m.get('lastModifiedTime') is not None:
            self.last_modified_time = m.get('lastModifiedTime')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('routeConfig') is not None:
            temp_model = main_models.RouteConfig()
            self.route_config = temp_model.from_map(m.get('routeConfig'))

        if m.get('subdomainCount') is not None:
            self.subdomain_count = m.get('subdomainCount')

        if m.get('tlsConfig') is not None:
            temp_model = main_models.TLSConfig()
            self.tls_config = temp_model.from_map(m.get('tlsConfig'))

        if m.get('wafConfig') is not None:
            temp_model = main_models.WAFConfig()
            self.waf_config = temp_model.from_map(m.get('wafConfig'))

        return self

