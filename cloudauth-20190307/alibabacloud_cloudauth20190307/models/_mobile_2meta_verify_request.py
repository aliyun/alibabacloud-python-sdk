# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Mobile2MetaVerifyRequest(DaraModel):
    def __init__(
        self,
        mobile: str = None,
        param_type: str = None,
        user_name: str = None,
    ):
        # Phone number:
        # - When paramType is normal: input the plaintext phone number.
        # - When paramType is md5: input the encrypted phone number.
        # 
        # This parameter is required.
        self.mobile = mobile
        # Encryption method:
        # - normal: plaintext without encryption
        # - md5: MD5 encryption
        # 
        # This parameter is required.
        self.param_type = param_type
        # Name:
        # - When paramType is normal: input the plaintext name.
        # - When paramType is md5: input the encrypted name.
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

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

