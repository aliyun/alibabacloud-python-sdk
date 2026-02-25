# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableSSLConnectionRequest(DaraModel):
    def __init__(
        self,
        custom_sslcertificate: str = None,
        enable_custom: bool = None,
        instance_id: str = None,
        renewal: bool = None,
        ssl_key_password: str = None,
        ssl_keystore_password: str = None,
    ):
        self.custom_sslcertificate = custom_sslcertificate
        self.enable_custom = enable_custom
        self.instance_id = instance_id
        self.renewal = renewal
        self.ssl_key_password = ssl_key_password
        self.ssl_keystore_password = ssl_keystore_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_sslcertificate is not None:
            result['CustomSSLCertificate'] = self.custom_sslcertificate

        if self.enable_custom is not None:
            result['EnableCustom'] = self.enable_custom

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.renewal is not None:
            result['Renewal'] = self.renewal

        if self.ssl_key_password is not None:
            result['SslKeyPassword'] = self.ssl_key_password

        if self.ssl_keystore_password is not None:
            result['SslKeystorePassword'] = self.ssl_keystore_password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomSSLCertificate') is not None:
            self.custom_sslcertificate = m.get('CustomSSLCertificate')

        if m.get('EnableCustom') is not None:
            self.enable_custom = m.get('EnableCustom')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Renewal') is not None:
            self.renewal = m.get('Renewal')

        if m.get('SslKeyPassword') is not None:
            self.ssl_key_password = m.get('SslKeyPassword')

        if m.get('SslKeystorePassword') is not None:
            self.ssl_keystore_password = m.get('SslKeystorePassword')

        return self

