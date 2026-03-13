# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnrollAccountResponseBody(DaraModel):
    def __init__(
        self,
        account_uid: int = None,
        request_id: str = None,
    ):
        # The account ID.
        self.account_uid = account_uid
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_uid is not None:
            result['AccountUid'] = self.account_uid

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountUid') is not None:
            self.account_uid = m.get('AccountUid')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

