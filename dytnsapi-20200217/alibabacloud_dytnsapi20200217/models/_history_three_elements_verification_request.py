# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HistoryThreeElementsVerificationRequest(DaraModel):
    def __init__(
        self,
        auth_code: str = None,
        carrier: str = None,
        cert_code: str = None,
        input_number: str = None,
        mask: str = None,
        name: str = None,
        verification_time: str = None,
    ):
        # This parameter is required.
        self.auth_code = auth_code
        self.carrier = carrier
        # This parameter is required.
        self.cert_code = cert_code
        # This parameter is required.
        self.input_number = input_number
        # This parameter is required.
        self.mask = mask
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.verification_time = verification_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code

        if self.carrier is not None:
            result['Carrier'] = self.carrier

        if self.cert_code is not None:
            result['CertCode'] = self.cert_code

        if self.input_number is not None:
            result['InputNumber'] = self.input_number

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.name is not None:
            result['Name'] = self.name

        if self.verification_time is not None:
            result['VerificationTime'] = self.verification_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')

        if m.get('CertCode') is not None:
            self.cert_code = m.get('CertCode')

        if m.get('InputNumber') is not None:
            self.input_number = m.get('InputNumber')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('VerificationTime') is not None:
            self.verification_time = m.get('VerificationTime')

        return self

