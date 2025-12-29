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
        # Specifies whether to obtain the kubeconfig file used to connect to the cluster over the internal network. Valid values:
        # 
        # *   `true`: Obtain the kubeconfig file used to connect to the cluster over the internal network.
        # *   `false`: Obtain the kubeconfig file used to connect to the cluster over the Internet.
        # 
        # Default value: `false`.
        self.private_ip_address = private_ip_address
        # The validity period of the temporary kubeconfig file. Unit: minutes.
        # 
        # Valid values: 15 to 4320 (three days).
        # 
        # > If you leave this parameter empty, the system sets a longer validity period and returns the value in the expiration parameter of the response.
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

