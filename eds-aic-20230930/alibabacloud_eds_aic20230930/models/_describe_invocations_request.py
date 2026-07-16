# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeInvocationsRequest(DaraModel):
    def __init__(
        self,
        instance_ids: List[str] = None,
        invocation_id: str = None,
    ):
        # The IDs of the cloud phone instances. A single request can query the execution results for up to 50 instances.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The ID of the command execution. Use this ID and the cloud phone instance ID to query the result of a command execution.
        # 
        # This parameter is required.
        self.invocation_id = invocation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.invocation_id is not None:
            result['InvocationId'] = self.invocation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('InvocationId') is not None:
            self.invocation_id = m.get('InvocationId')

        return self

