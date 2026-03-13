# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddressGetRequest(DaraModel):
    def __init__(
        self,
        action_type: int = None,
        arr_city_code: str = None,
        arr_city_name: str = None,
        car_scenes_code: str = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_date: str = None,
        itinerary_id: str = None,
        middle_page: int = None,
        order_id: str = None,
        phone: str = None,
        session_parameters: str = None,
        sub_corp_id: str = None,
        taobao_callback_url: str = None,
        thirdpart_apply_id: str = None,
        traveler_id: str = None,
        type: int = None,
        use_booking_proxy: int = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.action_type = action_type
        self.arr_city_code = arr_city_code
        self.arr_city_name = arr_city_name
        self.car_scenes_code = car_scenes_code
        self.dep_city_code = dep_city_code
        self.dep_city_name = dep_city_name
        self.dep_date = dep_date
        self.itinerary_id = itinerary_id
        self.middle_page = middle_page
        self.order_id = order_id
        self.phone = phone
        self.session_parameters = session_parameters
        self.sub_corp_id = sub_corp_id
        self.taobao_callback_url = taobao_callback_url
        self.thirdpart_apply_id = thirdpart_apply_id
        self.traveler_id = traveler_id
        self.type = type
        self.use_booking_proxy = use_booking_proxy
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['action_type'] = self.action_type

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_city_name is not None:
            result['arr_city_name'] = self.arr_city_name

        if self.car_scenes_code is not None:
            result['car_scenes_code'] = self.car_scenes_code

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_city_name is not None:
            result['dep_city_name'] = self.dep_city_name

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        if self.itinerary_id is not None:
            result['itinerary_id'] = self.itinerary_id

        if self.middle_page is not None:
            result['middle_page'] = self.middle_page

        if self.order_id is not None:
            result['order_Id'] = self.order_id

        if self.phone is not None:
            result['phone'] = self.phone

        if self.session_parameters is not None:
            result['session_parameters'] = self.session_parameters

        if self.sub_corp_id is not None:
            result['sub_corp_id'] = self.sub_corp_id

        if self.taobao_callback_url is not None:
            result['taobao_callback_url'] = self.taobao_callback_url

        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id

        if self.traveler_id is not None:
            result['traveler_id'] = self.traveler_id

        if self.type is not None:
            result['type'] = self.type

        if self.use_booking_proxy is not None:
            result['use_booking_proxy'] = self.use_booking_proxy

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action_type') is not None:
            self.action_type = m.get('action_type')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')

        if m.get('car_scenes_code') is not None:
            self.car_scenes_code = m.get('car_scenes_code')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_city_name') is not None:
            self.dep_city_name = m.get('dep_city_name')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        if m.get('itinerary_id') is not None:
            self.itinerary_id = m.get('itinerary_id')

        if m.get('middle_page') is not None:
            self.middle_page = m.get('middle_page')

        if m.get('order_Id') is not None:
            self.order_id = m.get('order_Id')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('session_parameters') is not None:
            self.session_parameters = m.get('session_parameters')

        if m.get('sub_corp_id') is not None:
            self.sub_corp_id = m.get('sub_corp_id')

        if m.get('taobao_callback_url') is not None:
            self.taobao_callback_url = m.get('taobao_callback_url')

        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')

        if m.get('traveler_id') is not None:
            self.traveler_id = m.get('traveler_id')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('use_booking_proxy') is not None:
            self.use_booking_proxy = m.get('use_booking_proxy')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

