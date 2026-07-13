# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        instance_name: str = None,
        network_type: str = None,
        zones_shrink: str = None,
    ):
        self.client_token = client_token
        # This parameter is required.
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.network_type = network_type
        self.zones_shrink = zones_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.zones_shrink is not None:
            result['Zones'] = self.zones_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Zones') is not None:
            self.zones_shrink = m.get('Zones')

        return self

