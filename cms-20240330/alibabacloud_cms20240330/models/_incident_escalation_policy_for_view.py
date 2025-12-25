# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class IncidentEscalationPolicyForView(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        enable: bool = None,
        escalation_stage_list: List[main_models.IncidentEscalationStageForView] = None,
        name: str = None,
        owner_type: str = None,
        region_id: str = None,
        source: str = None,
        sync_from_type: str = None,
        update_time: str = None,
        user_id: str = None,
        uuid: str = None,
        workspace: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.enable = enable
        self.escalation_stage_list = escalation_stage_list
        # This parameter is required.
        self.name = name
        self.owner_type = owner_type
        self.region_id = region_id
        self.source = source
        self.sync_from_type = sync_from_type
        self.update_time = update_time
        self.user_id = user_id
        self.uuid = uuid
        self.workspace = workspace

    def validate(self):
        if self.escalation_stage_list:
            for v1 in self.escalation_stage_list:
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

        if self.enable is not None:
            result['enable'] = self.enable

        result['escalationStageList'] = []
        if self.escalation_stage_list is not None:
            for k1 in self.escalation_stage_list:
                result['escalationStageList'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.owner_type is not None:
            result['ownerType'] = self.owner_type

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.source is not None:
            result['source'] = self.source

        if self.sync_from_type is not None:
            result['syncFromType'] = self.sync_from_type

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.uuid is not None:
            result['uuid'] = self.uuid

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        self.escalation_stage_list = []
        if m.get('escalationStageList') is not None:
            for k1 in m.get('escalationStageList'):
                temp_model = main_models.IncidentEscalationStageForView()
                self.escalation_stage_list.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('ownerType') is not None:
            self.owner_type = m.get('ownerType')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('syncFromType') is not None:
            self.sync_from_type = m.get('syncFromType')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

