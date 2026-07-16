# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchAssignSeatsRequest(DaraModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        locale: str = None,
        seat_type: str = None,
    ):
        # The list of target member IDs.
        self.account_ids = account_ids
        # The language. Valid values: zh-CN and en-US.
        self.locale = locale
        # The seat type. Valid values:
        # - standard: standard seat
        # - pro: pro seat
        # - max: premium seat
        # 
        # This parameter is required.
        self.seat_type = seat_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.locale is not None:
            result['Locale'] = self.locale

        if self.seat_type is not None:
            result['SeatType'] = self.seat_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('Locale') is not None:
            self.locale = m.get('Locale')

        if m.get('SeatType') is not None:
            self.seat_type = m.get('SeatType')

        return self

