# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSubaccountK8sClusterUserConfigRequest(DaraModel):
    def __init__(
        self,
        private_ip_address: bool = None,
        temporary_duration_minutes: int = None,
    ):
        # Specifies whether to obtain the internal network connection configuration. Valid values:
        # 
        # - `true`: Obtains only the KubeConfig credentials for internal network connections.
        # - `false`: Obtains only the KubeConfig credentials for public network connections.
        # 
        # Default value: `false`.
        self.private_ip_address = private_ip_address
        # The validity period of the temporary KubeConfig. Unit: minutes.
        # 
        # Valid values: [15, 4320], which is up to 3 days.
        # > If this parameter is not set, the system automatically determines a longer validity period. The specific expiration time is indicated by the value of the expiration field in the response.
        self.temporary_duration_minutes = temporary_duration_minutes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.temporary_duration_minutes is not None:
            result['TemporaryDurationMinutes'] = self.temporary_duration_minutes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('TemporaryDurationMinutes') is not None:
            self.temporary_duration_minutes = m.get('TemporaryDurationMinutes')

        return self

