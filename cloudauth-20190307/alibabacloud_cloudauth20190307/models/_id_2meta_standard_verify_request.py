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
        # ID number:
        # 
        # - When `paramType` is normal: enter the plain text of the ID number.
        # - When `paramType` is md5:
        # The first 6 digits (plain text) + date of birth (encrypted) + last 4 digits (plain text).
        self.identify_num = identify_num
        # Parameter type:
        # 
        # - normal: unencrypted.
        # - md5: md5 encrypted.
        self.param_type = param_type
        # Name:
        # 
        # - When `paramType` is normal: enter the plain text of the name.
        # - When `paramType` is md5: the first character of the name (encrypted) + the rest of the name (plain text).
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

