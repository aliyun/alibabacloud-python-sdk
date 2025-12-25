# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class IncidentEventStruct(DaraModel):
    def __init__(
        self,
        auto_recover_time: int = None,
        content: str = None,
        count: int = None,
        dimension: Dict[str, str] = None,
        group_by: Dict[str, str] = None,
        incident_event_id: str = None,
        incident_id: str = None,
        last_time: int = None,
        recover_time: int = None,
        resource: Dict[str, str] = None,
        status: int = None,
        time: str = None,
        title: str = None,
        user_id: str = None,
    ):
        self.auto_recover_time = auto_recover_time
        self.content = content
        self.count = count
        self.dimension = dimension
        self.group_by = group_by
        self.incident_event_id = incident_event_id
        self.incident_id = incident_id
        self.last_time = last_time
        self.recover_time = recover_time
        self.resource = resource
        self.status = status
        self.time = time
        self.title = title
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_recover_time is not None:
            result['autoRecoverTime'] = self.auto_recover_time

        if self.content is not None:
            result['content'] = self.content

        if self.count is not None:
            result['count'] = self.count

        if self.dimension is not None:
            result['dimension'] = self.dimension

        if self.group_by is not None:
            result['groupBy'] = self.group_by

        if self.incident_event_id is not None:
            result['incidentEventId'] = self.incident_event_id

        if self.incident_id is not None:
            result['incidentId'] = self.incident_id

        if self.last_time is not None:
            result['lastTime'] = self.last_time

        if self.recover_time is not None:
            result['recoverTime'] = self.recover_time

        if self.resource is not None:
            result['resource'] = self.resource

        if self.status is not None:
            result['status'] = self.status

        if self.time is not None:
            result['time'] = self.time

        if self.title is not None:
            result['title'] = self.title

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRecoverTime') is not None:
            self.auto_recover_time = m.get('autoRecoverTime')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('dimension') is not None:
            self.dimension = m.get('dimension')

        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')

        if m.get('incidentEventId') is not None:
            self.incident_event_id = m.get('incidentEventId')

        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')

        if m.get('lastTime') is not None:
            self.last_time = m.get('lastTime')

        if m.get('recoverTime') is not None:
            self.recover_time = m.get('recoverTime')

        if m.get('resource') is not None:
            self.resource = m.get('resource')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

