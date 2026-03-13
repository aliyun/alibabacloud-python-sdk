# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EstimatedPriceQueryRequest(DaraModel):
    def __init__(
        self,
        arr_city: str = None,
        category: str = None,
        dep_city: str = None,
        end_time: int = None,
        itinerary_id: str = None,
        start_time: int = None,
        sub_corp_id: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.arr_city = arr_city
        # This parameter is required.
        self.category = category
        # This parameter is required.
        self.dep_city = dep_city
        # This parameter is required.
        self.end_time = end_time
        self.itinerary_id = itinerary_id
        # This parameter is required.
        self.start_time = start_time
        self.sub_corp_id = sub_corp_id
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_city is not None:
            result['arr_city'] = self.arr_city

        if self.category is not None:
            result['category'] = self.category

        if self.dep_city is not None:
            result['dep_city'] = self.dep_city

        if self.end_time is not None:
            result['end_time'] = self.end_time

        if self.itinerary_id is not None:
            result['itinerary_id'] = self.itinerary_id

        if self.start_time is not None:
            result['start_time'] = self.start_time

        if self.sub_corp_id is not None:
            result['sub_corp_id'] = self.sub_corp_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city') is not None:
            self.arr_city = m.get('arr_city')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('dep_city') is not None:
            self.dep_city = m.get('dep_city')

        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')

        if m.get('itinerary_id') is not None:
            self.itinerary_id = m.get('itinerary_id')

        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')

        if m.get('sub_corp_id') is not None:
            self.sub_corp_id = m.get('sub_corp_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

