# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeletePublicKeyRequest(DaraModel):
    def __init__(
        self,
        key_name: str = None,
    ):
        # This parameter is required.
        self.key_name = key_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_name is not None:
            result['KeyName'] = self.key_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        return self

