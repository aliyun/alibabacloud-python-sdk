# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class E2BListedSandbox(DaraModel):
    def __init__(
        self,
        alias: str = None,
        client_id: str = None,
        cpu_count: int = None,
        disk_size_mb: int = None,
        end_at: str = None,
        envd_version: str = None,
        memory_mb: int = None,
        metadata: Dict[str, str] = None,
        sandbox_id: str = None,
        started_at: str = None,
        state: str = None,
        template_id: str = None,
        template_name: str = None,
        volume_mounts: List[main_models.E2BVolumeMount] = None,
    ):
        self.alias = alias
        self.client_id = client_id
        self.cpu_count = cpu_count
        self.disk_size_mb = disk_size_mb
        self.end_at = end_at
        self.envd_version = envd_version
        self.memory_mb = memory_mb
        self.metadata = metadata
        self.sandbox_id = sandbox_id
        self.started_at = started_at
        self.state = state
        self.template_id = template_id
        self.template_name = template_name
        self.volume_mounts = volume_mounts

    def validate(self):
        if self.volume_mounts:
            for v1 in self.volume_mounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.client_id is not None:
            result['clientID'] = self.client_id

        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count

        if self.disk_size_mb is not None:
            result['diskSizeMB'] = self.disk_size_mb

        if self.end_at is not None:
            result['endAt'] = self.end_at

        if self.envd_version is not None:
            result['envdVersion'] = self.envd_version

        if self.memory_mb is not None:
            result['memoryMB'] = self.memory_mb

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.sandbox_id is not None:
            result['sandboxID'] = self.sandbox_id

        if self.started_at is not None:
            result['startedAt'] = self.started_at

        if self.state is not None:
            result['state'] = self.state

        if self.template_id is not None:
            result['templateID'] = self.template_id

        if self.template_name is not None:
            result['templateName'] = self.template_name

        result['volumeMounts'] = []
        if self.volume_mounts is not None:
            for k1 in self.volume_mounts:
                result['volumeMounts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('clientID') is not None:
            self.client_id = m.get('clientID')

        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')

        if m.get('diskSizeMB') is not None:
            self.disk_size_mb = m.get('diskSizeMB')

        if m.get('endAt') is not None:
            self.end_at = m.get('endAt')

        if m.get('envdVersion') is not None:
            self.envd_version = m.get('envdVersion')

        if m.get('memoryMB') is not None:
            self.memory_mb = m.get('memoryMB')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('sandboxID') is not None:
            self.sandbox_id = m.get('sandboxID')

        if m.get('startedAt') is not None:
            self.started_at = m.get('startedAt')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        self.volume_mounts = []
        if m.get('volumeMounts') is not None:
            for k1 in m.get('volumeMounts'):
                temp_model = main_models.E2BVolumeMount()
                self.volume_mounts.append(temp_model.from_map(k1))

        return self

