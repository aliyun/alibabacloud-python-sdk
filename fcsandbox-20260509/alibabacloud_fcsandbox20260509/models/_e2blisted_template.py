# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class E2BListedTemplate(DaraModel):
    def __init__(
        self,
        build_status: str = None,
        category: str = None,
        cpu_count: int = None,
        created_at: str = None,
        function_name: str = None,
        log_configuration: main_models.LogConfiguration = None,
        memory_mb: int = None,
        names: List[str] = None,
        public: bool = None,
        resource_group_id: str = None,
        status_reason: str = None,
        tags: List[main_models.E2BTemplateTag] = None,
        team_id: str = None,
        team_name: str = None,
        template_id: str = None,
        updated_at: str = None,
        user_id: str = None,
    ):
        self.build_status = build_status
        self.category = category
        self.cpu_count = cpu_count
        self.created_at = created_at
        self.function_name = function_name
        self.log_configuration = log_configuration
        self.memory_mb = memory_mb
        self.names = names
        self.public = public
        self.resource_group_id = resource_group_id
        self.status_reason = status_reason
        self.tags = tags
        self.team_id = team_id
        self.team_name = team_name
        self.template_id = template_id
        self.updated_at = updated_at
        self.user_id = user_id

    def validate(self):
        if self.log_configuration:
            self.log_configuration.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_status is not None:
            result['buildStatus'] = self.build_status

        if self.category is not None:
            result['category'] = self.category

        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.function_name is not None:
            result['functionName'] = self.function_name

        if self.log_configuration is not None:
            result['logConfiguration'] = self.log_configuration.to_map()

        if self.memory_mb is not None:
            result['memoryMB'] = self.memory_mb

        if self.names is not None:
            result['names'] = self.names

        if self.public is not None:
            result['public'] = self.public

        if self.resource_group_id is not None:
            result['resourceGroupID'] = self.resource_group_id

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.team_name is not None:
            result['teamName'] = self.team_name

        if self.template_id is not None:
            result['templateID'] = self.template_id

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.user_id is not None:
            result['userID'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildStatus') is not None:
            self.build_status = m.get('buildStatus')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')

        if m.get('logConfiguration') is not None:
            temp_model = main_models.LogConfiguration()
            self.log_configuration = temp_model.from_map(m.get('logConfiguration'))

        if m.get('memoryMB') is not None:
            self.memory_mb = m.get('memoryMB')

        if m.get('names') is not None:
            self.names = m.get('names')

        if m.get('public') is not None:
            self.public = m.get('public')

        if m.get('resourceGroupID') is not None:
            self.resource_group_id = m.get('resourceGroupID')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.E2BTemplateTag()
                self.tags.append(temp_model.from_map(k1))

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('teamName') is not None:
            self.team_name = m.get('teamName')

        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('userID') is not None:
            self.user_id = m.get('userID')

        return self

