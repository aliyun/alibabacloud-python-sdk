# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightCreateOrderRequest(DaraModel):
    def __init__(
        self,
        arr_airport_code: str = None,
        arr_city_code: str = None,
        auto_pay: int = None,
        buyer_name: str = None,
        buyer_unique_key: str = None,
        contact_info: main_models.FlightCreateOrderRequestContactInfo = None,
        dep_airport_code: str = None,
        dep_city_code: str = None,
        dep_date: str = None,
        dis_order_id: str = None,
        order_attr: Dict[str, Any] = None,
        order_params: str = None,
        ota_item_id: str = None,
        price: int = None,
        receipt_address: str = None,
        receipt_target: int = None,
        receipt_title: str = None,
        traveler_info_list: List[main_models.FlightCreateOrderRequestTravelerInfoList] = None,
        trip_type: int = None,
    ):
        self.arr_airport_code = arr_airport_code
        # This parameter is required.
        self.arr_city_code = arr_city_code
        self.auto_pay = auto_pay
        self.buyer_name = buyer_name
        # This parameter is required.
        self.buyer_unique_key = buyer_unique_key
        # This parameter is required.
        self.contact_info = contact_info
        self.dep_airport_code = dep_airport_code
        # This parameter is required.
        self.dep_city_code = dep_city_code
        # This parameter is required.
        self.dep_date = dep_date
        # This parameter is required.
        self.dis_order_id = dis_order_id
        self.order_attr = order_attr
        # This parameter is required.
        self.order_params = order_params
        # This parameter is required.
        self.ota_item_id = ota_item_id
        # This parameter is required.
        self.price = price
        self.receipt_address = receipt_address
        self.receipt_target = receipt_target
        self.receipt_title = receipt_title
        # This parameter is required.
        self.traveler_info_list = traveler_info_list
        # This parameter is required.
        self.trip_type = trip_type

    def validate(self):
        if self.contact_info:
            self.contact_info.validate()
        if self.traveler_info_list:
            for v1 in self.traveler_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_airport_code is not None:
            result['arr_airport_code'] = self.arr_airport_code

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.auto_pay is not None:
            result['auto_pay'] = self.auto_pay

        if self.buyer_name is not None:
            result['buyer_name'] = self.buyer_name

        if self.buyer_unique_key is not None:
            result['buyer_unique_key'] = self.buyer_unique_key

        if self.contact_info is not None:
            result['contact_info'] = self.contact_info.to_map()

        if self.dep_airport_code is not None:
            result['dep_airport_code'] = self.dep_airport_code

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        if self.dis_order_id is not None:
            result['dis_order_id'] = self.dis_order_id

        if self.order_attr is not None:
            result['order_attr'] = self.order_attr

        if self.order_params is not None:
            result['order_params'] = self.order_params

        if self.ota_item_id is not None:
            result['ota_item_id'] = self.ota_item_id

        if self.price is not None:
            result['price'] = self.price

        if self.receipt_address is not None:
            result['receipt_address'] = self.receipt_address

        if self.receipt_target is not None:
            result['receipt_target'] = self.receipt_target

        if self.receipt_title is not None:
            result['receipt_title'] = self.receipt_title

        result['traveler_info_list'] = []
        if self.traveler_info_list is not None:
            for k1 in self.traveler_info_list:
                result['traveler_info_list'].append(k1.to_map() if k1 else None)

        if self.trip_type is not None:
            result['trip_type'] = self.trip_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_airport_code') is not None:
            self.arr_airport_code = m.get('arr_airport_code')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('auto_pay') is not None:
            self.auto_pay = m.get('auto_pay')

        if m.get('buyer_name') is not None:
            self.buyer_name = m.get('buyer_name')

        if m.get('buyer_unique_key') is not None:
            self.buyer_unique_key = m.get('buyer_unique_key')

        if m.get('contact_info') is not None:
            temp_model = main_models.FlightCreateOrderRequestContactInfo()
            self.contact_info = temp_model.from_map(m.get('contact_info'))

        if m.get('dep_airport_code') is not None:
            self.dep_airport_code = m.get('dep_airport_code')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        if m.get('dis_order_id') is not None:
            self.dis_order_id = m.get('dis_order_id')

        if m.get('order_attr') is not None:
            self.order_attr = m.get('order_attr')

        if m.get('order_params') is not None:
            self.order_params = m.get('order_params')

        if m.get('ota_item_id') is not None:
            self.ota_item_id = m.get('ota_item_id')

        if m.get('price') is not None:
            self.price = m.get('price')

        if m.get('receipt_address') is not None:
            self.receipt_address = m.get('receipt_address')

        if m.get('receipt_target') is not None:
            self.receipt_target = m.get('receipt_target')

        if m.get('receipt_title') is not None:
            self.receipt_title = m.get('receipt_title')

        self.traveler_info_list = []
        if m.get('traveler_info_list') is not None:
            for k1 in m.get('traveler_info_list'):
                temp_model = main_models.FlightCreateOrderRequestTravelerInfoList()
                self.traveler_info_list.append(temp_model.from_map(k1))

        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')

        return self

