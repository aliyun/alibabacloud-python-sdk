# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class IncidentPlanStruct(DaraModel):
    def __init__(
        self,
        auto_recover_seconds: int = None,
        close_expire: int = None,
        corporation: List[main_models.IncidentPlanCorporationStruct] = None,
        description: str = None,
        escalation_id: List[str] = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        group_by: List[main_models.IncidentPlanFieldPath] = None,
        incident_plan_id: str = None,
        name: str = None,
        resource_filed: List[main_models.IncidentPlanFieldPath] = None,
        status: str = None,
        user_id: int = None,
        workspace: str = None,
    ):
        self.auto_recover_seconds = auto_recover_seconds
        self.close_expire = close_expire
        self.corporation = corporation
        self.description = description
        self.escalation_id = escalation_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.group_by = group_by
        self.incident_plan_id = incident_plan_id
        self.name = name
        self.resource_filed = resource_filed
        self.status = status
        self.user_id = user_id
        self.workspace = workspace

    def validate(self):
        if self.corporation:
            for v1 in self.corporation:
                 if v1:
                    v1.validate()
        if self.group_by:
            for v1 in self.group_by:
                 if v1:
                    v1.validate()
        if self.resource_filed:
            for v1 in self.resource_filed:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_recover_seconds is not None:
            result['autoRecoverSeconds'] = self.auto_recover_seconds

        if self.close_expire is not None:
            result['closeExpire'] = self.close_expire

        result['corporation'] = []
        if self.corporation is not None:
            for k1 in self.corporation:
                result['corporation'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        if self.escalation_id is not None:
            result['escalationId'] = self.escalation_id

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        result['groupBy'] = []
        if self.group_by is not None:
            for k1 in self.group_by:
                result['groupBy'].append(k1.to_map() if k1 else None)

        if self.incident_plan_id is not None:
            result['incidentPlanId'] = self.incident_plan_id

        if self.name is not None:
            result['name'] = self.name

        result['resourceFiled'] = []
        if self.resource_filed is not None:
            for k1 in self.resource_filed:
                result['resourceFiled'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRecoverSeconds') is not None:
            self.auto_recover_seconds = m.get('autoRecoverSeconds')

        if m.get('closeExpire') is not None:
            self.close_expire = m.get('closeExpire')

        self.corporation = []
        if m.get('corporation') is not None:
            for k1 in m.get('corporation'):
                temp_model = main_models.IncidentPlanCorporationStruct()
                self.corporation.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('escalationId') is not None:
            self.escalation_id = m.get('escalationId')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        self.group_by = []
        if m.get('groupBy') is not None:
            for k1 in m.get('groupBy'):
                temp_model = main_models.IncidentPlanFieldPath()
                self.group_by.append(temp_model.from_map(k1))

        if m.get('incidentPlanId') is not None:
            self.incident_plan_id = m.get('incidentPlanId')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.resource_filed = []
        if m.get('resourceFiled') is not None:
            for k1 in m.get('resourceFiled'):
                temp_model = main_models.IncidentPlanFieldPath()
                self.resource_filed.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

