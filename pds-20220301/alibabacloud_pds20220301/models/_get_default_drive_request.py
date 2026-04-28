# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDefaultDriveRequest(DaraModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # The user ID. If you use an AccessKey pair for authentication, you must specify this parameter. If you use an access token for authentication, this parameter is optional. By default, the user ID associated with the access token is used.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

