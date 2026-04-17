# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTopicConfigRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        instance_id: str = None,
        region_id: str = None,
        topic: str = None,
        value: str = None,
    ):
        # The key of the topic configuration.
        # 
        # *   For reserved instances, you can modify only the configurations of the topics that use local storage.
        # *   For serverless instances, you can modify the configurations of all topics.
        # *   Reserved instances whose topics use local storage support the following keys: retention.ms, max.message.bytes, replications, message.timestamp.type, and message.timestamp.difference.max.ms.``
        # *   Serverless instances support the following keys: retention.hours, max.message.bytes, message.timestamp.type, message.timestamp.difference.max.ms.
        # 
        # This parameter is required.
        self.config = config
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The topic name.
        # 
        # This parameter is required.
        self.topic = topic
        # The value of the topic configuration.
        # 
        # *   Serverless instances support the following values:
        # 
        #     *   `retention.hours`: the message retention period. Value type: string. Valid values: 24 to 8760.
        #     *   `max.message.bytes`: the maximum size of a sent message. Value type: string. Valid values: 1048576 to 10485760.
        #     *   `message.timestamp.type`: the timestamp type of a message. Valid values: CreateTime and LogAppendTime. The value CreateTime specifies the timestamp that is specified by the producer when the message is sent. The value LogAppendTime specifies the time when the broker appends the message to its log. If you do not specify this parameter, the time when the message is created on the client is used.
        #     *   `message.timestamp.difference.max.ms`: the maximum positive or negative difference allowed between the timestamp when the broker receives a message and the timestamp specified in the message. If you set message.timestamp.type to CreateTime, **a message is rejected** if the difference in timestamp exceeds the threshold. If you set message.timestamp.type to LogAppendTime, this configuration does not take effect.
        # 
        # *   Reserved instances support the following values:
        # 
        #     *   `retention.ms`: the message retention period. Value type: string. Valid values: 3600000 to 31536000000.
        #     *   `max.message.bytes`: the maximum size of a sent message. Value type: string. Valid values: 1048576 to 10485760.
        #     *   `replications`: the number of replicas. Value type: string. Valid values: 1 to 3.
        #     *   `message.timestamp.type`: the timestamp type of a message. Valid values: CreateTime and LogAppendTime. The value CreateTime specifies the timestamp that is specified by the producer when the message is sent. The value LogAppendTime specifies the time when the broker appends the message to its log. If you do not specify this parameter, the time when the message is created on the client is used.
        #     *   `message.timestamp.difference.max.ms`: the maximum positive or negative difference allowed between the timestamp when the broker receives a message and the timestamp specified in the message. If you set message.timestamp.type to CreateTime, **a message is rejected** if the difference in timestamp exceeds the threshold. If you set message.timestamp.type to LogAppendTime, this configuration does not take effect.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

