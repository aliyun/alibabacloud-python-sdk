# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Id2MetaVerifyRequest(DaraModel):
    def __init__(
        self,
        identify_num: str = None,
        param_type: str = None,
        user_name: str = None,
    ):
        # ID number:
        # 
        # Note
        # Only supports the ID numbers of second-generation resident IDs and Hong Kong, Macao, and Taiwan residence permits.
        # 
        # - When paramType is normal: enter the plaintext ID number.
        # 
        # - When paramType is md5: first 6 digits of the ID number (plaintext) + date of birth (ciphertext) + last 4 digits of the ID number (plaintext).
        self.identify_num = identify_num
        # Encryption method:
        # 
        # - normal: plaintext, no encryption
        # 
        # - md5: MD5 encryption
        self.param_type = param_type
        # Name:
        # 
        # - When paramType is normal: enter the plaintext name.
        # 
        # - When paramType is md5: first character of the name in ciphertext + rest of the name in plaintext.
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

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentifyNum') is not None:
            self.identify_num = m.get('IdentifyNum')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

