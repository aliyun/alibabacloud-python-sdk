# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TimeTrigger(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        launch_expiration_time: int = None,
        launch_time: str = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
        start_time: int = None,
    ):
        # The timestamp that specifies the end time. Unit: milliseconds.
        self.end_time = end_time
        # The time period during which a scheduled task can be retried after it fails. Unit: seconds. Valid values: 0 to 3600.
        self.launch_expiration_time = launch_expiration_time
        # The execution time of the scaling rule. This parameter is required. The value is a string in the HH:MM format.
        # 
        # This parameter is required.
        self.launch_time = launch_time
        # The frequency of executing the specified rule whose trigger mode is scaling by time. Valid values:
        # 
        # *   DAILY
        # *   WEEKLY
        # *   MONTHLY
        self.recurrence_type = recurrence_type
        # The number of recurrences of the scheduled task. The value of this parameter depends on the value of RecurrenceType.
        # 
        # *   If the RecurrenceType parameter is set to DAILY, you can specify only one value for this parameter. Valid values: 1 to 31.
        # *   If the RecurrenceType parameter is set to WEEKLY, you can specify multiple values for this parameter and separate them with commas (,). The values MON, TUE, WED, THU, FRI, SAT, and SUN indicate the days from Monday to Sunday. For example, the value MON,FRI,SUN stands for Monday, Friday, and Sunday.
        # *   If the RecurrenceType parameter is set to MONTHLY, the value of this parameter is in the A-B or A,B format. The values of A and B are both in the range of 1 to 31. If you use the A-B format, the value of B must be greater than the value of A.
        self.recurrence_value = recurrence_value
        # The timestamp that specifies the start time. This parameter is required. Unit: milliseconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.launch_expiration_time is not None:
            result['LaunchExpirationTime'] = self.launch_expiration_time

        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time

        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type

        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('LaunchExpirationTime') is not None:
            self.launch_expiration_time = m.get('LaunchExpirationTime')

        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')

        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')

        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

