# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class E2BListedTemplate(DaraModel):
    def __init__(
        self,
        aliases: List[str] = None,
        build_status: str = None,
        cpu_count: int = None,
        created_at: str = None,
        last_spawned_at: str = None,
        log_configuration: main_models.LogConfiguration = None,
        memory_mb: int = None,
        names: List[str] = None,
        public: bool = None,
        spawn_count: str = None,
        status_reason: str = None,
        tags: List[main_models.E2BTemplateTag] = None,
        template_id: str = None,
        updated_at: str = None,
    ):
        self.aliases = aliases
        self.build_status = build_status
        self.cpu_count = cpu_count
        self.created_at = created_at
        self.last_spawned_at = last_spawned_at
        self.log_configuration = log_configuration
        self.memory_mb = memory_mb
        self.names = names
        self.public = public
        self.spawn_count = spawn_count
        self.status_reason = status_reason
        self.tags = tags
        self.template_id = template_id
        self.updated_at = updated_at

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
        if self.aliases is not None:
            result['aliases'] = self.aliases

        if self.build_status is not None:
            result['buildStatus'] = self.build_status

        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.last_spawned_at is not None:
            result['lastSpawnedAt'] = self.last_spawned_at

        if self.log_configuration is not None:
            result['logConfiguration'] = self.log_configuration.to_map()

        if self.memory_mb is not None:
            result['memoryMB'] = self.memory_mb

        if self.names is not None:
            result['names'] = self.names

        if self.public is not None:
            result['public'] = self.public

        if self.spawn_count is not None:
            result['spawnCount'] = self.spawn_count

        if self.status_reason is not None:
            result['statusReason'] = self.status_reason

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.template_id is not None:
            result['templateID'] = self.template_id

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliases') is not None:
            self.aliases = m.get('aliases')

        if m.get('buildStatus') is not None:
            self.build_status = m.get('buildStatus')

        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('lastSpawnedAt') is not None:
            self.last_spawned_at = m.get('lastSpawnedAt')

        if m.get('logConfiguration') is not None:
            temp_model = main_models.LogConfiguration()
            self.log_configuration = temp_model.from_map(m.get('logConfiguration'))

        if m.get('memoryMB') is not None:
            self.memory_mb = m.get('memoryMB')

        if m.get('names') is not None:
            self.names = m.get('names')

        if m.get('public') is not None:
            self.public = m.get('public')

        if m.get('spawnCount') is not None:
            self.spawn_count = m.get('spawnCount')

        if m.get('statusReason') is not None:
            self.status_reason = m.get('statusReason')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.E2BTemplateTag()
                self.tags.append(temp_model.from_map(k1))

        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

