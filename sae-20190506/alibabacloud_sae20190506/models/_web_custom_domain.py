# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class WebCustomDomain(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        default_forwarding_app_name: str = None,
        domain_name: str = None,
        last_modified_time: str = None,
        namespace_id: str = None,
        protocol: str = None,
        route_config: main_models.RouteConfig = None,
        web_cert_config: main_models.WebCertConfig = None,
        web_tlsconfig: main_models.WebTLSConfig = None,
        web_wafconfig: main_models.WebWAFConfig = None,
        account_id: str = None,
    ):
        self.created_time = created_time
        self.default_forwarding_app_name = default_forwarding_app_name
        self.domain_name = domain_name
        self.last_modified_time = last_modified_time
        self.namespace_id = namespace_id
        self.protocol = protocol
        self.route_config = route_config
        self.web_cert_config = web_cert_config
        self.web_tlsconfig = web_tlsconfig
        self.web_wafconfig = web_wafconfig
        self.account_id = account_id

    def validate(self):
        if self.route_config:
            self.route_config.validate()
        if self.web_cert_config:
            self.web_cert_config.validate()
        if self.web_tlsconfig:
            self.web_tlsconfig.validate()
        if self.web_wafconfig:
            self.web_wafconfig.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.default_forwarding_app_name is not None:
            result['DefaultForwardingAppName'] = self.default_forwarding_app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.route_config is not None:
            result['RouteConfig'] = self.route_config.to_map()

        if self.web_cert_config is not None:
            result['WebCertConfig'] = self.web_cert_config.to_map()

        if self.web_tlsconfig is not None:
            result['WebTLSConfig'] = self.web_tlsconfig.to_map()

        if self.web_wafconfig is not None:
            result['WebWAFConfig'] = self.web_wafconfig.to_map()

        if self.account_id is not None:
            result['accountId'] = self.account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('DefaultForwardingAppName') is not None:
            self.default_forwarding_app_name = m.get('DefaultForwardingAppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RouteConfig') is not None:
            temp_model = main_models.RouteConfig()
            self.route_config = temp_model.from_map(m.get('RouteConfig'))

        if m.get('WebCertConfig') is not None:
            temp_model = main_models.WebCertConfig()
            self.web_cert_config = temp_model.from_map(m.get('WebCertConfig'))

        if m.get('WebTLSConfig') is not None:
            temp_model = main_models.WebTLSConfig()
            self.web_tlsconfig = temp_model.from_map(m.get('WebTLSConfig'))

        if m.get('WebWAFConfig') is not None:
            temp_model = main_models.WebWAFConfig()
            self.web_wafconfig = temp_model.from_map(m.get('WebWAFConfig'))

        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        return self

