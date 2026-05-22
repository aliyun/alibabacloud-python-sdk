# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetClientCertificateResponseBody(DaraModel):
    def __init__(
        self,
        certificate: str = None,
        request_id: str = None,
        result: main_models.GetClientCertificateResponseBodyResult = None,
        site_id: int = None,
        site_name: str = None,
        status: str = None,
    ):
        # The certificate content.
        self.certificate = certificate
        # The request ID.
        self.request_id = request_id
        # The certificate information.
        self.result = result
        # The website ID.
        self.site_id = site_id
        # The website name.
        self.site_name = site_name
        # The certificate status.
        self.status = status

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate is not None:
            result['Certificate'] = self.certificate

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.site_name is not None:
            result['SiteName'] = self.site_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetClientCertificateResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('SiteName') is not None:
            self.site_name = m.get('SiteName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetClientCertificateResponseBodyResult(DaraModel):
    def __init__(
        self,
        cacertificate_id: str = None,
        common_name: str = None,
        create_time: str = None,
        fingerprint_sha_256: str = None,
        id: str = None,
        issuer: str = None,
        name: str = None,
        not_after: str = None,
        not_before: str = None,
        pubkey_algorithm: str = None,
        san: str = None,
        serial_number: str = None,
        signature_algorithm: str = None,
        status: str = None,
        type: str = None,
        update_time: str = None,
    ):
        # The ID of the CA certificate.
        self.cacertificate_id = cacertificate_id
        # The Common Name of the certificate.
        self.common_name = common_name
        # The time when the certificate was created.
        self.create_time = create_time
        self.fingerprint_sha_256 = fingerprint_sha_256
        # The certificate ID.
        self.id = id
        # The certificate authority (CA) that issued the certificate.
        self.issuer = issuer
        # The certificate name.
        self.name = name
        # The time when the certificate expires.
        self.not_after = not_after
        # The time when the certificate takes effect.
        self.not_before = not_before
        # The public-key algorithm of the certificate.
        self.pubkey_algorithm = pubkey_algorithm
        # The Subject Alternative Name (SAN) of the certificate.
        self.san = san
        self.serial_number = serial_number
        # The signature algorithm of the certificate.
        self.signature_algorithm = signature_algorithm
        # The certificate status.
        self.status = status
        # The certificate type.
        self.type = type
        # The time when the certificate was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cacertificate_id is not None:
            result['CACertificateId'] = self.cacertificate_id

        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.fingerprint_sha_256 is not None:
            result['FingerprintSha256'] = self.fingerprint_sha_256

        if self.id is not None:
            result['Id'] = self.id

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.name is not None:
            result['Name'] = self.name

        if self.not_after is not None:
            result['NotAfter'] = self.not_after

        if self.not_before is not None:
            result['NotBefore'] = self.not_before

        if self.pubkey_algorithm is not None:
            result['PubkeyAlgorithm'] = self.pubkey_algorithm

        if self.san is not None:
            result['SAN'] = self.san

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.signature_algorithm is not None:
            result['SignatureAlgorithm'] = self.signature_algorithm

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CACertificateId') is not None:
            self.cacertificate_id = m.get('CACertificateId')

        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FingerprintSha256') is not None:
            self.fingerprint_sha_256 = m.get('FingerprintSha256')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')

        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')

        if m.get('PubkeyAlgorithm') is not None:
            self.pubkey_algorithm = m.get('PubkeyAlgorithm')

        if m.get('SAN') is not None:
            self.san = m.get('SAN')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('SignatureAlgorithm') is not None:
            self.signature_algorithm = m.get('SignatureAlgorithm')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

