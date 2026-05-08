# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTicketRecordByticketCodePopRequest(DaraModel):
    def __init__(
        self,
        agenda_id: str = None,
        code: str = None,
        event: str = None,
        scene_id: str = None,
        time: str = None,
    ):
        self.agenda_id = agenda_id
        self.code = code
        self.event = event
        self.scene_id = scene_id
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agenda_id is not None:
            result['AgendaId'] = self.agenda_id

        if self.code is not None:
            result['Code'] = self.code

        if self.event is not None:
            result['Event'] = self.event

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgendaId') is not None:
            self.agenda_id = m.get('AgendaId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

