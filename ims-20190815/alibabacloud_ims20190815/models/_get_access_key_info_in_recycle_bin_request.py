# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAccessKeyInfoInRecycleBinRequest(DaraModel):
    def __init__(
        self,
        user_access_key_id: str = None,
    ):
        # The AccessKey ID of the Resource Access Management (RAM) user.
        # 
        # This parameter is required.
        self.user_access_key_id = user_access_key_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')

        return self

