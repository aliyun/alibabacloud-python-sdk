# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IncidentTimeline(DaraModel):
    def __init__(
        self,
        child_type: str = None,
        content: str = None,
        incident_id: str = None,
        incident_timeline_id: str = None,
        time: int = None,
        timeline_id: str = None,
        title: str = None,
        type: str = None,
        user_id: str = None,
    ):
        self.child_type = child_type
        self.content = content
        self.incident_id = incident_id
        self.incident_timeline_id = incident_timeline_id
        self.time = time
        self.timeline_id = timeline_id
        self.title = title
        self.type = type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.child_type is not None:
            result['childType'] = self.child_type

        if self.content is not None:
            result['content'] = self.content

        if self.incident_id is not None:
            result['incidentId'] = self.incident_id

        if self.incident_timeline_id is not None:
            result['incidentTimelineId'] = self.incident_timeline_id

        if self.time is not None:
            result['time'] = self.time

        if self.timeline_id is not None:
            result['timelineId'] = self.timeline_id

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('childType') is not None:
            self.child_type = m.get('childType')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')

        if m.get('incidentTimelineId') is not None:
            self.incident_timeline_id = m.get('incidentTimelineId')

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('timelineId') is not None:
            self.timeline_id = m.get('timelineId')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

