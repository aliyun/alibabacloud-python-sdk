# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class IncidentEscalationStruct(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        incident_escalation_id: str = None,
        modify_time: int = None,
        name: str = None,
        region_id: str = None,
        stage: List[main_models.IncidentEscalationStageStruct] = None,
        workspace: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.incident_escalation_id = incident_escalation_id
        self.modify_time = modify_time
        self.name = name
        self.region_id = region_id
        self.stage = stage
        self.workspace = workspace

    def validate(self):
        if self.stage:
            for v1 in self.stage:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.incident_escalation_id is not None:
            result['incidentEscalationId'] = self.incident_escalation_id

        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time

        if self.name is not None:
            result['name'] = self.name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        result['stage'] = []
        if self.stage is not None:
            for k1 in self.stage:
                result['stage'].append(k1.to_map() if k1 else None)

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('incidentEscalationId') is not None:
            self.incident_escalation_id = m.get('incidentEscalationId')

        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        self.stage = []
        if m.get('stage') is not None:
            for k1 in m.get('stage'):
                temp_model = main_models.IncidentEscalationStageStruct()
                self.stage.append(temp_model.from_map(k1))

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

