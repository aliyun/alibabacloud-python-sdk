# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateClientCertificateWithCsrResponseBody(DaraModel):
    def __init__(
        self,
        cert_kmc_rep_1: str = None,
        cert_sign_buf_kmc: str = None,
        certificate_chain: str = None,
        identifier: str = None,
        request_id: str = None,
        serial_number: str = None,
        x_509certificate: str = None,
    ):
        # CertKmcRep1.
        self.cert_kmc_rep_1 = cert_kmc_rep_1
        # Cert Sign Buf Kmc.
        self.cert_sign_buf_kmc = cert_sign_buf_kmc
        # The certificate chain of the client certificate.
        self.certificate_chain = certificate_chain
        # The unique identifier of the client certificate.
        self.identifier = identifier
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The serial number of the server certificate.
        self.serial_number = serial_number
        # The content of the client certificate.
        self.x_509certificate = x_509certificate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_kmc_rep_1 is not None:
            result['CertKmcRep1'] = self.cert_kmc_rep_1

        if self.cert_sign_buf_kmc is not None:
            result['CertSignBufKmc'] = self.cert_sign_buf_kmc

        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertKmcRep1') is not None:
            self.cert_kmc_rep_1 = m.get('CertKmcRep1')

        if m.get('CertSignBufKmc') is not None:
            self.cert_sign_buf_kmc = m.get('CertSignBufKmc')

        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')

        return self

