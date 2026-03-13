# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TrainOrderCreateRequest(DaraModel):
    def __init__(
        self,
        accept_no_seat: str = None,
        book_train_infos: List[main_models.TrainOrderCreateRequestBookTrainInfos] = None,
        btrip_user_id: str = None,
        btrip_user_name: str = None,
        business_info: main_models.TrainOrderCreateRequestBusinessInfo = None,
        contact_info: main_models.TrainOrderCreateRequestContactInfo = None,
        force_match: str = None,
        is_pay_now: bool = None,
        out_order_id: str = None,
        passenger_open_info_s: List[main_models.TrainOrderCreateRequestPassengerOpenInfoS] = None,
    ):
        self.accept_no_seat = accept_no_seat
        # This parameter is required.
        self.book_train_infos = book_train_infos
        # This parameter is required.
        self.btrip_user_id = btrip_user_id
        # This parameter is required.
        self.btrip_user_name = btrip_user_name
        self.business_info = business_info
        # This parameter is required.
        self.contact_info = contact_info
        self.force_match = force_match
        self.is_pay_now = is_pay_now
        # This parameter is required.
        self.out_order_id = out_order_id
        # This parameter is required.
        self.passenger_open_info_s = passenger_open_info_s

    def validate(self):
        if self.book_train_infos:
            for v1 in self.book_train_infos:
                 if v1:
                    v1.validate()
        if self.business_info:
            self.business_info.validate()
        if self.contact_info:
            self.contact_info.validate()
        if self.passenger_open_info_s:
            for v1 in self.passenger_open_info_s:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_no_seat is not None:
            result['accept_no_seat'] = self.accept_no_seat

        result['book_train_infos'] = []
        if self.book_train_infos is not None:
            for k1 in self.book_train_infos:
                result['book_train_infos'].append(k1.to_map() if k1 else None)

        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.btrip_user_name is not None:
            result['btrip_user_name'] = self.btrip_user_name

        if self.business_info is not None:
            result['business_info'] = self.business_info.to_map()

        if self.contact_info is not None:
            result['contact_info'] = self.contact_info.to_map()

        if self.force_match is not None:
            result['force_match'] = self.force_match

        if self.is_pay_now is not None:
            result['is_pay_now'] = self.is_pay_now

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        result['passenger_open_info_s'] = []
        if self.passenger_open_info_s is not None:
            for k1 in self.passenger_open_info_s:
                result['passenger_open_info_s'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accept_no_seat') is not None:
            self.accept_no_seat = m.get('accept_no_seat')

        self.book_train_infos = []
        if m.get('book_train_infos') is not None:
            for k1 in m.get('book_train_infos'):
                temp_model = main_models.TrainOrderCreateRequestBookTrainInfos()
                self.book_train_infos.append(temp_model.from_map(k1))

        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('btrip_user_name') is not None:
            self.btrip_user_name = m.get('btrip_user_name')

        if m.get('business_info') is not None:
            temp_model = main_models.TrainOrderCreateRequestBusinessInfo()
            self.business_info = temp_model.from_map(m.get('business_info'))

        if m.get('contact_info') is not None:
            temp_model = main_models.TrainOrderCreateRequestContactInfo()
            self.contact_info = temp_model.from_map(m.get('contact_info'))

        if m.get('force_match') is not None:
            self.force_match = m.get('force_match')

        if m.get('is_pay_now') is not None:
            self.is_pay_now = m.get('is_pay_now')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        self.passenger_open_info_s = []
        if m.get('passenger_open_info_s') is not None:
            for k1 in m.get('passenger_open_info_s'):
                temp_model = main_models.TrainOrderCreateRequestPassengerOpenInfoS()
                self.passenger_open_info_s.append(temp_model.from_map(k1))

        return self

class TrainOrderCreateRequestPassengerOpenInfoS(DaraModel):
    def __init__(
        self,
        cost_center_info: main_models.TrainOrderCreateRequestPassengerOpenInfoSCostCenterInfo = None,
        country_code: str = None,
        passenger_cert_no: str = None,
        passenger_cert_type: str = None,
        passenger_id: str = None,
        passenger_mobile: str = None,
        passenger_name: str = None,
        valid_date_end: str = None,
    ):
        self.cost_center_info = cost_center_info
        self.country_code = country_code
        # This parameter is required.
        self.passenger_cert_no = passenger_cert_no
        # This parameter is required.
        self.passenger_cert_type = passenger_cert_type
        # This parameter is required.
        self.passenger_id = passenger_id
        self.passenger_mobile = passenger_mobile
        # This parameter is required.
        self.passenger_name = passenger_name
        self.valid_date_end = valid_date_end

    def validate(self):
        if self.cost_center_info:
            self.cost_center_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_center_info is not None:
            result['cost_center_info'] = self.cost_center_info.to_map()

        if self.country_code is not None:
            result['country_code'] = self.country_code

        if self.passenger_cert_no is not None:
            result['passenger_cert_no'] = self.passenger_cert_no

        if self.passenger_cert_type is not None:
            result['passenger_cert_type'] = self.passenger_cert_type

        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        if self.passenger_mobile is not None:
            result['passenger_mobile'] = self.passenger_mobile

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        if self.valid_date_end is not None:
            result['valid_date_end'] = self.valid_date_end

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost_center_info') is not None:
            temp_model = main_models.TrainOrderCreateRequestPassengerOpenInfoSCostCenterInfo()
            self.cost_center_info = temp_model.from_map(m.get('cost_center_info'))

        if m.get('country_code') is not None:
            self.country_code = m.get('country_code')

        if m.get('passenger_cert_no') is not None:
            self.passenger_cert_no = m.get('passenger_cert_no')

        if m.get('passenger_cert_type') is not None:
            self.passenger_cert_type = m.get('passenger_cert_type')

        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        if m.get('passenger_mobile') is not None:
            self.passenger_mobile = m.get('passenger_mobile')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        if m.get('valid_date_end') is not None:
            self.valid_date_end = m.get('valid_date_end')

        return self

class TrainOrderCreateRequestPassengerOpenInfoSCostCenterInfo(DaraModel):
    def __init__(
        self,
        cascade_dept_name: str = None,
        cost_center_id: str = None,
        cost_center_name: str = None,
        cost_center_no: str = None,
        depart_id: str = None,
        depart_name: str = None,
        invoice_id: str = None,
        invoice_title: str = None,
        project_code: str = None,
        project_title: str = None,
    ):
        self.cascade_dept_name = cascade_dept_name
        self.cost_center_id = cost_center_id
        self.cost_center_name = cost_center_name
        self.cost_center_no = cost_center_no
        self.depart_id = depart_id
        self.depart_name = depart_name
        self.invoice_id = invoice_id
        self.invoice_title = invoice_title
        self.project_code = project_code
        self.project_title = project_title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cascade_dept_name is not None:
            result['cascade_dept_name'] = self.cascade_dept_name

        if self.cost_center_id is not None:
            result['cost_center_id'] = self.cost_center_id

        if self.cost_center_name is not None:
            result['cost_center_name'] = self.cost_center_name

        if self.cost_center_no is not None:
            result['cost_center_no'] = self.cost_center_no

        if self.depart_id is not None:
            result['depart_id'] = self.depart_id

        if self.depart_name is not None:
            result['depart_name'] = self.depart_name

        if self.invoice_id is not None:
            result['invoice_id'] = self.invoice_id

        if self.invoice_title is not None:
            result['invoice_title'] = self.invoice_title

        if self.project_code is not None:
            result['project_code'] = self.project_code

        if self.project_title is not None:
            result['project_title'] = self.project_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cascade_dept_name') is not None:
            self.cascade_dept_name = m.get('cascade_dept_name')

        if m.get('cost_center_id') is not None:
            self.cost_center_id = m.get('cost_center_id')

        if m.get('cost_center_name') is not None:
            self.cost_center_name = m.get('cost_center_name')

        if m.get('cost_center_no') is not None:
            self.cost_center_no = m.get('cost_center_no')

        if m.get('depart_id') is not None:
            self.depart_id = m.get('depart_id')

        if m.get('depart_name') is not None:
            self.depart_name = m.get('depart_name')

        if m.get('invoice_id') is not None:
            self.invoice_id = m.get('invoice_id')

        if m.get('invoice_title') is not None:
            self.invoice_title = m.get('invoice_title')

        if m.get('project_code') is not None:
            self.project_code = m.get('project_code')

        if m.get('project_title') is not None:
            self.project_title = m.get('project_title')

        return self

class TrainOrderCreateRequestContactInfo(DaraModel):
    def __init__(
        self,
        passenger_id: str = None,
        passenger_mobile: str = None,
        passenger_name: str = None,
    ):
        # This parameter is required.
        self.passenger_id = passenger_id
        # This parameter is required.
        self.passenger_mobile = passenger_mobile
        # This parameter is required.
        self.passenger_name = passenger_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        if self.passenger_mobile is not None:
            result['passenger_mobile'] = self.passenger_mobile

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        if m.get('passenger_mobile') is not None:
            self.passenger_mobile = m.get('passenger_mobile')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        return self

class TrainOrderCreateRequestBusinessInfo(DaraModel):
    def __init__(
        self,
        customer_apply_id: str = None,
        customer_itinerary_id: str = None,
    ):
        self.customer_apply_id = customer_apply_id
        self.customer_itinerary_id = customer_itinerary_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_apply_id is not None:
            result['customer_apply_id'] = self.customer_apply_id

        if self.customer_itinerary_id is not None:
            result['customer_itinerary_id'] = self.customer_itinerary_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customer_apply_id') is not None:
            self.customer_apply_id = m.get('customer_apply_id')

        if m.get('customer_itinerary_id') is not None:
            self.customer_itinerary_id = m.get('customer_itinerary_id')

        return self

class TrainOrderCreateRequestBookTrainInfos(DaraModel):
    def __init__(
        self,
        arr_station_code: str = None,
        book_ticket_infos: List[main_models.TrainOrderCreateRequestBookTrainInfosBookTicketInfos] = None,
        choose_beds: str = None,
        choose_seats: str = None,
        dep_station_code: str = None,
        dep_time: str = None,
        train_no: str = None,
    ):
        # This parameter is required.
        self.arr_station_code = arr_station_code
        # This parameter is required.
        self.book_ticket_infos = book_ticket_infos
        self.choose_beds = choose_beds
        self.choose_seats = choose_seats
        # This parameter is required.
        self.dep_station_code = dep_station_code
        # This parameter is required.
        self.dep_time = dep_time
        # This parameter is required.
        self.train_no = train_no

    def validate(self):
        if self.book_ticket_infos:
            for v1 in self.book_ticket_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arr_station_code is not None:
            result['arr_station_code'] = self.arr_station_code

        result['book_ticket_infos'] = []
        if self.book_ticket_infos is not None:
            for k1 in self.book_ticket_infos:
                result['book_ticket_infos'].append(k1.to_map() if k1 else None)

        if self.choose_beds is not None:
            result['choose_beds'] = self.choose_beds

        if self.choose_seats is not None:
            result['choose_seats'] = self.choose_seats

        if self.dep_station_code is not None:
            result['dep_station_code'] = self.dep_station_code

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.train_no is not None:
            result['train_no'] = self.train_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arr_station_code') is not None:
            self.arr_station_code = m.get('arr_station_code')

        self.book_ticket_infos = []
        if m.get('book_ticket_infos') is not None:
            for k1 in m.get('book_ticket_infos'):
                temp_model = main_models.TrainOrderCreateRequestBookTrainInfosBookTicketInfos()
                self.book_ticket_infos.append(temp_model.from_map(k1))

        if m.get('choose_beds') is not None:
            self.choose_beds = m.get('choose_beds')

        if m.get('choose_seats') is not None:
            self.choose_seats = m.get('choose_seats')

        if m.get('dep_station_code') is not None:
            self.dep_station_code = m.get('dep_station_code')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('train_no') is not None:
            self.train_no = m.get('train_no')

        return self

class TrainOrderCreateRequestBookTrainInfosBookTicketInfos(DaraModel):
    def __init__(
        self,
        passenger_id: str = None,
        seat_type: str = None,
        ticket_price: int = None,
        ticket_type: str = None,
    ):
        # This parameter is required.
        self.passenger_id = passenger_id
        # This parameter is required.
        self.seat_type = seat_type
        # This parameter is required.
        self.ticket_price = ticket_price
        # This parameter is required.
        self.ticket_type = ticket_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        if self.seat_type is not None:
            result['seat_type'] = self.seat_type

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.ticket_type is not None:
            result['ticket_type'] = self.ticket_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        if m.get('seat_type') is not None:
            self.seat_type = m.get('seat_type')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('ticket_type') is not None:
            self.ticket_type = m.get('ticket_type')

        return self

