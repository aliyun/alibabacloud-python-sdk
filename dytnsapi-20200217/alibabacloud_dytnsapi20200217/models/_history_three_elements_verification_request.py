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
        # The authorization code. You can obtain it from the following sources:
        # 
        # - On the [Tag Plaza](https://dytns.console.aliyun.com/analysis/square) page in the Phone Number Intelligence console, select the **three-element ID verification** tag and submit an application. You will receive an authorization code after the application is approved.
        # 
        # - On the [My Applications](https://dytns.console.aliyun.com/analysis/apply) page in the Phone Number Intelligence console, find the authorization ID for your approved **three-element ID verification** service.
        # 
        # This parameter is required.
        self.auth_code = auth_code
        # The carrier to query. By default, the system queries the number\\"s carrier of record. Specify this parameter to route the query to a specific carrier.
        # 
        # Valid values:
        # 
        # - `CMCC`: China Mobile
        # 
        # - `CUCC`: China Unicom
        # 
        # - `CTCC`: China Telecom
        # 
        # > Due to number portability, a ported number\\"s historical carrier may be unknown. Use this parameter to explicitly query a specific carrier. If omitted, the query defaults to the number\\"s current carrier of record.
        # >
        # > **Important** Specifying China Broadcasting Network is not supported and results in an HTTP 400 error.
        self.carrier = carrier
        # The ID number to verify.
        # 
        # - If `Mask` is set to `NORMAL`, the value of this parameter is in plaintext.
        # 
        # This parameter is required.
        self.cert_code = cert_code
        # The phone number to query.
        # 
        # - If `Mask` is set to `NORMAL`, this parameter must be an 11-digit mobile phone number.
        # 
        # This parameter is required.
        self.input_number = input_number
        # The encryption method. Valid value:
        # 
        # - **NORMAL**: The phone number is not encrypted.
        # 
        # This parameter is required.
        self.mask = mask
        # The name to verify.
        # 
        # This parameter is required.
        self.name = name
        # The historical point in time to verify, in `yyyyMMddHHmmss` format. If the specific time of day is unknown, set the `HHmmss` portion to `000000`. For example, `20230615000000` verifies ownership as of June 15, 2023.
        # 
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

