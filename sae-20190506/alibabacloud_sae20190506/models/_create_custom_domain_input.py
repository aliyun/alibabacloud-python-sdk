# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class CreateCustomDomainInput(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        cert_config: main_models.CertConfig = None,
        domain_name: str = None,
        keep_full_path: bool = None,
        namespace_id: str = None,
        protocol: str = None,
        tls_config: main_models.TLSConfig = None,
        waf_config: main_models.WAFConfig = None,
    ):
        self.application_name = application_name
        self.cert_config = cert_config
        self.domain_name = domain_name
        self.keep_full_path = keep_full_path
        self.namespace_id = namespace_id
        self.protocol = protocol
        self.tls_config = tls_config
        self.waf_config = waf_config

    def validate(self):
        if self.cert_config:
            self.cert_config.validate()
        if self.tls_config:
            self.tls_config.validate()
        if self.waf_config:
            self.waf_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['applicationName'] = self.application_name

        if self.cert_config is not None:
            result['certConfig'] = self.cert_config.to_map()

        if self.domain_name is not None:
            result['domainName'] = self.domain_name

        if self.keep_full_path is not None:
            result['keepFullPath'] = self.keep_full_path

        if self.namespace_id is not None:
            result['namespaceID'] = self.namespace_id

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.tls_config is not None:
            result['tlsConfig'] = self.tls_config.to_map()

        if self.waf_config is not None:
            result['wafConfig'] = self.waf_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationName') is not None:
            self.application_name = m.get('applicationName')

        if m.get('certConfig') is not None:
            temp_model = main_models.CertConfig()
            self.cert_config = temp_model.from_map(m.get('certConfig'))

        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')

        if m.get('keepFullPath') is not None:
            self.keep_full_path = m.get('keepFullPath')

        if m.get('namespaceID') is not None:
            self.namespace_id = m.get('namespaceID')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('tlsConfig') is not None:
            temp_model = main_models.TLSConfig()
            self.tls_config = temp_model.from_map(m.get('tlsConfig'))

        if m.get('wafConfig') is not None:
            temp_model = main_models.WAFConfig()
            self.waf_config = temp_model.from_map(m.get('wafConfig'))

        return self

