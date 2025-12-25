# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class IncidentResourceStruct(DaraModel):
    def __init__(
        self,
        description: str = None,
        incident_id: str = None,
        incident_resource_id: str = None,
        resource: main_models.IncidentResourceDetail = None,
        source: str = None,
        time: int = None,
        user_id: int = None,
    ):
        self.description = description
        self.incident_id = incident_id
        self.incident_resource_id = incident_resource_id
        self.resource = resource
        self.source = source
        self.time = time
        self.user_id = user_id

    def validate(self):
        if self.resource:
            self.resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.incident_id is not None:
            result['incidentId'] = self.incident_id

        if self.incident_resource_id is not None:
            result['incidentResourceId'] = self.incident_resource_id

        if self.resource is not None:
            result['resource'] = self.resource.to_map()

        if self.source is not None:
            result['source'] = self.source

        if self.time is not None:
            result['time'] = self.time

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')

        if m.get('incidentResourceId') is not None:
            self.incident_resource_id = m.get('incidentResourceId')

        if m.get('resource') is not None:
            temp_model = main_models.IncidentResourceDetail()
            self.resource = temp_model.from_map(m.get('resource'))

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

