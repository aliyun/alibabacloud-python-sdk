# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class RefundDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        data: main_models.RefundDetailResponseBodyData = None,
        error_code: str = None,
        error_data: Any = None,
        error_msg: str = None,
        status: int = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The data returned for a successful request.
        self.data = data
        # The business error code.
        self.error_code = error_code
        # The data returned with the error.
        self.error_data = error_data
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code. The value is always 200 for successful requests.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.error_code is not None:
            result['error_code'] = self.error_code

        if self.error_data is not None:
            result['error_data'] = self.error_data

        if self.error_msg is not None:
            result['error_msg'] = self.error_msg

        if self.status is not None:
            result['status'] = self.status

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('data') is not None:
            temp_model = main_models.RefundDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')

        if m.get('error_data') is not None:
            self.error_data = m.get('error_data')

        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class RefundDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        contain_multi_refund: bool = None,
        multi_refund_details: List[main_models.RefundDetailResponseBodyDataMultiRefundDetails] = None,
        order_num: int = None,
        passenger_refund_details: List[main_models.RefundDetailResponseBodyDataPassengerRefundDetails] = None,
        pay_success_utc_time: int = None,
        refund_attachment_urls: List[str] = None,
        refund_journeys: List[main_models.RefundDetailResponseBodyDataRefundJourneys] = None,
        refund_order_num: int = None,
        refund_reason: str = None,
        refund_type: int = None,
        refuse_reason: str = None,
        status: int = None,
        transaction_no: str = None,
        utc_create_time: int = None,
    ):
        # Indicates whether the refund contains a supplementary refund.
        self.contain_multi_refund = contain_multi_refund
        # The list of supplementary refund details associated with the initial refund.
        self.multi_refund_details = multi_refund_details
        # The order number.
        self.order_num = order_num
        # The list of passenger-level refund details.
        self.passenger_refund_details = passenger_refund_details
        # The actual refund time, in UTC timestamp.
        self.pay_success_utc_time = pay_success_utc_time
        # The list of attachment URLs for medical refund requests.
        self.refund_attachment_urls = refund_attachment_urls
        # The journeys included in the refund.
        self.refund_journeys = refund_journeys
        # The refund order number.
        self.refund_order_num = refund_order_num
        # The reason for the refund request.
        self.refund_reason = refund_reason
        # The refund request type. Valid values:
        # - 2: voluntary request.
        # - 5: airline-initiated reasons such as flight delay, cancellation, or schedule change.
        # - 6: medical reasons with a certificate from a Grade II Class A hospital or above.
        # - 7: involuntary definitive emergency guidance.
        # - 100: involuntary non-definitive emergency.
        self.refund_type = refund_type
        # The reason for rejecting the refund request.
        self.refuse_reason = refuse_reason
        # The refund order status. Valid values:
        # - 0: refund requested.
        # - 1: refund being processed.
        # - 2: refund failed.
        # - 3: refund succeeded.
        self.status = status
        # The transaction serial number.
        self.transaction_no = transaction_no
        # The creation time of the refund order, in UTC timestamp.
        self.utc_create_time = utc_create_time

    def validate(self):
        if self.multi_refund_details:
            for v1 in self.multi_refund_details:
                 if v1:
                    v1.validate()
        if self.passenger_refund_details:
            for v1 in self.passenger_refund_details:
                 if v1:
                    v1.validate()
        if self.refund_journeys:
            for v1 in self.refund_journeys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contain_multi_refund is not None:
            result['contain_multi_refund'] = self.contain_multi_refund

        result['multi_refund_details'] = []
        if self.multi_refund_details is not None:
            for k1 in self.multi_refund_details:
                result['multi_refund_details'].append(k1.to_map() if k1 else None)

        if self.order_num is not None:
            result['order_num'] = self.order_num

        result['passenger_refund_details'] = []
        if self.passenger_refund_details is not None:
            for k1 in self.passenger_refund_details:
                result['passenger_refund_details'].append(k1.to_map() if k1 else None)

        if self.pay_success_utc_time is not None:
            result['pay_success_utc_time'] = self.pay_success_utc_time

        if self.refund_attachment_urls is not None:
            result['refund_attachment_urls'] = self.refund_attachment_urls

        result['refund_journeys'] = []
        if self.refund_journeys is not None:
            for k1 in self.refund_journeys:
                result['refund_journeys'].append(k1.to_map() if k1 else None)

        if self.refund_order_num is not None:
            result['refund_order_num'] = self.refund_order_num

        if self.refund_reason is not None:
            result['refund_reason'] = self.refund_reason

        if self.refund_type is not None:
            result['refund_type'] = self.refund_type

        if self.refuse_reason is not None:
            result['refuse_reason'] = self.refuse_reason

        if self.status is not None:
            result['status'] = self.status

        if self.transaction_no is not None:
            result['transaction_no'] = self.transaction_no

        if self.utc_create_time is not None:
            result['utc_create_time'] = self.utc_create_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contain_multi_refund') is not None:
            self.contain_multi_refund = m.get('contain_multi_refund')

        self.multi_refund_details = []
        if m.get('multi_refund_details') is not None:
            for k1 in m.get('multi_refund_details'):
                temp_model = main_models.RefundDetailResponseBodyDataMultiRefundDetails()
                self.multi_refund_details.append(temp_model.from_map(k1))

        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')

        self.passenger_refund_details = []
        if m.get('passenger_refund_details') is not None:
            for k1 in m.get('passenger_refund_details'):
                temp_model = main_models.RefundDetailResponseBodyDataPassengerRefundDetails()
                self.passenger_refund_details.append(temp_model.from_map(k1))

        if m.get('pay_success_utc_time') is not None:
            self.pay_success_utc_time = m.get('pay_success_utc_time')

        if m.get('refund_attachment_urls') is not None:
            self.refund_attachment_urls = m.get('refund_attachment_urls')

        self.refund_journeys = []
        if m.get('refund_journeys') is not None:
            for k1 in m.get('refund_journeys'):
                temp_model = main_models.RefundDetailResponseBodyDataRefundJourneys()
                self.refund_journeys.append(temp_model.from_map(k1))

        if m.get('refund_order_num') is not None:
            self.refund_order_num = m.get('refund_order_num')

        if m.get('refund_reason') is not None:
            self.refund_reason = m.get('refund_reason')

        if m.get('refund_type') is not None:
            self.refund_type = m.get('refund_type')

        if m.get('refuse_reason') is not None:
            self.refuse_reason = m.get('refuse_reason')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('transaction_no') is not None:
            self.transaction_no = m.get('transaction_no')

        if m.get('utc_create_time') is not None:
            self.utc_create_time = m.get('utc_create_time')

        return self

