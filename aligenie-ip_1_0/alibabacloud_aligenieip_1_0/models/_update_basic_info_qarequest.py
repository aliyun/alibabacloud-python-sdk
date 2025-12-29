# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateBasicInfoQARequest(DaraModel):
    def __init__(
        self,
        check_in_time: str = None,
        check_out_time: str = None,
        hotel_address: str = None,
        hotel_id: str = None,
        hotel_introduction: str = None,
        hotel_member: str = None,
        hotel_service: str = None,
        parking_expenses: str = None,
        parking_position: str = None,
        phone_number: str = None,
        wifi_name: str = None,
        wifi_password: str = None,
    ):
        # This parameter is required.
        self.check_in_time = check_in_time
        # This parameter is required.
        self.check_out_time = check_out_time
        # This parameter is required.
        self.hotel_address = hotel_address
        # This parameter is required.
        self.hotel_id = hotel_id
        self.hotel_introduction = hotel_introduction
        self.hotel_member = hotel_member
        self.hotel_service = hotel_service
        # This parameter is required.
        self.parking_expenses = parking_expenses
        # This parameter is required.
        self.parking_position = parking_position
        # This parameter is required.
        self.phone_number = phone_number
        # This parameter is required.
        self.wifi_name = wifi_name
        # This parameter is required.
        self.wifi_password = wifi_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_in_time is not None:
            result['CheckInTime'] = self.check_in_time

        if self.check_out_time is not None:
            result['CheckOutTime'] = self.check_out_time

        if self.hotel_address is not None:
            result['HotelAddress'] = self.hotel_address

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.hotel_introduction is not None:
            result['HotelIntroduction'] = self.hotel_introduction

        if self.hotel_member is not None:
            result['HotelMember'] = self.hotel_member

        if self.hotel_service is not None:
            result['HotelService'] = self.hotel_service

        if self.parking_expenses is not None:
            result['ParkingExpenses'] = self.parking_expenses

        if self.parking_position is not None:
            result['ParkingPosition'] = self.parking_position

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.wifi_name is not None:
            result['WifiName'] = self.wifi_name

        if self.wifi_password is not None:
            result['WifiPassword'] = self.wifi_password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckInTime') is not None:
            self.check_in_time = m.get('CheckInTime')

        if m.get('CheckOutTime') is not None:
            self.check_out_time = m.get('CheckOutTime')

        if m.get('HotelAddress') is not None:
            self.hotel_address = m.get('HotelAddress')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('HotelIntroduction') is not None:
            self.hotel_introduction = m.get('HotelIntroduction')

        if m.get('HotelMember') is not None:
            self.hotel_member = m.get('HotelMember')

        if m.get('HotelService') is not None:
            self.hotel_service = m.get('HotelService')

        if m.get('ParkingExpenses') is not None:
            self.parking_expenses = m.get('ParkingExpenses')

        if m.get('ParkingPosition') is not None:
            self.parking_position = m.get('ParkingPosition')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('WifiName') is not None:
            self.wifi_name = m.get('WifiName')

        if m.get('WifiPassword') is not None:
            self.wifi_password = m.get('WifiPassword')

        return self

