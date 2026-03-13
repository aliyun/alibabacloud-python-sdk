# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TicketChangingEnquiryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.TicketChangingEnquiryResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        self.module = module
        self.request_id = request_id
        self.success = success
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
            temp_model = main_models.TicketChangingEnquiryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class TicketChangingEnquiryResponseBodyModule(DaraModel):
    def __init__(
        self,
        flight_info_list: List[main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoList] = None,
    ):
        self.flight_info_list = flight_info_list

    def validate(self):
        if self.flight_info_list:
            for v1 in self.flight_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['flight_info_list'] = []
        if self.flight_info_list is not None:
            for k1 in self.flight_info_list:
                result['flight_info_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.flight_info_list = []
        if m.get('flight_info_list') is not None:
            for k1 in m.get('flight_info_list'):
                temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoList()
                self.flight_info_list.append(temp_model.from_map(k1))

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoList(DaraModel):
    def __init__(
        self,
        airline_info: main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListAirlineInfo = None,
        arr_airport_info: main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListArrAirportInfo = None,
        cabin_list: List[main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinList] = None,
        carrier_airline: str = None,
        carrier_no: str = None,
        dep_airport_info: main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListDepAirportInfo = None,
        dep_city_code: str = None,
        flight_no: str = None,
        is_share: bool = None,
        lowest_cabin: str = None,
        lowest_cabin_class: str = None,
        lowest_cabin_desc: str = None,
        lowest_cabin_num: str = None,
        lowest_cabin_price: List[main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListLowestCabinPrice] = None,
        modify_flight_arr_time: str = None,
        modify_flight_dep_date: str = None,
        modify_flight_dep_time: str = None,
        session_id: str = None,
    ):
        self.airline_info = airline_info
        self.arr_airport_info = arr_airport_info
        self.cabin_list = cabin_list
        self.carrier_airline = carrier_airline
        self.carrier_no = carrier_no
        self.dep_airport_info = dep_airport_info
        self.dep_city_code = dep_city_code
        self.flight_no = flight_no
        self.is_share = is_share
        self.lowest_cabin = lowest_cabin
        self.lowest_cabin_class = lowest_cabin_class
        self.lowest_cabin_desc = lowest_cabin_desc
        self.lowest_cabin_num = lowest_cabin_num
        self.lowest_cabin_price = lowest_cabin_price
        self.modify_flight_arr_time = modify_flight_arr_time
        self.modify_flight_dep_date = modify_flight_dep_date
        self.modify_flight_dep_time = modify_flight_dep_time
        self.session_id = session_id

    def validate(self):
        if self.airline_info:
            self.airline_info.validate()
        if self.arr_airport_info:
            self.arr_airport_info.validate()
        if self.cabin_list:
            for v1 in self.cabin_list:
                 if v1:
                    v1.validate()
        if self.dep_airport_info:
            self.dep_airport_info.validate()
        if self.lowest_cabin_price:
            for v1 in self.lowest_cabin_price:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_info is not None:
            result['airline_info'] = self.airline_info.to_map()

        if self.arr_airport_info is not None:
            result['arr_airport_info'] = self.arr_airport_info.to_map()

        result['cabin_list'] = []
        if self.cabin_list is not None:
            for k1 in self.cabin_list:
                result['cabin_list'].append(k1.to_map() if k1 else None)

        if self.carrier_airline is not None:
            result['carrier_airline'] = self.carrier_airline

        if self.carrier_no is not None:
            result['carrier_no'] = self.carrier_no

        if self.dep_airport_info is not None:
            result['dep_airport_info'] = self.dep_airport_info.to_map()

        if self.dep_city_code is not None:
            result['dep_city_code'] = self.dep_city_code

        if self.flight_no is not None:
            result['flight_no'] = self.flight_no

        if self.is_share is not None:
            result['is_share'] = self.is_share

        if self.lowest_cabin is not None:
            result['lowest_cabin'] = self.lowest_cabin

        if self.lowest_cabin_class is not None:
            result['lowest_cabin_class'] = self.lowest_cabin_class

        if self.lowest_cabin_desc is not None:
            result['lowest_cabin_desc'] = self.lowest_cabin_desc

        if self.lowest_cabin_num is not None:
            result['lowest_cabin_num'] = self.lowest_cabin_num

        result['lowest_cabin_price'] = []
        if self.lowest_cabin_price is not None:
            for k1 in self.lowest_cabin_price:
                result['lowest_cabin_price'].append(k1.to_map() if k1 else None)

        if self.modify_flight_arr_time is not None:
            result['modify_flight_arr_time'] = self.modify_flight_arr_time

        if self.modify_flight_dep_date is not None:
            result['modify_flight_dep_date'] = self.modify_flight_dep_date

        if self.modify_flight_dep_time is not None:
            result['modify_flight_dep_time'] = self.modify_flight_dep_time

        if self.session_id is not None:
            result['session_id'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_info') is not None:
            temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListAirlineInfo()
            self.airline_info = temp_model.from_map(m.get('airline_info'))

        if m.get('arr_airport_info') is not None:
            temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListArrAirportInfo()
            self.arr_airport_info = temp_model.from_map(m.get('arr_airport_info'))

        self.cabin_list = []
        if m.get('cabin_list') is not None:
            for k1 in m.get('cabin_list'):
                temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinList()
                self.cabin_list.append(temp_model.from_map(k1))

        if m.get('carrier_airline') is not None:
            self.carrier_airline = m.get('carrier_airline')

        if m.get('carrier_no') is not None:
            self.carrier_no = m.get('carrier_no')

        if m.get('dep_airport_info') is not None:
            temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListDepAirportInfo()
            self.dep_airport_info = temp_model.from_map(m.get('dep_airport_info'))

        if m.get('dep_city_code') is not None:
            self.dep_city_code = m.get('dep_city_code')

        if m.get('flight_no') is not None:
            self.flight_no = m.get('flight_no')

        if m.get('is_share') is not None:
            self.is_share = m.get('is_share')

        if m.get('lowest_cabin') is not None:
            self.lowest_cabin = m.get('lowest_cabin')

        if m.get('lowest_cabin_class') is not None:
            self.lowest_cabin_class = m.get('lowest_cabin_class')

        if m.get('lowest_cabin_desc') is not None:
            self.lowest_cabin_desc = m.get('lowest_cabin_desc')

        if m.get('lowest_cabin_num') is not None:
            self.lowest_cabin_num = m.get('lowest_cabin_num')

        self.lowest_cabin_price = []
        if m.get('lowest_cabin_price') is not None:
            for k1 in m.get('lowest_cabin_price'):
                temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListLowestCabinPrice()
                self.lowest_cabin_price.append(temp_model.from_map(k1))

        if m.get('modify_flight_arr_time') is not None:
            self.modify_flight_arr_time = m.get('modify_flight_arr_time')

        if m.get('modify_flight_dep_date') is not None:
            self.modify_flight_dep_date = m.get('modify_flight_dep_date')

        if m.get('modify_flight_dep_time') is not None:
            self.modify_flight_dep_time = m.get('modify_flight_dep_time')

        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListLowestCabinPrice(DaraModel):
    def __init__(
        self,
        passenger_type: int = None,
        ticket_price: int = None,
        upgrade_fee: int = None,
        upgrade_price: int = None,
    ):
        self.passenger_type = passenger_type
        self.ticket_price = ticket_price
        self.upgrade_fee = upgrade_fee
        self.upgrade_price = upgrade_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passenger_type is not None:
            result['passenger_type'] = self.passenger_type

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.upgrade_fee is not None:
            result['upgrade_fee'] = self.upgrade_fee

        if self.upgrade_price is not None:
            result['upgrade_price'] = self.upgrade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger_type') is not None:
            self.passenger_type = m.get('passenger_type')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('upgrade_fee') is not None:
            self.upgrade_fee = m.get('upgrade_fee')

        if m.get('upgrade_price') is not None:
            self.upgrade_price = m.get('upgrade_price')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListDepAirportInfo(DaraModel):
    def __init__(
        self,
        airport_code: str = None,
        airport_name: str = None,
        city_code: str = None,
        city_name: str = None,
        terminal: str = None,
    ):
        self.airport_code = airport_code
        self.airport_name = airport_name
        self.city_code = city_code
        self.city_name = city_name
        self.terminal = terminal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airport_code is not None:
            result['airport_code'] = self.airport_code

        if self.airport_name is not None:
            result['airport_name'] = self.airport_name

        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_name is not None:
            result['city_name'] = self.city_name

        if self.terminal is not None:
            result['terminal'] = self.terminal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airport_code') is not None:
            self.airport_code = m.get('airport_code')

        if m.get('airport_name') is not None:
            self.airport_name = m.get('airport_name')

        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        if m.get('terminal') is not None:
            self.terminal = m.get('terminal')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinList(DaraModel):
    def __init__(
        self,
        cabin: str = None,
        cabin_class: str = None,
        cabin_desc: str = None,
        cabin_discount: int = None,
        change_ota_item_rule_rq: main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRq = None,
        child_cabin: str = None,
        left_num: str = None,
        modify_price_list: List[main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListModifyPriceList] = None,
        ota_itemid: str = None,
    ):
        self.cabin = cabin
        self.cabin_class = cabin_class
        self.cabin_desc = cabin_desc
        self.cabin_discount = cabin_discount
        self.change_ota_item_rule_rq = change_ota_item_rule_rq
        self.child_cabin = child_cabin
        self.left_num = left_num
        self.modify_price_list = modify_price_list
        self.ota_itemid = ota_itemid

    def validate(self):
        if self.change_ota_item_rule_rq:
            self.change_ota_item_rule_rq.validate()
        if self.modify_price_list:
            for v1 in self.modify_price_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cabin is not None:
            result['cabin'] = self.cabin

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.cabin_desc is not None:
            result['cabin_desc'] = self.cabin_desc

        if self.cabin_discount is not None:
            result['cabin_discount'] = self.cabin_discount

        if self.change_ota_item_rule_rq is not None:
            result['change_ota_item_rule_rq'] = self.change_ota_item_rule_rq.to_map()

        if self.child_cabin is not None:
            result['child_cabin'] = self.child_cabin

        if self.left_num is not None:
            result['left_num'] = self.left_num

        result['modify_price_list'] = []
        if self.modify_price_list is not None:
            for k1 in self.modify_price_list:
                result['modify_price_list'].append(k1.to_map() if k1 else None)

        if self.ota_itemid is not None:
            result['ota_itemid'] = self.ota_itemid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('cabin_desc') is not None:
            self.cabin_desc = m.get('cabin_desc')

        if m.get('cabin_discount') is not None:
            self.cabin_discount = m.get('cabin_discount')

        if m.get('change_ota_item_rule_rq') is not None:
            temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRq()
            self.change_ota_item_rule_rq = temp_model.from_map(m.get('change_ota_item_rule_rq'))

        if m.get('child_cabin') is not None:
            self.child_cabin = m.get('child_cabin')

        if m.get('left_num') is not None:
            self.left_num = m.get('left_num')

        self.modify_price_list = []
        if m.get('modify_price_list') is not None:
            for k1 in m.get('modify_price_list'):
                temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListModifyPriceList()
                self.modify_price_list.append(temp_model.from_map(k1))

        if m.get('ota_itemid') is not None:
            self.ota_itemid = m.get('ota_itemid')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListModifyPriceList(DaraModel):
    def __init__(
        self,
        passenger_type: int = None,
        ticket_price: int = None,
        upgrade_fee: int = None,
        upgrade_price: int = None,
    ):
        self.passenger_type = passenger_type
        self.ticket_price = ticket_price
        self.upgrade_fee = upgrade_fee
        self.upgrade_price = upgrade_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passenger_type is not None:
            result['passenger_type'] = self.passenger_type

        if self.ticket_price is not None:
            result['ticket_price'] = self.ticket_price

        if self.upgrade_fee is not None:
            result['upgrade_fee'] = self.upgrade_fee

        if self.upgrade_price is not None:
            result['upgrade_price'] = self.upgrade_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger_type') is not None:
            self.passenger_type = m.get('passenger_type')

        if m.get('ticket_price') is not None:
            self.ticket_price = m.get('ticket_price')

        if m.get('upgrade_fee') is not None:
            self.upgrade_fee = m.get('upgrade_fee')

        if m.get('upgrade_price') is not None:
            self.upgrade_price = m.get('upgrade_price')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRq(DaraModel):
    def __init__(
        self,
        baggage_details: List[main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetails] = None,
        change_details: List[main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqChangeDetails] = None,
        refund_details: List[main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqRefundDetails] = None,
    ):
        self.baggage_details = baggage_details
        self.change_details = change_details
        self.refund_details = refund_details

    def validate(self):
        if self.baggage_details:
            for v1 in self.baggage_details:
                 if v1:
                    v1.validate()
        if self.change_details:
            for v1 in self.change_details:
                 if v1:
                    v1.validate()
        if self.refund_details:
            for v1 in self.refund_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['baggage_details'] = []
        if self.baggage_details is not None:
            for k1 in self.baggage_details:
                result['baggage_details'].append(k1.to_map() if k1 else None)

        result['change_details'] = []
        if self.change_details is not None:
            for k1 in self.change_details:
                result['change_details'].append(k1.to_map() if k1 else None)

        result['refund_details'] = []
        if self.refund_details is not None:
            for k1 in self.refund_details:
                result['refund_details'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baggage_details = []
        if m.get('baggage_details') is not None:
            for k1 in m.get('baggage_details'):
                temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetails()
                self.baggage_details.append(temp_model.from_map(k1))

        self.change_details = []
        if m.get('change_details') is not None:
            for k1 in m.get('change_details'):
                temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqChangeDetails()
                self.change_details.append(temp_model.from_map(k1))

        self.refund_details = []
        if m.get('refund_details') is not None:
            for k1 in m.get('refund_details'):
                temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqRefundDetails()
                self.refund_details.append(temp_model.from_map(k1))

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqRefundDetails(DaraModel):
    def __init__(
        self,
        extra_contents: List[main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqRefundDetailsExtraContents] = None,
        index: int = None,
        refund_sub_items: List[main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqRefundDetailsRefundSubItems] = None,
        table_head: str = None,
        title: str = None,
        type: int = None,
    ):
        self.extra_contents = extra_contents
        self.index = index
        self.refund_sub_items = refund_sub_items
        self.table_head = table_head
        self.title = title
        self.type = type

    def validate(self):
        if self.extra_contents:
            for v1 in self.extra_contents:
                 if v1:
                    v1.validate()
        if self.refund_sub_items:
            for v1 in self.refund_sub_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['extra_contents'] = []
        if self.extra_contents is not None:
            for k1 in self.extra_contents:
                result['extra_contents'].append(k1.to_map() if k1 else None)

        if self.index is not None:
            result['index'] = self.index

        result['refund_sub_items'] = []
        if self.refund_sub_items is not None:
            for k1 in self.refund_sub_items:
                result['refund_sub_items'].append(k1.to_map() if k1 else None)

        if self.table_head is not None:
            result['table_head'] = self.table_head

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.extra_contents = []
        if m.get('extra_contents') is not None:
            for k1 in m.get('extra_contents'):
                temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqRefundDetailsExtraContents()
                self.extra_contents.append(temp_model.from_map(k1))

        if m.get('index') is not None:
            self.index = m.get('index')

        self.refund_sub_items = []
        if m.get('refund_sub_items') is not None:
            for k1 in m.get('refund_sub_items'):
                temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqRefundDetailsRefundSubItems()
                self.refund_sub_items.append(temp_model.from_map(k1))

        if m.get('table_head') is not None:
            self.table_head = m.get('table_head')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqRefundDetailsRefundSubItems(DaraModel):
    def __init__(
        self,
        content: str = None,
        is_struct: bool = None,
        ptc: str = None,
        refund_sub_contents: List[main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqRefundDetailsRefundSubItemsRefundSubContents] = None,
        title: str = None,
    ):
        self.content = content
        self.is_struct = is_struct
        self.ptc = ptc
        self.refund_sub_contents = refund_sub_contents
        self.title = title

    def validate(self):
        if self.refund_sub_contents:
            for v1 in self.refund_sub_contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.is_struct is not None:
            result['is_struct'] = self.is_struct

        if self.ptc is not None:
            result['ptc'] = self.ptc

        result['refund_sub_contents'] = []
        if self.refund_sub_contents is not None:
            for k1 in self.refund_sub_contents:
                result['refund_sub_contents'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('is_struct') is not None:
            self.is_struct = m.get('is_struct')

        if m.get('ptc') is not None:
            self.ptc = m.get('ptc')

        self.refund_sub_contents = []
        if m.get('refund_sub_contents') is not None:
            for k1 in m.get('refund_sub_contents'):
                temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqRefundDetailsRefundSubItemsRefundSubContents()
                self.refund_sub_contents.append(temp_model.from_map(k1))

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqRefundDetailsRefundSubItemsRefundSubContents(DaraModel):
    def __init__(
        self,
        fee_desc: str = None,
        fee_range: str = None,
        style: str = None,
    ):
        self.fee_desc = fee_desc
        self.fee_range = fee_range
        self.style = style

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fee_desc is not None:
            result['fee_desc'] = self.fee_desc

        if self.fee_range is not None:
            result['fee_range'] = self.fee_range

        if self.style is not None:
            result['style'] = self.style

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fee_desc') is not None:
            self.fee_desc = m.get('fee_desc')

        if m.get('fee_range') is not None:
            self.fee_range = m.get('fee_range')

        if m.get('style') is not None:
            self.style = m.get('style')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqRefundDetailsExtraContents(DaraModel):
    def __init__(
        self,
        content: str = None,
        icon: str = None,
        title: str = None,
    ):
        self.content = content
        self.icon = icon
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.icon is not None:
            result['icon'] = self.icon

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('icon') is not None:
            self.icon = m.get('icon')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqChangeDetails(DaraModel):
    def __init__(
        self,
        extra_contents: List[main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqChangeDetailsExtraContents] = None,
        index: int = None,
        refund_sub_items: List[main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqChangeDetailsRefundSubItems] = None,
        table_head: str = None,
        title: str = None,
        type: int = None,
    ):
        self.extra_contents = extra_contents
        self.index = index
        self.refund_sub_items = refund_sub_items
        self.table_head = table_head
        self.title = title
        self.type = type

    def validate(self):
        if self.extra_contents:
            for v1 in self.extra_contents:
                 if v1:
                    v1.validate()
        if self.refund_sub_items:
            for v1 in self.refund_sub_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['extra_contents'] = []
        if self.extra_contents is not None:
            for k1 in self.extra_contents:
                result['extra_contents'].append(k1.to_map() if k1 else None)

        if self.index is not None:
            result['index'] = self.index

        result['refund_sub_items'] = []
        if self.refund_sub_items is not None:
            for k1 in self.refund_sub_items:
                result['refund_sub_items'].append(k1.to_map() if k1 else None)

        if self.table_head is not None:
            result['table_head'] = self.table_head

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.extra_contents = []
        if m.get('extra_contents') is not None:
            for k1 in m.get('extra_contents'):
                temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqChangeDetailsExtraContents()
                self.extra_contents.append(temp_model.from_map(k1))

        if m.get('index') is not None:
            self.index = m.get('index')

        self.refund_sub_items = []
        if m.get('refund_sub_items') is not None:
            for k1 in m.get('refund_sub_items'):
                temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqChangeDetailsRefundSubItems()
                self.refund_sub_items.append(temp_model.from_map(k1))

        if m.get('table_head') is not None:
            self.table_head = m.get('table_head')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqChangeDetailsRefundSubItems(DaraModel):
    def __init__(
        self,
        content: str = None,
        is_struct: bool = None,
        ptc: str = None,
        refund_sub_contents: List[main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqChangeDetailsRefundSubItemsRefundSubContents] = None,
        title: str = None,
    ):
        self.content = content
        self.is_struct = is_struct
        self.ptc = ptc
        self.refund_sub_contents = refund_sub_contents
        self.title = title

    def validate(self):
        if self.refund_sub_contents:
            for v1 in self.refund_sub_contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.is_struct is not None:
            result['is_struct'] = self.is_struct

        if self.ptc is not None:
            result['ptc'] = self.ptc

        result['refund_sub_contents'] = []
        if self.refund_sub_contents is not None:
            for k1 in self.refund_sub_contents:
                result['refund_sub_contents'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('is_struct') is not None:
            self.is_struct = m.get('is_struct')

        if m.get('ptc') is not None:
            self.ptc = m.get('ptc')

        self.refund_sub_contents = []
        if m.get('refund_sub_contents') is not None:
            for k1 in m.get('refund_sub_contents'):
                temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqChangeDetailsRefundSubItemsRefundSubContents()
                self.refund_sub_contents.append(temp_model.from_map(k1))

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqChangeDetailsRefundSubItemsRefundSubContents(DaraModel):
    def __init__(
        self,
        fee_desc: str = None,
        fee_range: str = None,
        style: str = None,
    ):
        self.fee_desc = fee_desc
        self.fee_range = fee_range
        self.style = style

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fee_desc is not None:
            result['fee_desc'] = self.fee_desc

        if self.fee_range is not None:
            result['fee_range'] = self.fee_range

        if self.style is not None:
            result['style'] = self.style

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fee_desc') is not None:
            self.fee_desc = m.get('fee_desc')

        if m.get('fee_range') is not None:
            self.fee_range = m.get('fee_range')

        if m.get('style') is not None:
            self.style = m.get('style')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqChangeDetailsExtraContents(DaraModel):
    def __init__(
        self,
        content: str = None,
        icon: str = None,
        title: str = None,
    ):
        self.content = content
        self.icon = icon
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.icon is not None:
            result['icon'] = self.icon

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('icon') is not None:
            self.icon = m.get('icon')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetails(DaraModel):
    def __init__(
        self,
        baggage_sub_items: List[main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetailsBaggageSubItems] = None,
        index: int = None,
        table_head: str = None,
        tips: main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetailsTips = None,
        title: str = None,
        type: int = None,
    ):
        self.baggage_sub_items = baggage_sub_items
        self.index = index
        self.table_head = table_head
        self.tips = tips
        self.title = title
        self.type = type

    def validate(self):
        if self.baggage_sub_items:
            for v1 in self.baggage_sub_items:
                 if v1:
                    v1.validate()
        if self.tips:
            self.tips.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['baggage_sub_items'] = []
        if self.baggage_sub_items is not None:
            for k1 in self.baggage_sub_items:
                result['baggage_sub_items'].append(k1.to_map() if k1 else None)

        if self.index is not None:
            result['index'] = self.index

        if self.table_head is not None:
            result['table_head'] = self.table_head

        if self.tips is not None:
            result['tips'] = self.tips.to_map()

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baggage_sub_items = []
        if m.get('baggage_sub_items') is not None:
            for k1 in m.get('baggage_sub_items'):
                temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetailsBaggageSubItems()
                self.baggage_sub_items.append(temp_model.from_map(k1))

        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('table_head') is not None:
            self.table_head = m.get('table_head')

        if m.get('tips') is not None:
            temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetailsTips()
            self.tips = temp_model.from_map(m.get('tips'))

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetailsTips(DaraModel):
    def __init__(
        self,
        logo: str = None,
        tips_desc: str = None,
        tips_image: str = None,
    ):
        self.logo = logo
        self.tips_desc = tips_desc
        self.tips_image = tips_image

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logo is not None:
            result['logo'] = self.logo

        if self.tips_desc is not None:
            result['tips_desc'] = self.tips_desc

        if self.tips_image is not None:
            result['tips_image'] = self.tips_image

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logo') is not None:
            self.logo = m.get('logo')

        if m.get('tips_desc') is not None:
            self.tips_desc = m.get('tips_desc')

        if m.get('tips_image') is not None:
            self.tips_image = m.get('tips_image')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetailsBaggageSubItems(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, Any] = None,
        baggage_sub_content_visualizes: List[main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetailsBaggageSubItemsBaggageSubContentVisualizes] = None,
        baggage_sub_contents: List[main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetailsBaggageSubItemsBaggageSubContents] = None,
        content: str = None,
        is_struct: bool = None,
        ptc: str = None,
        title: str = None,
    ):
        # attributes
        self.attributes = attributes
        self.baggage_sub_content_visualizes = baggage_sub_content_visualizes
        self.baggage_sub_contents = baggage_sub_contents
        self.content = content
        self.is_struct = is_struct
        self.ptc = ptc
        self.title = title

    def validate(self):
        if self.baggage_sub_content_visualizes:
            for v1 in self.baggage_sub_content_visualizes:
                 if v1:
                    v1.validate()
        if self.baggage_sub_contents:
            for v1 in self.baggage_sub_contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['attributes'] = self.attributes

        result['baggage_sub_content_visualizes'] = []
        if self.baggage_sub_content_visualizes is not None:
            for k1 in self.baggage_sub_content_visualizes:
                result['baggage_sub_content_visualizes'].append(k1.to_map() if k1 else None)

        result['baggage_sub_contents'] = []
        if self.baggage_sub_contents is not None:
            for k1 in self.baggage_sub_contents:
                result['baggage_sub_contents'].append(k1.to_map() if k1 else None)

        if self.content is not None:
            result['content'] = self.content

        if self.is_struct is not None:
            result['is_struct'] = self.is_struct

        if self.ptc is not None:
            result['ptc'] = self.ptc

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')

        self.baggage_sub_content_visualizes = []
        if m.get('baggage_sub_content_visualizes') is not None:
            for k1 in m.get('baggage_sub_content_visualizes'):
                temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetailsBaggageSubItemsBaggageSubContentVisualizes()
                self.baggage_sub_content_visualizes.append(temp_model.from_map(k1))

        self.baggage_sub_contents = []
        if m.get('baggage_sub_contents') is not None:
            for k1 in m.get('baggage_sub_contents'):
                temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetailsBaggageSubItemsBaggageSubContents()
                self.baggage_sub_contents.append(temp_model.from_map(k1))

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('is_struct') is not None:
            self.is_struct = m.get('is_struct')

        if m.get('ptc') is not None:
            self.ptc = m.get('ptc')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetailsBaggageSubItemsBaggageSubContents(DaraModel):
    def __init__(
        self,
        baggage_desc: str = None,
        icon: str = None,
        style: int = None,
        sub_title: str = None,
    ):
        self.baggage_desc = baggage_desc
        self.icon = icon
        self.style = style
        self.sub_title = sub_title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baggage_desc is not None:
            result['baggage_desc'] = self.baggage_desc

        if self.icon is not None:
            result['icon'] = self.icon

        if self.style is not None:
            result['style'] = self.style

        if self.sub_title is not None:
            result['sub_title'] = self.sub_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baggage_desc') is not None:
            self.baggage_desc = m.get('baggage_desc')

        if m.get('icon') is not None:
            self.icon = m.get('icon')

        if m.get('style') is not None:
            self.style = m.get('style')

        if m.get('sub_title') is not None:
            self.sub_title = m.get('sub_title')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetailsBaggageSubItemsBaggageSubContentVisualizes(DaraModel):
    def __init__(
        self,
        baggage_desc: List[str] = None,
        baggage_sub_content_type: int = None,
        description: main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetailsBaggageSubItemsBaggageSubContentVisualizesDescription = None,
        image_do: main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetailsBaggageSubItemsBaggageSubContentVisualizesImageDO = None,
        is_highlight: bool = None,
        sub_title: str = None,
    ):
        self.baggage_desc = baggage_desc
        self.baggage_sub_content_type = baggage_sub_content_type
        self.description = description
        self.image_do = image_do
        self.is_highlight = is_highlight
        self.sub_title = sub_title

    def validate(self):
        if self.description:
            self.description.validate()
        if self.image_do:
            self.image_do.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baggage_desc is not None:
            result['baggage_desc'] = self.baggage_desc

        if self.baggage_sub_content_type is not None:
            result['baggage_sub_content_type'] = self.baggage_sub_content_type

        if self.description is not None:
            result['description'] = self.description.to_map()

        if self.image_do is not None:
            result['imageDO'] = self.image_do.to_map()

        if self.is_highlight is not None:
            result['is_highlight'] = self.is_highlight

        if self.sub_title is not None:
            result['subTitle'] = self.sub_title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('baggage_desc') is not None:
            self.baggage_desc = m.get('baggage_desc')

        if m.get('baggage_sub_content_type') is not None:
            self.baggage_sub_content_type = m.get('baggage_sub_content_type')

        if m.get('description') is not None:
            temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetailsBaggageSubItemsBaggageSubContentVisualizesDescription()
            self.description = temp_model.from_map(m.get('description'))

        if m.get('imageDO') is not None:
            temp_model = main_models.TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetailsBaggageSubItemsBaggageSubContentVisualizesImageDO()
            self.image_do = temp_model.from_map(m.get('imageDO'))

        if m.get('is_highlight') is not None:
            self.is_highlight = m.get('is_highlight')

        if m.get('subTitle') is not None:
            self.sub_title = m.get('subTitle')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetailsBaggageSubItemsBaggageSubContentVisualizesImageDO(DaraModel):
    def __init__(
        self,
        image: str = None,
        largest: str = None,
        middle: str = None,
        smallest: str = None,
    ):
        self.image = image
        self.largest = largest
        self.middle = middle
        self.smallest = smallest

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image is not None:
            result['image'] = self.image

        if self.largest is not None:
            result['largest'] = self.largest

        if self.middle is not None:
            result['middle'] = self.middle

        if self.smallest is not None:
            result['smallest'] = self.smallest

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('largest') is not None:
            self.largest = m.get('largest')

        if m.get('middle') is not None:
            self.middle = m.get('middle')

        if m.get('smallest') is not None:
            self.smallest = m.get('smallest')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListCabinListChangeOtaItemRuleRqBaggageDetailsBaggageSubItemsBaggageSubContentVisualizesDescription(DaraModel):
    def __init__(
        self,
        desc: str = None,
        icon: str = None,
        image: str = None,
        title: str = None,
    ):
        self.desc = desc
        self.icon = icon
        self.image = image
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['desc'] = self.desc

        if self.icon is not None:
            result['icon'] = self.icon

        if self.image is not None:
            result['image'] = self.image

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('icon') is not None:
            self.icon = m.get('icon')

        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListArrAirportInfo(DaraModel):
    def __init__(
        self,
        airport_code: str = None,
        airport_name: str = None,
        city_code: str = None,
        city_name: str = None,
        terminal: str = None,
    ):
        self.airport_code = airport_code
        self.airport_name = airport_name
        self.city_code = city_code
        self.city_name = city_name
        self.terminal = terminal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airport_code is not None:
            result['airport_code'] = self.airport_code

        if self.airport_name is not None:
            result['airport_name'] = self.airport_name

        if self.city_code is not None:
            result['city_code'] = self.city_code

        if self.city_name is not None:
            result['city_name'] = self.city_name

        if self.terminal is not None:
            result['terminal'] = self.terminal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airport_code') is not None:
            self.airport_code = m.get('airport_code')

        if m.get('airport_name') is not None:
            self.airport_name = m.get('airport_name')

        if m.get('city_code') is not None:
            self.city_code = m.get('city_code')

        if m.get('city_name') is not None:
            self.city_name = m.get('city_name')

        if m.get('terminal') is not None:
            self.terminal = m.get('terminal')

        return self

class TicketChangingEnquiryResponseBodyModuleFlightInfoListAirlineInfo(DaraModel):
    def __init__(
        self,
        airline_code: str = None,
        airline_name: str = None,
        airline_simple_name: str = None,
    ):
        self.airline_code = airline_code
        self.airline_name = airline_name
        self.airline_simple_name = airline_simple_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.airline_code is not None:
            result['airline_code'] = self.airline_code

        if self.airline_name is not None:
            result['airline_name'] = self.airline_name

        if self.airline_simple_name is not None:
            result['airline_simple_name'] = self.airline_simple_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('airline_code') is not None:
            self.airline_code = m.get('airline_code')

        if m.get('airline_name') is not None:
            self.airline_name = m.get('airline_name')

        if m.get('airline_simple_name') is not None:
            self.airline_simple_name = m.get('airline_simple_name')

        return self

