# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class IncidentMemberStruct(DaraModel):
    def __init__(
        self,
        acknowledge: main_models.IncidentMemberStructAcknowledge = None,
        contact_id: str = None,
        contacts: List[main_models.IncidentMemberStructContacts] = None,
        escalation: main_models.IncidentMemberStructEscalation = None,
        incident_id: str = None,
        incident_member_id: str = None,
        schedule_group: main_models.IncidentMemberStructScheduleGroup = None,
        time: int = None,
        user_id: int = None,
    ):
        self.acknowledge = acknowledge
        self.contact_id = contact_id
        self.contacts = contacts
        self.escalation = escalation
        self.incident_id = incident_id
        self.incident_member_id = incident_member_id
        self.schedule_group = schedule_group
        self.time = time
        self.user_id = user_id

    def validate(self):
        if self.acknowledge:
            self.acknowledge.validate()
        if self.contacts:
            for v1 in self.contacts:
                 if v1:
                    v1.validate()
        if self.escalation:
            self.escalation.validate()
        if self.schedule_group:
            self.schedule_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acknowledge is not None:
            result['acknowledge'] = self.acknowledge.to_map()

        if self.contact_id is not None:
            result['contactId'] = self.contact_id

        result['contacts'] = []
        if self.contacts is not None:
            for k1 in self.contacts:
                result['contacts'].append(k1.to_map() if k1 else None)

        if self.escalation is not None:
            result['escalation'] = self.escalation.to_map()

        if self.incident_id is not None:
            result['incidentId'] = self.incident_id

        if self.incident_member_id is not None:
            result['incidentMemberId'] = self.incident_member_id

        if self.schedule_group is not None:
            result['scheduleGroup'] = self.schedule_group.to_map()

        if self.time is not None:
            result['time'] = self.time

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acknowledge') is not None:
            temp_model = main_models.IncidentMemberStructAcknowledge()
            self.acknowledge = temp_model.from_map(m.get('acknowledge'))

        if m.get('contactId') is not None:
            self.contact_id = m.get('contactId')

        self.contacts = []
        if m.get('contacts') is not None:
            for k1 in m.get('contacts'):
                temp_model = main_models.IncidentMemberStructContacts()
                self.contacts.append(temp_model.from_map(k1))

        if m.get('escalation') is not None:
            temp_model = main_models.IncidentMemberStructEscalation()
            self.escalation = temp_model.from_map(m.get('escalation'))

        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')

        if m.get('incidentMemberId') is not None:
            self.incident_member_id = m.get('incidentMemberId')

        if m.get('scheduleGroup') is not None:
            temp_model = main_models.IncidentMemberStructScheduleGroup()
            self.schedule_group = temp_model.from_map(m.get('scheduleGroup'))

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class IncidentMemberStructScheduleGroup(DaraModel):
    def __init__(
        self,
        contact_id: str = None,
        name: str = None,
    ):
        self.contact_id = contact_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['contactId'] = self.contact_id

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contactId') is not None:
            self.contact_id = m.get('contactId')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class IncidentMemberStructEscalation(DaraModel):
    def __init__(
        self,
        description: str = None,
        incident_escalation_id: str = None,
        name: str = None,
        stage_index: str = None,
        title: str = None,
    ):
        self.description = description
        self.incident_escalation_id = incident_escalation_id
        self.name = name
        self.stage_index = stage_index
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.incident_escalation_id is not None:
            result['incidentEscalationId'] = self.incident_escalation_id

        if self.name is not None:
            result['name'] = self.name

        if self.stage_index is not None:
            result['stageIndex'] = self.stage_index

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('incidentEscalationId') is not None:
            self.incident_escalation_id = m.get('incidentEscalationId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('stageIndex') is not None:
            self.stage_index = m.get('stageIndex')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class IncidentMemberStructContacts(DaraModel):
    def __init__(
        self,
        channel: str = None,
        contact_mask: str = None,
    ):
        self.channel = channel
        self.contact_mask = contact_mask

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['channel'] = self.channel

        if self.contact_mask is not None:
            result['contactMask'] = self.contact_mask

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')

        if m.get('contactMask') is not None:
            self.contact_mask = m.get('contactMask')

        return self

class IncidentMemberStructAcknowledge(DaraModel):
    def __init__(
        self,
        break_level: str = None,
        verify_time: int = None,
    ):
        self.break_level = break_level
        self.verify_time = verify_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.break_level is not None:
            result['breakLevel'] = self.break_level

        if self.verify_time is not None:
            result['verifyTime'] = self.verify_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('breakLevel') is not None:
            self.break_level = m.get('breakLevel')

        if m.get('verifyTime') is not None:
            self.verify_time = m.get('verifyTime')

        return self

