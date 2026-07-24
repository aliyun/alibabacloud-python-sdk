# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class ChangeApplyRequest(DaraModel):
    def __init__(
        self,
        change_passenger_list: List[main_models.ChangeApplyRequestChangePassengerList] = None,
        changed_journeys: List[main_models.ChangeApplyRequestChangedJourneys] = None,
        contact: main_models.ChangeApplyRequestContact = None,
        order_num: int = None,
        remark: str = None,
        type: int = None,
    ):
        # The list of passengers for the change.
        # 
        # This parameter is required.
        self.change_passenger_list = change_passenger_list
        # The target journey for the change.
        # 
        # This parameter is required.
        self.changed_journeys = changed_journeys
        # The contact information for the change.
        # 
        # This parameter is required.
        self.contact = contact
        # The order number.
        # 
        # This parameter is required.
        self.order_num = order_num
        # The buyer remarks.
        self.remark = remark
        # The change type. Valid values:
        # - 0: voluntary change
        # - 1: flight schedule change or flight cancellation.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.change_passenger_list:
            for v1 in self.change_passenger_list:
                 if v1:
                    v1.validate()
        if self.changed_journeys:
            for v1 in self.changed_journeys:
                 if v1:
                    v1.validate()
        if self.contact:
            self.contact.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['change_passenger_list'] = []
        if self.change_passenger_list is not None:
            for k1 in self.change_passenger_list:
                result['change_passenger_list'].append(k1.to_map() if k1 else None)

        result['changed_journeys'] = []
        if self.changed_journeys is not None:
            for k1 in self.changed_journeys:
                result['changed_journeys'].append(k1.to_map() if k1 else None)

        if self.contact is not None:
            result['contact'] = self.contact.to_map()

        if self.order_num is not None:
            result['order_num'] = self.order_num

        if self.remark is not None:
            result['remark'] = self.remark

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.change_passenger_list = []
        if m.get('change_passenger_list') is not None:
            for k1 in m.get('change_passenger_list'):
                temp_model = main_models.ChangeApplyRequestChangePassengerList()
                self.change_passenger_list.append(temp_model.from_map(k1))

        self.changed_journeys = []
        if m.get('changed_journeys') is not None:
            for k1 in m.get('changed_journeys'):
                temp_model = main_models.ChangeApplyRequestChangedJourneys()
                self.changed_journeys.append(temp_model.from_map(k1))

        if m.get('contact') is not None:
            temp_model = main_models.ChangeApplyRequestContact()
            self.contact = temp_model.from_map(m.get('contact'))

        if m.get('order_num') is not None:
            self.order_num = m.get('order_num')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ChangeApplyRequestContact(DaraModel):
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

