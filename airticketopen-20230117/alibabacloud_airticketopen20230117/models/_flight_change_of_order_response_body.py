# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class FlightChangeOfOrderResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[main_models.FlightChangeOfOrderResponseBodyData] = None,
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
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.FlightChangeOfOrderResponseBodyData()
                self.data.append(temp_model.from_map(k1))

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

class FlightChangeOfOrderResponseBodyData(DaraModel):
    def __init__(
        self,
        flight_change_detail: main_models.FlightChangeOfOrderResponseBodyDataFlightChangeDetail = None,
        order_num: int = None,
    ):
        # The flight change information.
        self.flight_change_detail = flight_change_detail
        # The order number.
        self.order_num = order_num

    def validate(self):
        if self.flight_change_detail:
            self.flight_change_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flight_change_detail is not None:
            result['flight_change_detail'] = self.flight_change_detail.to_map()

        if self.order_num is not None:
            result['order_num'] = self.order_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flight_change_detail') is not None:
            temp_model = main_models.FlightChangeOfOrderResponseBodyDataFlightChangeDetail()
            self.flight_change_detail = temp_model.from_map(m.get('flight_change_detail'))

        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')

        return self

class FlightChangeOfOrderResponseBodyDataFlightChangeDetail(DaraModel):
    def __init__(
        self,
        change_reason: str = None,
        change_time: str = None,
        change_type: int = None,
        new_arrival_airport: str = None,
        new_arrival_time: str = None,
        new_departure_airport: str = None,
        new_departure_time: str = None,
        new_flight_no: str = None,
        old_arrival_airport: str = None,
        old_arrival_time: str = None,
        old_departure_airport: str = None,
        old_departure_time: str = None,
        old_flight_no: str = None,
    ):
        # The reason for the flight change.
        self.change_reason = change_reason
        # The time of the flight change in string format (yyyy-MM-dd HH:mm:ss).
        self.change_time = change_time
        # The type of the flight change. Valid values:
        # - 1: cancellation
        # - 2: schedule change.
        self.change_type = change_type
        # The three-letter IATA code of the new arrival airport (uppercase).
        self.new_arrival_airport = new_arrival_airport
        # The arrival date and time of the new flight in string format (yyyy-MM-dd HH:mm:ss).
        self.new_arrival_time = new_arrival_time
        # The three-letter IATA code of the new departure airport (uppercase).
        self.new_departure_airport = new_departure_airport
        # The departure date and time of the new flight in string format (yyyy-MM-dd HH:mm:ss).
        self.new_departure_time = new_departure_time
        # The new flight number.
        self.new_flight_no = new_flight_no
        # The three-letter IATA code of the original arrival airport (uppercase).
        self.old_arrival_airport = old_arrival_airport
        # The arrival date and time of the original flight in string format (yyyy-MM-dd HH:mm:ss).
        self.old_arrival_time = old_arrival_time
        # The three-letter IATA code of the original departure airport (uppercase).
        self.old_departure_airport = old_departure_airport
        # The departure date and time of the original flight in string format (yyyy-MM-dd HH:mm:ss).
        self.old_departure_time = old_departure_time
        # The original flight number.
        self.old_flight_no = old_flight_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_reason is not None:
            result['change_reason'] = self.change_reason

        if self.change_time is not None:
            result['change_time'] = self.change_time

        if self.change_type is not None:
            result['change_type'] = self.change_type

        if self.new_arrival_airport is not None:
            result['new_arrival_airport'] = self.new_arrival_airport

        if self.new_arrival_time is not None:
            result['new_arrival_time'] = self.new_arrival_time

        if self.new_departure_airport is not None:
            result['new_departure_airport'] = self.new_departure_airport

        if self.new_departure_time is not None:
            result['new_departure_time'] = self.new_departure_time

        if self.new_flight_no is not None:
            result['new_flight_no'] = self.new_flight_no

        if self.old_arrival_airport is not None:
            result['old_arrival_airport'] = self.old_arrival_airport

        if self.old_arrival_time is not None:
            result['old_arrival_time'] = self.old_arrival_time

        if self.old_departure_airport is not None:
            result['old_departure_airport'] = self.old_departure_airport

        if self.old_departure_time is not None:
            result['old_departure_time'] = self.old_departure_time

        if self.old_flight_no is not None:
            result['old_flight_no'] = self.old_flight_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('change_reason') is not None:
            self.change_reason = m.get('change_reason')

        if m.get('change_time') is not None:
            self.change_time = m.get('change_time')

        if m.get('change_type') is not None:
            self.change_type = m.get('change_type')

        if m.get('new_arrival_airport') is not None:
            self.new_arrival_airport = m.get('new_arrival_airport')

        if m.get('new_arrival_time') is not None:
            self.new_arrival_time = m.get('new_arrival_time')

        if m.get('new_departure_airport') is not None:
            self.new_departure_airport = m.get('new_departure_airport')

        if m.get('new_departure_time') is not None:
            self.new_departure_time = m.get('new_departure_time')

        if m.get('new_flight_no') is not None:
            self.new_flight_no = m.get('new_flight_no')

        if m.get('old_arrival_airport') is not None:
            self.old_arrival_airport = m.get('old_arrival_airport')

        if m.get('old_arrival_time') is not None:
            self.old_arrival_time = m.get('old_arrival_time')

        if m.get('old_departure_airport') is not None:
            self.old_departure_airport = m.get('old_departure_airport')

        if m.get('old_departure_time') is not None:
            self.old_departure_time = m.get('old_departure_time')

        if m.get('old_flight_no') is not None:
            self.old_flight_no = m.get('old_flight_no')

        return self

