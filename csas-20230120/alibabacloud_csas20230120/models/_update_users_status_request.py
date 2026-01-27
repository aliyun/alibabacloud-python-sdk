# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateUsersStatusRequest(DaraModel):
    def __init__(
        self,
        sase_user_ids: List[str] = None,
        status: str = None,
    ):
        # This parameter is required.
        self.sase_user_ids = sase_user_ids
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sase_user_ids is not None:
            result['SaseUserIds'] = self.sase_user_ids

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SaseUserIds') is not None:
            self.sase_user_ids = m.get('SaseUserIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

