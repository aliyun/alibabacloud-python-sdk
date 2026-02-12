# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OnsTrendTopicInputTpsRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        instance_id: str = None,
        period: int = None,
        topic: str = None,
        type: int = None,
    ):
        # The timestamp that indicates the beginning of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The timestamp that indicates the end of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the instance to which the topic you want to query belongs.
        self.instance_id = instance_id
        # The sampling period. Unit: minutes. Valid values: 1, 5, and 10.
        self.period = period
        # The name of the topic that you want to query.
        # 
        # This parameter is required.
        self.topic = topic
        # The type of information that you want to query. Valid values:
        # 
        # *   **0**: the number of messages that are published to the topic during each sampling period.
        # *   **1**: the TPS for message publishing in the topic during each sampling period.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.period is not None:
            result['Period'] = self.period

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

