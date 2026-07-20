# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class FlightOrderDetailV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.FlightOrderDetailV2ResponseBodyModule = None,
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
            temp_model = main_models.FlightOrderDetailV2ResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class FlightOrderDetailV2ResponseBodyModule(DaraModel):
    def __init__(
        self,
        b_2g_vip_code: str = None,
        book_succ_time: str = None,
        book_user_id: str = None,
        book_user_name: str = None,
        build_price: int = None,
        contact_info_dto: main_models.FlightOrderDetailV2ResponseBodyModuleContactInfoDTO = None,
        create_time: str = None,
        facevalue: int = None,
        flight_tale_info_dto: main_models.FlightOrderDetailV2ResponseBodyModuleFlightTaleInfoDTO = None,
        is_protocol: bool = None,
        isemergency: bool = None,
        issendmessage: bool = None,
        oil_price: int = None,
        order_id: int = None,
        order_price: int = None,
        out_order_id: str = None,
        passenger_list: List[main_models.FlightOrderDetailV2ResponseBodyModulePassengerList] = None,
        passenger_segment_map: Dict[str, str] = None,
        pay_time: str = None,
        saleprice: int = None,
        sendcpsms: bool = None,
        status: int = None,
        total_service_fee_price: int = None,
    ):
        self.b_2g_vip_code = b_2g_vip_code
        self.book_succ_time = book_succ_time
        self.book_user_id = book_user_id
        self.book_user_name = book_user_name
        self.build_price = build_price
        self.contact_info_dto = contact_info_dto
        self.create_time = create_time
        self.facevalue = facevalue
        self.flight_tale_info_dto = flight_tale_info_dto
        self.is_protocol = is_protocol
        self.isemergency = isemergency
        self.issendmessage = issendmessage
        self.oil_price = oil_price
        self.order_id = order_id
        self.order_price = order_price
        self.out_order_id = out_order_id
        self.passenger_list = passenger_list
        # key :passengerId
        # 
        # value :segmentId
        self.passenger_segment_map = passenger_segment_map
        self.pay_time = pay_time
        self.saleprice = saleprice
        self.sendcpsms = sendcpsms
        self.status = status
        self.total_service_fee_price = total_service_fee_price

    def validate(self):
        if self.contact_info_dto:
            self.contact_info_dto.validate()
        if self.flight_tale_info_dto:
            self.flight_tale_info_dto.validate()
        if self.passenger_list:
            for v1 in self.passenger_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.b_2g_vip_code is not None:
            result['b2g_vip_code'] = self.b_2g_vip_code

        if self.book_succ_time is not None:
            result['book_succ_time'] = self.book_succ_time

        if self.book_user_id is not None:
            result['book_user_id'] = self.book_user_id

        if self.book_user_name is not None:
            result['book_user_name'] = self.book_user_name

        if self.build_price is not None:
            result['build_price'] = self.build_price

        if self.contact_info_dto is not None:
            result['contact_info_d_t_o'] = self.contact_info_dto.to_map()

        if self.create_time is not None:
            result['create_time'] = self.create_time

        if self.facevalue is not None:
            result['facevalue'] = self.facevalue

        if self.flight_tale_info_dto is not None:
            result['flight_tale_info_d_t_o'] = self.flight_tale_info_dto.to_map()

        if self.is_protocol is not None:
            result['is_protocol'] = self.is_protocol

        if self.isemergency is not None:
            result['isemergency'] = self.isemergency

        if self.issendmessage is not None:
            result['issendmessage'] = self.issendmessage

        if self.oil_price is not None:
            result['oil_price'] = self.oil_price

        if self.order_id is not None:
            result['order_id'] = self.order_id

        if self.order_price is not None:
            result['order_price'] = self.order_price

        if self.out_order_id is not None:
            result['out_order_id'] = self.out_order_id

        result['passenger_list'] = []
        if self.passenger_list is not None:
            for k1 in self.passenger_list:
                result['passenger_list'].append(k1.to_map() if k1 else None)

        if self.passenger_segment_map is not None:
            result['passenger_segment_map'] = self.passenger_segment_map

        if self.pay_time is not None:
            result['pay_time'] = self.pay_time

        if self.saleprice is not None:
            result['saleprice'] = self.saleprice

        if self.sendcpsms is not None:
            result['sendcpsms'] = self.sendcpsms

        if self.status is not None:
            result['status'] = self.status

        if self.total_service_fee_price is not None:
            result['total_service_fee_price'] = self.total_service_fee_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('b2g_vip_code') is not None:
            self.b_2g_vip_code = m.get('b2g_vip_code')

        if m.get('book_succ_time') is not None:
            self.book_succ_time = m.get('book_succ_time')

        if m.get('book_user_id') is not None:
            self.book_user_id = m.get('book_user_id')

        if m.get('book_user_name') is not None:
            self.book_user_name = m.get('book_user_name')

        if m.get('build_price') is not None:
            self.build_price = m.get('build_price')

        if m.get('contact_info_d_t_o') is not None:
            temp_model = main_models.FlightOrderDetailV2ResponseBodyModuleContactInfoDTO()
            self.contact_info_dto = temp_model.from_map(m.get('contact_info_d_t_o'))

        if m.get('create_time') is not None:
            self.create_time = m.get('create_time')

        if m.get('facevalue') is not None:
            self.facevalue = m.get('facevalue')

        if m.get('flight_tale_info_d_t_o') is not None:
            temp_model = main_models.FlightOrderDetailV2ResponseBodyModuleFlightTaleInfoDTO()
            self.flight_tale_info_dto = temp_model.from_map(m.get('flight_tale_info_d_t_o'))

        if m.get('is_protocol') is not None:
            self.is_protocol = m.get('is_protocol')

        if m.get('isemergency') is not None:
            self.isemergency = m.get('isemergency')

        if m.get('issendmessage') is not None:
            self.issendmessage = m.get('issendmessage')

        if m.get('oil_price') is not None:
            self.oil_price = m.get('oil_price')

        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')

        if m.get('order_price') is not None:
            self.order_price = m.get('order_price')

        if m.get('out_order_id') is not None:
            self.out_order_id = m.get('out_order_id')

        self.passenger_list = []
        if m.get('passenger_list') is not None:
            for k1 in m.get('passenger_list'):
                temp_model = main_models.FlightOrderDetailV2ResponseBodyModulePassengerList()
                self.passenger_list.append(temp_model.from_map(k1))

        if m.get('passenger_segment_map') is not None:
            self.passenger_segment_map = m.get('passenger_segment_map')

        if m.get('pay_time') is not None:
            self.pay_time = m.get('pay_time')

        if m.get('saleprice') is not None:
            self.saleprice = m.get('saleprice')

        if m.get('sendcpsms') is not None:
            self.sendcpsms = m.get('sendcpsms')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('total_service_fee_price') is not None:
            self.total_service_fee_price = m.get('total_service_fee_price')

        return self

