# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupMachineStatusRequest(DaraModel):
    def __init__(
        self,
        policy_id: int = None,
        policy_version: str = None,
        uuid: str = None,
    ):
        # The ID of the anti-ransomware policy.
        # 
        # >  You can call the [DescribeBackupPolicies](~~DescribeBackupPolicies~~) operation to query the IDs of anti-ransomware policies.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The version of the anti-ransomware policy. Valid values:
        # 
        # *   **1.0.0**
        # *   **2.0.0**
        self.policy_version = policy_version
        # The UUID of the server.
        # 
        # >  You can call the [DescribeBackupPolicy](~~DescribeBackupPolicy~~) operation to query the UUIDs of servers.
        # 
        # This parameter is required.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyVersion') is not None:
            self.policy_version = m.get('PolicyVersion')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

