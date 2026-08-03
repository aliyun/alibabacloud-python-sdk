# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GlobalHotelSearchCityPageRequest(DaraModel):
    def __init__(
        self,
        account_no: int = None,
        count: int = None,
        country_code: str = None,
        start: int = None,
        tracer_id: str = None,
    ):
        # This parameter is required.
        self.account_no = account_no
        # This parameter is required.
        self.count = count
        self.country_code = country_code
        self.start = start
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_no is not None:
            result['AccountNo'] = self.account_no

        if self.count is not None:
            result['Count'] = self.count

        if self.country_code is not None:
            result['CountryCode'] = self.country_code

        if self.start is not None:
            result['Start'] = self.start

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

