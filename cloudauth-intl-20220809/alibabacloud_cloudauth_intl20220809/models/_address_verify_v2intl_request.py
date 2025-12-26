# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddressVerifyV2IntlRequest(DaraModel):
    def __init__(
        self,
        device_token: str = None,
        mobile: str = None,
        product_code: str = None,
        reg_country: str = None,
        text: str = None,
        verify_type: str = None,
    ):
        # DeviceToken obtained via the client SDK
        # 
        # This parameter is required.
        self.device_token = device_token
        # Supported: Chinese mobile phone numbers
        self.mobile = mobile
        # Fixed value: ADD_VERIFY_PRO
        # 
        # This parameter is required.
        self.product_code = product_code
        # List of prohibited countries or regions
        # 
        # This parameter is required.
        self.reg_country = reg_country
        # Detailed address text content
        self.text = text
        # Address verification method:
        # 
        # - **HOME**: Home address verification
        # 
        # - **WORK**: Work address verification
        self.verify_type = verify_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.reg_country is not None:
            result['RegCountry'] = self.reg_country

        if self.text is not None:
            result['Text'] = self.text

        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('RegCountry') is not None:
            self.reg_country = m.get('RegCountry')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')

        return self

