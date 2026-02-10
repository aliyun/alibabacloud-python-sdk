# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UninstallBackupClientRequest(DaraModel):
    def __init__(
        self,
        policy_version: str = None,
        uuid: str = None,
        uuid_list: List[str] = None,
    ):
        # The version of the anti-ransomware policy. You can call the [DescribeBackupPolicies](~~DescribeBackupPolicies~~) operation to query the versions of anti-ransomware policies. Valid values:
        # 
        # *   **1.0.0**
        # *   **2.0.0**
        # 
        # This parameter is required.
        self.policy_version = policy_version
        # The UUID of the server from which you want to uninstall the anti-ransomware agent.
        # 
        # > You must specify at least one of the UuidList and Uuid parameters.
        self.uuid = uuid
        # The UUIDs of the servers from which you want to uninstall the anti-ransomware agent.
        # 
        # > You must specify at least one of the UuidList and Uuid parameters.
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyVersion') is not None:
            self.policy_version = m.get('PolicyVersion')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

