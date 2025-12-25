# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AkSkIdentityConfig(DaraModel):
    def __init__(
        self,
        ak: str = None,
        generate_mode: str = None,
        sk: str = None,
        type: str = None,
    ):
        self.ak = ak
        self.generate_mode = generate_mode
        self.sk = sk
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ak is not None:
            result['ak'] = self.ak

        if self.generate_mode is not None:
            result['generateMode'] = self.generate_mode

        if self.sk is not None:
            result['sk'] = self.sk

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ak') is not None:
            self.ak = m.get('ak')

        if m.get('generateMode') is not None:
            self.generate_mode = m.get('generateMode')

        if m.get('sk') is not None:
            self.sk = m.get('sk')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

