# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GlobalHotelBatchGetHotelDetailRequest(DaraModel):
    def __init__(
        self,
        account_no: int = None,
        language: str = None,
        standard_hotel_ids: List[str] = None,
        tracer_id: str = None,
    ):
        # The ID of the distributor account.
        # 
        # This parameter is required.
        self.account_no = account_no
        # The language. For example, en or zh.
        self.language = language
        # The list of standard hotel IDs. A maximum of 100 IDs are supported.
        # 
        # This parameter is required.
        self.standard_hotel_ids = standard_hotel_ids
        # string
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

        if self.language is not None:
            result['Language'] = self.language

        if self.standard_hotel_ids is not None:
            result['StandardHotelIds'] = self.standard_hotel_ids

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('StandardHotelIds') is not None:
            self.standard_hotel_ids = m.get('StandardHotelIds')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

