# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateJobShrinkRequest(DaraModel):
    def __init__(
        self,
        dependency_policy_shrink: str = None,
        deployment_policy_shrink: str = None,
        job_description: str = None,
        job_name: str = None,
        job_scheduler: str = None,
        security_policy_shrink: str = None,
        tasks_shrink: str = None,
    ):
        # Dependency policy.
        self.dependency_policy_shrink = dependency_policy_shrink
        # The resource deployment policy.
        self.deployment_policy_shrink = deployment_policy_shrink
        # The description of the job.
        self.job_description = job_description
        # The job name. The name must be 2 to 64 characters in length and can contain letters, digits, and Chinese characters. It can contain hyphens (-) and underscores (_).
        # 
        # This parameter is required.
        self.job_name = job_name
        # The type of the job scheduler.
        # 
        # *   HPC
        # *   K8S
        # 
        # Default value: HPC
        self.job_scheduler = job_scheduler
        # The security policy.
        self.security_policy_shrink = security_policy_shrink
        # The list of tasks. Only one task is supported.
        # 
        # This parameter is required.
        self.tasks_shrink = tasks_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dependency_policy_shrink is not None:
            result['DependencyPolicy'] = self.dependency_policy_shrink

        if self.deployment_policy_shrink is not None:
            result['DeploymentPolicy'] = self.deployment_policy_shrink

        if self.job_description is not None:
            result['JobDescription'] = self.job_description

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_scheduler is not None:
            result['JobScheduler'] = self.job_scheduler

        if self.security_policy_shrink is not None:
            result['SecurityPolicy'] = self.security_policy_shrink

        if self.tasks_shrink is not None:
            result['Tasks'] = self.tasks_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DependencyPolicy') is not None:
            self.dependency_policy_shrink = m.get('DependencyPolicy')

        if m.get('DeploymentPolicy') is not None:
            self.deployment_policy_shrink = m.get('DeploymentPolicy')

        if m.get('JobDescription') is not None:
            self.job_description = m.get('JobDescription')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobScheduler') is not None:
            self.job_scheduler = m.get('JobScheduler')

        if m.get('SecurityPolicy') is not None:
            self.security_policy_shrink = m.get('SecurityPolicy')

        if m.get('Tasks') is not None:
            self.tasks_shrink = m.get('Tasks')

        return self

