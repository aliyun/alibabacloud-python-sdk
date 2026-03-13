# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightCreateOrderV2Request(DaraModel):
    def __init__(
        self,
        async_create_order_key: str = None,
        async_create_order_mode: bool = None,
        btrip_user_id: str = None,
        buyer_name: str = None,
        contact_info: main_models.FlightCreateOrderV2RequestContactInfo = None,
        isv_name: str = None,
        ota_item_id: str = None,
        out_order_id: str = None,
        total_price_cent: int = None,
        travelers: List[main_models.FlightCreateOrderV2RequestTravelers] = None,
    ):
        self.async_create_order_key = async_create_order_key
        self.async_create_order_mode = async_create_order_mode
        self.btrip_user_id = btrip_user_id
        self.buyer_name = buyer_name
        # This parameter is required.
        self.contact_info = contact_info
        # This parameter is required.
        self.isv_name = isv_name
        # This parameter is required.
        self.ota_item_id = ota_item_id
        # This parameter is required.
        self.out_order_id = out_order_id
        self.total_price_cent = total_price_cent
        # This parameter is required.
        self.travelers = travelers

    def validate(self):
        if self.contact_info:
            self.contact_info.validate()
        if self.travelers:
            for v1 in self.travelers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_create_order_key is not None:
            result['async_create_order_key'] = self.async_create_order_key

        if self.async_create_order_mode is not None:
            result['async_create_order_mode'] = self.async_create_order_mode

        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.buyer_name is not None:
            result['buyer_name'] = self.buyer_name

        if self.contact_info is not None:
            result['contact_info'] = self.contact_info.to_map()

        if self.isv_name is not None:
            result['isv_name'] = self.isv_name

        if self.ota_item_id is not None:
            result['ota_item_id'] = self.ota_item_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        if self.total_price_cent is not None:
            result['total_price_cent'] = self.total_price_cent

        result['travelers'] = []
        if self.travelers is not None:
            for k1 in self.travelers:
                result['travelers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_create_order_key') is not None:
            self.async_create_order_key = m.get('async_create_order_key')

        if m.get('async_create_order_mode') is not None:
            self.async_create_order_mode = m.get('async_create_order_mode')

        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('buyer_name') is not None:
            self.buyer_name = m.get('buyer_name')

        if m.get('contact_info') is not None:
            temp_model = main_models.FlightCreateOrderV2RequestContactInfo()
            self.contact_info = temp_model.from_map(m.get('contact_info'))

        if m.get('isv_name') is not None:
            self.isv_name = m.get('isv_name')

        if m.get('ota_item_id') is not None:
            self.ota_item_id = m.get('ota_item_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        if m.get('total_price_cent') is not None:
            self.total_price_cent = m.get('total_price_cent')

        self.travelers = []
        if m.get('travelers') is not None:
            for k1 in m.get('travelers'):
                temp_model = main_models.FlightCreateOrderV2RequestTravelers()
                self.travelers.append(temp_model.from_map(k1))

        return self

class FlightCreateOrderV2RequestTravelers(DaraModel):
    def __init__(
        self,
        birthday: str = None,
        cert_nation: str = None,
        cert_no: str = None,
        cert_type: int = None,
        cert_valid_date: str = None,
        cost_center_name: str = None,
        cost_center_number: str = None,
        dept_id: str = None,
        dept_name: str = None,
        gender: int = None,
        invoice_title: str = None,
        nationality: str = None,
        nationality_code: str = None,
        passenger_name: str = None,
        passenger_type: int = None,
        phone: str = None,
        project_code: str = None,
        project_title: str = None,
        tax_number: str = None,
        user_id: str = None,
        user_type: int = None,
    ):
        # This parameter is required.
        self.birthday = birthday
        self.cert_nation = cert_nation
        # This parameter is required.
        self.cert_no = cert_no
        # This parameter is required.
        self.cert_type = cert_type
        self.cert_valid_date = cert_valid_date
        self.cost_center_name = cost_center_name
        self.cost_center_number = cost_center_number
        self.dept_id = dept_id
        self.dept_name = dept_name
        # This parameter is required.
        self.gender = gender
        self.invoice_title = invoice_title
        self.nationality = nationality
        self.nationality_code = nationality_code
        # This parameter is required.
        self.passenger_name = passenger_name
        # This parameter is required.
        self.passenger_type = passenger_type
        # This parameter is required.
        self.phone = phone
        self.project_code = project_code
        self.project_title = project_title
        self.tax_number = tax_number
        # This parameter is required.
        self.user_id = user_id
        self.user_type = user_type

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

        if self.cost_center_name is not None:
            result['cost_center_name'] = self.cost_center_name

        if self.cost_center_number is not None:
            result['cost_center_number'] = self.cost_center_number

        if self.dept_id is not None:
            result['dept_id'] = self.dept_id

        if self.dept_name is not None:
            result['dept_name'] = self.dept_name

        if self.gender is not None:
            result['gender'] = self.gender

        if self.invoice_title is not None:
            result['invoice_title'] = self.invoice_title

        if self.nationality is not None:
            result['nationality'] = self.nationality

        if self.nationality_code is not None:
            result['nationality_code'] = self.nationality_code

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        if self.passenger_type is not None:
            result['passenger_type'] = self.passenger_type

        if self.phone is not None:
            result['phone'] = self.phone

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_title is not None:
            result['project_title'] = self.project_title

        if self.tax_number is not None:
            result['tax_number'] = self.tax_number

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_type is not None:
            result['user_type'] = self.user_type

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

        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')

        if m.get('cost_center_number') is not None:
            self.cost_center_number = m.get('cost_center_number')

        if m.get('dept_id') is not None:
            self.dept_id = m.get('dept_id')

        if m.get('dept_name') is not None:
            self.dept_name = m.get('dept_name')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('invoice_title') is not None:
            self.invoice_title = m.get('invoice_title')

        if m.get('nationality') is not None:
            self.nationality = m.get('nationality')

        if m.get('nationality_code') is not None:
            self.nationality_code = m.get('nationality_code')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        if m.get('passenger_type') is not None:
            self.passenger_type = m.get('passenger_type')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        if m.get('tax_number') is not None:
            self.tax_number = m.get('tax_number')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_type') is not None:
            self.user_type = m.get('user_type')

        return self

class FlightCreateOrderV2RequestContactInfo(DaraModel):
    def __init__(
        self,
        contact_email: str = None,
        contact_name: str = None,
        contact_phone: str = None,
        send_msg_to_passenger: bool = None,
    ):
        self.contact_email = contact_email
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        self.send_msg_to_passenger = send_msg_to_passenger

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

        if self.send_msg_to_passenger is not None:
            result['send_msg_to_passenger'] = self.send_msg_to_passenger

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contact_email') is not None:
            self.contact_email = m.get('contact_email')

        if m.get('contact_name') is not None:
            self.contact_name = m.get('contact_name')

        if m.get('contact_phone') is not None:
            self.contact_phone = m.get('contact_phone')

        if m.get('send_msg_to_passenger') is not None:
            self.send_msg_to_passenger = m.get('send_msg_to_passenger')

        return self

