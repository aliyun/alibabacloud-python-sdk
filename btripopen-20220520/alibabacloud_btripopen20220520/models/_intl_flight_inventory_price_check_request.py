# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class IntlFlightInventoryPriceCheckRequest(DaraModel):
    def __init__(
        self,
        btrip_user_id: str = None,
        buyer_name: str = None,
        isv_name: str = None,
        order_price: int = None,
        ota_item_id: str = None,
        passenger_list: List[main_models.IntlFlightInventoryPriceCheckRequestPassengerList] = None,
    ):
        # This parameter is required.
        self.btrip_user_id = btrip_user_id
        self.buyer_name = buyer_name
        self.isv_name = isv_name
        self.order_price = order_price
        # This parameter is required.
        self.ota_item_id = ota_item_id
        # This parameter is required.
        self.passenger_list = passenger_list

    def validate(self):
        if self.passenger_list:
            for v1 in self.passenger_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.buyer_name is not None:
            result['buyer_name'] = self.buyer_name

        if self.isv_name is not None:
            result['isv_name'] = self.isv_name

        if self.order_price is not None:
            result['order_price'] = self.order_price

        if self.ota_item_id is not None:
            result['ota_item_id'] = self.ota_item_id

        result['passenger_list'] = []
        if self.passenger_list is not None:
            for k1 in self.passenger_list:
                result['passenger_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('buyer_name') is not None:
            self.buyer_name = m.get('buyer_name')

        if m.get('isv_name') is not None:
            self.isv_name = m.get('isv_name')

        if m.get('order_price') is not None:
            self.order_price = m.get('order_price')

        if m.get('ota_item_id') is not None:
            self.ota_item_id = m.get('ota_item_id')

        self.passenger_list = []
        if m.get('passenger_list') is not None:
            for k1 in m.get('passenger_list'):
                temp_model = main_models.IntlFlightInventoryPriceCheckRequestPassengerList()
                self.passenger_list.append(temp_model.from_map(k1))

        return self

class IntlFlightInventoryPriceCheckRequestPassengerList(DaraModel):
    def __init__(
        self,
        birthday: str = None,
        cert_info: main_models.IntlFlightInventoryPriceCheckRequestPassengerListCertInfo = None,
        full_name: str = None,
        gender: int = None,
        job_no: str = None,
        nationality: str = None,
        nationality_code: str = None,
        phone: str = None,
        type: int = None,
        user_id: str = None,
        user_type: int = None,
    ):
        # This parameter is required.
        self.birthday = birthday
        # This parameter is required.
        self.cert_info = cert_info
        # This parameter is required.
        self.full_name = full_name
        # This parameter is required.
        self.gender = gender
        self.job_no = job_no
        # This parameter is required.
        self.nationality = nationality
        self.nationality_code = nationality_code
        # This parameter is required.
        self.phone = phone
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.user_id = user_id
        self.user_type = user_type

    def validate(self):
        if self.cert_info:
            self.cert_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.birthday is not None:
            result['birthday'] = self.birthday

        if self.cert_info is not None:
            result['cert_info'] = self.cert_info.to_map()

        if self.full_name is not None:
            result['full_name'] = self.full_name

        if self.gender is not None:
            result['gender'] = self.gender

        if self.job_no is not None:
            result['job_no'] = self.job_no

        if self.nationality is not None:
            result['nationality'] = self.nationality

        if self.nationality_code is not None:
            result['nationality_code'] = self.nationality_code

        if self.phone is not None:
            result['phone'] = self.phone

        if self.type is not None:
            result['type'] = self.type

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.user_type is not None:
            result['user_type'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')

        if m.get('cert_info') is not None:
            temp_model = main_models.IntlFlightInventoryPriceCheckRequestPassengerListCertInfo()
            self.cert_info = temp_model.from_map(m.get('cert_info'))

        if m.get('full_name') is not None:
            self.full_name = m.get('full_name')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('job_no') is not None:
            self.job_no = m.get('job_no')

        if m.get('nationality') is not None:
            self.nationality = m.get('nationality')

        if m.get('nationality_code') is not None:
            self.nationality_code = m.get('nationality_code')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('user_type') is not None:
            self.user_type = m.get('user_type')

        return self

class IntlFlightInventoryPriceCheckRequestPassengerListCertInfo(DaraModel):
    def __init__(
        self,
        cert_no: str = None,
        cert_type: int = None,
        cert_valid_date: str = None,
        issue_place: str = None,
    ):
        # This parameter is required.
        self.cert_no = cert_no
        # This parameter is required.
        self.cert_type = cert_type
        self.cert_valid_date = cert_valid_date
        self.issue_place = issue_place

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_no is not None:
            result['cert_no'] = self.cert_no

        if self.cert_type is not None:
            result['cert_type'] = self.cert_type

        if self.cert_valid_date is not None:
            result['cert_valid_date'] = self.cert_valid_date

        if self.issue_place is not None:
            result['issue_place'] = self.issue_place

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cert_no') is not None:
            self.cert_no = m.get('cert_no')

        if m.get('cert_type') is not None:
            self.cert_type = m.get('cert_type')

        if m.get('cert_valid_date') is not None:
            self.cert_valid_date = m.get('cert_valid_date')

        if m.get('issue_place') is not None:
            self.issue_place = m.get('issue_place')

        return self

