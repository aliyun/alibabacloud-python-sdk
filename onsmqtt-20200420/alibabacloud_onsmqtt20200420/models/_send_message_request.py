# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendMessageRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        mqtt_topic: str = None,
        payload: str = None,
    ):
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can view the instance ID in the **Basic Information** section on the **Instance Details** page that corresponds to the instance in the [ApsaraMQ for MQTT console](https://mqtt.console.aliyun.com).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The topic to which you want to send a message on the ApsaraMQ for MQTT instance.
        # 
        # This parameter is required.
        self.mqtt_topic = mqtt_topic
        # The message content, which is the payload of the message. We recommend that you encode the content in Base64 to prevent non-printable characters from being transmitted.
        # 
        # This parameter is required.
        self.payload = payload

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mqtt_topic is not None:
            result['MqttTopic'] = self.mqtt_topic

        if self.payload is not None:
            result['Payload'] = self.payload

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MqttTopic') is not None:
            self.mqtt_topic = m.get('MqttTopic')

        if m.get('Payload') is not None:
            self.payload = m.get('Payload')

        return self

