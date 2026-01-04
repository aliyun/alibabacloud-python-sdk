# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddNetworkInterfaceToInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_start: bool = None,
        instance_id: str = None,
        networks: str = None,
    ):
        # Specifies whether to automatically restart the instance.
        self.auto_start = auto_start
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The network. The value is a JSON string. Only IPv6 is supported. Sample code of an IPv6 network: [{ "ipType": "public", "ipAddressType": "ipv6" }]
        # 
        # This parameter is required.
        self.networks = networks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_start is not None:
            result['AutoStart'] = self.auto_start

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.networks is not None:
            result['Networks'] = self.networks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoStart') is not None:
            self.auto_start = m.get('AutoStart')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Networks') is not None:
            self.networks = m.get('Networks')

        return self

