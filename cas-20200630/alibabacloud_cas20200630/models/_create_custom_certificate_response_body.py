# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomCertificateResponseBody(DaraModel):
    def __init__(
        self,
        certificate: str = None,
        certificate_chain: str = None,
        identifier: str = None,
        request_id: str = None,
        serial_number: str = None,
    ):
        # The content of the certificate. This parameter is returned only if Immediately is set to 1 or 2.
        self.certificate = certificate
        # The certificate chain of the certificate. This parameter is returned only if Immediately is set to 2.
        self.certificate_chain = certificate_chain
        # The unique identifier of the certificate.
        self.identifier = identifier
        # The request ID.
        self.request_id = request_id
        # The serial number of the certificate. This parameter is returned only if Immediately is set to 1 or 2.
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate is not None:
            result['Certificate'] = self.certificate

        if self.certificate_chain is not None:
            result['CertificateChain'] = self.certificate_chain

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')

        if m.get('CertificateChain') is not None:
            self.certificate_chain = m.get('CertificateChain')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        return self