class RefundDetailResponseBodyDataRefundJourneys(DaraModel):
    def __init__(
        self,
        segment_list: List[main_models.RefundDetailResponseBodyDataRefundJourneysSegmentList] = None,
        transfer_count: int = None,
    ):
        # The segment information.
        self.segment_list = segment_list
        # The number of transfers.
        self.transfer_count = transfer_count

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
        result['segment_list'] = []
        if self.segment_list is not None:
            for k1 in self.segment_list:
                result['segment_list'].append(k1.to_map() if k1 else None)

        if self.transfer_count is not None:
            result['transfer_count'] = self.transfer_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.segment_list = []
        if m.get('segment_list') is not None:
            for k1 in m.get('segment_list'):
                temp_model = main_models.RefundDetailResponseBodyDataRefundJourneysSegmentList()
                self.segment_list.append(temp_model.from_map(k1))

        if m.get('transfer_count') is not None:
            self.transfer_count = m.get('transfer_count')

        return self

class RefundDetailResponseBodyDataRefundJourneysSegmentList(DaraModel):
    def __init__(
        self,
        arrival_airport: str = None,
        arrival_city: str = None,
        arrival_terminal: str = None,
        arrival_time: str = None,
        availability: str = None,
        cabin: str = None,
        cabin_class: str = None,
        code_share: bool = None,
        departure_airport: str = None,
        departure_city: str = None,
        departure_terminal: str = None,
        departure_time: str = None,
        equip_type: str = None,
        flight_duration: int = None,
        marketing_airline: str = None,
        marketing_flight_no: str = None,
        marketing_flight_no_int: int = None,
        operating_airline: str = None,
        operating_flight_no: str = None,
        segment_id: str = None,
        stop_city_list: str = None,
        stop_quantity: int = None,
    ):
        # The three-letter IATA code of the arrival airport (uppercase).
        self.arrival_airport = arrival_airport
        # The three-letter IATA code of the arrival city (uppercase).
        self.arrival_city = arrival_city
        # The arrival terminal.
        self.arrival_terminal = arrival_terminal
        # The arrival date and time in string format (yyyy-MM-dd HH:mm:ss).
        self.arrival_time = arrival_time
        # The number of remaining seats.
        self.availability = availability
        # The cabin code.
        self.cabin = cabin
        # The cabin class.
        self.cabin_class = cabin_class
        # Indicates whether the flight is a codeshare flight.
        self.code_share = code_share
        # The three-letter IATA code of the departure airport (uppercase).
        self.departure_airport = departure_airport
        # The three-letter IATA code of the departure city (uppercase).
        self.departure_city = departure_city
        # The departure terminal.
        self.departure_terminal = departure_terminal
        # The departure date and time in string format (yyyy-MM-dd HH:mm:ss).
        self.departure_time = departure_time
        # The aircraft type.
        self.equip_type = equip_type
        # The flight duration, in minutes.
        self.flight_duration = flight_duration
        # The marketing airline code (such as HO).
        self.marketing_airline = marketing_airline
        # The marketing flight number (such as HO1295).
        self.marketing_flight_no = marketing_flight_no
        # The numeric marketing flight number (such as 1295).
        self.marketing_flight_no_int = marketing_flight_no_int
        # The operating airline code (such as CX).
        self.operating_airline = operating_airline
        # The operating flight number (such as CX601).
        self.operating_flight_no = operating_flight_no
        # The segment ID. Format: flight number + departure airport + arrival airport + departure date (MMdd).
        self.segment_id = segment_id
        # The list of stopover cities. This field has a value when stopQuantity is greater than 0. Multiple cities are separated by commas.
        self.stop_city_list = stop_city_list
        # The number of stopover cities.
        self.stop_quantity = stop_quantity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arrival_airport is not None:
            result['arrival_airport'] = self.arrival_airport

        if self.arrival_city is not None:
            result['arrival_city'] = self.arrival_city

        if self.arrival_terminal is not None:
            result['arrival_terminal'] = self.arrival_terminal

        if self.arrival_time is not None:
            result['arrival_time'] = self.arrival_time

        if self.availability is not None:
            result['availability'] = self.availability

        if self.cabin is not None:
            result['cabin'] = self.cabin

        if self.cabin_class is not None:
            result['cabin_class'] = self.cabin_class

        if self.code_share is not None:
            result['code_share'] = self.code_share

        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport

        if self.departure_city is not None:
            result['departure_city'] = self.departure_city

        if self.departure_terminal is not None:
            result['departure_terminal'] = self.departure_terminal

        if self.departure_time is not None:
            result['departure_time'] = self.departure_time

        if self.equip_type is not None:
            result['equip_type'] = self.equip_type

        if self.flight_duration is not None:
            result['flight_duration'] = self.flight_duration

        if self.marketing_airline is not None:
            result['marketing_airline'] = self.marketing_airline

        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no

        if self.marketing_flight_no_int is not None:
            result['marketing_flight_no_int'] = self.marketing_flight_no_int

        if self.operating_airline is not None:
            result['operating_airline'] = self.operating_airline

        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no

        if self.segment_id is not None:
            result['segment_id'] = self.segment_id

        if self.stop_city_list is not None:
            result['stop_city_list'] = self.stop_city_list

        if self.stop_quantity is not None:
            result['stop_quantity'] = self.stop_quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')

        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')

        if m.get('arrival_terminal') is not None:
            self.arrival_terminal = m.get('arrival_terminal')

        if m.get('arrival_time') is not None:
            self.arrival_time = m.get('arrival_time')

        if m.get('availability') is not None:
            self.availability = m.get('availability')

        if m.get('cabin') is not None:
            self.cabin = m.get('cabin')

        if m.get('cabin_class') is not None:
            self.cabin_class = m.get('cabin_class')

        if m.get('code_share') is not None:
            self.code_share = m.get('code_share')

        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')

        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')

        if m.get('departure_terminal') is not None:
            self.departure_terminal = m.get('departure_terminal')

        if m.get('departure_time') is not None:
            self.departure_time = m.get('departure_time')

        if m.get('equip_type') is not None:
            self.equip_type = m.get('equip_type')

        if m.get('flight_duration') is not None:
            self.flight_duration = m.get('flight_duration')

        if m.get('marketing_airline') is not None:
            self.marketing_airline = m.get('marketing_airline')

        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')

        if m.get('marketing_flight_no_int') is not None:
            self.marketing_flight_no_int = m.get('marketing_flight_no_int')

        if m.get('operating_airline') is not None:
            self.operating_airline = m.get('operating_airline')

        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')

        if m.get('segment_id') is not None:
            self.segment_id = m.get('segment_id')

        if m.get('stop_city_list') is not None:
            self.stop_city_list = m.get('stop_city_list')

        if m.get('stop_quantity') is not None:
            self.stop_quantity = m.get('stop_quantity')

        return self

