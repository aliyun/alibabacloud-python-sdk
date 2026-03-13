# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateEmployeeLeaveStatusRequest(DaraModel):
    def __init__(
        self,
        is_leave: bool = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.is_leave = is_leave
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_leave is not None:
            result['is_leave'] = self.is_leave

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('is_leave') is not None:
            self.is_leave = m.get('is_leave')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

