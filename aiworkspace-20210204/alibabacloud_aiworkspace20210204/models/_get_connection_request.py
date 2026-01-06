# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetConnectionRequest(DaraModel):
    def __init__(
        self,
        encrypt_option: str = None,
    ):
        # The encryption settings. Valid values:
        # 
        # *   PlainText
        # *   Secret
        self.encrypt_option = encrypt_option

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encrypt_option is not None:
            result['EncryptOption'] = self.encrypt_option

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptOption') is not None:
            self.encrypt_option = m.get('EncryptOption')

        return self

