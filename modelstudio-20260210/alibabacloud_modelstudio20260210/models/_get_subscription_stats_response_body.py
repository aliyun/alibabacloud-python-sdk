# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_modelstudio20260210 import models as main_models
from darabonba.model import DaraModel

class GetSubscriptionStatsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetSubscriptionStatsResponseBodyData = None,
        message: str = None,
        success: bool = None,
    ):
        # The response status code.
        self.code = code
        # The business data.
        self.data = data
        # The response message.
        self.message = message
        # Indicates whether the API call is successful. Valid values:
        # 
        # - true: Successful.
        # - false: Failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetSubscriptionStatsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSubscriptionStatsResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.GetSubscriptionStatsResponseBodyDataItems] = None,
        subscription_end_time: int = None,
        subscription_start_time: int = None,
    ):
        # The list of seat information, grouped by specType.
        self.items = items
        # The subscription end time, in milliseconds.
        self.subscription_end_time = subscription_end_time
        # The subscription start time, in milliseconds.
        self.subscription_start_time = subscription_start_time

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.subscription_end_time is not None:
            result['SubscriptionEndTime'] = self.subscription_end_time

        if self.subscription_start_time is not None:
            result['SubscriptionStartTime'] = self.subscription_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.GetSubscriptionStatsResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('SubscriptionEndTime') is not None:
            self.subscription_end_time = m.get('SubscriptionEndTime')

        if m.get('SubscriptionStartTime') is not None:
            self.subscription_start_time = m.get('SubscriptionStartTime')

        return self

class GetSubscriptionStatsResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        assigned_seats: int = None,
        seat_credits: float = None,
        seat_refresh_time: int = None,
        seat_remaining_credits: float = None,
        seat_type: str = None,
        total_seats: int = None,
    ):
        # The number of assigned seats.
        self.assigned_seats = assigned_seats
        # The total credits quota for the seat.
        self.seat_credits = seat_credits
        # The refresh time of the current cycle, in milliseconds.
        self.seat_refresh_time = seat_refresh_time
        # The remaining credits for the current cycle.
        self.seat_remaining_credits = seat_remaining_credits
        # The seat type (specType). Valid values:
        # - standard: Standard seat.
        # - pro: Pro seat.
        # - max: Premium seat.
        self.seat_type = seat_type
        # The total number of seats.
        self.total_seats = total_seats

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assigned_seats is not None:
            result['AssignedSeats'] = self.assigned_seats

        if self.seat_credits is not None:
            result['SeatCredits'] = self.seat_credits

        if self.seat_refresh_time is not None:
            result['SeatRefreshTime'] = self.seat_refresh_time

        if self.seat_remaining_credits is not None:
            result['SeatRemainingCredits'] = self.seat_remaining_credits

        if self.seat_type is not None:
            result['SeatType'] = self.seat_type

        if self.total_seats is not None:
            result['TotalSeats'] = self.total_seats

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignedSeats') is not None:
            self.assigned_seats = m.get('AssignedSeats')

        if m.get('SeatCredits') is not None:
            self.seat_credits = m.get('SeatCredits')

        if m.get('SeatRefreshTime') is not None:
            self.seat_refresh_time = m.get('SeatRefreshTime')

        if m.get('SeatRemainingCredits') is not None:
            self.seat_remaining_credits = m.get('SeatRemainingCredits')

        if m.get('SeatType') is not None:
            self.seat_type = m.get('SeatType')

        if m.get('TotalSeats') is not None:
            self.total_seats = m.get('TotalSeats')

        return self

