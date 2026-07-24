# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class ChangeDetailListOfOrderNumResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        data: main_models.ChangeDetailListOfOrderNumResponseBodyData = None,
        error_code: str = None,
        error_data: Any = None,
        error_msg: str = None,
        status: int = None,
        success: bool = None,
    ):
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
            temp_model = main_models.ChangeDetailListOfOrderNumResponseBodyData()
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

class ChangeDetailListOfOrderNumResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ChangeDetailListOfOrderNumResponseBodyDataList] = None,
        pagination: main_models.ChangeDetailListOfOrderNumResponseBodyDataPagination = None,
    ):
        # The data list.
        self.list = list
        # The pagination information.
        self.pagination = pagination

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()
        if self.pagination:
            self.pagination.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['list'] = []
        if self.list is not None:
            for k1 in self.list:
                result['list'].append(k1.to_map() if k1 else None)

        if self.pagination is not None:
            result['pagination'] = self.pagination.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k1 in m.get('list'):
                temp_model = main_models.ChangeDetailListOfOrderNumResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('pagination') is not None:
            temp_model = main_models.ChangeDetailListOfOrderNumResponseBodyDataPagination()
            self.pagination = temp_model.from_map(m.get('pagination'))

        return self

class ChangeDetailListOfOrderNumResponseBodyDataPagination(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The number of records per page.
        self.page_size = page_size
        # The total number of records.
        self.total_count = total_count
        # The total number of pages.
        self.total_page = total_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['current_page'] = self.current_page

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.total_count is not None:
            result['total_count'] = self.total_count

        if self.total_page is not None:
            result['total_page'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current_page') is not None:
            self.current_page = m.get('current_page')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')

        if m.get('total_page') is not None:
            self.total_page = m.get('total_page')

        return self

class ChangeDetailListOfOrderNumResponseBodyDataList(DaraModel):
    def __init__(
        self,
        change_fee_details: List[main_models.ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetails] = None,
        change_order_num: int = None,
        change_passengers: List[main_models.ChangeDetailListOfOrderNumResponseBodyDataListChangePassengers] = None,
        change_reason_type: int = None,
        changed_journeys: List[main_models.ChangeDetailListOfOrderNumResponseBodyDataListChangedJourneys] = None,
        close_reason: str = None,
        close_utc_time: int = None,
        contact: main_models.ChangeDetailListOfOrderNumResponseBodyDataListContact = None,
        create_utc_time: int = None,
        last_confirm_utc_time: int = None,
        last_journeys: List[main_models.ChangeDetailListOfOrderNumResponseBodyDataListLastJourneys] = None,
        order_num: int = None,
        order_status: int = None,
        original_journeys: List[main_models.ChangeDetailListOfOrderNumResponseBodyDataListOriginalJourneys] = None,
        pay_status: int = None,
        pay_success_utc_time: int = None,
        total_amount: float = None,
        transaction_no: str = None,
    ):
        # The change fee details at the passenger level.
        self.change_fee_details = change_fee_details
        # The change order number.
        self.change_order_num = change_order_num
        # The list of passengers for the change order.
        self.change_passengers = change_passengers
        # The change reason type. Valid values:
        # - 0: voluntary date change
        # - 1: flight schedule change or flight cancellation
        # - 2: change due to epidemic.
        self.change_reason_type = change_reason_type
        # The journeys after the change.
        self.changed_journeys = changed_journeys
        # The reason for closing the change order.
        self.close_reason = close_reason
        # The time when the order was closed, in UTC timestamp.
        self.close_utc_time = close_utc_time
        # The contact information for the change order.
        self.contact = contact
        # The creation time of the change order, in UTC timestamp.
        self.create_utc_time = create_utc_time
        # The latest payment deadline for the buyer, in UTC timestamp.
        self.last_confirm_utc_time = last_confirm_utc_time
        # The journeys from the previous change.
        self.last_journeys = last_journeys
        # The order number.
        self.order_num = order_num
        # The change order status. Valid values:
        # - 0: initial state
        # - 1: pending payment
        # - 2: payment successful
        # - 3: change successful
        # - 4: change closed.
        self.order_status = order_status
        # The original journeys.
        self.original_journeys = original_journeys
        # The payment status. Valid values:
        # - 0: initial state
        # - 1: pending payment
        # - 2: payment successful
        # - 3: transaction transfer successful
        # - 4: paid order closed successfully
        # - 5: unpaid order closed successfully.
        self.pay_status = pay_status
        # The time when the buyer completed the payment, in UTC timestamp.
        self.pay_success_utc_time = pay_success_utc_time
        # The total payment amount of the change order.
        self.total_amount = total_amount
        # The transaction number.
        self.transaction_no = transaction_no

    def validate(self):
        if self.change_fee_details:
            for v1 in self.change_fee_details:
                 if v1:
                    v1.validate()
        if self.change_passengers:
            for v1 in self.change_passengers:
                 if v1:
                    v1.validate()
        if self.changed_journeys:
            for v1 in self.changed_journeys:
                 if v1:
                    v1.validate()
        if self.contact:
            self.contact.validate()
        if self.last_journeys:
            for v1 in self.last_journeys:
                 if v1:
                    v1.validate()
        if self.original_journeys:
            for v1 in self.original_journeys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['change_fee_details'] = []
        if self.change_fee_details is not None:
            for k1 in self.change_fee_details:
                result['change_fee_details'].append(k1.to_map() if k1 else None)

        if self.change_order_num is not None:
            result['change_order_num'] = self.change_order_num

        result['change_passengers'] = []
        if self.change_passengers is not None:
            for k1 in self.change_passengers:
                result['change_passengers'].append(k1.to_map() if k1 else None)

        if self.change_reason_type is not None:
            result['change_reason_type'] = self.change_reason_type

        result['changed_journeys'] = []
        if self.changed_journeys is not None:
            for k1 in self.changed_journeys:
                result['changed_journeys'].append(k1.to_map() if k1 else None)

        if self.close_reason is not None:
            result['close_reason'] = self.close_reason

        if self.close_utc_time is not None:
            result['close_utc_time'] = self.close_utc_time

        if self.contact is not None:
            result['contact'] = self.contact.to_map()

        if self.create_utc_time is not None:
            result['create_utc_time'] = self.create_utc_time

        if self.last_confirm_utc_time is not None:
            result['last_confirm_utc_time'] = self.last_confirm_utc_time

        result['last_journeys'] = []
        if self.last_journeys is not None:
            for k1 in self.last_journeys:
                result['last_journeys'].append(k1.to_map() if k1 else None)

        if self.order_num is not None:
            result['order_num'] = self.order_num

        if self.order_status is not None:
            result['order_status'] = self.order_status

        result['original_journeys'] = []
        if self.original_journeys is not None:
            for k1 in self.original_journeys:
                result['original_journeys'].append(k1.to_map() if k1 else None)

        if self.pay_status is not None:
            result['pay_status'] = self.pay_status

        if self.pay_success_utc_time is not None:
            result['pay_success_utc_time'] = self.pay_success_utc_time

        if self.total_amount is not None:
            result['total_amount'] = self.total_amount

        if self.transaction_no is not None:
            result['transaction_no'] = self.transaction_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.change_fee_details = []
        if m.get('change_fee_details') is not None:
            for k1 in m.get('change_fee_details'):
                temp_model = main_models.ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetails()
                self.change_fee_details.append(temp_model.from_map(k1))

        if m.get('change_order_num') is not None:
            self.change_order_num = m.get('change_order_num')

        self.change_passengers = []
        if m.get('change_passengers') is not None:
            for k1 in m.get('change_passengers'):
                temp_model = main_models.ChangeDetailListOfOrderNumResponseBodyDataListChangePassengers()
                self.change_passengers.append(temp_model.from_map(k1))

        if m.get('change_reason_type') is not None:
            self.change_reason_type = m.get('change_reason_type')

        self.changed_journeys = []
        if m.get('changed_journeys') is not None:
            for k1 in m.get('changed_journeys'):
                temp_model = main_models.ChangeDetailListOfOrderNumResponseBodyDataListChangedJourneys()
                self.changed_journeys.append(temp_model.from_map(k1))

        if m.get('close_reason') is not None:
            self.close_reason = m.get('close_reason')

        if m.get('close_utc_time') is not None:
            self.close_utc_time = m.get('close_utc_time')

        if m.get('contact') is not None:
            temp_model = main_models.ChangeDetailListOfOrderNumResponseBodyDataListContact()
            self.contact = temp_model.from_map(m.get('contact'))

        if m.get('create_utc_time') is not None:
            self.create_utc_time = m.get('create_utc_time')

        if m.get('last_confirm_utc_time') is not None:
            self.last_confirm_utc_time = m.get('last_confirm_utc_time')

        self.last_journeys = []
        if m.get('last_journeys') is not None:
            for k1 in m.get('last_journeys'):
                temp_model = main_models.ChangeDetailListOfOrderNumResponseBodyDataListLastJourneys()
                self.last_journeys.append(temp_model.from_map(k1))

        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')

        if m.get('order_status') is not None:
            self.order_status = m.get('order_status')

        self.original_journeys = []
        if m.get('original_journeys') is not None:
            for k1 in m.get('original_journeys'):
                temp_model = main_models.ChangeDetailListOfOrderNumResponseBodyDataListOriginalJourneys()
                self.original_journeys.append(temp_model.from_map(k1))

        if m.get('pay_status') is not None:
            self.pay_status = m.get('pay_status')

        if m.get('pay_success_utc_time') is not None:
            self.pay_success_utc_time = m.get('pay_success_utc_time')

        if m.get('total_amount') is not None:
            self.total_amount = m.get('total_amount')

        if m.get('transaction_no') is not None:
            self.transaction_no = m.get('transaction_no')

        return self

class ChangeDetailListOfOrderNumResponseBodyDataListOriginalJourneys(DaraModel):
    def __init__(
        self,
        segment_list: List[main_models.ChangeDetailListOfOrderNumResponseBodyDataListOriginalJourneysSegmentList] = None,
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
                temp_model = main_models.ChangeDetailListOfOrderNumResponseBodyDataListOriginalJourneysSegmentList()
                self.segment_list.append(temp_model.from_map(k1))

        if m.get('transfer_count') is not None:
            self.transfer_count = m.get('transfer_count')

        return self

class ChangeDetailListOfOrderNumResponseBodyDataListOriginalJourneysSegmentList(DaraModel):
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
        # Indicates whether this is a codeshare flight.
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
        # The flight duration in minutes.
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

class ChangeDetailListOfOrderNumResponseBodyDataListLastJourneys(DaraModel):
    def __init__(
        self,
        segment_list: List[main_models.ChangeDetailListOfOrderNumResponseBodyDataListLastJourneysSegmentList] = None,
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
                temp_model = main_models.ChangeDetailListOfOrderNumResponseBodyDataListLastJourneysSegmentList()
                self.segment_list.append(temp_model.from_map(k1))

        if m.get('transfer_count') is not None:
            self.transfer_count = m.get('transfer_count')

        return self

class ChangeDetailListOfOrderNumResponseBodyDataListLastJourneysSegmentList(DaraModel):
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
        # Indicates whether this is a codeshare flight.
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
        # The flight duration in minutes.
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

class ChangeDetailListOfOrderNumResponseBodyDataListContact(DaraModel):
    def __init__(
        self,
        email: str = None,
        mobile_country_code: str = None,
        mobile_phone_num: str = None,
    ):
        # The email address.
        self.email = email
        # The country calling code.
        self.mobile_country_code = mobile_country_code
        # The mobile phone number of the contact.
        self.mobile_phone_num = mobile_phone_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['email'] = self.email

        if self.mobile_country_code is not None:
            result['mobile_country_code'] = self.mobile_country_code

        if self.mobile_phone_num is not None:
            result['mobile_phone_num'] = self.mobile_phone_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('mobile_country_code') is not None:
            self.mobile_country_code = m.get('mobile_country_code')

        if m.get('mobile_phone_num') is not None:
            self.mobile_phone_num = m.get('mobile_phone_num')

        return self

class ChangeDetailListOfOrderNumResponseBodyDataListChangedJourneys(DaraModel):
    def __init__(
        self,
        segment_list: List[main_models.ChangeDetailListOfOrderNumResponseBodyDataListChangedJourneysSegmentList] = None,
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
                temp_model = main_models.ChangeDetailListOfOrderNumResponseBodyDataListChangedJourneysSegmentList()
                self.segment_list.append(temp_model.from_map(k1))

        if m.get('transfer_count') is not None:
            self.transfer_count = m.get('transfer_count')

        return self

class ChangeDetailListOfOrderNumResponseBodyDataListChangedJourneysSegmentList(DaraModel):
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
        # Indicates whether this is a codeshare flight.
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
        # The flight duration in minutes.
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

class ChangeDetailListOfOrderNumResponseBodyDataListChangePassengers(DaraModel):
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

class ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetails(DaraModel):
    def __init__(
        self,
        change_fee: main_models.ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetailsChangeFee = None,
        passenger: main_models.ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetailsPassenger = None,
    ):
        # The change fee details for the passenger.
        self.change_fee = change_fee
        # The passenger information for the change.
        self.passenger = passenger

    def validate(self):
        if self.change_fee:
            self.change_fee.validate()
        if self.passenger:
            self.passenger.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_fee is not None:
            result['change_fee'] = self.change_fee.to_map()

        if self.passenger is not None:
            result['passenger'] = self.passenger.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change_fee') is not None:
            temp_model = main_models.ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetailsChangeFee()
            self.change_fee = temp_model.from_map(m.get('change_fee'))

        if m.get('passenger') is not None:
            temp_model = main_models.ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetailsPassenger()
            self.passenger = temp_model.from_map(m.get('passenger'))

        return self

class ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetailsPassenger(DaraModel):
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

class ChangeDetailListOfOrderNumResponseBodyDataListChangeFeeDetailsChangeFee(DaraModel):
    def __init__(
        self,
        service_fee: float = None,
        suez_service_fee: float = None,
        tax_fee: float = None,
        upgrade_fee: float = None,
    ):
        # The service fee.
        self.service_fee = service_fee
        self.suez_service_fee = suez_service_fee
        # The change tax fee.
        self.tax_fee = tax_fee
        # The upgrade fee.
        self.upgrade_fee = upgrade_fee

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_fee is not None:
            result['service_fee'] = self.service_fee

        if self.suez_service_fee is not None:
            result['suez_service_fee'] = self.suez_service_fee

        if self.tax_fee is not None:
            result['tax_fee'] = self.tax_fee

        if self.upgrade_fee is not None:
            result['upgrade_fee'] = self.upgrade_fee

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('service_fee') is not None:
            self.service_fee = m.get('service_fee')

        if m.get('suez_service_fee') is not None:
            self.suez_service_fee = m.get('suez_service_fee')

        if m.get('tax_fee') is not None:
            self.tax_fee = m.get('tax_fee')

        if m.get('upgrade_fee') is not None:
            self.upgrade_fee = m.get('upgrade_fee')

        return self

