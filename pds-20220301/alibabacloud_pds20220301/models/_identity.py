# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Identity(DaraModel):
    def __init__(
        self,
        identity_id: str = None,
        identity_type: str = None,
    ):
        # The ID of the user or the group.
        self.identity_id = identity_id
        # The type of the identity. Valid values:
        # 
        # *   IT_User
        # *   IT_Group
        self.identity_type = identity_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_id is not None:
            result['identity_id'] = self.identity_id

        if self.identity_type is not None:
            result['identity_type'] = self.identity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identity_id') is not None:
            self.identity_id = m.get('identity_id')

        if m.get('identity_type') is not None:
            self.identity_type = m.get('identity_type')

        return self

