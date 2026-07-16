# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class E2BSandbox(DaraModel):
    def __init__(
        self,
        access_endpoint: str = None,
        cpu_count: int = None,
        disk_size_mb: int = None,
        domain: str = None,
        end_at: str = None,
        fc_function_name: str = None,
        fc_instance_id: str = None,
        fc_session_id: str = None,
        memory_mb: int = None,
        metadata: Dict[str, str] = None,
        resource_group_id: str = None,
        sandbox_id: str = None,
        started_at: str = None,
        state: str = None,
        team_id: str = None,
        team_name: str = None,
        template_id: str = None,
        template_name: str = None,
        user_id: str = None,
    ):
        self.access_endpoint = access_endpoint
        self.cpu_count = cpu_count
        self.disk_size_mb = disk_size_mb
        self.domain = domain
        self.end_at = end_at
        self.fc_function_name = fc_function_name
        self.fc_instance_id = fc_instance_id
        self.fc_session_id = fc_session_id
        self.memory_mb = memory_mb
        self.metadata = metadata
        self.resource_group_id = resource_group_id
        self.sandbox_id = sandbox_id
        self.started_at = started_at
        self.state = state
        self.team_id = team_id
        self.team_name = team_name
        self.template_id = template_id
        self.template_name = template_name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_endpoint is not None:
            result['accessEndpoint'] = self.access_endpoint

        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count

        if self.disk_size_mb is not None:
            result['diskSizeMB'] = self.disk_size_mb

        if self.domain is not None:
            result['domain'] = self.domain

        if self.end_at is not None:
            result['endAt'] = self.end_at

        if self.fc_function_name is not None:
            result['fcFunctionName'] = self.fc_function_name

        if self.fc_instance_id is not None:
            result['fcInstanceID'] = self.fc_instance_id

        if self.fc_session_id is not None:
            result['fcSessionID'] = self.fc_session_id

        if self.memory_mb is not None:
            result['memoryMB'] = self.memory_mb

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.resource_group_id is not None:
            result['resourceGroupID'] = self.resource_group_id

        if self.sandbox_id is not None:
            result['sandboxID'] = self.sandbox_id

        if self.started_at is not None:
            result['startedAt'] = self.started_at

        if self.state is not None:
            result['state'] = self.state

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.team_name is not None:
            result['teamName'] = self.team_name

        if self.template_id is not None:
            result['templateID'] = self.template_id

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.user_id is not None:
            result['userID'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessEndpoint') is not None:
            self.access_endpoint = m.get('accessEndpoint')

        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')

        if m.get('diskSizeMB') is not None:
            self.disk_size_mb = m.get('diskSizeMB')

        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('endAt') is not None:
            self.end_at = m.get('endAt')

        if m.get('fcFunctionName') is not None:
            self.fc_function_name = m.get('fcFunctionName')

        if m.get('fcInstanceID') is not None:
            self.fc_instance_id = m.get('fcInstanceID')

        if m.get('fcSessionID') is not None:
            self.fc_session_id = m.get('fcSessionID')

        if m.get('memoryMB') is not None:
            self.memory_mb = m.get('memoryMB')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('resourceGroupID') is not None:
            self.resource_group_id = m.get('resourceGroupID')

        if m.get('sandboxID') is not None:
            self.sandbox_id = m.get('sandboxID')

        if m.get('startedAt') is not None:
            self.started_at = m.get('startedAt')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('teamName') is not None:
            self.team_name = m.get('teamName')

        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('userID') is not None:
            self.user_id = m.get('userID')

        return self

