# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        instance_name: str = None,
        instance_spec: str = None,
        network_type: str = None,
        payment_type: str = None,
        vpc_id: str = None,
        zones_shrink: str = None,
    ):
        self.client_token = client_token
        # This parameter is required.
        self.instance_name = instance_name
        # This parameter is required.
        self.instance_spec = instance_spec
        # This parameter is required.
        self.network_type = network_type
        self.payment_type = payment_type
        # This parameter is required.
        self.vpc_id = vpc_id
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

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zones_shrink is not None:
            result['Zones'] = self.zones_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('Zones') is not None:
            self.zones_shrink = m.get('Zones')

        return self

