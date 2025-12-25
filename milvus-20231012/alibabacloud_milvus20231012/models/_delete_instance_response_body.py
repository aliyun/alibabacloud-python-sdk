# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteInstanceResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
        order_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id
        self.order_id = order_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.order_id is not None:
            result['orderId'] = self.order_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

