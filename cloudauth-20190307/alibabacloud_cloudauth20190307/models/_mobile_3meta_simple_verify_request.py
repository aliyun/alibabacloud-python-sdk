# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Mobile3MetaSimpleVerifyRequest(DaraModel):
    def __init__(
        self,
        identify_num: str = None,
        mobile: str = None,
        param_type: str = None,
        user_name: str = None,
    ):
        # ID card number:
        # 
        # Note
        # Only the ID numbers of the second-generation resident ID card and Hong Kong, Macao, and Taiwan residence permits are supported.
        # 
        # - When paramType is set to normal: pass in the ID card number in plaintext.
        # 
        # - When paramType is set to md5: pass in the encrypted ID card number.
        self.identify_num = identify_num
        # Mobile number:
        # 
        # - When paramType is set to normal: pass in the mobile number in plaintext.
        # 
        # - When paramType is set to md5: pass in the encrypted mobile number.
        self.mobile = mobile
        # Encryption method:
        # 
        # - normal: plaintext, no encryption
        # 
        # - md5: MD5 encryption
        self.param_type = param_type
        # Name:
        # 
        # - When paramType is set to normal: pass in the name in plaintext.
        # 
        # - When paramType is set to md5: pass in the encrypted name.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identify_num is not None:
            result['IdentifyNum'] = self.identify_num

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