class ChangeApplyRequestChangedJourneys(DaraModel):
    def __init__(
        self,
        segment_list: List[main_models.ChangeApplyRequestChangedJourneysSegmentList] = None,
    ):
        # The list of target segments for the change.
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
        result['segment_list'] = []
        if self.segment_list is not None:
            for k1 in self.segment_list:
                result['segment_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.segment_list = []
        if m.get('segment_list') is not None:
            for k1 in m.get('segment_list'):
                temp_model = main_models.ChangeApplyRequestChangedJourneysSegmentList()
                self.segment_list.append(temp_model.from_map(k1))

        return self

class ChangeApplyRequestChangedJourneysSegmentList(DaraModel):
    def __init__(
        self,
        arrival_airport: str = None,
        arrival_city: str = None,
        arrive_terminal: str = None,
        arrive_time: int = None,
        arrive_time_str: str = None,
        code_share: bool = None,
        departure_airport: str = None,
        departure_city: str = None,
        departure_date: str = None,
        departure_terminal: str = None,
        departure_time: int = None,
        departure_time_str: str = None,
        marketing_flight_no: str = None,
        operating_flight_no: str = None,
    ):
        # The three-letter IATA code of the arrival airport.
        self.arrival_airport = arrival_airport
        # The three-letter IATA code of the arrival city.
        # 
        # This parameter is required.
        self.arrival_city = arrival_city
        # The arrival terminal of the flight.
        self.arrive_terminal = arrive_terminal
        # (该属性废弃)航班到达日期时间，utc时间戳
        self.arrive_time = arrive_time
        # (必填参数)航班到达日期时间，航班的旅行时间，格式：yyyy-MM-dd HH:mm:ss
        self.arrive_time_str = arrive_time_str
        # Indicates whether the flight is a codeshare flight.
        self.code_share = code_share
        # The three-letter IATA code of the departure airport.
        self.departure_airport = departure_airport
        # The three-letter IATA code of the departure city.
        # 
        # This parameter is required.
        self.departure_city = departure_city
        # The departure date (for example, yyyyMMdd).
        # [_single.params.changed_journeys.items.segment_list.items.departure_time.desc](Deprecated) The departure date and time of the flight, in UTC timestamp.
        # [_single.params.changed_journeys.items.segment_list.items.departure_time_str.desc](Required) The departure date and time of the flight, in local travel time. Format: yyyy-MM-dd HH:mm:ss.
        # [_single.params.changed_journeys.items.segment_list.items.arrive_time.desc](Deprecated) The arrival date and time of the flight, in UTC timestamp.
        # [_single.params.changed_journeys.items.segment_list.items.arrive_time_str.desc](Required) The arrival date and time of the flight, in local travel time. Format: yyyy-MM-dd HH:mm:ss.
        # 
        # This parameter is required.
        self.departure_date = departure_date
        # The departure terminal of the flight.
        self.departure_terminal = departure_terminal
        # (该属性废弃)航班起飞日期，utc时间戳
        self.departure_time = departure_time
        # (必填参数)航班起飞日期时间，航班的旅行时间，格式：yyyy-MM-dd HH:mm:ss
        self.departure_time_str = departure_time_str
        # The marketing flight number (such as KA5809).
        # 
        # This parameter is required.
        self.marketing_flight_no = marketing_flight_no
        # The operating flight number (such as CX601).
        self.operating_flight_no = operating_flight_no

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

        if self.arrive_terminal is not None:
            result['arrive_terminal'] = self.arrive_terminal

        if self.arrive_time is not None:
            result['arrive_time'] = self.arrive_time

        if self.arrive_time_str is not None:
            result['arrive_time_str'] = self.arrive_time_str

        if self.code_share is not None:
            result['code_share'] = self.code_share

        if self.departure_airport is not None:
            result['departure_airport'] = self.departure_airport

        if self.departure_city is not None:
            result['departure_city'] = self.departure_city

        if self.departure_date is not None:
            result['departure_date'] = self.departure_date

        if self.departure_terminal is not None:
            result['departure_terminal'] = self.departure_terminal

        if self.departure_time is not None:
            result['departure_time'] = self.departure_time

        if self.departure_time_str is not None:
            result['departure_time_str'] = self.departure_time_str

        if self.marketing_flight_no is not None:
            result['marketing_flight_no'] = self.marketing_flight_no

        if self.operating_flight_no is not None:
            result['operating_flight_no'] = self.operating_flight_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arrival_airport') is not None:
            self.arrival_airport = m.get('arrival_airport')

        if m.get('arrival_city') is not None:
            self.arrival_city = m.get('arrival_city')

        if m.get('arrive_terminal') is not None:
            self.arrive_terminal = m.get('arrive_terminal')

        if m.get('arrive_time') is not None:
            self.arrive_time = m.get('arrive_time')

        if m.get('arrive_time_str') is not None:
            self.arrive_time_str = m.get('arrive_time_str')

        if m.get('code_share') is not None:
            self.code_share = m.get('code_share')

        if m.get('departure_airport') is not None:
            self.departure_airport = m.get('departure_airport')

        if m.get('departure_city') is not None:
            self.departure_city = m.get('departure_city')

        if m.get('departure_date') is not None:
            self.departure_date = m.get('departure_date')

        if m.get('departure_terminal') is not None:
            self.departure_terminal = m.get('departure_terminal')

        if m.get('departure_time') is not None:
            self.departure_time = m.get('departure_time')

        if m.get('departure_time_str') is not None:
            self.departure_time_str = m.get('departure_time_str')

        if m.get('marketing_flight_no') is not None:
            self.marketing_flight_no = m.get('marketing_flight_no')

        if m.get('operating_flight_no') is not None:
            self.operating_flight_no = m.get('operating_flight_no')

        return self

class ChangeApplyRequestChangePassengerList(DaraModel):
    def __init__(
        self,
        document: str = None,
        first_name: str = None,
        last_name: str = None,
    ):
        # The document number.
        self.document = document
        # The first name of the passenger.
        # 
        # This parameter is required.
        self.first_name = first_name
        # The last name of the passenger.
        # 
        # This parameter is required.
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

