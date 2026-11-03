# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Id2MetaStandardVerifyRequest(DaraModel):
    def __init__(
        self,
        identify_num: str = None,
        param_type: str = None,
        user_name: str = None,
    ):
        # The ID card number.
        # - If paramType is set to normal: enter the plaintext ID card number.
        # - If paramType is set to md5: enter the first 6 digits of the ID card number (plaintext) + the date of birth (ciphertext) + the last 4 digits of the ID card number (plaintext).
        self.identify_num = identify_num
        # The parameter type. Valid values:
        # - normal: No encryption.
        # - md5: MD5 encryption.
        self.param_type = param_type
        # The name.
        # - If paramType is set to normal: enter the plaintext name.
        # - If paramType is set to md5: enter the first character of the name (ciphertext) + the rest of the name (plaintext).
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

