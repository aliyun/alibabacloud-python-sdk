# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class E2BSnapshot(DaraModel):
    def __init__(
        self,
        cpu_count: float = None,
        created_time: str = None,
        expired_time: str = None,
        memory_mb: int = None,
        name: str = None,
        resource_group_id: str = None,
        snapshot_id: str = None,
        source_sandbox_id: str = None,
        status: str = None,
        tag: str = None,
        team_id: str = None,
        team_name: str = None,
        user_id: str = None,
    ):
        # The CPU specifications of the snapshot.
        self.cpu_count = cpu_count
        # The creation time of the snapshot.
        self.created_time = created_time
        # The expiration time of the snapshot.
        self.expired_time = expired_time
        # The memory specifications of the snapshot.
        self.memory_mb = memory_mb
        # The short name of the snapshot.
        self.name = name
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The snapshot ID.
        self.snapshot_id = snapshot_id
        # The source sandbox ID.
        self.source_sandbox_id = source_sandbox_id
        # The snapshot status.
        self.status = status
        # The snapshot tag.
        self.tag = tag
        # The team ID.
        self.team_id = team_id
        # The team name.
        self.team_name = team_name
        # The Alibaba Cloud account ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time

        if self.memory_mb is not None:
            result['memoryMB'] = self.memory_mb

        if self.name is not None:
            result['name'] = self.name

        if self.resource_group_id is not None:
            result['resourceGroupID'] = self.resource_group_id

        if self.snapshot_id is not None:
            result['snapshotID'] = self.snapshot_id

        if self.source_sandbox_id is not None:
            result['sourceSandboxID'] = self.source_sandbox_id

        if self.status is not None:
            result['status'] = self.status

        if self.tag is not None:
            result['tag'] = self.tag

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.team_name is not None:
            result['teamName'] = self.team_name

        if self.user_id is not None:
            result['userID'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')

        if m.get('memoryMB') is not None:
            self.memory_mb = m.get('memoryMB')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resourceGroupID') is not None:
            self.resource_group_id = m.get('resourceGroupID')

        if m.get('snapshotID') is not None:
            self.snapshot_id = m.get('snapshotID')

        if m.get('sourceSandboxID') is not None:
            self.source_sandbox_id = m.get('sourceSandboxID')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('teamName') is not None:
            self.team_name = m.get('teamName')

        if m.get('userID') is not None:
            self.user_id = m.get('userID')

        return self

