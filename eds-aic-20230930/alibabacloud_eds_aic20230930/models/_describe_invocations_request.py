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
        # The IDs of the cloud phone instances. You can specify a maximum of 50 cloud phone instances.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The ID of the execution. You can retrieve the output of a command once by using either the execution ID or the cloud phone instance ID.
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

