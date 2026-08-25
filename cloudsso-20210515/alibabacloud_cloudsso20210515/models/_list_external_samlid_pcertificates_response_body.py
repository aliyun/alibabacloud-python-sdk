# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class ListExternalSAMLIdPCertificatesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        samlid_pcertificates: List[main_models.ListExternalSAMLIdPCertificatesResponseBodySAMLIdPCertificates] = None,
        total_counts: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The SAML signing certificates.
        self.samlid_pcertificates = samlid_pcertificates
        # The total number of entries returned.
        self.total_counts = total_counts

    def validate(self):
        if self.samlid_pcertificates:
            for v1 in self.samlid_pcertificates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SAMLIdPCertificates'] = []
        if self.samlid_pcertificates is not None:
            for k1 in self.samlid_pcertificates:
                result['SAMLIdPCertificates'].append(k1.to_map() if k1 else None)

        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.samlid_pcertificates = []
        if m.get('SAMLIdPCertificates') is not None:
            for k1 in m.get('SAMLIdPCertificates'):
                temp_model = main_models.ListExternalSAMLIdPCertificatesResponseBodySAMLIdPCertificates()
                self.samlid_pcertificates.append(temp_model.from_map(k1))

        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')

        return self

class ListExternalSAMLIdPCertificatesResponseBodySAMLIdPCertificates(DaraModel):
    def __init__(
        self,
        certificate_id: str = None,
        issuer: str = None,
        not_after: str = None,
        not_before: str = None,
        public_key: str = None,
        serial_number: str = None,
        signature_algorithm: str = None,
        subject: str = None,
        version: int = None,
        x_509certificate: str = None,
    ):
        # The ID of the certificate.
        self.certificate_id = certificate_id
        # The issuer of the certificate.
        self.issuer = issuer
        # The time when the certificate expires.
        self.not_after = not_after
        # The time when the certificate was created.
        self.not_before = not_before
        # The public key of the certificate. The value of this parameter is in the PEM format and is Base64-encoded.
        self.public_key = public_key
        # The serial number of the certificate.
        self.serial_number = serial_number
        # The signature algorithm of the certificate.
        self.signature_algorithm = signature_algorithm
        # The subject of the certificate.
        self.subject = subject
        # The version of the certificate.
        self.version = version
        # The X.509 certificate in the PEM format.
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

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.not_after is not None:
            result['NotAfter'] = self.not_after

        if self.not_before is not None:
            result['NotBefore'] = self.not_before

        if self.public_key is not None:
            result['PublicKey'] = self.public_key

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.signature_algorithm is not None:
            result['SignatureAlgorithm'] = self.signature_algorithm

        if self.subject is not None:
            result['Subject'] = self.subject

        if self.version is not None:
            result['Version'] = self.version

        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')

        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')

        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('SignatureAlgorithm') is not None:
            self.signature_algorithm = m.get('SignatureAlgorithm')

        if m.get('Subject') is not None:
            self.subject = m.get('Subject')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')

        return self

