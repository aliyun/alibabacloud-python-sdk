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
        # The bank card number.
        # 
        # - If ParamType is set to normal, enter the bank card number in plaintext.
        # - If ParamType is set to md5, enter all digits of the card number except the last 6 in plaintext, followed by the MD5 hash (32-character lowercase) of the last 6 digits.
        self.bank_card = bank_card
        # The ID card number.
        # 
        # - This parameter is required when ProductType is set to BANK_CARD_3_META.
        # - If ParamType is set to normal, enter the ID card number in plaintext.
        # - If ParamType is set to md5, enter the first 6 digits of the ID card number in plaintext, followed by the date of birth encrypted with MD5 (32-character lowercase MD5 hash), followed by the last 4 digits of the ID card number.
        self.identify_num = identify_num
        # The ID document type.
        self.identity_type = identity_type
        # The mobile phone number.
        # 
        # - This parameter is required when ProductType is set to BANK_CARD_4_META.
        # - If ParamType is set to normal, enter the mobile phone number in plaintext.
        # - If ParamType is set to md5, enter the MD5 hash (32-character lowercase) of the mobile phone number.
        self.mobile = mobile
        # The parameter type.
        # 
        # - normal: no encryption.
        # - md5: MD5 encryption.
        self.param_type = param_type
        # The product type.
        # 
        # - BANK_CARD_2_META: verifies the bank card number and name.
        # - BANK_CARD_3_META: verifies the bank card number, name, and ID card number.
        # - BANK_CARD_4_META: verifies the bank card number, name, ID card number, and mobile phone number.
        self.product_type = product_type
        # The name.
        # 
        # - If ParamType is set to normal, enter the name in plaintext.
        # - If ParamType is set to md5, enter the first character of the name encrypted with MD5 (32-character lowercase MD5 hash) followed by the remaining characters of the name in plaintext.
        self.user_name = user_name
        # VERIFY_BANK_CARD: the bank card verification mode. Verifies whether the bank card number matches the user\\"s real name, ID card number, and mobile phone number.
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