class RefundDetailResponseBodyDataPassengerRefundDetails(DaraModel):
    def __init__(
        self,
        passenger: main_models.RefundDetailResponseBodyDataPassengerRefundDetailsPassenger = None,
        refund_fee: main_models.RefundDetailResponseBodyDataPassengerRefundDetailsRefundFee = None,
    ):
        # The passenger information for the refund.
        self.passenger = passenger
        # The refund fee breakdown.
        self.refund_fee = refund_fee

    def validate(self):
        if self.passenger:
            self.passenger.validate()
        if self.refund_fee:
            self.refund_fee.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.passenger is not None:
            result['passenger'] = self.passenger.to_map()

        if self.refund_fee is not None:
            result['refund_fee'] = self.refund_fee.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('passenger') is not None:
            temp_model = main_models.RefundDetailResponseBodyDataPassengerRefundDetailsPassenger()
            self.passenger = temp_model.from_map(m.get('passenger'))

        if m.get('refund_fee') is not None:
            temp_model = main_models.RefundDetailResponseBodyDataPassengerRefundDetailsRefundFee()
            self.refund_fee = temp_model.from_map(m.get('refund_fee'))

        return self

class RefundDetailResponseBodyDataPassengerRefundDetailsRefundFee(DaraModel):
    def __init__(
        self,
        already_used_total_fee: float = None,
        ancillary_refund_to_buyer_money: float = None,
        modify_refund_to_buyer_money: float = None,
        non_refundable_change_service_fee: float = None,
        non_refundable_change_upgrade_fee: float = None,
        non_refundable_tax_fee: float = None,
        non_refundable_ticket_fee: float = None,
        refund_to_buyer_money: float = None,
        suez_service_fee: float = None,
    ):
        # The total price of already used tickets.
        self.already_used_total_fee = already_used_total_fee
        self.ancillary_refund_to_buyer_money = ancillary_refund_to_buyer_money
        # The refundable amount to the buyer from rebooking.
        self.modify_refund_to_buyer_money = modify_refund_to_buyer_money
        # The non-refundable rebooking service fee.
        self.non_refundable_change_service_fee = non_refundable_change_service_fee
        # The non-refundable cabin upgrade service fee.
        self.non_refundable_change_upgrade_fee = non_refundable_change_upgrade_fee
        # The non-refundable tax amount, which is the tax refund service fee.
        self.non_refundable_tax_fee = non_refundable_tax_fee
        # The non-refundable ticket amount, which is the ticket refund service fee.
        self.non_refundable_ticket_fee = non_refundable_ticket_fee
        # The refundable amount to the buyer from the original ticket (ticket price + taxes - ticket refund service fee - tax refund service fee - total price of already used tickets).
        self.refund_to_buyer_money = refund_to_buyer_money
        self.suez_service_fee = suez_service_fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.already_used_total_fee is not None:
            result['already_used_total_fee'] = self.already_used_total_fee

        if self.ancillary_refund_to_buyer_money is not None:
            result['ancillary_refund_to_buyer_money'] = self.ancillary_refund_to_buyer_money

        if self.modify_refund_to_buyer_money is not None:
            result['modify_refund_to_buyer_money'] = self.modify_refund_to_buyer_money

        if self.non_refundable_change_service_fee is not None:
            result['non_refundable_change_service_fee'] = self.non_refundable_change_service_fee

        if self.non_refundable_change_upgrade_fee is not None:
            result['non_refundable_change_upgrade_fee'] = self.non_refundable_change_upgrade_fee

        if self.non_refundable_tax_fee is not None:
            result['non_refundable_tax_fee'] = self.non_refundable_tax_fee

        if self.non_refundable_ticket_fee is not None:
            result['non_refundable_ticket_fee'] = self.non_refundable_ticket_fee

        if self.refund_to_buyer_money is not None:
            result['refund_to_buyer_money'] = self.refund_to_buyer_money

        if self.suez_service_fee is not None:
            result['suez_service_fee'] = self.suez_service_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('already_used_total_fee') is not None:
            self.already_used_total_fee = m.get('already_used_total_fee')

        if m.get('ancillary_refund_to_buyer_money') is not None:
            self.ancillary_refund_to_buyer_money = m.get('ancillary_refund_to_buyer_money')

        if m.get('modify_refund_to_buyer_money') is not None:
            self.modify_refund_to_buyer_money = m.get('modify_refund_to_buyer_money')

        if m.get('non_refundable_change_service_fee') is not None:
            self.non_refundable_change_service_fee = m.get('non_refundable_change_service_fee')

        if m.get('non_refundable_change_upgrade_fee') is not None:
            self.non_refundable_change_upgrade_fee = m.get('non_refundable_change_upgrade_fee')

        if m.get('non_refundable_tax_fee') is not None:
            self.non_refundable_tax_fee = m.get('non_refundable_tax_fee')

        if m.get('non_refundable_ticket_fee') is not None:
            self.non_refundable_ticket_fee = m.get('non_refundable_ticket_fee')

        if m.get('refund_to_buyer_money') is not None:
            self.refund_to_buyer_money = m.get('refund_to_buyer_money')

        if m.get('suez_service_fee') is not None:
            self.suez_service_fee = m.get('suez_service_fee')

        return self

