# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class IncidentNoteStruct(DaraModel):
    def __init__(
        self,
        content: str = None,
        format: str = None,
        incident_id: str = None,
        note_id: str = None,
        operator: main_models.IncidentNoteStructOperator = None,
        time: int = None,
        type: str = None,
    ):
        self.content = content
        self.format = format
        self.incident_id = incident_id
        self.note_id = note_id
        self.operator = operator
        self.time = time
        self.type = type

    def validate(self):
        if self.operator:
            self.operator.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.format is not None:
            result['format'] = self.format

        if self.incident_id is not None:
            result['incidentId'] = self.incident_id

        if self.note_id is not None:
            result['noteId'] = self.note_id

        if self.operator is not None:
            result['operator'] = self.operator.to_map()

        if self.time is not None:
            result['time'] = self.time

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('format') is not None:
            self.format = m.get('format')

        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')

        if m.get('noteId') is not None:
            self.note_id = m.get('noteId')

        if m.get('operator') is not None:
            temp_model = main_models.IncidentNoteStructOperator()
            self.operator = temp_model.from_map(m.get('operator'))

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class IncidentNoteStructOperator(DaraModel):
    def __init__(
        self,
        contact: str = None,
        contact_id: str = None,
        name: str = None,
        user_id: int = None,
    ):
        self.contact = contact
        self.contact_id = contact_id
        self.name = name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact is not None:
            result['contact'] = self.contact

        if self.contact_id is not None:
            result['contactId'] = self.contact_id

        if self.name is not None:
            result['name'] = self.name

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contact') is not None:
            self.contact = m.get('contact')

        if m.get('contactId') is not None:
            self.contact_id = m.get('contactId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

