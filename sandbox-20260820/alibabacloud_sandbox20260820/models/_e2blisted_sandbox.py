# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class E2BListedSandbox(DaraModel):
    def __init__(
        self,
        cpu_count: int = None,
        disk_size_mb: int = None,
        end_at: str = None,
        generation: int = None,
        memory_mb: int = None,
        metadata: Dict[str, str] = None,
        resource_group_id: str = None,
        resource_tags: List[main_models.E2BListedSandboxResourceTags] = None,
        sandbox_id: str = None,
        snapshot_id: str = None,
        started_at: str = None,
        state: str = None,
        team_id: str = None,
        team_name: str = None,
        team_plan: str = None,
        template_id: str = None,
        template_name: str = None,
        user_id: str = None,
    ):
        # The number of vCPUs.
        self.cpu_count = cpu_count
        # The ephemeral disk size.
        self.disk_size_mb = disk_size_mb
        # The end time.
        self.end_at = end_at
        # The sandbox version.
        self.generation = generation
        # The memory size.
        self.memory_mb = memory_mb
        # The metadata.
        self.metadata = metadata
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The resource tags.
        self.resource_tags = resource_tags
        # The sandbox ID.
        self.sandbox_id = sandbox_id
        # The snapshot ID.
        self.snapshot_id = snapshot_id
        # The start time.
        self.started_at = started_at
        # The sandbox state. Valid values:
        # - running: Running.
        # - pausing: Pausing.
        # - paused: Paused.
        # - resuming: Resuming.
        # - pause_fail: Pause failed.
        # - resume_fail: Resume failed.
        # - snapshotting: Creating a snapshot.
        # - snapshot_failed: Snapshot creation failed.
        # - terminated: Terminated.
        self.state = state
        # The unique identifier of the team.
        self.team_id = team_id
        # The team name.
        self.team_name = team_name
        # The QoS version.
        self.team_plan = team_plan
        # The unique identifier of the template.
        self.template_id = template_id
        # The template name.
        self.template_name = template_name
        # The UID of the creator.
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

        if self.disk_size_mb is not None:
            result['diskSizeMB'] = self.disk_size_mb

        if self.end_at is not None:
            result['endAt'] = self.end_at

        if self.generation is not None:
            result['generation'] = self.generation

        if self.memory_mb is not None:
            result['memoryMB'] = self.memory_mb

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.resource_group_id is not None:
            result['resourceGroupID'] = self.resource_group_id

        if self.resource_tags is not None:
            result['resourceTags'] = []
            for k1 in self.resource_tags:
                result['resourceTags'].append(k1.to_map() if k1 else None)

        if self.sandbox_id is not None:
            result['sandboxID'] = self.sandbox_id

        if self.snapshot_id is not None:
            result['snapshotID'] = self.snapshot_id

        if self.started_at is not None:
            result['startedAt'] = self.started_at

        if self.state is not None:
            result['state'] = self.state

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.team_name is not None:
            result['teamName'] = self.team_name

        if self.team_plan is not None:
            result['teamPlan'] = self.team_plan

        if self.template_id is not None:
            result['templateID'] = self.template_id

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.user_id is not None:
            result['userID'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')

        if m.get('diskSizeMB') is not None:
            self.disk_size_mb = m.get('diskSizeMB')

        if m.get('endAt') is not None:
            self.end_at = m.get('endAt')

        if m.get('generation') is not None:
            self.generation = m.get('generation')

        if m.get('memoryMB') is not None:
            self.memory_mb = m.get('memoryMB')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('resourceGroupID') is not None:
            self.resource_group_id = m.get('resourceGroupID')

        if m.get('resourceTags') is not None:
            self.resource_tags = []
            for k1 in m.get('resourceTags'):
                temp_model = main_models.E2BListedSandboxResourceTags()
                self.resource_tags.append(temp_model.from_map(k1))

        if m.get('sandboxID') is not None:
            self.sandbox_id = m.get('sandboxID')

        if m.get('snapshotID') is not None:
            self.snapshot_id = m.get('snapshotID')

        if m.get('startedAt') is not None:
            self.started_at = m.get('startedAt')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('teamName') is not None:
            self.team_name = m.get('teamName')

        if m.get('teamPlan') is not None:
            self.team_plan = m.get('teamPlan')

        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('userID') is not None:
            self.user_id = m.get('userID')

        return self

class E2BListedSandboxResourceTags(DaraModel):
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

