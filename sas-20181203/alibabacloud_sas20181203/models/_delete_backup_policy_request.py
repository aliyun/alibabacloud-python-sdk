# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteBackupPolicyRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        policy_version: str = None,
    ):
        # The ID of the mitigation policies that you want to delete.
        # >Invoke the [DescribeBackupPolicies](~~DescribeBackupPolicies~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.id = id
        # The version of the mitigation policies that you want to delete. You can invoke the [DescribeBackupPolicies](~~DescribeBackupPolicies~~) operation to query this parameter. Valid values:
        # 
        # - **1.0.0**: The mitigation policies version is 1.0.0.
        # - **2.0.0**: The mitigation policies version is 2.0.0.
        self.policy_version = policy_version

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PolicyVersion') is not None:
            self.policy_version = m.get('PolicyVersion')

        return self

