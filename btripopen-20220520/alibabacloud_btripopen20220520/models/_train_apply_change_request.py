# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TrainApplyChangeRequest(DaraModel):
    def __init__(
        self,
        accept_no_seat: str = None,
        change_train_info_s: List[main_models.TrainApplyChangeRequestChangeTrainInfoS] = None,
        force_match: str = None,
        is_pay_now: bool = None,
        order_id: str = None,
        out_change_apply_id: str = None,
        out_order_id: str = None,
    ):
        self.accept_no_seat = accept_no_seat
        # This parameter is required.
        self.change_train_info_s = change_train_info_s
        self.force_match = force_match
        self.is_pay_now = is_pay_now
        # This parameter is required.
        self.order_id = order_id
        # This parameter is required.
        self.out_change_apply_id = out_change_apply_id
        # This parameter is required.
        self.out_order_id = out_order_id

    def validate(self):
        if self.change_train_info_s:
            for v1 in self.change_train_info_s:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_no_seat is not None:
            result['accept_no_seat'] = self.accept_no_seat

        result['change_train_info_s'] = []
        if self.change_train_info_s is not None:
            for k1 in self.change_train_info_s:
                result['change_train_info_s'].append(k1.to_map() if k1 else None)

        if self.force_match is not None:
            result['force_match'] = self.force_match

        if self.is_pay_now is not None:
            result['is_pay_now'] = self.is_pay_now

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.out_change_apply_id is not None:
            result['out_change_apply_id'] = self.out_change_apply_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accept_no_seat') is not None:
            self.accept_no_seat = m.get('accept_no_seat')

        self.change_train_info_s = []
        if m.get('change_train_info_s') is not None:
            for k1 in m.get('change_train_info_s'):
                temp_model = main_models.TrainApplyChangeRequestChangeTrainInfoS()
                self.change_train_info_s.append(temp_model.from_map(k1))

        if m.get('force_match') is not None:
            self.force_match = m.get('force_match')

        if m.get('is_pay_now') is not None:
            self.is_pay_now = m.get('is_pay_now')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_change_apply_id') is not None:
            self.out_change_apply_id = m.get('out_change_apply_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        return self

class TrainApplyChangeRequestChangeTrainInfoS(DaraModel):
    def __init__(
        self,
        arr_station_code: str = None,
        change_ticket_info_s: List[main_models.TrainApplyChangeRequestChangeTrainInfoSChangeTicketInfoS] = None,
        choose_bed_s: str = None,
        choose_seat_s: str = None,
        dep_station_code: str = None,
        dep_time: str = None,
        original_dep_time: str = None,
        original_train_no: str = None,
        train_no: str = None,
    ):
        # This parameter is required.
        self.arr_station_code = arr_station_code
        # This parameter is required.
        self.change_ticket_info_s = change_ticket_info_s
        self.choose_bed_s = choose_bed_s
        self.choose_seat_s = choose_seat_s
        # This parameter is required.
        self.dep_station_code = dep_station_code
        # This parameter is required.
        self.dep_time = dep_time
        # This parameter is required.
        self.original_dep_time = original_dep_time
        # This parameter is required.
        self.original_train_no = original_train_no
        # This parameter is required.
        self.train_no = train_no

    def validate(self):
        if self.change_ticket_info_s:
            for v1 in self.change_ticket_info_s:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_station_code is not None:
            result['arr_station_code'] = self.arr_station_code

        result['change_ticket_info_s'] = []
        if self.change_ticket_info_s is not None:
            for k1 in self.change_ticket_info_s:
                result['change_ticket_info_s'].append(k1.to_map() if k1 else None)

        if self.choose_bed_s is not None:
            result['choose_bed_s'] = self.choose_bed_s

        if self.choose_seat_s is not None:
            result['choose_seat_s'] = self.choose_seat_s

        if self.dep_station_code is not None:
            result['dep_station_code'] = self.dep_station_code

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.original_dep_time is not None:
            result['original_dep_time'] = self.original_dep_time

        if self.original_train_no is not None:
            result['original_train_no'] = self.original_train_no

        if self.train_no is not None:
            result['train_no'] = self.train_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_station_code') is not None:
            self.arr_station_code = m.get('arr_station_code')

        self.change_ticket_info_s = []
        if m.get('change_ticket_info_s') is not None:
            for k1 in m.get('change_ticket_info_s'):
                temp_model = main_models.TrainApplyChangeRequestChangeTrainInfoSChangeTicketInfoS()
                self.change_ticket_info_s.append(temp_model.from_map(k1))

        if m.get('choose_bed_s') is not None:
            self.choose_bed_s = m.get('choose_bed_s')

        if m.get('choose_seat_s') is not None:
            self.choose_seat_s = m.get('choose_seat_s')

        if m.get('dep_station_code') is not None:
            self.dep_station_code = m.get('dep_station_code')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('original_dep_time') is not None:
            self.original_dep_time = m.get('original_dep_time')

        if m.get('original_train_no') is not None:
            self.original_train_no = m.get('original_train_no')

        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')

        return self

class TrainApplyChangeRequestChangeTrainInfoSChangeTicketInfoS(DaraModel):
    def __init__(
        self,
        passenger_info: main_models.TrainApplyChangeRequestChangeTrainInfoSChangeTicketInfoSPassengerInfo = None,
        seat_type: str = None,
        ticket_price: str = None,
        ticket_type: str = None,
    ):
        # This parameter is required.
        self.passenger_info = passenger_info
        # This parameter is required.
        self.seat_type = seat_type
        # This parameter is required.
        self.ticket_price = ticket_price
        # This parameter is required.
        self.ticket_type = ticket_type

    def validate(self):
        if self.passenger_info:
            self.passenger_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passenger_info is not None:
            result['passenger_info'] = self.passenger_info.to_map()

        if self.seat_type is not None:
            result['seat_type'] = self.seat_type

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.ticket_type is not None:
            result['ticket_type'] = self.ticket_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger_info') is not None:
            temp_model = main_models.TrainApplyChangeRequestChangeTrainInfoSChangeTicketInfoSPassengerInfo()
            self.passenger_info = temp_model.from_map(m.get('passenger_info'))

        if m.get('seat_type') is not None:
            self.seat_type = m.get('seat_type')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('ticket_type') is not None:
            self.ticket_type = m.get('ticket_type')

        return self

class TrainApplyChangeRequestChangeTrainInfoSChangeTicketInfoSPassengerInfo(DaraModel):
    def __init__(
        self,
        passenger_cert_no: str = None,
        passenger_cert_type: str = None,
        passenger_id: str = None,
        passenger_name: str = None,
    ):
        # This parameter is required.
        self.passenger_cert_no = passenger_cert_no
        # This parameter is required.
        self.passenger_cert_type = passenger_cert_type
        # This parameter is required.
        self.passenger_id = passenger_id
        # This parameter is required.
        self.passenger_name = passenger_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passenger_cert_no is not None:
            result['passenger_cert_no'] = self.passenger_cert_no

        if self.passenger_cert_type is not None:
            result['passenger_cert_type'] = self.passenger_cert_type

        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger_cert_no') is not None:
            self.passenger_cert_no = m.get('passenger_cert_no')

        if m.get('passenger_cert_type') is not None:
            self.passenger_cert_type = m.get('passenger_cert_type')

        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        return self

