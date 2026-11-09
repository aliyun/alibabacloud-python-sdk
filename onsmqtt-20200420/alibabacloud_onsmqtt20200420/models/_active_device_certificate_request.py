# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ActiveDeviceCertificateRequest(DaraModel):
    def __init__(
        self,
        ca_sn: str = None,
        device_sn: str = None,
        mqtt_instance_id: str = None,
    ):
        # The SN of the CA certificate to which the device certificate to be activated belongs. The SN uniquely identifies a CA certificate.
        # Valid values: up to 128 bytes.
        # 
        # This parameter is required.
        self.ca_sn = ca_sn
        # The serial number (SN) of the device certificate to be activated. The SN uniquely identifies a device certificate.
        # 
        # This parameter is required.
        self.device_sn = device_sn
        # The instance ID to which the device certificate is attached, which is the instance ID of MSMQ for MQTT.
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
        if self.ca_sn is not None:
            result['CaSn'] = self.ca_sn

        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn

        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaSn') is not None:
            self.ca_sn = m.get('CaSn')

        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')

        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')

        return self

