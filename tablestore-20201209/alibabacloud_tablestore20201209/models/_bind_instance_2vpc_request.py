# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindInstance2VpcRequest(DaraModel):
    def __init__(
        self,
        instance_name: str = None,
        instance_vpc_name: str = None,
        virtual_switch_id: str = None,
        vpc_id: str = None,
    ):
        # This parameter is required.
        self.instance_name = instance_name
        # This parameter is required.
        self.instance_vpc_name = instance_vpc_name
        # This parameter is required.
        self.virtual_switch_id = virtual_switch_id
        # VPC ID
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_vpc_name is not None:
            result['InstanceVpcName'] = self.instance_vpc_name

        if self.virtual_switch_id is not None:
            result['VirtualSwitchId'] = self.virtual_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceVpcName') is not None:
            self.instance_vpc_name = m.get('InstanceVpcName')

        if m.get('VirtualSwitchId') is not None:
            self.virtual_switch_id = m.get('VirtualSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

