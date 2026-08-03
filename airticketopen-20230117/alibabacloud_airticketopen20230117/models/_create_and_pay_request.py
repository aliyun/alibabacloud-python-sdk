# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class CreateAndPayRequest(DaraModel):
    def __init__(
        self,
        account_no: int = None,
        contact: main_models.CreateAndPayRequestContact = None,
        external_order_no: str = None,
        guests: List[List[main_models.CreateAndPayRequestGuests]] = None,
        item_offer_id: str = None,
        room_count: int = None,
        tracer_id: str = None,
    ):
        # This parameter is required.
        self.account_no = account_no
        # This parameter is required.
        self.contact = contact
        self.external_order_no = external_order_no
        # This parameter is required.
        self.guests = guests
        # This parameter is required.
        self.item_offer_id = item_offer_id
        # This parameter is required.
        self.room_count = room_count
        self.tracer_id = tracer_id

    def validate(self):
        if self.contact:
            self.contact.validate()
        if self.guests:
            for v1 in self.guests:
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_no is not None:
            result['AccountNo'] = self.account_no

        if self.contact is not None:
            result['Contact'] = self.contact.to_map()

        if self.external_order_no is not None:
            result['ExternalOrderNo'] = self.external_order_no

        result['Guests'] = []
        if self.guests is not None:
            for k1 in self.guests:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['Guests'].append(l1)

        if self.item_offer_id is not None:
            result['ItemOfferId'] = self.item_offer_id

        if self.room_count is not None:
            result['RoomCount'] = self.room_count

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')

        if m.get('Contact') is not None:
            temp_model = main_models.CreateAndPayRequestContact()
            self.contact = temp_model.from_map(m.get('Contact'))

        if m.get('ExternalOrderNo') is not None:
            self.external_order_no = m.get('ExternalOrderNo')

        self.guests = []
        if m.get('Guests') is not None:
            for k1 in m.get('Guests'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.CreateAndPayRequestGuests()
                    l1.append(temp_model.from_map(k2))
                self.guests.append(l1)

        if m.get('ItemOfferId') is not None:
            self.item_offer_id = m.get('ItemOfferId')

        if m.get('RoomCount') is not None:
            self.room_count = m.get('RoomCount')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class CreateAndPayRequestGuests(DaraModel):
    def __init__(
        self,
        first_name: str = None,
        last_name: str = None,
        tracer_id: str = None,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.first_name is not None:
            result['FirstName'] = self.first_name

        if self.last_name is not None:
            result['LastName'] = self.last_name

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')

        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

class CreateAndPayRequestContact(DaraModel):
    def __init__(
        self,
        email: str = None,
        first_name: str = None,
        last_name: str = None,
        phone: str = None,
        tracer_id: str = None,
    ):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.tracer_id = tracer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.first_name is not None:
            result['FirstName'] = self.first_name

        if self.last_name is not None:
            result['LastName'] = self.last_name

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.tracer_id is not None:
            result['TracerId'] = self.tracer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')

        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('TracerId') is not None:
            self.tracer_id = m.get('TracerId')

        return self

