# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class IntlFlightReShopApplyRequest(DaraModel):
    def __init__(
        self,
        async_apply_key: str = None,
        async_apply_mode: bool = None,
        order_id: str = None,
        out_order_id: str = None,
        out_re_shop_apply_id: str = None,
        passenger_journey_group_key: str = None,
        re_shop_reason_code: str = None,
        selected_journeys: List[main_models.IntlFlightReShopApplyRequestSelectedJourneys] = None,
        selected_passengers: List[main_models.IntlFlightReShopApplyRequestSelectedPassengers] = None,
        user_intention_memo: str = None,
    ):
        self.async_apply_key = async_apply_key
        self.async_apply_mode = async_apply_mode
        # This parameter is required.
        self.order_id = order_id
        self.out_order_id = out_order_id
        self.out_re_shop_apply_id = out_re_shop_apply_id
        # This parameter is required.
        self.passenger_journey_group_key = passenger_journey_group_key
        # This parameter is required.
        self.re_shop_reason_code = re_shop_reason_code
        # This parameter is required.
        self.selected_journeys = selected_journeys
        # This parameter is required.
        self.selected_passengers = selected_passengers
        self.user_intention_memo = user_intention_memo

    def validate(self):
        if self.selected_journeys:
            for v1 in self.selected_journeys:
                 if v1:
                    v1.validate()
        if self.selected_passengers:
            for v1 in self.selected_passengers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_apply_key is not None:
            result['async_apply_key'] = self.async_apply_key

        if self.async_apply_mode is not None:
            result['async_apply_mode'] = self.async_apply_mode

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        if self.out_re_shop_apply_id is not None:
            result['out_re_shop_apply_id'] = self.out_re_shop_apply_id

        if self.passenger_journey_group_key is not None:
            result['passenger_journey_group_key'] = self.passenger_journey_group_key

        if self.re_shop_reason_code is not None:
            result['re_shop_reason_code'] = self.re_shop_reason_code

        result['selected_journeys'] = []
        if self.selected_journeys is not None:
            for k1 in self.selected_journeys:
                result['selected_journeys'].append(k1.to_map() if k1 else None)

        result['selected_passengers'] = []
        if self.selected_passengers is not None:
            for k1 in self.selected_passengers:
                result['selected_passengers'].append(k1.to_map() if k1 else None)

        if self.user_intention_memo is not None:
            result['user_intention_memo'] = self.user_intention_memo

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_apply_key') is not None:
            self.async_apply_key = m.get('async_apply_key')

        if m.get('async_apply_mode') is not None:
            self.async_apply_mode = m.get('async_apply_mode')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        if m.get('out_re_shop_apply_id') is not None:
            self.out_re_shop_apply_id = m.get('out_re_shop_apply_id')

        if m.get('passenger_journey_group_key') is not None:
            self.passenger_journey_group_key = m.get('passenger_journey_group_key')

        if m.get('re_shop_reason_code') is not None:
            self.re_shop_reason_code = m.get('re_shop_reason_code')

        self.selected_journeys = []
        if m.get('selected_journeys') is not None:
            for k1 in m.get('selected_journeys'):
                temp_model = main_models.IntlFlightReShopApplyRequestSelectedJourneys()
                self.selected_journeys.append(temp_model.from_map(k1))

        self.selected_passengers = []
        if m.get('selected_passengers') is not None:
            for k1 in m.get('selected_passengers'):
                temp_model = main_models.IntlFlightReShopApplyRequestSelectedPassengers()
                self.selected_passengers.append(temp_model.from_map(k1))

        if m.get('user_intention_memo') is not None:
            self.user_intention_memo = m.get('user_intention_memo')

        return self

class IntlFlightReShopApplyRequestSelectedPassengers(DaraModel):
    def __init__(
        self,
        full_name: str = None,
        passenger_id: int = None,
    ):
        self.full_name = full_name
        # This parameter is required.
        self.passenger_id = passenger_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.full_name is not None:
            result['full_name'] = self.full_name

        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('full_name') is not None:
            self.full_name = m.get('full_name')

        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        return self

class IntlFlightReShopApplyRequestSelectedJourneys(DaraModel):
    def __init__(
        self,
        arr_city_code: str = None,
        dep_city_code: str = None,
        intent_date: str = None,
        selected_flights: List[main_models.IntlFlightReShopApplyRequestSelectedJourneysSelectedFlights] = None,
    ):
        # This parameter is required.
        self.arr_city_code = arr_city_code
        # This parameter is required.
        self.dep_city_code = dep_city_code
        # This parameter is required.
        self.intent_date = intent_date
        # This parameter is required.
        self.selected_flights = selected_flights

    def validate(self):
        if self.selected_flights:
            for v1 in self.selected_flights:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.intent_date is not None:
            result['intent_date'] = self.intent_date

        result['selected_flights'] = []
        if self.selected_flights is not None:
            for k1 in self.selected_flights:
                result['selected_flights'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('intent_date') is not None:
            self.intent_date = m.get('intent_date')

        self.selected_flights = []
        if m.get('selected_flights') is not None:
            for k1 in m.get('selected_flights'):
                temp_model = main_models.IntlFlightReShopApplyRequestSelectedJourneysSelectedFlights()
                self.selected_flights.append(temp_model.from_map(k1))

        return self

class IntlFlightReShopApplyRequestSelectedJourneysSelectedFlights(DaraModel):
    def __init__(
        self,
        arr_city_code: str = None,
        dep_city_code: str = None,
        segment_key: str = None,
    ):
        # This parameter is required.
        self.arr_city_code = arr_city_code
        # This parameter is required.
        self.dep_city_code = dep_city_code
        # This parameter is required.
        self.segment_key = segment_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.segment_key is not None:
            result['segment_key'] = self.segment_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('segment_key') is not None:
            self.segment_key = m.get('segment_key')

        return self

