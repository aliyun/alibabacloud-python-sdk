# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateQosResponseBody(DaraModel):
    def __init__(
        self,
        qos_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the QoS policy.
        self.qos_id = qos_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group to which the QoS policy belongs.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.qos_id is not None:
            result['QosId'] = self.qos_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QosId') is not None:
            self.qos_id = m.get('QosId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

