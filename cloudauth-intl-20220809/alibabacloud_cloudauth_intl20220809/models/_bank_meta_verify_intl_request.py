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
        # - If paramType is set to normal, enter the plaintext bank card number.
        # - If paramType is set to md5, enter the plaintext of the bank card number except the last 6 digits, followed by the 32-character lowercase MD5 hash of the last 6 digits.
        # 
        # This parameter is required.
        self.bank_card = bank_card
        # The identification document number.
        # - If paramType is set to normal, enter the plaintext identification document number.
        # - If paramType is set to md5:
        #     - For an ID card, enter the first 6 digits in plaintext, followed by the ciphertext of the date of birth, and then the last 4 digits in plaintext.
        #     - For other identification documents, encrypt the last two characters by using MD5.
        # 
        # Important:
        # This parameter is required if ProductType is set to one of the following values:
        # - BANK_CARD_3_META
        # - BANK_CARD_4_META
        self.identify_num = identify_num
        # The type of the identification document. If you leave this parameter empty, the default value is ID card. For other types of identification documents, see the following table.
        self.identity_type = identity_type
        # The mobile phone number.
        # - If paramType is set to normal, enter the plaintext mobile phone number.
        # - If paramType is set to md5, enter the ciphertext mobile phone number.
        # 
        # Important:
        # 
        # - This parameter is required if ProductType is set to BANK_CARD_4_META.
        self.mobile = mobile
        # The encryption method. Valid values:
        # - normal: No encryption.
        # - md5: MD5 encryption.
        # 
        # Important:
        # 
        # - The ciphertext of all parameters must be a 32-character lowercase MD5 string.
        # - Different MD5 tools may generate different ciphertexts. If the API call succeeds before encryption but fails after encryption, try using a different MD5 tool.
        # 
        # This parameter is required.
        self.param_type = param_type
        # The fixed value. Valid value: BANK_CARD_N_META.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The product type. Valid values:
        # 
        # - BANK_CARD_2_META: Verifies the bank card number and name.
        # - BANK_CARD_3_META: Verifies the bank card number, name, and ID card number.
        # - BANK_CARD_4_META: Verifies the bank card number, name, ID card number, and mobile phone number.
        # 
        # This parameter is required.
        self.product_type = product_type
        # The name.
        # 
        # - If paramType is set to normal, enter the plaintext name.
        # - If paramType is set to md5, enter the 32-character lowercase MD5 hash of the first character of the name, followed by the plaintext of the remaining characters.
        # 
        # This parameter is required.
        self.user_name = user_name
        # The verification mode. Valid value: VERIFY_BANK_CARD. This value indicates the bank card authentication mode, which verifies whether the provided bank card number matches the real name, ID card number, and mobile phone number of the user.
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

