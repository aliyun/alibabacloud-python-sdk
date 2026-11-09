# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InactivateCaCertificateRequest(DaraModel):
    def __init__(
        self,
        mqtt_instance_id: str = None,
        sn: str = None,
    ):
        # The ID of the ApsaraMQ for MQTT instance to which the CA certificate is attached.
        # 
        # This parameter is required.
        self.mqtt_instance_id = mqtt_instance_id
        # The serial number (SN) of the CA certificate that you want to unregister. The SN uniquely identifies a CA certificate.
        # 
        # The value can be up to 128 bytes long.
        # 
        # This parameter is required.
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id

        if self.sn is not None:
            result['Sn'] = self.sn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')

        if m.get('Sn') is not None:
            self.sn = m.get('Sn')

        return self

