# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class Snapshot(DaraModel):
    def __init__(
        self,
        artifact_disk_total_size_in_b: int = None,
        artifact_disk_used_size_in_b: int = None,
        artifact_mem_cache_size_in_b: int = None,
        artifact_mem_total_size_in_b: int = None,
        artifact_mem_used_size_in_b: int = None,
        cpu: int = None,
        created_time: str = None,
        description: str = None,
        disk_size_mb: int = None,
        envs: Dict[str, str] = None,
        expired_time: str = None,
        function_name: str = None,
        image_digest: str = None,
        image_repository: str = None,
        memory_mb: int = None,
        os_type: str = None,
        qualifier: str = None,
        ready_command: str = None,
        resolved_version: str = None,
        snapshot_id: str = None,
        source_session_id: str = None,
        start_command: str = None,
        status: str = None,
    ):
        # This parameter is required.
        self.artifact_disk_total_size_in_b = artifact_disk_total_size_in_b
        # This parameter is required.
        self.artifact_disk_used_size_in_b = artifact_disk_used_size_in_b
        # This parameter is required.
        self.artifact_mem_cache_size_in_b = artifact_mem_cache_size_in_b
        # This parameter is required.
        self.artifact_mem_total_size_in_b = artifact_mem_total_size_in_b
        # This parameter is required.
        self.artifact_mem_used_size_in_b = artifact_mem_used_size_in_b
        # This parameter is required.
        self.cpu = cpu
        # This parameter is required.
        self.created_time = created_time
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.disk_size_mb = disk_size_mb
        # This parameter is required.
        self.envs = envs
        # This parameter is required.
        self.expired_time = expired_time
        # This parameter is required.
        self.function_name = function_name
        # This parameter is required.
        self.image_digest = image_digest
        # This parameter is required.
        self.image_repository = image_repository
        # This parameter is required.
        self.memory_mb = memory_mb
        # This parameter is required.
        self.os_type = os_type
        # This parameter is required.
        self.qualifier = qualifier
        # This parameter is required.
        self.ready_command = ready_command
        self.resolved_version = resolved_version
        # This parameter is required.
        self.snapshot_id = snapshot_id
        # This parameter is required.
        self.source_session_id = source_session_id
        # This parameter is required.
        self.start_command = start_command
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_disk_total_size_in_b is not None:
            result['artifactDiskTotalSizeInB'] = self.artifact_disk_total_size_in_b

        if self.artifact_disk_used_size_in_b is not None:
            result['artifactDiskUsedSizeInB'] = self.artifact_disk_used_size_in_b

        if self.artifact_mem_cache_size_in_b is not None:
            result['artifactMemCacheSizeInB'] = self.artifact_mem_cache_size_in_b

        if self.artifact_mem_total_size_in_b is not None:
            result['artifactMemTotalSizeInB'] = self.artifact_mem_total_size_in_b

        if self.artifact_mem_used_size_in_b is not None:
            result['artifactMemUsedSizeInB'] = self.artifact_mem_used_size_in_b

        if self.cpu is not None:
            result['cpu'] = self.cpu

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.description is not None:
            result['description'] = self.description

        if self.disk_size_mb is not None:
            result['diskSizeMB'] = self.disk_size_mb

        if self.envs is not None:
            result['envs'] = self.envs

        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time

        if self.function_name is not None:
            result['functionName'] = self.function_name

        if self.image_digest is not None:
            result['imageDigest'] = self.image_digest

        if self.image_repository is not None:
            result['imageRepository'] = self.image_repository

        if self.memory_mb is not None:
            result['memoryMB'] = self.memory_mb

        if self.os_type is not None:
            result['osType'] = self.os_type

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        if self.ready_command is not None:
            result['readyCommand'] = self.ready_command

        if self.resolved_version is not None:
            result['resolvedVersion'] = self.resolved_version

        if self.snapshot_id is not None:
            result['snapshotId'] = self.snapshot_id

        if self.source_session_id is not None:
            result['sourceSessionId'] = self.source_session_id

        if self.start_command is not None:
            result['startCommand'] = self.start_command

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifactDiskTotalSizeInB') is not None:
            self.artifact_disk_total_size_in_b = m.get('artifactDiskTotalSizeInB')

        if m.get('artifactDiskUsedSizeInB') is not None:
            self.artifact_disk_used_size_in_b = m.get('artifactDiskUsedSizeInB')

        if m.get('artifactMemCacheSizeInB') is not None:
            self.artifact_mem_cache_size_in_b = m.get('artifactMemCacheSizeInB')

        if m.get('artifactMemTotalSizeInB') is not None:
            self.artifact_mem_total_size_in_b = m.get('artifactMemTotalSizeInB')

        if m.get('artifactMemUsedSizeInB') is not None:
            self.artifact_mem_used_size_in_b = m.get('artifactMemUsedSizeInB')

        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('diskSizeMB') is not None:
            self.disk_size_mb = m.get('diskSizeMB')

        if m.get('envs') is not None:
            self.envs = m.get('envs')

        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')

        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')

        if m.get('imageDigest') is not None:
            self.image_digest = m.get('imageDigest')

        if m.get('imageRepository') is not None:
            self.image_repository = m.get('imageRepository')

        if m.get('memoryMB') is not None:
            self.memory_mb = m.get('memoryMB')

        if m.get('osType') is not None:
            self.os_type = m.get('osType')

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        if m.get('readyCommand') is not None:
            self.ready_command = m.get('readyCommand')

        if m.get('resolvedVersion') is not None:
            self.resolved_version = m.get('resolvedVersion')

        if m.get('snapshotId') is not None:
            self.snapshot_id = m.get('snapshotId')

        if m.get('sourceSessionId') is not None:
            self.source_session_id = m.get('sourceSessionId')

        if m.get('startCommand') is not None:
            self.start_command = m.get('startCommand')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

