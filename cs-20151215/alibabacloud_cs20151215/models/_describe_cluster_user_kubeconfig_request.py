# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeClusterUserKubeconfigRequest(DaraModel):
    def __init__(
        self,
        private_ip_address: bool = None,
        temporary_duration_minutes: int = None,
    ):
        # Specifies whether to obtain the kubeconfig file that is used to connect to the cluster over the internal network. You can obtain the terminal ID by calling one of the following operations:
        # 
        # *   `true`: obtains the kubeconfig file that is used to connect to the master instance over the internal network.
        # *   `false`: obtains the kubeconfig file that is used to connect to the master instance over the Internet.
        # 
        # Default value: `false`
        self.private_ip_address = private_ip_address
        # The validity period of the temporary kubeconfig file. Unit: minutes. Valid values: 15 to 4320 (3 days).
        # 
        # **
        # 
        # **Usage notes** If you do not specify this parameter, the system specifies a longer validity period. The validity period is returned in the `expiration` parameter.
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

