# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class CustomDomainResp(DaraModel):
    def __init__(
        self,
        cert_config: main_models.CertConfig = None,
        created_at: int = None,
        description: str = None,
        domain_name: str = None,
        tls_config: main_models.TLSConfig = None,
        updated_at: int = None,
    ):
        # The HTTPS certificate configuration used by the domain name.
        self.cert_config = cert_config
        # The time when the domain name was created. The value is a UNIX timestamp in milliseconds.
        self.created_at = created_at
        # The description of the custom domain name.
        self.description = description
        # The custom domain name.
        self.domain_name = domain_name
        # The TLS protocol configuration used by the domain name.
        self.tls_config = tls_config
        # The time when the domain name was last updated. The value is a UNIX timestamp in milliseconds.
        self.updated_at = updated_at

    def validate(self):
        if self.cert_config:
            self.cert_config.validate()
        if self.tls_config:
            self.tls_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_config is not None:
            result['certConfig'] = self.cert_config.to_map()

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.domain_name is not None:
            result['domainName'] = self.domain_name

        if self.tls_config is not None:
            result['tlsConfig'] = self.tls_config.to_map()

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('certConfig') is not None:
            temp_model = main_models.CertConfig()
            self.cert_config = temp_model.from_map(m.get('certConfig'))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domainName') is not None:
            self.domain_name = m.get('domainName')

        if m.get('tlsConfig') is not None:
            temp_model = main_models.TLSConfig()
            self.tls_config = temp_model.from_map(m.get('tlsConfig'))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

