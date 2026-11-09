# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RegisterCaCertificateRequest(DaraModel):
    def __init__(
        self,
        ca_content: str = None,
        ca_name: str = None,
        mqtt_instance_id: str = None,
        verification_content: str = None,
    ):
        # The content of the CA certificate that you want to register with an ApsaraMQ for MQTT broker.
        # 
        # > In the example, 
        #  indicates a line feed.
        # 
        # This parameter is required.
        self.ca_content = ca_content
        # The name of the CA certificate that you want to register with an ApsaraMQ for MQTT broker.
        # 
        # This parameter is required.
        self.ca_name = ca_name
        # The ID of the ApsaraMQ for MQTT instance to which you want to bind the CA certificate.
        # 
        # This parameter is required.
        self.mqtt_instance_id = mqtt_instance_id
        # The content of the validation certificate issued by the CA certificate that you want to register with an ApsaraMQ for MQTT broker. The validation certificate must be used together with the registration code of the CA certificate to verify the private key of the CA certificate.
        # 
        # > In the example, 
        #  indicates a line feed.
        # 
        # This parameter is required.
        self.verification_content = verification_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ca_content is not None:
            result['CaContent'] = self.ca_content

        if self.ca_name is not None:
            result['CaName'] = self.ca_name

        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id

        if self.verification_content is not None:
            result['VerificationContent'] = self.verification_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaContent') is not None:
            self.ca_content = m.get('CaContent')

        if m.get('CaName') is not None:
            self.ca_name = m.get('CaName')

        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')

        if m.get('VerificationContent') is not None:
            self.verification_content = m.get('VerificationContent')

        return self