class FlightOrderDetailV2ResponseBodyModulePassengerList(DaraModel):
    def __init__(
        self,
        birthday: str = None,
        btrip_user_id: str = None,
        code: int = None,
        country: str = None,
        country_code: str = None,
        credential: main_models.FlightOrderDetailV2ResponseBodyModulePassengerListCredential = None,
        credentials: List[main_models.FlightOrderDetailV2ResponseBodyModulePassengerListCredentials] = None,
        email: str = None,
        en_first_name: str = None,
        en_last_name: str = None,
        english_name: str = None,
        gender: int = None,
        id: str = None,
        is_complete: bool = None,
        is_frequently: bool = None,
        memo: str = None,
        mobile_country_code: str = None,
        mobile_phone_number: str = None,
        name: str = None,
        oneself: bool = None,
        order_name: str = None,
        out_passenger_id: str = None,
        phone: str = None,
        sheng_pi_pinyin: str = None,
        ticket_nos: List[str] = None,
        tickets: List[main_models.FlightOrderDetailV2ResponseBodyModulePassengerListTickets] = None,
        type: int = None,
        user_id: str = None,
    ):
        self.birthday = birthday
        self.btrip_user_id = btrip_user_id
        self.code = code
        self.country = country
        self.country_code = country_code
        self.credential = credential
        self.credentials = credentials
        self.email = email
        self.en_first_name = en_first_name
        self.en_last_name = en_last_name
        self.english_name = english_name
        self.gender = gender
        self.id = id
        self.is_complete = is_complete
        self.is_frequently = is_frequently
        self.memo = memo
        self.mobile_country_code = mobile_country_code
        self.mobile_phone_number = mobile_phone_number
        self.name = name
        self.oneself = oneself
        self.order_name = order_name
        self.out_passenger_id = out_passenger_id
        self.phone = phone
        self.sheng_pi_pinyin = sheng_pi_pinyin
        self.ticket_nos = ticket_nos
        self.tickets = tickets
        self.type = type
        self.user_id = user_id

    def validate(self):
        if self.credential:
            self.credential.validate()
        if self.credentials:
            for v1 in self.credentials:
                 if v1:
                    v1.validate()
        if self.tickets:
            for v1 in self.tickets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.birthday is not None:
            result['birthday'] = self.birthday

        if self.btrip_user_id is not None:
            result['btrip_user_id'] = self.btrip_user_id

        if self.code is not None:
            result['code'] = self.code

        if self.country is not None:
            result['country'] = self.country

        if self.country_code is not None:
            result['country_code'] = self.country_code

        if self.credential is not None:
            result['credential'] = self.credential.to_map()

        result['credentials'] = []
        if self.credentials is not None:
            for k1 in self.credentials:
                result['credentials'].append(k1.to_map() if k1 else None)

        if self.email is not None:
            result['email'] = self.email

        if self.en_first_name is not None:
            result['en_first_name'] = self.en_first_name

        if self.en_last_name is not None:
            result['en_last_name'] = self.en_last_name

        if self.english_name is not None:
            result['english_name'] = self.english_name

        if self.gender is not None:
            result['gender'] = self.gender

        if self.id is not None:
            result['id'] = self.id

        if self.is_complete is not None:
            result['is_complete'] = self.is_complete

        if self.is_frequently is not None:
            result['is_frequently'] = self.is_frequently

        if self.memo is not None:
            result['memo'] = self.memo

        if self.mobile_country_code is not None:
            result['mobile_country_code'] = self.mobile_country_code

        if self.mobile_phone_number is not None:
            result['mobile_phone_number'] = self.mobile_phone_number

        if self.name is not None:
            result['name'] = self.name

        if self.oneself is not None:
            result['oneself'] = self.oneself

        if self.order_name is not None:
            result['order_name'] = self.order_name

        if self.out_passenger_id is not None:
            result['out_passenger_id'] = self.out_passenger_id

        if self.phone is not None:
            result['phone'] = self.phone

        if self.sheng_pi_pinyin is not None:
            result['sheng_pi_pinyin'] = self.sheng_pi_pinyin

        if self.ticket_nos is not None:
            result['ticket_nos'] = self.ticket_nos

        result['tickets'] = []
        if self.tickets is not None:
            for k1 in self.tickets:
                result['tickets'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('birthday') is not None:
            self.birthday = m.get('birthday')

        if m.get('btrip_user_id') is not None:
            self.btrip_user_id = m.get('btrip_user_id')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('country') is not None:
            self.country = m.get('country')

        if m.get('country_code') is not None:
            self.country_code = m.get('country_code')

        if m.get('credential') is not None:
            temp_model = main_models.FlightOrderDetailV2ResponseBodyModulePassengerListCredential()
            self.credential = temp_model.from_map(m.get('credential'))

        self.credentials = []
        if m.get('credentials') is not None:
            for k1 in m.get('credentials'):
                temp_model = main_models.FlightOrderDetailV2ResponseBodyModulePassengerListCredentials()
                self.credentials.append(temp_model.from_map(k1))

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('en_first_name') is not None:
            self.en_first_name = m.get('en_first_name')

        if m.get('en_last_name') is not None:
            self.en_last_name = m.get('en_last_name')

        if m.get('english_name') is not None:
            self.english_name = m.get('english_name')

        if m.get('gender') is not None:
            self.gender = m.get('gender')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('is_complete') is not None:
            self.is_complete = m.get('is_complete')

        if m.get('is_frequently') is not None:
            self.is_frequently = m.get('is_frequently')

        if m.get('memo') is not None:
            self.memo = m.get('memo')

        if m.get('mobile_country_code') is not None:
            self.mobile_country_code = m.get('mobile_country_code')

        if m.get('mobile_phone_number') is not None:
            self.mobile_phone_number = m.get('mobile_phone_number')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('oneself') is not None:
            self.oneself = m.get('oneself')

        if m.get('order_name') is not None:
            self.order_name = m.get('order_name')

        if m.get('out_passenger_id') is not None:
            self.out_passenger_id = m.get('out_passenger_id')

        if m.get('phone') is not None:
            self.phone = m.get('phone')

        if m.get('sheng_pi_pinyin') is not None:
            self.sheng_pi_pinyin = m.get('sheng_pi_pinyin')

        if m.get('ticket_nos') is not None:
            self.ticket_nos = m.get('ticket_nos')

        self.tickets = []
        if m.get('tickets') is not None:
            for k1 in m.get('tickets'):
                temp_model = main_models.FlightOrderDetailV2ResponseBodyModulePassengerListTickets()
                self.tickets.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

class FlightOrderDetailV2ResponseBodyModulePassengerListTickets(DaraModel):
    def __init__(
        self,
        channel: str = None,
        journey_title: str = None,
        open_ticket_status: str = None,
        pcc: str = None,
        segment_open_ticket_list: List[main_models.FlightOrderDetailV2ResponseBodyModulePassengerListTicketsSegmentOpenTicketList] = None,
        ticket_auth_memo: str = None,
        ticket_auth_status: int = None,
        ticket_no: str = None,
        ticket_price: int = None,
        ticket_status: str = None,
    ):
        self.channel = channel
        self.journey_title = journey_title
        self.open_ticket_status = open_ticket_status
        # pcc/office
        self.pcc = pcc
        self.segment_open_ticket_list = segment_open_ticket_list
        self.ticket_auth_memo = ticket_auth_memo
        self.ticket_auth_status = ticket_auth_status
        self.ticket_no = ticket_no
        self.ticket_price = ticket_price
        self.ticket_status = ticket_status

    def validate(self):
        if self.segment_open_ticket_list:
            for v1 in self.segment_open_ticket_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['channel'] = self.channel

        if self.journey_title is not None:
            result['journey_title'] = self.journey_title

        if self.open_ticket_status is not None:
            result['open_ticket_status'] = self.open_ticket_status

        if self.pcc is not None:
            result['pcc'] = self.pcc

        result['segment_open_ticket_list'] = []
        if self.segment_open_ticket_list is not None:
            for k1 in self.segment_open_ticket_list:
                result['segment_open_ticket_list'].append(k1.to_map() if k1 else None)

        if self.ticket_auth_memo is not None:
            result['ticket_auth_memo'] = self.ticket_auth_memo

        if self.ticket_auth_status is not None:
            result['ticket_auth_status'] = self.ticket_auth_status

        if self.ticket_no is not None:
            result['ticket_no'] = self.ticket_no

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.ticket_status is not None:
            result['ticket_status'] = self.ticket_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')

        if m.get('journey_title') is not None:
            self.journey_title = m.get('journey_title')

        if m.get('open_ticket_status') is not None:
            self.open_ticket_status = m.get('open_ticket_status')

        if m.get('pcc') is not None:
            self.pcc = m.get('pcc')

        self.segment_open_ticket_list = []
        if m.get('segment_open_ticket_list') is not None:
            for k1 in m.get('segment_open_ticket_list'):
                temp_model = main_models.FlightOrderDetailV2ResponseBodyModulePassengerListTicketsSegmentOpenTicketList()
                self.segment_open_ticket_list.append(temp_model.from_map(k1))

        if m.get('ticket_auth_memo') is not None:
            self.ticket_auth_memo = m.get('ticket_auth_memo')

        if m.get('ticket_auth_status') is not None:
            self.ticket_auth_status = m.get('ticket_auth_status')

        if m.get('ticket_no') is not None:
            self.ticket_no = m.get('ticket_no')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('ticket_status') is not None:
            self.ticket_status = m.get('ticket_status')

        return self

class FlightOrderDetailV2ResponseBodyModulePassengerListTicketsSegmentOpenTicketList(DaraModel):
    def __init__(
        self,
        journey_index: int = None,
        open_ticket_status: int = None,
        segment_index: int = None,
    ):
        self.journey_index = journey_index
        self.open_ticket_status = open_ticket_status
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

        if self.open_ticket_status is not None:
            result['open_ticket_status'] = self.open_ticket_status

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('journey_index') is not None:
            self.journey_index = m.get('journey_index')

        if m.get('open_ticket_status') is not None:
            self.open_ticket_status = m.get('open_ticket_status')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        return self

class FlightOrderDetailV2ResponseBodyModulePassengerListCredentials(DaraModel):
    def __init__(
        self,
        birth_date: str = None,
        cert_issue_date: str = None,
        cert_issue_place: str = None,
        credential_no: str = None,
        drive_licence_first: str = None,
        drive_licence_type: str = None,
        expire_date: str = None,
        holder_nationality: str = None,
        id: int = None,
        id_check_code: str = None,
        issue_country: str = None,
        type: int = None,
    ):
        self.birth_date = birth_date
        self.cert_issue_date = cert_issue_date
        self.cert_issue_place = cert_issue_place
        self.credential_no = credential_no
        self.drive_licence_first = drive_licence_first
        self.drive_licence_type = drive_licence_type
        self.expire_date = expire_date
        self.holder_nationality = holder_nationality
        self.id = id
        self.id_check_code = id_check_code
        self.issue_country = issue_country
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.birth_date is not None:
            result['birth_date'] = self.birth_date

        if self.cert_issue_date is not None:
            result['cert_issue_date'] = self.cert_issue_date

        if self.cert_issue_place is not None:
            result['cert_issue_place'] = self.cert_issue_place

        if self.credential_no is not None:
            result['credential_no'] = self.credential_no

        if self.drive_licence_first is not None:
            result['drive_licence_first'] = self.drive_licence_first

        if self.drive_licence_type is not None:
            result['drive_licence_type'] = self.drive_licence_type

        if self.expire_date is not None:
            result['expire_date'] = self.expire_date

        if self.holder_nationality is not None:
            result['holder_nationality'] = self.holder_nationality

        if self.id is not None:
            result['id'] = self.id

        if self.id_check_code is not None:
            result['id_check_code'] = self.id_check_code

        if self.issue_country is not None:
            result['issue_country'] = self.issue_country

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('birth_date') is not None:
            self.birth_date = m.get('birth_date')

        if m.get('cert_issue_date') is not None:
            self.cert_issue_date = m.get('cert_issue_date')

        if m.get('cert_issue_place') is not None:
            self.cert_issue_place = m.get('cert_issue_place')

        if m.get('credential_no') is not None:
            self.credential_no = m.get('credential_no')

        if m.get('drive_licence_first') is not None:
            self.drive_licence_first = m.get('drive_licence_first')

        if m.get('drive_licence_type') is not None:
            self.drive_licence_type = m.get('drive_licence_type')

        if m.get('expire_date') is not None:
            self.expire_date = m.get('expire_date')

        if m.get('holder_nationality') is not None:
            self.holder_nationality = m.get('holder_nationality')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('id_check_code') is not None:
            self.id_check_code = m.get('id_check_code')

        if m.get('issue_country') is not None:
            self.issue_country = m.get('issue_country')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class FlightOrderDetailV2ResponseBodyModulePassengerListCredential(DaraModel):
    def __init__(
        self,
        birth_date: str = None,
        cert_issue_date: str = None,
        cert_issue_place: str = None,
        credential_no: str = None,
        drive_licence_first: str = None,
        drive_licence_type: str = None,
        expire_date: str = None,
        holder_nationality: str = None,
        id: int = None,
        id_check_code: str = None,
        issue_country: str = None,
        type: int = None,
    ):
        self.birth_date = birth_date
        self.cert_issue_date = cert_issue_date
        self.cert_issue_place = cert_issue_place
        self.credential_no = credential_no
        self.drive_licence_first = drive_licence_first
        self.drive_licence_type = drive_licence_type
        self.expire_date = expire_date
        self.holder_nationality = holder_nationality
        self.id = id
        self.id_check_code = id_check_code
        self.issue_country = issue_country
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.birth_date is not None:
            result['birth_date'] = self.birth_date

        if self.cert_issue_date is not None:
            result['cert_issue_date'] = self.cert_issue_date

        if self.cert_issue_place is not None:
            result['cert_issue_place'] = self.cert_issue_place

        if self.credential_no is not None:
            result['credential_no'] = self.credential_no

        if self.drive_licence_first is not None:
            result['drive_licence_first'] = self.drive_licence_first

        if self.drive_licence_type is not None:
            result['drive_licence_type'] = self.drive_licence_type

        if self.expire_date is not None:
            result['expire_date'] = self.expire_date

        if self.holder_nationality is not None:
            result['holder_nationality'] = self.holder_nationality

        if self.id is not None:
            result['id'] = self.id

        if self.id_check_code is not None:
            result['id_check_code'] = self.id_check_code

        if self.issue_country is not None:
            result['issue_country'] = self.issue_country

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('birth_date') is not None:
            self.birth_date = m.get('birth_date')

        if m.get('cert_issue_date') is not None:
            self.cert_issue_date = m.get('cert_issue_date')

        if m.get('cert_issue_place') is not None:
            self.cert_issue_place = m.get('cert_issue_place')

        if m.get('credential_no') is not None:
            self.credential_no = m.get('credential_no')

        if m.get('drive_licence_first') is not None:
            self.drive_licence_first = m.get('drive_licence_first')

        if m.get('drive_licence_type') is not None:
            self.drive_licence_type = m.get('drive_licence_type')

        if m.get('expire_date') is not None:
            self.expire_date = m.get('expire_date')

        if m.get('holder_nationality') is not None:
            self.holder_nationality = m.get('holder_nationality')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('id_check_code') is not None:
            self.id_check_code = m.get('id_check_code')

        if m.get('issue_country') is not None:
            self.issue_country = m.get('issue_country')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class FlightOrderDetailV2ResponseBodyModuleFlightTaleInfoDTO(DaraModel):
    def __init__(
        self,
        journeys: List[main_models.FlightOrderDetailV2ResponseBodyModuleFlightTaleInfoDTOJourneys] = None,
        notice_tips: str = None,
        trip_type: str = None,
        trip_type_code: int = None,
    ):
        self.journeys = journeys
        self.notice_tips = notice_tips
        self.trip_type = trip_type
        self.trip_type_code = trip_type_code

    def validate(self):
        if self.journeys:
            for v1 in self.journeys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['journeys'] = []
        if self.journeys is not None:
            for k1 in self.journeys:
                result['journeys'].append(k1.to_map() if k1 else None)

        if self.notice_tips is not None:
            result['notice_tips'] = self.notice_tips

        if self.trip_type is not None:
            result['trip_type'] = self.trip_type

        if self.trip_type_code is not None:
            result['trip_type_code'] = self.trip_type_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.journeys = []
        if m.get('journeys') is not None:
            for k1 in m.get('journeys'):
                temp_model = main_models.FlightOrderDetailV2ResponseBodyModuleFlightTaleInfoDTOJourneys()
                self.journeys.append(temp_model.from_map(k1))

        if m.get('notice_tips') is not None:
            self.notice_tips = m.get('notice_tips')

        if m.get('trip_type') is not None:
            self.trip_type = m.get('trip_type')

        if m.get('trip_type_code') is not None:
            self.trip_type_code = m.get('trip_type_code')

        return self

class FlightOrderDetailV2ResponseBodyModuleFlightTaleInfoDTOJourneys(DaraModel):
    def __init__(
        self,
        all_fly_duration: int = None,
        all_fly_duration_after_change: int = None,
        apply_id: int = None,
        arr_city_code: str = None,
        arr_city_name: str = None,
        arr_time: str = None,
        baggage_details: str = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_time: str = None,
        flight_status: str = None,
        iata_no: str = None,
        is_reshop_journey: bool = None,
        is_transfer: bool = None,
        journey_title: str = None,
        refund_change_details: str = None,
        segment_list: List[main_models.FlightOrderDetailV2ResponseBodyModuleFlightTaleInfoDTOJourneysSegmentList] = None,
    ):
        self.all_fly_duration = all_fly_duration
        self.all_fly_duration_after_change = all_fly_duration_after_change
        self.apply_id = apply_id
        self.arr_city_code = arr_city_code
        self.arr_city_name = arr_city_name
        self.arr_time = arr_time
        self.baggage_details = baggage_details
        self.dep_city_code = dep_city_code
        self.dep_city_name = dep_city_name
        self.dep_time = dep_time
        self.flight_status = flight_status
        # iata_no
        self.iata_no = iata_no
        self.is_reshop_journey = is_reshop_journey
        self.is_transfer = is_transfer
        self.journey_title = journey_title
        self.refund_change_details = refund_change_details
        self.segment_list = segment_list

    def validate(self):
        if self.segment_list:
            for v1 in self.segment_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_fly_duration is not None:
            result['all_fly_duration'] = self.all_fly_duration

        if self.all_fly_duration_after_change is not None:
            result['all_fly_duration_after_change'] = self.all_fly_duration_after_change

        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_city_name is not None:
            result['arr_city_name'] = self.arr_city_name

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.baggage_details is not None:
            result['baggage_details'] = self.baggage_details

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_city_name is not None:
            result['dep_city_name'] = self.dep_city_name

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.flight_status is not None:
            result['flight_status'] = self.flight_status

        if self.iata_no is not None:
            result['iata_no'] = self.iata_no

        if self.is_reshop_journey is not None:
            result['is_reshop_journey'] = self.is_reshop_journey

        if self.is_transfer is not None:
            result['is_transfer'] = self.is_transfer

        if self.journey_title is not None:
            result['journey_title'] = self.journey_title

        if self.refund_change_details is not None:
            result['refund_change_details'] = self.refund_change_details

        result['segment_list'] = []
        if self.segment_list is not None:
            for k1 in self.segment_list:
                result['segment_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all_fly_duration') is not None:
            self.all_fly_duration = m.get('all_fly_duration')

        if m.get('all_fly_duration_after_change') is not None:
            self.all_fly_duration_after_change = m.get('all_fly_duration_after_change')

        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('baggage_details') is not None:
            self.baggage_details = m.get('baggage_details')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_city_name') is not None:
            self.dep_city_name = m.get('dep_city_name')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('flight_status') is not None:
            self.flight_status = m.get('flight_status')

        if m.get('iata_no') is not None:
            self.iata_no = m.get('iata_no')

        if m.get('is_reshop_journey') is not None:
            self.is_reshop_journey = m.get('is_reshop_journey')

        if m.get('is_transfer') is not None:
            self.is_transfer = m.get('is_transfer')

        if m.get('journey_title') is not None:
            self.journey_title = m.get('journey_title')

        if m.get('refund_change_details') is not None:
            self.refund_change_details = m.get('refund_change_details')

        self.segment_list = []
        if m.get('segment_list') is not None:
            for k1 in m.get('segment_list'):
                temp_model = main_models.FlightOrderDetailV2ResponseBodyModuleFlightTaleInfoDTOJourneysSegmentList()
                self.segment_list.append(temp_model.from_map(k1))

        return self

class FlightOrderDetailV2ResponseBodyModuleFlightTaleInfoDTOJourneysSegmentList(DaraModel):
    def __init__(
        self,
        air_line_code: str = None,
        air_line_english_name: str = None,
        air_line_name: str = None,
        air_line_phone: str = None,
        airline_icon_url: str = None,
        airline_short_name: str = None,
        arr_airport_code: str = None,
        arr_airport_name: str = None,
        arr_city_code: str = None,
        arr_city_name: str = None,
        arr_time: str = None,
        arrive_terminal: str = None,
        cabin: str = None,
        cabin_and_discount: str = None,
        cabin_class: str = None,
        cabin_class_name: str = None,
        code_share: bool = None,
        deadline_text: str = None,
        dep_airport_code: str = None,
        dep_airport_name: str = None,
        dep_city_code: str = None,
        dep_city_name: str = None,
        dep_date: str = None,
        dep_time: str = None,
        depart_terminal: str = None,
        discount: float = None,
        flight_change: main_models.FlightOrderDetailV2ResponseBodyModuleFlightTaleInfoDTOJourneysSegmentListFlightChange = None,
        flight_no: str = None,
        flight_type: str = None,
        fly_duration: int = None,
        manufacturer: str = None,
        meal_desc: str = None,
        on_time_rate: str = None,
        operating_air_short_name: str = None,
        operating_airline_code: str = None,
        operating_airline_english_name: str = None,
        operating_airline_icon_url: str = None,
        operating_airline_name: str = None,
        operating_airline_phone: str = None,
        operating_flight_no: str = None,
        plane_type: str = None,
        raise_price: int = None,
        segment_id: str = None,
        segment_index: int = None,
        segment_position: main_models.FlightOrderDetailV2ResponseBodyModuleFlightTaleInfoDTOJourneysSegmentListSegmentPosition = None,
        stop_airport: str = None,
        stop_arr_time: str = None,
        stop_city: str = None,
        stop_city_name: str = None,
        stop_dep_time: str = None,
        stop_quantity: int = None,
    ):
        self.air_line_code = air_line_code
        self.air_line_english_name = air_line_english_name
        self.air_line_name = air_line_name
        self.air_line_phone = air_line_phone
        self.airline_icon_url = airline_icon_url
        self.airline_short_name = airline_short_name
        self.arr_airport_code = arr_airport_code
        self.arr_airport_name = arr_airport_name
        self.arr_city_code = arr_city_code
        self.arr_city_name = arr_city_name
        self.arr_time = arr_time
        self.arrive_terminal = arrive_terminal
        # cabin
        self.cabin = cabin
        self.cabin_and_discount = cabin_and_discount
        # cabin_class
        self.cabin_class = cabin_class
        # cabin_class_name
        self.cabin_class_name = cabin_class_name
        self.code_share = code_share
        self.deadline_text = deadline_text
        self.dep_airport_code = dep_airport_code
        self.dep_airport_name = dep_airport_name
        self.dep_city_code = dep_city_code
        self.dep_city_name = dep_city_name
        self.dep_date = dep_date
        self.dep_time = dep_time
        self.depart_terminal = depart_terminal
        self.discount = discount
        self.flight_change = flight_change
        self.flight_no = flight_no
        self.flight_type = flight_type
        self.fly_duration = fly_duration
        self.manufacturer = manufacturer
        self.meal_desc = meal_desc
        self.on_time_rate = on_time_rate
        self.operating_air_short_name = operating_air_short_name
        self.operating_airline_code = operating_airline_code
        self.operating_airline_english_name = operating_airline_english_name
        self.operating_airline_icon_url = operating_airline_icon_url
        self.operating_airline_name = operating_airline_name
        self.operating_airline_phone = operating_airline_phone
        self.operating_flight_no = operating_flight_no
        self.plane_type = plane_type
        self.raise_price = raise_price
        self.segment_id = segment_id
        # segmentIndex
        self.segment_index = segment_index
        self.segment_position = segment_position
        self.stop_airport = stop_airport
        self.stop_arr_time = stop_arr_time
        self.stop_city = stop_city
        self.stop_city_name = stop_city_name
        self.stop_dep_time = stop_dep_time
        self.stop_quantity = stop_quantity

    def validate(self):
        if self.flight_change:
            self.flight_change.validate()
        if self.segment_position:
            self.segment_position.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.air_line_code is not None:
            result['air_line_code'] = self.air_line_code

        if self.air_line_english_name is not None:
            result['air_line_english_name'] = self.air_line_english_name

        if self.air_line_name is not None:
            result['air_line_name'] = self.air_line_name

        if self.air_line_phone is not None:
            result['air_line_phone'] = self.air_line_phone

        if self.airline_icon_url is not None:
            result['airline_icon_url'] = self.airline_icon_url

        if self.airline_short_name is not None:
            result['airline_short_name'] = self.airline_short_name

        if self.arr_airport_code is not None:
            result['arr_airport_code'] = self.arr_airport_code

        if self.arr_airport_name is not None:
            result['arr_airport_name'] = self.arr_airport_name

        if self.arr_city_code is not None:
            result['arr_city_code'] = self.arr_city_code

        if self.arr_city_name is not None:
            result['arr_city_name'] = self.arr_city_name

        if self.arr_time is not None:
            result['arr_time'] = self.arr_time

        if self.arrive_terminal is not None:
            result['arrive_terminal'] = self.arrive_terminal

        if self.cabin is not None:
            result['cabin'] = self.cabin

        if self.cabin_and_discount is not None:
            result['cabin_and_discount'] = self.cabin_and_discount

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.cabin_class_name is not None:
            result['cabin_class_name'] = self.cabin_class_name

        if self.code_share is not None:
            result['code_share'] = self.code_share

        if self.deadline_text is not None:
            result['deadline_text'] = self.deadline_text

        if self.dep_airport_code is not None:
            result['dep_airport_code'] = self.dep_airport_code

        if self.dep_airport_name is not None:
            result['dep_airport_name'] = self.dep_airport_name

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.dep_city_name is not None:
            result['dep_city_name'] = self.dep_city_name

        if self.dep_date is not None:
            result['dep_date'] = self.dep_date

        if self.dep_time is not None:
            result['dep_time'] = self.dep_time

        if self.depart_terminal is not None:
            result['depart_terminal'] = self.depart_terminal

        if self.discount is not None:
            result['discount'] = self.discount

        if self.flight_change is not None:
            result['flight_change'] = self.flight_change.to_map()

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.flight_type is not None:
            result['flight_type'] = self.flight_type

        if self.fly_duration is not None:
            result['fly_duration'] = self.fly_duration

        if self.manufacturer is not None:
            result['manufacturer'] = self.manufacturer

        if self.meal_desc is not None:
            result['meal_desc'] = self.meal_desc

        if self.on_time_rate is not None:
            result['on_time_rate'] = self.on_time_rate

        if self.operating_air_short_name is not None:
            result['operating_air_short_name'] = self.operating_air_short_name

        if self.operating_airline_code is not None:
            result['operating_airline_code'] = self.operating_airline_code

        if self.operating_airline_english_name is not None:
            result['operating_airline_english_name'] = self.operating_airline_english_name

        if self.operating_airline_icon_url is not None:
            result['operating_airline_icon_url'] = self.operating_airline_icon_url

        if self.operating_airline_name is not None:
            result['operating_airline_name'] = self.operating_airline_name

        if self.operating_airline_phone is not None:
            result['operating_airline_phone'] = self.operating_airline_phone

        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no

        if self.plane_type is not None:
            result['plane_type'] = self.plane_type

        if self.raise_price is not None:
            result['raise_price'] = self.raise_price

        if self.segment_id is not None:
            result['segment_id'] = self.segment_id

        if self.segment_index is not None:
            result['segment_index'] = self.segment_index

        if self.segment_position is not None:
            result['segment_position'] = self.segment_position.to_map()

        if self.stop_airport is not None:
            result['stop_airport'] = self.stop_airport

        if self.stop_arr_time is not None:
            result['stop_arr_time'] = self.stop_arr_time

        if self.stop_city is not None:
            result['stop_city'] = self.stop_city

        if self.stop_city_name is not None:
            result['stop_city_name'] = self.stop_city_name

        if self.stop_dep_time is not None:
            result['stop_dep_time'] = self.stop_dep_time

        if self.stop_quantity is not None:
            result['stop_quantity'] = self.stop_quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('air_line_code') is not None:
            self.air_line_code = m.get('air_line_code')

        if m.get('air_line_english_name') is not None:
            self.air_line_english_name = m.get('air_line_english_name')

        if m.get('air_line_name') is not None:
            self.air_line_name = m.get('air_line_name')

        if m.get('air_line_phone') is not None:
            self.air_line_phone = m.get('air_line_phone')

        if m.get('airline_icon_url') is not None:
            self.airline_icon_url = m.get('airline_icon_url')

        if m.get('airline_short_name') is not None:
            self.airline_short_name = m.get('airline_short_name')

        if m.get('arr_airport_code') is not None:
            self.arr_airport_code = m.get('arr_airport_code')

        if m.get('arr_airport_name') is not None:
            self.arr_airport_name = m.get('arr_airport_name')

        if m.get('arr_city_code') is not None:
            self.arr_city_code = m.get('arr_city_code')

        if m.get('arr_city_name') is not None:
            self.arr_city_name = m.get('arr_city_name')

        if m.get('arr_time') is not None:
            self.arr_time = m.get('arr_time')

        if m.get('arrive_terminal') is not None:
            self.arrive_terminal = m.get('arrive_terminal')

        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('cabin_and_discount') is not None:
            self.cabin_and_discount = m.get('cabin_and_discount')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('cabin_class_name') is not None:
            self.cabin_class_name = m.get('cabin_class_name')

        if m.get('code_share') is not None:
            self.code_share = m.get('code_share')

        if m.get('deadline_text') is not None:
            self.deadline_text = m.get('deadline_text')

        if m.get('dep_airport_code') is not None:
            self.dep_airport_code = m.get('dep_airport_code')

        if m.get('dep_airport_name') is not None:
            self.dep_airport_name = m.get('dep_airport_name')

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('dep_city_name') is not None:
            self.dep_city_name = m.get('dep_city_name')

        if m.get('dep_date') is not None:
            self.dep_date = m.get('dep_date')

        if m.get('dep_time') is not None:
            self.dep_time = m.get('dep_time')

        if m.get('depart_terminal') is not None:
            self.depart_terminal = m.get('depart_terminal')

        if m.get('discount') is not None:
            self.discount = m.get('discount')

        if m.get('flight_change') is not None:
            temp_model = main_models.FlightOrderDetailV2ResponseBodyModuleFlightTaleInfoDTOJourneysSegmentListFlightChange()
            self.flight_change = temp_model.from_map(m.get('flight_change'))

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('flight_type') is not None:
            self.flight_type = m.get('flight_type')

        if m.get('fly_duration') is not None:
            self.fly_duration = m.get('fly_duration')

        if m.get('manufacturer') is not None:
            self.manufacturer = m.get('manufacturer')

        if m.get('meal_desc') is not None:
            self.meal_desc = m.get('meal_desc')

        if m.get('on_time_rate') is not None:
            self.on_time_rate = m.get('on_time_rate')

        if m.get('operating_air_short_name') is not None:
            self.operating_air_short_name = m.get('operating_air_short_name')

        if m.get('operating_airline_code') is not None:
            self.operating_airline_code = m.get('operating_airline_code')

        if m.get('operating_airline_english_name') is not None:
            self.operating_airline_english_name = m.get('operating_airline_english_name')

        if m.get('operating_airline_icon_url') is not None:
            self.operating_airline_icon_url = m.get('operating_airline_icon_url')

        if m.get('operating_airline_name') is not None:
            self.operating_airline_name = m.get('operating_airline_name')

        if m.get('operating_airline_phone') is not None:
            self.operating_airline_phone = m.get('operating_airline_phone')

        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')

        if m.get('plane_type') is not None:
            self.plane_type = m.get('plane_type')

        if m.get('raise_price') is not None:
            self.raise_price = m.get('raise_price')

        if m.get('segment_id') is not None:
            self.segment_id = m.get('segment_id')

        if m.get('segment_index') is not None:
            self.segment_index = m.get('segment_index')

        if m.get('segment_position') is not None:
            temp_model = main_models.FlightOrderDetailV2ResponseBodyModuleFlightTaleInfoDTOJourneysSegmentListSegmentPosition()
            self.segment_position = temp_model.from_map(m.get('segment_position'))

        if m.get('stop_airport') is not None:
            self.stop_airport = m.get('stop_airport')

        if m.get('stop_arr_time') is not None:
            self.stop_arr_time = m.get('stop_arr_time')

        if m.get('stop_city') is not None:
            self.stop_city = m.get('stop_city')

        if m.get('stop_city_name') is not None:
            self.stop_city_name = m.get('stop_city_name')

        if m.get('stop_dep_time') is not None:
            self.stop_dep_time = m.get('stop_dep_time')

        if m.get('stop_quantity') is not None:
            self.stop_quantity = m.get('stop_quantity')

        return self

class FlightOrderDetailV2ResponseBodyModuleFlightTaleInfoDTOJourneysSegmentListSegmentPosition(DaraModel):
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

class FlightOrderDetailV2ResponseBodyModuleFlightTaleInfoDTOJourneysSegmentListFlightChange(DaraModel):
    def __init__(
        self,
        change_desc: str = None,
        change_status: str = None,
        change_status_code: str = None,
        new_segment: Any = None,
        passenger_names: List[str] = None,
    ):
        self.change_desc = change_desc
        self.change_status = change_status
        self.change_status_code = change_status_code
        self.new_segment = new_segment
        self.passenger_names = passenger_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_desc is not None:
            result['change_desc'] = self.change_desc

        if self.change_status is not None:
            result['change_status'] = self.change_status

        if self.change_status_code is not None:
            result['change_status_code'] = self.change_status_code

        if self.new_segment is not None:
            result['new_segment'] = self.new_segment

        if self.passenger_names is not None:
            result['passenger_names'] = self.passenger_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change_desc') is not None:
            self.change_desc = m.get('change_desc')

        if m.get('change_status') is not None:
            self.change_status = m.get('change_status')

        if m.get('change_status_code') is not None:
            self.change_status_code = m.get('change_status_code')

        if m.get('new_segment') is not None:
            self.new_segment = m.get('new_segment')

        if m.get('passenger_names') is not None:
            self.passenger_names = m.get('passenger_names')

        return self

class FlightOrderDetailV2ResponseBodyModuleContactInfoDTO(DaraModel):
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

