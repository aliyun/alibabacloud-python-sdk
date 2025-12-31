# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cas20200630 import models as main_models
from darabonba.model import DaraModel

class DescribeClientCertificateStatusResponseBody(DaraModel):
    def __init__(
        self,
        certificate_status: List[main_models.DescribeClientCertificateStatusResponseBodyCertificateStatus] = None,
        request_id: str = None,
    ):
        # An array that consists of the status information about the certificates.
        self.certificate_status = certificate_status
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.certificate_status:
            for v1 in self.certificate_status:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CertificateStatus'] = []
        if self.certificate_status is not None:
            for k1 in self.certificate_status:
                result['CertificateStatus'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.certificate_status = []
        if m.get('CertificateStatus') is not None:
            for k1 in m.get('CertificateStatus'):
                temp_model = main_models.DescribeClientCertificateStatusResponseBodyCertificateStatus()
                self.certificate_status.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeClientCertificateStatusResponseBodyCertificateStatus(DaraModel):
    def __init__(
        self,
        revoke_time: int = None,
        serial_number: str = None,
        status: str = None,
    ):
        # The date on which the certificate was revoked.
        # 
        # >  This parameter is returned only when the value of the **Status** parameter is **revoked**. The value revoked indicates that the certificate is revoked.
        self.revoke_time = revoke_time
        # The serial number of the certificate.
        self.serial_number = serial_number
        # The status of the certificate. Valid values:
        # 
        # *   **good**: The certificate is not revoked.
        # *   **revoked**: The certificate is revoked.
        # *   **unknown**: The server cannot determine the status of the certificate.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.revoke_time is not None:
            result['RevokeTime'] = self.revoke_time

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RevokeTime') is not None:
            self.revoke_time = m.get('RevokeTime')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

