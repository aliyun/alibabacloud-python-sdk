# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CreateOncallScheduleRequest(DaraModel):
    def __init__(
        self,
        oncall_schedule_id: str = None,
        oncall_schedule_name: str = None,
        rotations: List[main_models.CreateOncallScheduleRequestRotations] = None,
        shift_robot_id: str = None,
        substitudes: List[main_models.CreateOncallScheduleRequestSubstitudes] = None,
        workspace: str = None,
    ):
        self.oncall_schedule_id = oncall_schedule_id
        self.oncall_schedule_name = oncall_schedule_name
        self.rotations = rotations
        self.shift_robot_id = shift_robot_id
        self.substitudes = substitudes
        self.workspace = workspace

    def validate(self):
        if self.rotations:
            for v1 in self.rotations:
                 if v1:
                    v1.validate()
        if self.substitudes:
            for v1 in self.substitudes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oncall_schedule_id is not None:
            result['oncallScheduleId'] = self.oncall_schedule_id

        if self.oncall_schedule_name is not None:
            result['oncallScheduleName'] = self.oncall_schedule_name

        result['rotations'] = []
        if self.rotations is not None:
            for k1 in self.rotations:
                result['rotations'].append(k1.to_map() if k1 else None)

        if self.shift_robot_id is not None:
            result['shiftRobotId'] = self.shift_robot_id

        result['substitudes'] = []
        if self.substitudes is not None:
            for k1 in self.substitudes:
                result['substitudes'].append(k1.to_map() if k1 else None)

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('oncallScheduleId') is not None:
            self.oncall_schedule_id = m.get('oncallScheduleId')

        if m.get('oncallScheduleName') is not None:
            self.oncall_schedule_name = m.get('oncallScheduleName')

        self.rotations = []
        if m.get('rotations') is not None:
            for k1 in m.get('rotations'):
                temp_model = main_models.CreateOncallScheduleRequestRotations()
                self.rotations.append(temp_model.from_map(k1))

        if m.get('shiftRobotId') is not None:
            self.shift_robot_id = m.get('shiftRobotId')

        self.substitudes = []
        if m.get('substitudes') is not None:
            for k1 in m.get('substitudes'):
                temp_model = main_models.CreateOncallScheduleRequestSubstitudes()
                self.substitudes.append(temp_model.from_map(k1))

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class CreateOncallScheduleRequestSubstitudes(DaraModel):
    def __init__(
        self,
        contact_id: str = None,
        end_time: str = None,
        replaced_contact_id: str = None,
        start_time: str = None,
    ):
        self.contact_id = contact_id
        self.end_time = end_time
        self.replaced_contact_id = replaced_contact_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['contactId'] = self.contact_id

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.replaced_contact_id is not None:
            result['replacedContactId'] = self.replaced_contact_id

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contactId') is not None:
            self.contact_id = m.get('contactId')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('replacedContactId') is not None:
            self.replaced_contact_id = m.get('replacedContactId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

class CreateOncallScheduleRequestRotations(DaraModel):
    def __init__(
        self,
        active_days: List[int] = None,
        contacts: List[str] = None,
        rotation_end_time: str = None,
        rotation_name: str = None,
        rotation_start_time: str = None,
        shift_length: int = None,
        shift_recurrence_frequency: str = None,
        start_date: str = None,
        time_zone: str = None,
    ):
        # This parameter is required.
        self.active_days = active_days
        # This parameter is required.
        self.contacts = contacts
        # This parameter is required.
        self.rotation_end_time = rotation_end_time
        # This parameter is required.
        self.rotation_name = rotation_name
        # This parameter is required.
        self.rotation_start_time = rotation_start_time
        self.shift_length = shift_length
        # This parameter is required.
        self.shift_recurrence_frequency = shift_recurrence_frequency
        # This parameter is required.
        self.start_date = start_date
        # This parameter is required.
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_days is not None:
            result['activeDays'] = self.active_days

        if self.contacts is not None:
            result['contacts'] = self.contacts

        if self.rotation_end_time is not None:
            result['rotationEndTime'] = self.rotation_end_time

        if self.rotation_name is not None:
            result['rotationName'] = self.rotation_name

        if self.rotation_start_time is not None:
            result['rotationStartTime'] = self.rotation_start_time

        if self.shift_length is not None:
            result['shiftLength'] = self.shift_length

        if self.shift_recurrence_frequency is not None:
            result['shiftRecurrenceFrequency'] = self.shift_recurrence_frequency

        if self.start_date is not None:
            result['startDate'] = self.start_date

        if self.time_zone is not None:
            result['timeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeDays') is not None:
            self.active_days = m.get('activeDays')

        if m.get('contacts') is not None:
            self.contacts = m.get('contacts')

        if m.get('rotationEndTime') is not None:
            self.rotation_end_time = m.get('rotationEndTime')

        if m.get('rotationName') is not None:
            self.rotation_name = m.get('rotationName')

        if m.get('rotationStartTime') is not None:
            self.rotation_start_time = m.get('rotationStartTime')

        if m.get('shiftLength') is not None:
            self.shift_length = m.get('shiftLength')

        if m.get('shiftRecurrenceFrequency') is not None:
            self.shift_recurrence_frequency = m.get('shiftRecurrenceFrequency')

        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        return self

