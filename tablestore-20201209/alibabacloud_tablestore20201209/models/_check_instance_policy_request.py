# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckInstancePolicyRequest(DaraModel):
    def __init__(
        self,
        instance_name: str = None,
        policy: str = None,
    ):
        # The name of the instance.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The instance policy in the JSON format.
        # 
        # This parameter is required.
        self.policy = policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.policy is not None:
            result['Policy'] = self.policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        return self

