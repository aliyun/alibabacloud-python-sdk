# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteInstanceVpcEndpointLinkedVpcRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        module_name: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the module that you want to access. Valid values:
        # 
        # *   `Registry`: the image repository.
        # *   `Chart`: a Helm chart.
        self.module_name = module_name
        # The ID of the VPC.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The ID of the vSwitch.
        # 
        # This parameter is required.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

