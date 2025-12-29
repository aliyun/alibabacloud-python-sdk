# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MobileDetectRequest(DaraModel):
    def __init__(
        self,
        mobiles: str = None,
        param_type: str = None,
    ):
        # List of phone numbers.
        self.mobiles = mobiles
        # Encryption method:
        # - normal: plaintext, no encryption
        # - md5: MD5 encryption
        self.param_type = param_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mobiles is not None:
            result['Mobiles'] = self.mobiles

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mobiles') is not None:
            self.mobiles = m.get('Mobiles')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        return self

