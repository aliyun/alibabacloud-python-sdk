# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadClientCaCertificateResponseBody(DaraModel):
    def __init__(
        self,
        common_name: str = None,
        fingerprint_sha_256: str = None,
        id: str = None,
        issuer: str = None,
        not_after: str = None,
        not_before: str = None,
        request_id: str = None,
        serial_number: str = None,
        signature_algorithm: str = None,
        status: str = None,
        validity_days: str = None,
    ):
        # The Common Name of the certificate.
        self.common_name = common_name
        # The SHA-256 fingerprint of the certificate.
        self.fingerprint_sha_256 = fingerprint_sha_256
        # The certificate ID.
        self.id = id
        # The CA that issued the certificate.
        self.issuer = issuer
        # The time when the certificate expires.
        self.not_after = not_after
        # The time when the certificate takes effect.
        self.not_before = not_before
        # The request ID.
        self.request_id = request_id
        # The serial number of the certificate.
        self.serial_number = serial_number
        # The signature algorithm of the certificate.
        self.signature_algorithm = signature_algorithm
        # The status of the certificate.
        self.status = status
        # The validity period of the certificate. Unit: day.
        self.validity_days = validity_days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_name is not None:
            result['CommonName'] = self.common_name

        if self.fingerprint_sha_256 is not None:
            result['FingerprintSha256'] = self.fingerprint_sha_256

        if self.id is not None:
            result['Id'] = self.id

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.not_after is not None:
            result['NotAfter'] = self.not_after

        if self.not_before is not None:
            result['NotBefore'] = self.not_before

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.signature_algorithm is not None:
            result['SignatureAlgorithm'] = self.signature_algorithm

        if self.status is not None:
            result['Status'] = self.status

        if self.validity_days is not None:
            result['ValidityDays'] = self.validity_days

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonName') is not None:
            self.common_name = m.get('CommonName')

        if m.get('FingerprintSha256') is not None:
            self.fingerprint_sha_256 = m.get('FingerprintSha256')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')

        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('SignatureAlgorithm') is not None:
            self.signature_algorithm = m.get('SignatureAlgorithm')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ValidityDays') is not None:
            self.validity_days = m.get('ValidityDays')

        return self

