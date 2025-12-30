# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssumeRoleForWorkloadIdentityRequest(DaraModel):
    def __init__(
        self,
        duration_seconds: int = None,
        policy: str = None,
        role_session_name: str = None,
        workload_access_token: str = None,
    ):
        self.duration_seconds = duration_seconds
        self.policy = policy
        self.role_session_name = role_session_name
        self.workload_access_token = workload_access_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration_seconds is not None:
            result['DurationSeconds'] = self.duration_seconds

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.role_session_name is not None:
            result['RoleSessionName'] = self.role_session_name

        if self.workload_access_token is not None:
            result['WorkloadAccessToken'] = self.workload_access_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DurationSeconds') is not None:
            self.duration_seconds = m.get('DurationSeconds')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('RoleSessionName') is not None:
            self.role_session_name = m.get('RoleSessionName')

        if m.get('WorkloadAccessToken') is not None:
            self.workload_access_token = m.get('WorkloadAccessToken')

        return self

