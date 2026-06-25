# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceLogRequest(DaraModel):
    def __init__(
        self,
        container_id: str = None,
        instance_id: str = None,
        previous: str = None,
    ):
        # The ID of the sidecar container. Call the [ListApplicationInstances](https://help.aliyun.com/document_detail/2834847.html) operation to obtain this ID.
        self.container_id = container_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether to view the log of the instance from before its last restart. Note: This parameter is active only if the instance was restarted.
        self.previous = previous

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_id is not None:
            result['ContainerId'] = self.container_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.previous is not None:
            result['Previous'] = self.previous

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Previous') is not None:
            self.previous = m.get('Previous')

        return self

