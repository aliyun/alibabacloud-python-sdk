# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ScaleoutApplicationWithNewInstancesResponseBody(DaraModel):
    def __init__(
        self,
        change_order_id: str = None,
        code: int = None,
        instance_ids: List[str] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The ID of the change process for the scale-out.
        self.change_order_id = change_order_id
        # The HTTP status code that is returned.
        self.code = code
        # The IDs of ECS instances.
        self.instance_ids = instance_ids
        # The additional information that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id

        if self.code is not None:
            result['Code'] = self.code

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

