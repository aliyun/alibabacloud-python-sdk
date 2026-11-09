# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRegisterCodeRequest(DaraModel):
    def __init__(
        self,
        mqtt_instance_id: str = None,
    ):
        # The ID of the ApsaraMQ for MQTT instance.
        # 
        # This parameter is required.
        self.mqtt_instance_id = mqtt_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')

        return self

