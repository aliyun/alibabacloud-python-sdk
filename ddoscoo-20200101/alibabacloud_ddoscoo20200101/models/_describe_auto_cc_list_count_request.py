# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAutoCcListCountRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        query_type: str = None,
    ):
        # The ID of the instance.
        # 
        # > You can call the **DescribeInstanceIds** operation to query the IDs of all instances.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The mode of how an IP address is added to the whitelist or blacklist. Valid values:
        # 
        # *   **manual**: manually added
        # *   **auto**: automatically added
        self.query_type = query_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        return self

