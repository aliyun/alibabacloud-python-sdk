# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClientCertificateForSerialNumberRequest(DaraModel):
    def __init__(
        self,
        serial_number: str = None,
    ):
        # The serial numbers of the client certificates or server certificates that you want to query. Separate multiple serial numbers with commas (,).
        # 
        # > You can call [ListClientCertificate](https://help.aliyun.com/document_detail/330884.html) to query the serial numbers of all client certificates and server certificates.
        # 
        # This parameter is required.
        self.serial_number = serial_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        return self

