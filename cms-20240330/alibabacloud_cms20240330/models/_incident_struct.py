# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class IncidentStruct(DaraModel):
    def __init__(
        self,
        content: str = None,
        escalations: List[main_models.IncidentEscalationStruct] = None,
        incident_id: str = None,
        incident_plan: main_models.IncidentPlanStruct = None,
        resource: main_models.IncidentResourceDetail = None,
        severity: str = None,
        status: str = None,
        time: int = None,
        title: str = None,
        user_id: str = None,
    ):
        self.content = content
        self.escalations = escalations
        self.incident_id = incident_id
        self.incident_plan = incident_plan
        self.resource = resource
        self.severity = severity
        self.status = status
        self.time = time
        self.title = title
        self.user_id = user_id

    def validate(self):
        if self.escalations:
            for v1 in self.escalations:
                 if v1:
                    v1.validate()
        if self.incident_plan:
            self.incident_plan.validate()
        if self.resource:
            self.resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        result['escalations'] = []
        if self.escalations is not None:
            for k1 in self.escalations:
                result['escalations'].append(k1.to_map() if k1 else None)

        if self.incident_id is not None:
            result['incidentId'] = self.incident_id

        if self.incident_plan is not None:
            result['incidentPlan'] = self.incident_plan.to_map()

        if self.resource is not None:
            result['resource'] = self.resource.to_map()

        if self.severity is not None:
            result['severity'] = self.severity

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
        if m.get('content') is not None:
            self.content = m.get('content')

        self.escalations = []
        if m.get('escalations') is not None:
            for k1 in m.get('escalations'):
                temp_model = main_models.IncidentEscalationStruct()
                self.escalations.append(temp_model.from_map(k1))

        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')

        if m.get('incidentPlan') is not None:
            temp_model = main_models.IncidentPlanStruct()
            self.incident_plan = temp_model.from_map(m.get('incidentPlan'))

        if m.get('resource') is not None:
            temp_model = main_models.IncidentResourceDetail()
            self.resource = temp_model.from_map(m.get('resource'))

        if m.get('severity') is not None:
            self.severity = m.get('severity')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

