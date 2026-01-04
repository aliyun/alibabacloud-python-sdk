# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceStatusResponseBody(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_status: int = None,
        request_id: str = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id
        # The status of the instance. Valid values:
        # 
        # *   **1**: normal
        # *   **2**: expired
        # *   **3**: overdue
        # *   **4**: released
        self.instance_status = instance_status
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

