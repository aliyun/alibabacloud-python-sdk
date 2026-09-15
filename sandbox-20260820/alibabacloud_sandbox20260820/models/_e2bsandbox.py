# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class E2BSandbox(DaraModel):
    def __init__(
        self,
        access_endpoint: str = None,
        allow_internet_access: bool = None,
        cpu_count: int = None,
        disk_size_mb: int = None,
        domain: str = None,
        end_at: str = None,
        env_vars: Dict[str, str] = None,
        envd_access_token: str = None,
        fc_function_name: str = None,
        fc_instance_id: str = None,
        fc_session_id: str = None,
        generation: int = None,
        memory_mb: int = None,
        metadata: Dict[str, str] = None,
        network: main_models.E2BNetwork = None,
        resource_group_id: str = None,
        runtime: main_models.InnerSandboxRuntimeConfig = None,
        sandbox_id: str = None,
        started_at: str = None,
        state: str = None,
        team_id: str = None,
        team_name: str = None,
        team_plan: str = None,
        template_id: str = None,
        template_name: str = None,
        user_id: str = None,
        volume_mounts: main_models.InnerSandboxVolumeMount = None,
    ):
        self.access_endpoint = access_endpoint
        self.allow_internet_access = allow_internet_access
        self.cpu_count = cpu_count
        self.disk_size_mb = disk_size_mb
        self.domain = domain
        self.end_at = end_at
        self.env_vars = env_vars
        self.envd_access_token = envd_access_token
        self.fc_function_name = fc_function_name
        self.fc_instance_id = fc_instance_id
        self.fc_session_id = fc_session_id
        self.generation = generation
        self.memory_mb = memory_mb
        self.metadata = metadata
        self.network = network
        self.resource_group_id = resource_group_id
        self.runtime = runtime
        self.sandbox_id = sandbox_id
        self.started_at = started_at
        self.state = state
        self.team_id = team_id
        self.team_name = team_name
        self.team_plan = team_plan
        self.template_id = template_id
        self.template_name = template_name
        self.user_id = user_id
        self.volume_mounts = volume_mounts

    def validate(self):
        if self.network:
            self.network.validate()
        if self.runtime:
            self.runtime.validate()
        if self.volume_mounts:
            self.volume_mounts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_endpoint is not None:
            result['accessEndpoint'] = self.access_endpoint

        if self.allow_internet_access is not None:
            result['allowInternetAccess'] = self.allow_internet_access

        if self.cpu_count is not None:
            result['cpuCount'] = self.cpu_count

        if self.disk_size_mb is not None:
            result['diskSizeMB'] = self.disk_size_mb

        if self.domain is not None:
            result['domain'] = self.domain

        if self.end_at is not None:
            result['endAt'] = self.end_at

        if self.env_vars is not None:
            result['envVars'] = self.env_vars

        if self.envd_access_token is not None:
            result['envdAccessToken'] = self.envd_access_token

        if self.fc_function_name is not None:
            result['fcFunctionName'] = self.fc_function_name

        if self.fc_instance_id is not None:
            result['fcInstanceID'] = self.fc_instance_id

        if self.fc_session_id is not None:
            result['fcSessionID'] = self.fc_session_id

        if self.generation is not None:
            result['generation'] = self.generation

        if self.memory_mb is not None:
            result['memoryMB'] = self.memory_mb

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.network is not None:
            result['network'] = self.network.to_map()

        if self.resource_group_id is not None:
            result['resourceGroupID'] = self.resource_group_id

        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()

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

        if self.team_plan is not None:
            result['teamPlan'] = self.team_plan

        if self.template_id is not None:
            result['templateID'] = self.template_id

        if self.template_name is not None:
            result['templateName'] = self.template_name

        if self.user_id is not None:
            result['userID'] = self.user_id

        if self.volume_mounts is not None:
            result['volumeMounts'] = self.volume_mounts.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessEndpoint') is not None:
            self.access_endpoint = m.get('accessEndpoint')

        if m.get('allowInternetAccess') is not None:
            self.allow_internet_access = m.get('allowInternetAccess')

        if m.get('cpuCount') is not None:
            self.cpu_count = m.get('cpuCount')

        if m.get('diskSizeMB') is not None:
            self.disk_size_mb = m.get('diskSizeMB')

        if m.get('domain') is not None:
            self.domain = m.get('domain')

        if m.get('endAt') is not None:
            self.end_at = m.get('endAt')

        if m.get('envVars') is not None:
            self.env_vars = m.get('envVars')

        if m.get('envdAccessToken') is not None:
            self.envd_access_token = m.get('envdAccessToken')

        if m.get('fcFunctionName') is not None:
            self.fc_function_name = m.get('fcFunctionName')

        if m.get('fcInstanceID') is not None:
            self.fc_instance_id = m.get('fcInstanceID')

        if m.get('fcSessionID') is not None:
            self.fc_session_id = m.get('fcSessionID')

        if m.get('generation') is not None:
            self.generation = m.get('generation')

        if m.get('memoryMB') is not None:
            self.memory_mb = m.get('memoryMB')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('network') is not None:
            temp_model = main_models.E2BNetwork()
            self.network = temp_model.from_map(m.get('network'))

        if m.get('resourceGroupID') is not None:
            self.resource_group_id = m.get('resourceGroupID')

        if m.get('runtime') is not None:
            temp_model = main_models.InnerSandboxRuntimeConfig()
            self.runtime = temp_model.from_map(m.get('runtime'))

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

        if m.get('teamPlan') is not None:
            self.team_plan = m.get('teamPlan')

        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')

        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')

        if m.get('userID') is not None:
            self.user_id = m.get('userID')

        if m.get('volumeMounts') is not None:
            temp_model = main_models.InnerSandboxVolumeMount()
            self.volume_mounts = temp_model.from_map(m.get('volumeMounts'))

        return self

