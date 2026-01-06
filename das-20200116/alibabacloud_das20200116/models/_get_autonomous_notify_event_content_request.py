# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAutonomousNotifyEventContentRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        span_id: str = None,
        context: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The unique identifier of the event. You can call the [GetAutonomousNotifyEventsInRange](https://help.aliyun.com/document_detail/288371.html) operation to query the unique identifier returned by the SpanId response parameter.
        # 
        # This parameter is required.
        self.span_id = span_id
        # The reserved parameter.
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.span_id is not None:
            result['SpanId'] = self.span_id

        if self.context is not None:
            result['__context'] = self.context

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('SpanId') is not None:
            self.span_id = m.get('SpanId')

        if m.get('__context') is not None:
            self.context = m.get('__context')

        return self

