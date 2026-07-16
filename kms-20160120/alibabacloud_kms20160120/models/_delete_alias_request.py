# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAliasRequest(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
    ):
        # The alias that you want to delete.
        # 
        # The value must be 1 to 255 characters in length and must include the alias/ prefix.
        # 
        # This parameter is required.
        self.alias_name = alias_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        return self

