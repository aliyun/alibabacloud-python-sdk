# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VirtualThreeElementsVerificationRequest(DaraModel):
    def __init__(
        self,
        auth_code: str = None,
        cert_code: str = None,
        cert_name: str = None,
        input_number: str = None,
        mask: str = None,
    ):
        # This parameter is required.
        self.auth_code = auth_code
        # This parameter is required.
        self.cert_code = cert_code
        # This parameter is required.
        self.cert_name = cert_name
        # This parameter is required.
        self.input_number = input_number
        # This parameter is required.
        self.mask = mask

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code

        if self.cert_code is not None:
            result['CertCode'] = self.cert_code

        if self.cert_name is not None:
            result['CertName'] = self.cert_name

        if self.input_number is not None:
            result['InputNumber'] = self.input_number

        if self.mask is not None:
            result['Mask'] = self.mask

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('CertCode') is not None:
            self.cert_code = m.get('CertCode')

        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')

        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        return self

