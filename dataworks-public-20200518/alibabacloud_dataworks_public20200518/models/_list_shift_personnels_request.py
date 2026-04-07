# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListShiftPersonnelsRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        shift_person_uid: str = None,
        shift_schedule_identifier: str = None,
        user_type: str = None,
    ):
        # The time when the on-duty engineer starts a shift. Set the value to a UNIX timestamp.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The time when the on-duty engineer ends a shift. Set the value to a UNIX timestamp.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the Alibaba Cloud account. You can log on to the DataWorks console and move the pointer over the profile picture in the upper-right corner to view the ID.
        self.shift_person_uid = shift_person_uid
        # The unique identifier of the shift schedule.
        # 
        # This parameter is required.
        self.shift_schedule_identifier = shift_schedule_identifier
        # The type of the on-duty engineer that you want to query. Valid values: ALL, PRIMARY, BACKUP, and DESIGNATED_USER.
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.shift_person_uid is not None:
            result['ShiftPersonUID'] = self.shift_person_uid

        if self.shift_schedule_identifier is not None:
            result['ShiftScheduleIdentifier'] = self.shift_schedule_identifier

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ShiftPersonUID') is not None:
            self.shift_person_uid = m.get('ShiftPersonUID')

        if m.get('ShiftScheduleIdentifier') is not None:
            self.shift_schedule_identifier = m.get('ShiftScheduleIdentifier')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

