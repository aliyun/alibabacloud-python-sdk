# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EstimatedPriceQueryV2Request(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        depart_date: str = None,
        from_city: str = None,
        leave_date: str = None,
        to_city: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.biz_type = biz_type
        # This parameter is required.
        self.depart_date = depart_date
        # This parameter is required.
        self.from_city = from_city
        # This parameter is required.
        self.leave_date = leave_date
        # This parameter is required.
        self.to_city = to_city
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['biz_type'] = self.biz_type

        if self.depart_date is not None:
            result['depart_date'] = self.depart_date

        if self.from_city is not None:
            result['from_city'] = self.from_city

        if self.leave_date is not None:
            result['leave_date'] = self.leave_date

        if self.to_city is not None:
            result['to_city'] = self.to_city

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('biz_type') is not None:
            self.biz_type = m.get('biz_type')

        if m.get('depart_date') is not None:
            self.depart_date = m.get('depart_date')

        if m.get('from_city') is not None:
            self.from_city = m.get('from_city')

        if m.get('leave_date') is not None:
            self.leave_date = m.get('leave_date')

        if m.get('to_city') is not None:
            self.to_city = m.get('to_city')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

