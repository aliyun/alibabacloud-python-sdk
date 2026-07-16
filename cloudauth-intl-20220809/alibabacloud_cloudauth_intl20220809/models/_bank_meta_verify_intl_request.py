# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BankMetaVerifyIntlRequest(DaraModel):
    def __init__(
        self,
        bank_card: str = None,
        identify_num: str = None,
        identity_type: str = None,
        mobile: str = None,
        param_type: str = None,
        product_code: str = None,
        product_type: str = None,
        user_name: str = None,
        verify_mode: str = None,
    ):
        # The bank card number.
        # 
        # - If paramType is set to normal, enter the bank card number in plaintext.
        # - If paramType is set to md5, provide the plaintext of all digits except the last 6 digits + the MD5 value (32-character lowercase) of the last 6 digits.
        # 
        # This parameter is required.
        self.bank_card = bank_card
        # The ID document number.
        # - If paramType is set to normal, enter the ID document number in plaintext.
        # - If paramType is set to md5:
        #     - For ID cards: the first 6 digits (plaintext) + date of birth (ciphertext) + the last 4 digits (plaintext).
        #     - For other documents: the last 2 characters are MD5-encrypted.
        # 
        # Important:
        # This parameter is required when ProductType is set to one of the following values:
        # - BANK_CARD_3_META
        # - BANK_CARD_4_META.
        self.identify_num = identify_num
        # The ID document type. If left empty, the default value is ID card. For other document types, refer to the table below.
        self.identity_type = identity_type
        # The phone number.
        # - If paramType is set to normal, enter the phone number in plaintext.
        # - If paramType is set to md5, enter the phone number in ciphertext.
        # 
        # Important:
        # 
        # - This parameter is required when ProductType is set to BANK_CARD_4_META.
        self.mobile = mobile
        # The encryption method. Valid values:
        # - normal: no encryption
        # - md5: MD5 encryption
        # 
        # Important:
        # 
        # - All encrypted parameter values must be 32-character lowercase MD5 strings.
        # - Different MD5 tools may produce different ciphertext. If the API call succeeds before encryption but fails after encryption, try a different MD5 tool.
        # 
        # This parameter is required.
        self.param_type = param_type
        # Fixed value: BANK_CARD_N_META.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The product type to call. Valid values:
        # 
        # - BANK_CARD_2_META: Bank card number + name verification.
        # - BANK_CARD_3_META: Bank card number + name + ID card number verification.
        # - BANK_CARD_4_META: Bank card number + name + ID card number + phone number verification.
        # 
        # This parameter is required.
        self.product_type = product_type
        # The name.
        # 
        # - If paramType is set to normal, enter the name in plaintext.
        # - If paramType is set to md5, provide the MD5-encrypted first character of the name (32-character lowercase MD5) + the plaintext of the remaining characters.
        # 
        # This parameter is required.
        self.user_name = user_name
        # VERIFY_BANK_CARD: bank card authentication mode. Indicates whether the provided bank card number matches the user\\"s real name, ID card number, and phone number.
        # 
        # This parameter is required.
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

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

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

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('VerifyMode') is not None:
            self.verify_mode = m.get('VerifyMode')

        return self

