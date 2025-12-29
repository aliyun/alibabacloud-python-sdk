# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BankMetaVerifyRequest(DaraModel):
    def __init__(
        self,
        bank_card: str = None,
        identify_num: str = None,
        identity_type: str = None,
        mobile: str = None,
        param_type: str = None,
        product_type: str = None,
        user_name: str = None,
        verify_mode: str = None,
    ):
        # Bank card number.
        # 
        # - When `paramType` is `normal`, enter the plain text bank card number.
        # - When `paramType` is `md5`, enter the part of the card number except the last 6 digits in plain text + the last 6 digits encrypted with MD5 (32 lowercase).
        self.bank_card = bank_card
        # ID number.
        # 
        # - When `ProductType` is `BANK_CARD_3_META`, this field is required.
        # - When `paramType` is `normal`, enter the plain text ID number.
        # - When `paramType` is `md5`, enter the first 6 digits of the ID number in plain text + the birth date encrypted with MD5 (32 lowercase MD5) + the last 4 digits of the ID number.
        self.identify_num = identify_num
        # Identity type.
        self.identity_type = identity_type
        # Mobile phone number.
        # 
        # - When `ProductType` is `BANK_CARD_4_META`, this field is required.
        # - When `paramType` is `normal`, enter the plain text mobile phone number.
        # - When `paramType` is `md5`, enter the mobile phone number (32 lowercase MD5).
        self.mobile = mobile
        # Parameter type:
        # 
        # - normal: Unencrypted.
        # - md5: MD5 encrypted.
        self.param_type = param_type
        # Product type to call:
        # 
        # - BANK_CARD_2_META: Bank card number + name verification.
        # - BANK_CARD_3_META: Bank card number + name + ID number verification.
        # - BANK_CARD_4_META: Bank card number + name + ID number + mobile phone number verification.
        self.product_type = product_type
        # Name.
        # 
        # - When `paramType` is `normal`, enter the plain text name.
        # - When `paramType` is `md5`, encrypt the first character of the name with MD5 (32 lowercase MD5) + the rest of the name in plain text.
        self.user_name = user_name
        # VERIFY_BANK_CARD: Bank card authentication mode. It indicates whether the provided bank card number matches the user\\"s real name, ID number, and mobile phone number.
        self.verify_mode = verify_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bank_card is not None:
            result['BankCard'] = self.bank_card

        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num

        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.verify_mode is not None:
            result['VerifyMode'] = self.verify_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BankCard') is not None:
            self.bank_card = m.get('BankCard')

        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')

        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('VerifyMode') is not None:
            self.verify_mode = m.get('VerifyMode')

        return self

