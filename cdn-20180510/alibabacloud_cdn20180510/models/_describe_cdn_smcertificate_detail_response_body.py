# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCdnSMCertificateDetailResponseBody(DaraModel):
    def __init__(
        self,
        cert_expire_time: str = None,
        cert_identifier: str = None,
        cert_name: str = None,
        cert_org: str = None,
        common_name: str = None,
        encrypt_certificate: str = None,
        request_id: str = None,
        sans: str = None,
        sign_certificate: str = None,
    ):
        # The expiration time of the certificate. The time is displayed in UTC.
        self.cert_expire_time = cert_expire_time
        # The ID of the certificate.
        self.cert_identifier = cert_identifier
        # The name of the certificate.
        self.cert_name = cert_name
        # The certificate authority (CA) that issued the certificate.
        self.cert_org = cert_org
        # The common name.
        self.common_name = common_name
        # The content of the encryption certificate.
        self.encrypt_certificate = encrypt_certificate
        # The ID of the request.
        self.request_id = request_id
        # The subdomain name.
        self.sans = sans
        # The content of the signature certificate.
        self.sign_certificate = sign_certificate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_expire_time is not None:
            result['CertExpireTime'] = self.cert_expire_time

        if self.cert_identifier is not None:
            result['CertIdentifier'] = self.cert_identifier

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.cert_org is not None:
            result['CertOrg'] = self.cert_org

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.encrypt_certificate is not None:
            result['EncryptCertificate'] = self.encrypt_certificate

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sans is not None:
            result['Sans'] = self.sans

        if self.sign_certificate is not None:
            result['SignCertificate'] = self.sign_certificate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertExpireTime') is not None:
            self.cert_expire_time = m.get('CertExpireTime')

        if m.get('CertIdentifier') is not None:
            self.cert_identifier = m.get('CertIdentifier')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('CertOrg') is not None:
            self.cert_org = m.get('CertOrg')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('EncryptCertificate') is not None:
            self.encrypt_certificate = m.get('EncryptCertificate')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Sans') is not None:
            self.sans = m.get('Sans')

        if m.get('SignCertificate') is not None:
            self.sign_certificate = m.get('SignCertificate')

        return self

