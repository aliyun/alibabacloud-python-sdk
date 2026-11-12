# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sandbox20260820 import models as main_models
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
        resource_tags: List[main_models.E2BSnapshotResourceTags] = None,
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
        # The resource tags.
        self.resource_tags = resource_tags
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
        if self.resource_tags:
            for v1 in self.resource_tags:
                 if v1:
                    v1.validate()

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

        if self.resource_tags is not None:
            result['resourceTags'] = []
            for k1 in self.resource_tags:
                result['resourceTags'].append(k1.to_map() if k1 else None)

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

        if m.get('resourceTags') is not None:
            self.resource_tags = []
            for k1 in m.get('resourceTags'):
                temp_model = main_models.E2BSnapshotResourceTags()
                self.resource_tags.append(temp_model.from_map(k1))

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

class E2BSnapshotResourceTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key

        if self.tag_value is not None:
            result['tagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')

        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')

        return self

