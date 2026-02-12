# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OnsTraceGetResultRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        query_id: str = None,
        topic: str = None,
    ):
        # The ID of the instance to which the message you want to query belongs.
        self.instance_id = instance_id
        # The ID of the task that was created to query the trace of the message.
        # 
        # This parameter is required.
        self.query_id = query_id
        # The topic to which the message belongs.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.query_id is not None:
            result['QueryId'] = self.query_id

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

