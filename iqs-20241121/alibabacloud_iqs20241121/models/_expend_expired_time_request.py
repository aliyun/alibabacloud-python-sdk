# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExpendExpiredTimeRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        test_start_time: str = None,
    ):
        self.account_id = account_id
        self.test_start_time = test_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.test_start_time is not None:
            result['testStartTime'] = self.test_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('testStartTime') is not None:
            self.test_start_time = m.get('testStartTime')

        return self

