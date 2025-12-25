# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCiphersRequest(DaraModel):
    def __init__(
        self,
        ciphers_group: str = None,
    ):
        # The name of the cipher suite group, which can be: all, strict, custom.
        # 
        # This parameter is required.
        self.ciphers_group = ciphers_group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ciphers_group is not None:
            result['CiphersGroup'] = self.ciphers_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CiphersGroup') is not None:
            self.ciphers_group = m.get('CiphersGroup')

        return self

