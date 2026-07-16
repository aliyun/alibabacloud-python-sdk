# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MobileOnlineStatusRequest(DaraModel):
    def __init__(
        self,
        mobile: str = None,
        param_type: str = None,
    ):
        # The phone number. Valid values:
        # 
        # - If paramType is set to normal, pass in the phone number in plaintext.
        # - If paramType is set to md5, pass in the MD5-encrypted phone number.
        self.mobile = mobile
        # The parameter type. Valid values:
        # 
        # - normal: not encrypted.
        # - md5: MD5-encrypted.
        self.param_type = param_type

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        return self

