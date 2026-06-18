# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class E2BTemplateBuild(DaraModel):
    def __init__(
        self,
        build_id: str = None,
        cpu_count: int = None,
        created_at: str = None,
        disk_size_mb: int = None,
        envd_version: str = None,
        finished_at: str = None,
        memory_mb: int = None,
        status: str = None,
        updated_at: str = None,
    ):
        self.build_id = build_id
        self.cpu_count = cpu_count
        self.created_at = created_at
        self.disk_size_mb = disk_size_mb
        self.envd_version = envd_version
        self.finished_at = finished_at
        self.memory_mb = memory_mb
        self.status = status
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_id is not None:
            result['buildID'] = self.build_id

        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.disk_size_mb is not None:
            result['diskSizeMB'] = self.disk_size_mb

        if self.envd_version is not None:
            result['envdVersion'] = self.envd_version

        if self.finished_at is not None:
            result['finishedAt'] = self.finished_at

        if self.memory_mb is not None:
            result['memoryMB'] = self.memory_mb

        if self.status is not None:
            result['status'] = self.status

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildID') is not None:
            self.build_id = m.get('buildID')

        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('diskSizeMB') is not None:
            self.disk_size_mb = m.get('diskSizeMB')

        if m.get('envdVersion') is not None:
            self.envd_version = m.get('envdVersion')

        if m.get('finishedAt') is not None:
            self.finished_at = m.get('finishedAt')

        if m.get('memoryMB') is not None:
            self.memory_mb = m.get('memoryMB')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

