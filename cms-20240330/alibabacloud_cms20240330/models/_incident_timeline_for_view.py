# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class IncidentTimelineForView(DaraModel):
    def __init__(
        self,
        change_type: str = None,
        content: Any = None,
        incident_uuid: str = None,
        operator: main_models.ContactForIncidentView = None,
        time: int = None,
        timeline_uuid: str = None,
        title: str = None,
        type: str = None,
        user_id: str = None,
        workspace: str = None,
    ):
        self.change_type = change_type
        self.content = content
        self.incident_uuid = incident_uuid
        self.operator = operator
        self.time = time
        self.timeline_uuid = timeline_uuid
        self.title = title
        self.type = type
        self.user_id = user_id
        self.workspace = workspace

    def validate(self):
        if self.operator:
            self.operator.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_type is not None:
            result['changeType'] = self.change_type

        if self.content is not None:
            result['content'] = self.content

        if self.incident_uuid is not None:
            result['incidentUuid'] = self.incident_uuid

        if self.operator is not None:
            result['operator'] = self.operator.to_map()

        if self.time is not None:
            result['time'] = self.time

        if self.timeline_uuid is not None:
            result['timelineUuid'] = self.timeline_uuid

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('changeType') is not None:
            self.change_type = m.get('changeType')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('incidentUuid') is not None:
            self.incident_uuid = m.get('incidentUuid')

        if m.get('operator') is not None:
            temp_model = main_models.ContactForIncidentView()
            self.operator = temp_model.from_map(m.get('operator'))

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('timelineUuid') is not None:
            self.timeline_uuid = m.get('timelineUuid')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

