# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RestoreAccessKeyFromRecycleBinRequest(DaraModel):
    def __init__(
        self,
        user_access_key_id: str = None,
        user_id: str = None,
    ):
        self.user_access_key_id = user_access_key_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

