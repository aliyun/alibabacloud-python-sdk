# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightRefundDetailV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.FlightRefundDetailV2ResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        # module
        self.module = module
        # requestId
        self.request_id = request_id
        self.success = success
        # traceId
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.module is not None:
            result['module'] = self.module.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('module') is not None:
            temp_model = main_models.FlightRefundDetailV2ResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class FlightRefundDetailV2ResponseBodyModule(DaraModel):
    def __init__(
        self,
        apply_time: str = None,
        contact_info_dto: main_models.FlightRefundDetailV2ResponseBodyModuleContactInfoDTO = None,
        flight_info_dtos: List[main_models.FlightRefundDetailV2ResponseBodyModuleFlightInfoDTOS] = None,
        non_refundable_change_service_price: int = None,
        non_refundable_change_upgrade_price: int = None,
        order_id: int = None,
        out_order_id: str = None,
        out_sub_order_id: str = None,
        reason: str = None,
        reason_code: str = None,
        refund_fail_reason: str = None,
        refund_handling_fee: int = None,
        refund_money: int = None,
        status: int = None,
        sub_order_id: int = None,
        traveler_info_dtos: List[main_models.FlightRefundDetailV2ResponseBodyModuleTravelerInfoDTOS] = None,
    ):
        self.apply_time = apply_time
        self.contact_info_dto = contact_info_dto
        self.flight_info_dtos = flight_info_dtos
        self.non_refundable_change_service_price = non_refundable_change_service_price
        self.non_refundable_change_upgrade_price = non_refundable_change_upgrade_price
        self.order_id = order_id
        self.out_order_id = out_order_id
        self.out_sub_order_id = out_sub_order_id
        self.reason = reason
        self.reason_code = reason_code
        self.refund_fail_reason = refund_fail_reason
        self.refund_handling_fee = refund_handling_fee
        self.refund_money = refund_money
        self.status = status
        self.sub_order_id = sub_order_id
        self.traveler_info_dtos = traveler_info_dtos

    def validate(self):
        if self.contact_info_dto:
            self.contact_info_dto.validate()
        if self.flight_info_dtos:
            for v1 in self.flight_info_dtos:
                 if v1:
                    v1.validate()
        if self.traveler_info_dtos:
            for v1 in self.traveler_info_dtos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_time is not None:
            result['apply_time'] = self.apply_time

        if self.contact_info_dto is not None:
            result['contact_info_d_t_o'] = self.contact_info_dto.to_map()

        result['flight_info_d_t_o_s'] = []
        if self.flight_info_dtos is not None:
            for k1 in self.flight_info_dtos:
                result['flight_info_d_t_o_s'].append(k1.to_map() if k1 else None)

        if self.non_refundable_change_service_price is not None:
            result['non_refundable_change_service_price'] = self.non_refundable_change_service_price

        if self.non_refundable_change_upgrade_price is not None:
            result['non_refundable_change_upgrade_price'] = self.non_refundable_change_upgrade_price

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        if self.out_sub_order_id is not None:
            result['out_sub_order_id'] = self.out_sub_order_id

        if self.reason is not None:
            result['reason'] = self.reason

        if self.reason_code is not None:
            result['reason_code'] = self.reason_code

        if self.refund_fail_reason is not None:
            result['refund_fail_reason'] = self.refund_fail_reason

        if self.refund_handling_fee is not None:
            result['refund_handling_fee'] = self.refund_handling_fee

        if self.refund_money is not None:
            result['refund_money'] = self.refund_money

        if self.status is not None:
            result['status'] = self.status

        if self.sub_order_id is not None:
            result['sub_order_id'] = self.sub_order_id

        result['traveler_info_d_t_o_s'] = []
        if self.traveler_info_dtos is not None:
            for k1 in self.traveler_info_dtos:
                result['traveler_info_d_t_o_s'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_time') is not None:
            self.apply_time = m.get('apply_time')

        if m.get('contact_info_d_t_o') is not None:
            temp_model = main_models.FlightRefundDetailV2ResponseBodyModuleContactInfoDTO()
            self.contact_info_dto = temp_model.from_map(m.get('contact_info_d_t_o'))

        self.flight_info_dtos = []
        if m.get('flight_info_d_t_o_s') is not None:
            for k1 in m.get('flight_info_d_t_o_s'):
                temp_model = main_models.FlightRefundDetailV2ResponseBodyModuleFlightInfoDTOS()
                self.flight_info_dtos.append(temp_model.from_map(k1))

        if m.get('non_refundable_change_service_price') is not None:
            self.non_refundable_change_service_price = m.get('non_refundable_change_service_price')

        if m.get('non_refundable_change_upgrade_price') is not None:
            self.non_refundable_change_upgrade_price = m.get('non_refundable_change_upgrade_price')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        if m.get('out_sub_order_id') is not None:
            self.out_sub_order_id = m.get('out_sub_order_id')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('reason_code') is not None:
            self.reason_code = m.get('reason_code')

        if m.get('refund_fail_reason') is not None:
            self.refund_fail_reason = m.get('refund_fail_reason')

        if m.get('refund_handling_fee') is not None:
            self.refund_handling_fee = m.get('refund_handling_fee')

        if m.get('refund_money') is not None:
            self.refund_money = m.get('refund_money')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('sub_order_id') is not None:
            self.sub_order_id = m.get('sub_order_id')

        self.traveler_info_dtos = []
        if m.get('traveler_info_d_t_o_s') is not None:
            for k1 in m.get('traveler_info_d_t_o_s'):
                temp_model = main_models.FlightRefundDetailV2ResponseBodyModuleTravelerInfoDTOS()
                self.traveler_info_dtos.append(temp_model.from_map(k1))

        return self

class FlightRefundDetailV2ResponseBodyModuleTravelerInfoDTOS(DaraModel):
    def __init__(
        self,
        birth_date: str = None,
        cert_no: str = None,
        cert_type: int = None,
        gender: int = None,
        origin_ticket_nos: List[str] = None,
        passenger_id: str = None,
        passenger_name: str = None,
        passenger_type: int = None,
        phone: str = None,
        pid: int = None,
        ticket_nos: List[str] = None,
    ):
        self.birth_date = birth_date
        self.cert_no = cert_no
        self.cert_type = cert_type
        self.gender = gender
        self.origin_ticket_nos = origin_ticket_nos
        self.passenger_id = passenger_id
        self.passenger_name = passenger_name
        self.passenger_type = passenger_type
        self.phone = phone
        self.pid = pid
        self.ticket_nos = ticket_nos

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.birth_date is not None:
            result['birth_date'] = self.birth_date

        if self.cert_no is not None:
            result['cert_no'] = self.cert_no

        if self.cert_type is not None:
            result['cert_type'] = self.cert_type

        if self.gender is not None:
            result['gender'] = self.gender

        if self.origin_ticket_nos is not None:
            result['origin_ticket_nos'] = self.origin_ticket_nos

        if self.passenger_id is not None:
            result['passenger_id'] = self.passenger_id

        if self.passenger_name is not None:
            result['passenger_name'] = self.passenger_name

        if self.passenger_type is not None:
            result['passenger_type'] = self.passenger_type

        if self.phone is not None:
            result['phone'] = self.phone

        if self.pid is not None:
            result['pid'] = self.pid

        if self.ticket_nos is not None:
            result['ticket_nos'] = self.ticket_nos

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('birth_date') is not None:
            self.birth_date = m.get('birth_date')

        if m.get('cert_no') is not None:
            self.cert_no = m.get('cert_no')

        if m.get('cert_type') is not None:
            self.cert_type = m.get('cert_type')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('origin_ticket_nos') is not None:
            self.origin_ticket_nos = m.get('origin_ticket_nos')

        if m.get('passenger_id') is not None:
            self.passenger_id = m.get('passenger_id')

        if m.get('passenger_name') is not None:
            self.passenger_name = m.get('passenger_name')

        if m.get('passenger_type') is not None:
            self.passenger_type = m.get('passenger_type')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('pid') is not None:
            self.pid = m.get('pid')

        if m.get('ticket_nos') is not None:
            self.ticket_nos = m.get('ticket_nos')

        return self

class FlightRefundDetailV2ResponseBodyModuleFlightInfoDTOS(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_icon_url: str = None,
        airline_name: str = None,
        arr_airport_code: str = None,
        arr_airport_name: str = None,
        arr_city_code: str = None,
        arr_city_name: str = None,
        arr_terminal: str = None,
        arr_time: str = None,
        cabin: str = None,
        cabin_class: str = None,
        cabin_class_name: str = None,
        cabin_discount: int = None,
        carrier_airline_code: str = None,
        carrier_airline_icon_url: str = None,
        carrier_airline_name: str = None,
        carrier_flight_no: str = None,
        dep_airport_code: str = None,
        dep_airport_name: str = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_terminal: str = None,
        dep_time: str = None,
        flight_no: str = None,
        flight_type: str = None,
        meal_desc: str = None,
        segment_id: str = None,
        segment_position: main_models.FlightRefundDetailV2ResponseBodyModuleFlightInfoDTOSSegmentPosition = None,
        stop_arr_time: str = None,
        stop_city: str = None,
        stop_dep_time: str = None,
    ):
        self.airline_code = airline_code
        self.airline_icon_url = airline_icon_url
        self.airline_name = airline_name
        self.arr_airport_code = arr_airport_code
        self.arr_airport_name = arr_airport_name
        self.arr_city_code = arr_city_code
        self.arr_city_name = arr_city_name
        self.arr_terminal = arr_terminal
        self.arr_time = arr_time
        self.cabin = cabin
        self.cabin_class = cabin_class
        self.cabin_class_name = cabin_class_name
        self.cabin_discount = cabin_discount
        self.carrier_airline_code = carrier_airline_code
        self.carrier_airline_icon_url = carrier_airline_icon_url
        self.carrier_airline_name = carrier_airline_name
        self.carrier_flight_no = carrier_flight_no
        self.dep_airport_code = dep_airport_code
        self.dep_airport_name = dep_airport_name
        self.dep_city_code = dep_city_code
        self.dep_city_name = dep_city_name
        self.dep_terminal = dep_terminal
        self.dep_time = dep_time
        self.flight_no = flight_no
        self.flight_type = flight_type
        self.meal_desc = meal_desc
        self.segment_id = segment_id
        self.segment_position = segment_position
        self.stop_arr_time = stop_arr_time
        self.stop_city = stop_city
        self.stop_dep_time = stop_dep_time

    def validate(self):
        if self.segment_position:
            self.segment_position.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.airline_icon_url is not None:
            result['airline_icon_url'] = self.airline_icon_url

        if self.airline_name is not None:
            result['airline_name'] = self.airline_name

        if self.arr_airport_code is not None:
            result['arr_airport_code'] = self.arr_airport_code

        if self.arr_airport_name is not None:
            result['arr_airport_name'] = self.arr_airport_name

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_city_name is not None:
            result['arr_city_name'] = self.arr_city_name

        if self.arr_terminal is not None:
            result['arr_terminal'] = self.arr_terminal

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.cabin is not None:
            result['cabin'] = self.cabin

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.cabin_class_name is not None:
            result['cabin_class_name'] = self.cabin_class_name

        if self.cabin_discount is not None:
            result['cabin_discount'] = self.cabin_discount

        if self.carrier_airline_code is not None:
            result['carrier_airline_code'] = self.carrier_airline_code

        if self.carrier_airline_icon_url is not None:
            result['carrier_airline_icon_url'] = self.carrier_airline_icon_url

        if self.carrier_airline_name is not None:
            result['carrier_airline_name'] = self.carrier_airline_name

        if self.carrier_flight_no is not None:
            result['carrier_flight_no'] = self.carrier_flight_no

        if self.dep_airport_code is not None:
            result['dep_airport_code'] = self.dep_airport_code

        if self.dep_airport_name is not None:
            result['dep_airport_name'] = self.dep_airport_name

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_city_name is not None:
            result['dep_city_name'] = self.dep_city_name

        if self.dep_terminal is not None:
            result['dep_terminal'] = self.dep_terminal

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.flight_type is not None:
            result['flight_type'] = self.flight_type

        if self.meal_desc is not None:
            result['meal_desc'] = self.meal_desc

        if self.segment_id is not None:
            result['segment_id'] = self.segment_id

        if self.segment_position is not None:
            result['segment_position'] = self.segment_position.to_map()

        if self.stop_arr_time is not None:
            result['stop_arr_time'] = self.stop_arr_time

        if self.stop_city is not None:
            result['stop_city'] = self.stop_city

        if self.stop_dep_time is not None:
            result['stop_dep_time'] = self.stop_dep_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_icon_url') is not None:
            self.airline_icon_url = m.get('airline_icon_url')

        if m.get('airline_name') is not None:
            self.airline_name = m.get('airline_name')

        if m.get('arr_airport_code') is not None:
            self.arr_airport_code = m.get('arr_airport_code')

        if m.get('arr_airport_name') is not None:
            self.arr_airport_name = m.get('arr_airport_name')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')

        if m.get('arr_terminal') is not None:
            self.arr_terminal = m.get('arr_terminal')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('cabin_class_name') is not None:
            self.cabin_class_name = m.get('cabin_class_name')

        if m.get('cabin_discount') is not None:
            self.cabin_discount = m.get('cabin_discount')

        if m.get('carrier_airline_code') is not None:
            self.carrier_airline_code = m.get('carrier_airline_code')

        if m.get('carrier_airline_icon_url') is not None:
            self.carrier_airline_icon_url = m.get('carrier_airline_icon_url')

        if m.get('carrier_airline_name') is not None:
            self.carrier_airline_name = m.get('carrier_airline_name')

        if m.get('carrier_flight_no') is not None:
            self.carrier_flight_no = m.get('carrier_flight_no')

        if m.get('dep_airport_code') is not None:
            self.dep_airport_code = m.get('dep_airport_code')

        if m.get('dep_airport_name') is not None:
            self.dep_airport_name = m.get('dep_airport_name')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_city_name') is not None:
            self.dep_city_name = m.get('dep_city_name')

        if m.get('dep_terminal') is not None:
            self.dep_terminal = m.get('dep_terminal')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('flight_type') is not None:
            self.flight_type = m.get('flight_type')

        if m.get('meal_desc') is not None:
            self.meal_desc = m.get('meal_desc')

        if m.get('segment_id') is not None:
            self.segment_id = m.get('segment_id')

        if m.get('segment_position') is not None:
            temp_model = main_models.FlightRefundDetailV2ResponseBodyModuleFlightInfoDTOSSegmentPosition()
            self.segment_position = temp_model.from_map(m.get('segment_position'))

        if m.get('stop_arr_time') is not None:
            self.stop_arr_time = m.get('stop_arr_time')

        if m.get('stop_city') is not None:
            self.stop_city = m.get('stop_city')

        if m.get('stop_dep_time') is not None:
            self.stop_dep_time = m.get('stop_dep_time')

        return self

class FlightRefundDetailV2ResponseBodyModuleFlightInfoDTOSSegmentPosition(DaraModel):
    def __init__(
        self,
        journey_index: int = None,
        segment_index: int = None,
    ):
        self.journey_index = journey_index
        self.segment_index = segment_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.journey_index is not None:
            result['journey_index'] = self.journey_index

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        return self

class FlightRefundDetailV2ResponseBodyModuleContactInfoDTO(DaraModel):
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

