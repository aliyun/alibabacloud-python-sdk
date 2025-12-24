# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_slb20140515 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainExtensionsResponseBody(DaraModel):
    def __init__(
        self,
        domain_extensions: main_models.DescribeDomainExtensionsResponseBodyDomainExtensions = None,
        request_id: str = None,
    ):
        # A list of additional certificates.
        self.domain_extensions = domain_extensions
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.domain_extensions:
            self.domain_extensions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_extensions is not None:
            result['DomainExtensions'] = self.domain_extensions.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainExtensions') is not None:
            temp_model = main_models.DescribeDomainExtensionsResponseBodyDomainExtensions()
            self.domain_extensions = temp_model.from_map(m.get('DomainExtensions'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDomainExtensionsResponseBodyDomainExtensions(DaraModel):
    def __init__(
        self,
        domain_extension: List[main_models.DescribeDomainExtensionsResponseBodyDomainExtensionsDomainExtension] = None,
    ):
        self.domain_extension = domain_extension

    def validate(self):
        if self.domain_extension:
            for v1 in self.domain_extension:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainExtension'] = []
        if self.domain_extension is not None:
            for k1 in self.domain_extension:
                result['DomainExtension'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_extension = []
        if m.get('DomainExtension') is not None:
            for k1 in m.get('DomainExtension'):
                temp_model = main_models.DescribeDomainExtensionsResponseBodyDomainExtensionsDomainExtension()
                self.domain_extension.append(temp_model.from_map(k1))

        return self

class DescribeDomainExtensionsResponseBodyDomainExtensionsDomainExtension(DaraModel):
    def __init__(
        self,
        domain: str = None,
        domain_extension_id: str = None,
        server_certificate_id: str = None,
    ):
        # The domain name.
        self.domain = domain
        # The ID of the additional certificate.
        self.domain_extension_id = domain_extension_id
        # The ID of the certificate used by the domain name.
        self.server_certificate_id = server_certificate_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.domain_extension_id is not None:
            result['DomainExtensionId'] = self.domain_extension_id

        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('DomainExtensionId') is not None:
            self.domain_extension_id = m.get('DomainExtensionId')

        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')

        return self

