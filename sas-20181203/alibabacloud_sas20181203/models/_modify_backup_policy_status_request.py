# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBackupPolicyStatusRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        policy_version: str = None,
        status: str = None,
    ):
        # The ID of the anti-ransomware policy that you want to enable or shutdown.
        # 
        # This parameter is required.
        self.id = id
        # The version of the policy that you want to enable or disable. Set the value to **2.0.0**.
        self.policy_version = policy_version
        # Specifies whether to enable or disable the anti-ransomware policy. Valid values:
        # 
        # - **enabled**: Enables the anti-ransomware policy. After the policy is enabled, anti-ransomware can protect your server data by backing up data on specified servers based on your anti-ransomware policy.
        # - **disabled**: Disables the anti-ransomware policy. After the policy is disabled, running backup tasks are stopped.
        # 
        # > Backup tasks consume network bandwidth. Enable the policy during off-peak hours to execute data backup tasks.
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PolicyVersion') is not None:
            self.policy_version = m.get('PolicyVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

