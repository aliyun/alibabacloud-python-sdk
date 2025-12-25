# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class IncidentEventForView(DaraModel):
    def __init__(
        self,
        auto_recover_time: int = None,
        content: main_models.CmsEventForView = None,
        count: int = None,
        dimension: Dict[str, Any] = None,
        event_resource: main_models.EventResourceForIncidentView = None,
        group_by: Dict[str, Any] = None,
        incident_event_uuid: str = None,
        incident_uuid: str = None,
        labels: Dict[str, Any] = None,
        last_time: int = None,
        recover_time: int = None,
        search_index: List[str] = None,
        severity: str = None,
        severity_count_map: Dict[str, Any] = None,
        state: int = None,
        text_index: str = None,
        time: int = None,
        title: str = None,
        user_id: str = None,
        workspace: str = None,
    ):
        self.auto_recover_time = auto_recover_time
        self.content = content
        self.count = count
        self.dimension = dimension
        self.event_resource = event_resource
        self.group_by = group_by
        self.incident_event_uuid = incident_event_uuid
        self.incident_uuid = incident_uuid
        self.labels = labels
        self.last_time = last_time
        self.recover_time = recover_time
        self.search_index = search_index
        self.severity = severity
        self.severity_count_map = severity_count_map
        self.state = state
        self.text_index = text_index
        self.time = time
        self.title = title
        self.user_id = user_id
        self.workspace = workspace

    def validate(self):
        if self.content:
            self.content.validate()
        if self.event_resource:
            self.event_resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_recover_time is not None:
            result['autoRecoverTime'] = self.auto_recover_time

        if self.content is not None:
            result['content'] = self.content.to_map()

        if self.count is not None:
            result['count'] = self.count

        if self.dimension is not None:
            result['dimension'] = self.dimension

        if self.event_resource is not None:
            result['eventResource'] = self.event_resource.to_map()

        if self.group_by is not None:
            result['groupBy'] = self.group_by

        if self.incident_event_uuid is not None:
            result['incidentEventUuid'] = self.incident_event_uuid

        if self.incident_uuid is not None:
            result['incidentUuid'] = self.incident_uuid

        if self.labels is not None:
            result['labels'] = self.labels

        if self.last_time is not None:
            result['lastTime'] = self.last_time

        if self.recover_time is not None:
            result['recoverTime'] = self.recover_time

        if self.search_index is not None:
            result['searchIndex'] = self.search_index

        if self.severity is not None:
            result['severity'] = self.severity

        if self.severity_count_map is not None:
            result['severityCountMap'] = self.severity_count_map

        if self.state is not None:
            result['state'] = self.state

        if self.text_index is not None:
            result['textIndex'] = self.text_index

        if self.time is not None:
            result['time'] = self.time

        if self.title is not None:
            result['title'] = self.title

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRecoverTime') is not None:
            self.auto_recover_time = m.get('autoRecoverTime')

        if m.get('content') is not None:
            temp_model = main_models.CmsEventForView()
            self.content = temp_model.from_map(m.get('content'))

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('dimension') is not None:
            self.dimension = m.get('dimension')

        if m.get('eventResource') is not None:
            temp_model = main_models.EventResourceForIncidentView()
            self.event_resource = temp_model.from_map(m.get('eventResource'))

        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')

        if m.get('incidentEventUuid') is not None:
            self.incident_event_uuid = m.get('incidentEventUuid')

        if m.get('incidentUuid') is not None:
            self.incident_uuid = m.get('incidentUuid')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('lastTime') is not None:
            self.last_time = m.get('lastTime')

        if m.get('recoverTime') is not None:
            self.recover_time = m.get('recoverTime')

        if m.get('searchIndex') is not None:
            self.search_index = m.get('searchIndex')

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('severityCountMap') is not None:
            self.severity_count_map = m.get('severityCountMap')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('textIndex') is not None:
            self.text_index = m.get('textIndex')

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