class FlightCreateOrderRequestTravelerInfoList(DaraModel):
    def __init__(
        self,
        birthday: str = None,
        cert_nation: str = None,
        cert_no: str = None,
        cert_type: str = None,
        cert_valid_date: str = None,
        name: str = None,
        nationality: str = None,
        nationality_code: str = None,
        out_user_id: str = None,
        phone: str = None,
        sex: int = None,
        type: str = None,
    ):
        self.birthday = birthday
        self.cert_nation = cert_nation
        # This parameter is required.
        self.cert_no = cert_no
        # This parameter is required.
        self.cert_type = cert_type
        self.cert_valid_date = cert_valid_date
        # This parameter is required.
        self.name = name
        # 国籍
        self.nationality = nationality
        # 国籍二字码
        self.nationality_code = nationality_code
        # This parameter is required.
        self.out_user_id = out_user_id
        # This parameter is required.
        self.phone = phone
        self.sex = sex
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.birthday is not None:
            result['birthday'] = self.birthday

        if self.cert_nation is not None:
            result['cert_nation'] = self.cert_nation

        if self.cert_no is not None:
            result['cert_no'] = self.cert_no

        if self.cert_type is not None:
            result['cert_type'] = self.cert_type

        if self.cert_valid_date is not None:
            result['cert_valid_date'] = self.cert_valid_date

        if self.name is not None:
            result['name'] = self.name

        if self.nationality is not None:
            result['nationality'] = self.nationality

        if self.nationality_code is not None:
            result['nationality_code'] = self.nationality_code

        if self.out_user_id is not None:
            result['out_user_id'] = self.out_user_id

        if self.phone is not None:
            result['phone'] = self.phone

        if self.sex is not None:
            result['sex'] = self.sex

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')

        if m.get('cert_nation') is not None:
            self.cert_nation = m.get('cert_nation')

        if m.get('cert_no') is not None:
            self.cert_no = m.get('cert_no')

        if m.get('cert_type') is not None:
            self.cert_type = m.get('cert_type')

        if m.get('cert_valid_date') is not None:
            self.cert_valid_date = m.get('cert_valid_date')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nationality') is not None:
            self.nationality = m.get('nationality')

        if m.get('nationality_code') is not None:
            self.nationality_code = m.get('nationality_code')

        if m.get('out_user_id') is not None:
            self.out_user_id = m.get('out_user_id')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('sex') is not None:
            self.sex = m.get('sex')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class FlightCreateOrderRequestContactInfo(DaraModel):
    def __init__(
        self,
        contact_email: str = None,
        contact_name: str = None,
        contact_phone: str = None,
    ):
        self.contact_email = contact_email
        # This parameter is required.
        self.contact_name = contact_name
        # This parameter is required.
        self.contact_phone = contact_phone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_email is not None:
            result['contact_email'] = self.contact_email

        if self.contact_name is not None:
            result['contact_name'] = self.contact_name

        if self.contact_phone is not None:
            result['contact_phone'] = self.contact_phone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contact_email') is not None:
            self.contact_email = m.get('contact_email')

        if m.get('contact_name') is not None:
            self.contact_name = m.get('contact_name')

        if m.get('contact_phone') is not None:
            self.contact_phone = m.get('contact_phone')

        return self

