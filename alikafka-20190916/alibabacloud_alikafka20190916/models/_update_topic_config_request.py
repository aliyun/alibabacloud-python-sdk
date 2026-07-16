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
        # - You can modify the configurations only for topics that use the local storage engine on reserved instances. You cannot modify the configurations for topics that use the cloud storage engine.
        # 
        # - You can modify the configurations of topics for Serverless instances.
        # 
        # - For `local topics` on reserved instances, the supported keys are \\`retention.ms\\`, \\`max.message.bytes\\`, \\`message.timestamp.type\\`, and \\`message.timestamp.difference.max.ms\\`.
        # 
        # - For Serverless instances, the supported keys are \\`retention.hours\\`, \\`max.message.bytes\\`, \\`message.timestamp.type\\`, and \\`message.timestamp.difference.max.ms\\`.
        # 
        # This parameter is required.
        self.config = config
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The topic name.
        # 
        # This parameter is required.
        self.topic = topic
        # The value of the topic configuration.
        # 
        # - The following configurations are supported for Serverless instances:
        # 
        #   - `retention.hours` specifies the message retention period. The value must be a string. The value must be in the range of 24 to 8,760.
        # 
        #   - `max.message.bytes` specifies the maximum message size. The value must be a string. The value must be in the range of 1,048,576 to 10,485,760.
        # 
        #   - `message.timestamp.type` specifies the message timestamp type. \\`CreateTime\\` indicates the timestamp that is specified by the producer when the message is sent. If no timestamp is specified, the time when the message is created on the client is used. \\`LogAppendTime\\` indicates the time when the message is stored on the server. Valid values: \\`CreateTime\\` and \\`LogAppendTime\\`.
        # 
        #   - `message.timestamp.difference.max.ms` specifies the maximum allowed difference between the timestamp of the server that receives the message and the timestamp specified in the message. If \\`message.timestamp.type\\` is set to \\`CreateTime\\` and the time difference exceeds this threshold, **the message is rejected**. This configuration does not take effect if \\`message.timestamp.type\\` is set to \\`LogAppendTime\\`.
        # 
        # - The following configurations are supported for reserved instances:
        # 
        #   - `retention.ms` specifies the message retention period. The value must be a string. The value must be in the range of 3,600,000 to 31,536,000,000.
        # 
        #   - `max.message.bytes` specifies the maximum message size. The value must be a string. The value must be in the range of 1,048,576 to 10,485,760.
        # 
        #   - `message.timestamp.type` specifies the message timestamp type. \\`CreateTime\\` indicates the timestamp that is specified by the producer when the message is sent. If no timestamp is specified, the time when the message is created on the client is used. \\`LogAppendTime\\` indicates the time when the message is stored on the server. Valid values: \\`CreateTime\\` and \\`LogAppendTime\\`.
        # 
        #   - `message.timestamp.difference.max.ms` specifies the maximum allowed difference between the timestamp of the server that receives the message and the timestamp specified in the message. If \\`message.timestamp.type\\` is set to \\`CreateTime\\` and the time difference exceeds this threshold, **the message is rejected**. This configuration does not take effect if \\`message.timestamp.type\\` is set to \\`LogAppendTime\\`.
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

