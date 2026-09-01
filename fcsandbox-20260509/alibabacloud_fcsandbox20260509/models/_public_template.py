# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class PublicTemplate(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        name: str = None,
        resource_group_id: str = None,
        runtime_config: main_models.PublicTemplateRuntimeConfig = None,
        status: main_models.PublicTemplateStatus = None,
        team_id: str = None,
        team_name: str = None,
        template_id: str = None,
    ):
        self.created_time = created_time
        self.name = name
        self.resource_group_id = resource_group_id
        self.runtime_config = runtime_config
        self.status = status
        self.team_id = team_id
        self.team_name = team_name
        self.template_id = template_id

    def validate(self):
        if self.runtime_config:
            self.runtime_config.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.name is not None:
            result['name'] = self.name

        if self.resource_group_id is not None:
            result['resourceGroupID'] = self.resource_group_id

        if self.runtime_config is not None:
            result['runtimeConfig'] = self.runtime_config.to_map()

        if self.status is not None:
            result['status'] = self.status.to_map()

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.team_name is not None:
            result['teamName'] = self.team_name

        if self.template_id is not None:
            result['templateID'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resourceGroupID') is not None:
            self.resource_group_id = m.get('resourceGroupID')

        if m.get('runtimeConfig') is not None:
            temp_model = main_models.PublicTemplateRuntimeConfig()
            self.runtime_config = temp_model.from_map(m.get('runtimeConfig'))

        if m.get('status') is not None:
            temp_model = main_models.PublicTemplateStatus()
            self.status = temp_model.from_map(m.get('status'))

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('teamName') is not None:
            self.team_name = m.get('teamName')

        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')

        return self

