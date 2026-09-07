# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetOnCallSchedulesDetailResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetOnCallSchedulesDetailResponseBodyData = None,
        request_id: str = None,
    ):
        # The details of the on-call schedule.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetOnCallSchedulesDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetOnCallSchedulesDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        alert_robot_id: int = None,
        description: str = None,
        id: int = None,
        name: str = None,
        rendered_finnal_entries: List[main_models.GetOnCallSchedulesDetailResponseBodyDataRenderedFinnalEntries] = None,
        rendered_layer_entries: List[List[main_models.GetOnCallSchedulesDetailResponseBodyDataRenderedLayerEntries]] = None,
        rendered_substitude_entries: List[main_models.GetOnCallSchedulesDetailResponseBodyDataRenderedSubstitudeEntries] = None,
        schedule_layers: List[main_models.GetOnCallSchedulesDetailResponseBodyDataScheduleLayers] = None,
    ):
        # The webhook URL of the DingTalk bot for rotation notifications.
        self.alert_robot_id = alert_robot_id
        # The description of the on-call schedule.
        self.description = description
        # The ID of the on-call schedule.
        self.id = id
        # The name of the on-call schedule.
        self.name = name
        # The final list of on-call contacts, after accounting for all rotations and substitutions.
        self.rendered_finnal_entries = rendered_finnal_entries
        # A list of contacts on duty within the specified time range, as defined by the schedule layers.
        self.rendered_layer_entries = rendered_layer_entries
        # A list of substitutes scheduled within the specified time range.
        self.rendered_substitude_entries = rendered_substitude_entries
        # A list of schedule layers.
        self.schedule_layers = schedule_layers

    def validate(self):
        if self.rendered_finnal_entries:
            for v1 in self.rendered_finnal_entries:
                 if v1:
                    v1.validate()
        if self.rendered_layer_entries:
            for v1 in self.rendered_layer_entries:
                for v2 in v1:
                     if v2:
                        v2.validate()
        if self.rendered_substitude_entries:
            for v1 in self.rendered_substitude_entries:
                 if v1:
                    v1.validate()
        if self.schedule_layers:
            for v1 in self.schedule_layers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_robot_id is not None:
            result['AlertRobotId'] = self.alert_robot_id

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        result['RenderedFinnalEntries'] = []
        if self.rendered_finnal_entries is not None:
            for k1 in self.rendered_finnal_entries:
                result['RenderedFinnalEntries'].append(k1.to_map() if k1 else None)

        result['RenderedLayerEntries'] = []
        if self.rendered_layer_entries is not None:
            for k1 in self.rendered_layer_entries:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['RenderedLayerEntries'].append(l1)

        result['RenderedSubstitudeEntries'] = []
        if self.rendered_substitude_entries is not None:
            for k1 in self.rendered_substitude_entries:
                result['RenderedSubstitudeEntries'].append(k1.to_map() if k1 else None)

        result['ScheduleLayers'] = []
        if self.schedule_layers is not None:
            for k1 in self.schedule_layers:
                result['ScheduleLayers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertRobotId') is not None:
            self.alert_robot_id = m.get('AlertRobotId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.rendered_finnal_entries = []
        if m.get('RenderedFinnalEntries') is not None:
            for k1 in m.get('RenderedFinnalEntries'):
                temp_model = main_models.GetOnCallSchedulesDetailResponseBodyDataRenderedFinnalEntries()
                self.rendered_finnal_entries.append(temp_model.from_map(k1))

        self.rendered_layer_entries = []
        if m.get('RenderedLayerEntries') is not None:
            for k1 in m.get('RenderedLayerEntries'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.GetOnCallSchedulesDetailResponseBodyDataRenderedLayerEntries()
                    l1.append(temp_model.from_map(k2))
                self.rendered_layer_entries.append(l1)

        self.rendered_substitude_entries = []
        if m.get('RenderedSubstitudeEntries') is not None:
            for k1 in m.get('RenderedSubstitudeEntries'):
                temp_model = main_models.GetOnCallSchedulesDetailResponseBodyDataRenderedSubstitudeEntries()
                self.rendered_substitude_entries.append(temp_model.from_map(k1))

        self.schedule_layers = []
        if m.get('ScheduleLayers') is not None:
            for k1 in m.get('ScheduleLayers'):
                temp_model = main_models.GetOnCallSchedulesDetailResponseBodyDataScheduleLayers()
                self.schedule_layers.append(temp_model.from_map(k1))

        return self

class GetOnCallSchedulesDetailResponseBodyDataScheduleLayers(DaraModel):
    def __init__(
        self,
        contact_ids: List[int] = None,
        restrictions: List[main_models.GetOnCallSchedulesDetailResponseBodyDataScheduleLayersRestrictions] = None,
        rotation_type: str = None,
        shift_length: int = None,
        start_time: str = None,
    ):
        # A list of contact IDs for the schedule layer.
        self.contact_ids = contact_ids
        # A list of restrictions for the schedule layer.
        self.restrictions = restrictions
        # The rotation type. Valid values:
        # 
        # - `DAY`: Rotates every day.
        # 
        # - `WEEK`: Rotates every week.
        # 
        # - `CUSTOM`: Rotates based on a custom schedule.
        self.rotation_type = rotation_type
        # The shift length for the rotation, in hours.
        self.shift_length = shift_length
        # The start time for the rotation.
        self.start_time = start_time

    def validate(self):
        if self.restrictions:
            for v1 in self.restrictions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids

        result['Restrictions'] = []
        if self.restrictions is not None:
            for k1 in self.restrictions:
                result['Restrictions'].append(k1.to_map() if k1 else None)

        if self.rotation_type is not None:
            result['RotationType'] = self.rotation_type

        if self.shift_length is not None:
            result['ShiftLength'] = self.shift_length

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')

        self.restrictions = []
        if m.get('Restrictions') is not None:
            for k1 in m.get('Restrictions'):
                temp_model = main_models.GetOnCallSchedulesDetailResponseBodyDataScheduleLayersRestrictions()
                self.restrictions.append(temp_model.from_map(k1))

        if m.get('RotationType') is not None:
            self.rotation_type = m.get('RotationType')

        if m.get('ShiftLength') is not None:
            self.shift_length = m.get('ShiftLength')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class GetOnCallSchedulesDetailResponseBodyDataScheduleLayersRestrictions(DaraModel):
    def __init__(
        self,
        end_time_of_day: str = None,
        restriction_type: str = None,
        start_time_of_day: str = None,
    ):
        # The end time for on-call duty each day.
        self.end_time_of_day = end_time_of_day
        # The type of restriction. Valid values:
        # 
        # - `daily_restriction`: A daily time-based restriction.
        # 
        # - `weekly_restriction`: A weekly time-based restriction.
        self.restriction_type = restriction_type
        # The start time for on-call duty each day.
        self.start_time_of_day = start_time_of_day

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time_of_day is not None:
            result['EndTimeOfDay'] = self.end_time_of_day

        if self.restriction_type is not None:
            result['RestrictionType'] = self.restriction_type

        if self.start_time_of_day is not None:
            result['StartTimeOfDay'] = self.start_time_of_day

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimeOfDay') is not None:
            self.end_time_of_day = m.get('EndTimeOfDay')

        if m.get('RestrictionType') is not None:
            self.restriction_type = m.get('RestrictionType')

        if m.get('StartTimeOfDay') is not None:
            self.start_time_of_day = m.get('StartTimeOfDay')

        return self

class GetOnCallSchedulesDetailResponseBodyDataRenderedSubstitudeEntries(DaraModel):
    def __init__(
        self,
        end: str = None,
        simple_contact: main_models.GetOnCallSchedulesDetailResponseBodyDataRenderedSubstitudeEntriesSimpleContact = None,
        start: str = None,
    ):
        # The end time of the on-call duty for the substitute.
        self.end = end
        # Details of the substitute.
        self.simple_contact = simple_contact
        # The start time of the on-call duty for the substitute.
        self.start = start

    def validate(self):
        if self.simple_contact:
            self.simple_contact.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end

        if self.simple_contact is not None:
            result['SimpleContact'] = self.simple_contact.to_map()

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('SimpleContact') is not None:
            temp_model = main_models.GetOnCallSchedulesDetailResponseBodyDataRenderedSubstitudeEntriesSimpleContact()
            self.simple_contact = temp_model.from_map(m.get('SimpleContact'))

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class GetOnCallSchedulesDetailResponseBodyDataRenderedSubstitudeEntriesSimpleContact(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The substitute ID.
        self.id = id
        # The substitute name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetOnCallSchedulesDetailResponseBodyDataRenderedLayerEntries(DaraModel):
    def __init__(
        self,
        start: str = None,
        end: str = None,
        simple_contact: main_models.GetOnCallSchedulesDetailResponseBodyDataRenderedLayerEntriesSimpleContact = None,
    ):
        # The start time of the on-call duty for the contact.
        self.start = start
        # The end time of the on-call duty for the contact.
        self.end = end
        # Details of the on-duty contact.
        self.simple_contact = simple_contact

    def validate(self):
        if self.simple_contact:
            self.simple_contact.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.start is not None:
            result['Start'] = self.start

        if self.end is not None:
            result['End'] = self.end

        if self.simple_contact is not None:
            result['SimpleContact'] = self.simple_contact.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('SimpleContact') is not None:
            temp_model = main_models.GetOnCallSchedulesDetailResponseBodyDataRenderedLayerEntriesSimpleContact()
            self.simple_contact = temp_model.from_map(m.get('SimpleContact'))

        return self

class GetOnCallSchedulesDetailResponseBodyDataRenderedLayerEntriesSimpleContact(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The contact ID.
        self.id = id
        # The contact name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetOnCallSchedulesDetailResponseBodyDataRenderedFinnalEntries(DaraModel):
    def __init__(
        self,
        end: str = None,
        simple_contact: main_models.GetOnCallSchedulesDetailResponseBodyDataRenderedFinnalEntriesSimpleContact = None,
        start: str = None,
    ):
        # The end time of the on-call duty for the contact.
        self.end = end
        # Details of the final on-call contact.
        self.simple_contact = simple_contact
        # The start time of the on-call duty for the contact.
        self.start = start

    def validate(self):
        if self.simple_contact:
            self.simple_contact.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end

        if self.simple_contact is not None:
            result['SimpleContact'] = self.simple_contact.to_map()

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('SimpleContact') is not None:
            temp_model = main_models.GetOnCallSchedulesDetailResponseBodyDataRenderedFinnalEntriesSimpleContact()
            self.simple_contact = temp_model.from_map(m.get('SimpleContact'))

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class GetOnCallSchedulesDetailResponseBodyDataRenderedFinnalEntriesSimpleContact(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The contact ID.
        self.id = id
        # The contact name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

