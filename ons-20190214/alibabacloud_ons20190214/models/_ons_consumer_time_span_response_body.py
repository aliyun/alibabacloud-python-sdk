# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ons20190214 import models as main_models
from darabonba.model import DaraModel

class OnsConsumerTimeSpanResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.OnsConsumerTimeSpanResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.OnsConsumerTimeSpanResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class OnsConsumerTimeSpanResponseBodyData(DaraModel):
    def __init__(
        self,
        consume_time_stamp: int = None,
        instance_id: str = None,
        max_time_stamp: int = None,
        min_time_stamp: int = None,
        topic: str = None,
    ):
        # The most recent point in time when a message in the topic was consumed by the customer group.
        self.consume_time_stamp = consume_time_stamp
        # The ID of the instance to which the consumer group belongs.
        self.instance_id = instance_id
        # The point in time when the most recently stored message was published to the topic.
        self.max_time_stamp = max_time_stamp
        # The point in time when the earliest stored message was published to the topic.
        self.min_time_stamp = min_time_stamp
        # The name of the topic that you want to query.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consume_time_stamp is not None:
            result['ConsumeTimeStamp'] = self.consume_time_stamp

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_time_stamp is not None:
            result['MaxTimeStamp'] = self.max_time_stamp

        if self.min_time_stamp is not None:
            result['MinTimeStamp'] = self.min_time_stamp

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumeTimeStamp') is not None:
            self.consume_time_stamp = m.get('ConsumeTimeStamp')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxTimeStamp') is not None:
            self.max_time_stamp = m.get('MaxTimeStamp')

        if m.get('MinTimeStamp') is not None:
            self.min_time_stamp = m.get('MinTimeStamp')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

