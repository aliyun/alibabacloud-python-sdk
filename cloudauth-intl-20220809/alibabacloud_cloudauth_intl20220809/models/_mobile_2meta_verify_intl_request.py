# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Mobile2MetaVerifyIntlRequest(DaraModel):
    def __init__(
        self,
        mobile: str = None,
        param_type: str = None,
        product_code: str = None,
        user_name: str = None,
    ):
        # The phone number.
        # 
        # - If ParamType is set to normal, pass in the phone number in plaintext.
        # - If ParamType is set to md5, pass in the phone number in ciphertext as a 32-character lowercase MD5 string.
        # 
        # This parameter is required.
        self.mobile = mobile
        # The parameter type. Valid values:
        # 
        # - normal: not encrypted
        # - md5: MD5-encrypted.
        # 
        # This parameter is required.
        self.param_type = param_type
        # The product code. Set this parameter to MOBILE_2META.
        # 
        # This parameter is required.
        self.product_code = product_code
        # The name. Valid values:
        # 
        # - If ParamType is set to normal, pass in the name in plaintext.
        # - If ParamType is set to md5, pass in the name in ciphertext as a 32-character lowercase MD5 string.
        # 
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

