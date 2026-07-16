# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class ListSAMLIdentityProviderCertificatesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        x_509certificates: List[main_models.ListSAMLIdentityProviderCertificatesResponseBodyX509Certificates] = None,
    ):
        self.request_id = request_id
        self.x_509certificates = x_509certificates

    def validate(self):
        if self.x_509certificates:
            for v1 in self.x_509certificates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['X509Certificates'] = []
        if self.x_509certificates is not None:
            for k1 in self.x_509certificates:
                result['X509Certificates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.x_509certificates = []
        if m.get('X509Certificates') is not None:
            for k1 in m.get('X509Certificates'):
                temp_model = main_models.ListSAMLIdentityProviderCertificatesResponseBodyX509Certificates()
                self.x_509certificates.append(temp_model.from_map(k1))

        return self

class ListSAMLIdentityProviderCertificatesResponseBodyX509Certificates(DaraModel):
    def __init__(
        self,
        certificate_id: str = None,
        x_509certificate: str = None,
    ):
        self.certificate_id = certificate_id
        self.x_509certificate = x_509certificate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id

        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')

        return self