class RefundDetailResponseBodyDataPassengerRefundDetailsPassenger(DaraModel):
    def __init__(
        self,
        document: str = None,
        first_name: str = None,
        last_name: str = None,
    ):
        # The document number.
        self.document = document
        # The first name of the passenger.
        self.first_name = first_name
        # The last name of the passenger.
        self.last_name = last_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document is not None:
            result['document'] = self.document

        if self.first_name is not None:
            result['first_name'] = self.first_name

        if self.last_name is not None:
            result['last_name'] = self.last_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('document') is not None:
            self.document = m.get('document')

        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')

        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')

        return self

class RefundDetailResponseBodyDataMultiRefundDetails(DaraModel):
    def __init__(
        self,
        multi_refund_order_num: int = None,
        multi_refund_transaction_no: str = None,
        passenger_multi_refund_details: List[main_models.RefundDetailResponseBodyDataMultiRefundDetailsPassengerMultiRefundDetails] = None,
    ):
        # The refund order number of the supplementary refund.
        self.multi_refund_order_num = multi_refund_order_num
        # The transaction serial number of the supplementary refund.
        self.multi_refund_transaction_no = multi_refund_transaction_no
        # The passenger-level supplementary refund details.
        self.passenger_multi_refund_details = passenger_multi_refund_details

    def validate(self):
        if self.passenger_multi_refund_details:
            for v1 in self.passenger_multi_refund_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.multi_refund_order_num is not None:
            result['multi_refund_order_num'] = self.multi_refund_order_num

        if self.multi_refund_transaction_no is not None:
            result['multi_refund_transaction_no'] = self.multi_refund_transaction_no

        result['passenger_multi_refund_details'] = []
        if self.passenger_multi_refund_details is not None:
            for k1 in self.passenger_multi_refund_details:
                result['passenger_multi_refund_details'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('multi_refund_order_num') is not None:
            self.multi_refund_order_num = m.get('multi_refund_order_num')

        if m.get('multi_refund_transaction_no') is not None:
            self.multi_refund_transaction_no = m.get('multi_refund_transaction_no')

        self.passenger_multi_refund_details = []
        if m.get('passenger_multi_refund_details') is not None:
            for k1 in m.get('passenger_multi_refund_details'):
                temp_model = main_models.RefundDetailResponseBodyDataMultiRefundDetailsPassengerMultiRefundDetails()
                self.passenger_multi_refund_details.append(temp_model.from_map(k1))

        return self

class RefundDetailResponseBodyDataMultiRefundDetailsPassengerMultiRefundDetails(DaraModel):
    def __init__(
        self,
        change_order_refund_fee: float = None,
        original_order_refund_fee: float = None,
        passenger: main_models.RefundDetailResponseBodyDataMultiRefundDetailsPassengerMultiRefundDetailsPassenger = None,
    ):
        # The supplementary refund amount from the rebooking order.
        self.change_order_refund_fee = change_order_refund_fee
        # The supplementary refund amount from the original order.
        self.original_order_refund_fee = original_order_refund_fee
        # The passenger for the refund.
        self.passenger = passenger

    def validate(self):
        if self.passenger:
            self.passenger.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_order_refund_fee is not None:
            result['change_order_refund_fee'] = self.change_order_refund_fee

        if self.original_order_refund_fee is not None:
            result['original_order_refund_fee'] = self.original_order_refund_fee

        if self.passenger is not None:
            result['passenger'] = self.passenger.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change_order_refund_fee') is not None:
            self.change_order_refund_fee = m.get('change_order_refund_fee')

        if m.get('original_order_refund_fee') is not None:
            self.original_order_refund_fee = m.get('original_order_refund_fee')

        if m.get('passenger') is not None:
            temp_model = main_models.RefundDetailResponseBodyDataMultiRefundDetailsPassengerMultiRefundDetailsPassenger()
            self.passenger = temp_model.from_map(m.get('passenger'))

        return self

class RefundDetailResponseBodyDataMultiRefundDetailsPassengerMultiRefundDetailsPassenger(DaraModel):
    def __init__(
        self,
        document: str = None,
        first_name: str = None,
        last_name: str = None,
    ):
        # The document number.
        self.document = document
        # The first name of the passenger.
        self.first_name = first_name
        # The last name of the passenger.
        self.last_name = last_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document is not None:
            result['document'] = self.document

        if self.first_name is not None:
            result['first_name'] = self.first_name

        if self.last_name is not None:
            result['last_name'] = self.last_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('document') is not None:
            self.document = m.get('document')

        if m.get('first_name') is not None:
            self.first_name = m.get('first_name')

        if m.get('last_name') is not None:
            self.last_name = m.get('last_name')

        return self

