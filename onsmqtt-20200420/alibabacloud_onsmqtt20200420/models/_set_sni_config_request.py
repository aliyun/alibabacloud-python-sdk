# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetSniConfigRequest(DaraModel):
    def __init__(
        self,
        default_certificate: str = None,
        mqtt_instance_id: str = None,
        sni_config: str = None,
    ):
        # The default certificate. This certificate is returned if no matching domain name is found in the server certificate list.
        # 
        # This parameter is required.
        self.default_certificate = default_certificate
        # The instance ID.
        # 
        # This parameter is required.
        self.mqtt_instance_id = mqtt_instance_id
        # The Server Name Indication (SNI) configuration that maps domain names to certificates. Format: DomainName#CertificateID#Password(if any);DomainName#CertificateID#Password(if any)
        self.sni_config = sni_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_certificate is not None:
            result['DefaultCertificate'] = self.default_certificate

        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id

        if self.sni_config is not None:
            result['SniConfig'] = self.sni_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultCertificate') is not None:
            self.default_certificate = m.get('DefaultCertificate')

        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')

        if m.get('SniConfig') is not None:
            self.sni_config = m.get('SniConfig')

        return self

