# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAdUsersCountResponseBody(DaraModel):
    def __init__(
        self,
        ad_user_count: int = None,
        request_id: str = None,
    ):
        self.ad_user_count = ad_user_count
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_user_count is not None:
            result['AdUserCount'] = self.ad_user_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdUserCount') is not None:
            self.ad_user_count = m.get('AdUserCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

