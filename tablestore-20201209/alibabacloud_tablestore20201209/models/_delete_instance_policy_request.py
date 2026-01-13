# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteInstancePolicyRequest(DaraModel):
    def __init__(
        self,
        instance_name: str = None,
        policy_version: int = None,
    ):
        # The name of the instance.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The version of the instance policy.
        # 
        # This parameter is required.
        self.policy_version = policy_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.policy_version is not None:
            result['PolicyVersion'] = self.policy_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PolicyVersion') is not None:
            self.policy_version = m.get('PolicyVersion')

        return self

