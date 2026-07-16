# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_eas20210701 import models as main_models
from darabonba.model import DaraModel

class CreateGroupRequest(DaraModel):
    def __init__(
        self,
        labels: Dict[str, str] = None,
        name: str = None,
        network: main_models.CreateGroupRequestNetwork = None,
        work_space_id: str = None,
    ):
        # The user-defined labels.
        self.labels = labels
        # The name of the group.
        self.name = name
        # The virtual private cloud (VPC) configuration.
        self.network = network
        # The workspace ID.
        self.work_space_id = work_space_id

    def validate(self):
        if self.network:
            self.network.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.labels is not None:
            result['Labels'] = self.labels

        if self.name is not None:
            result['Name'] = self.name

        if self.network is not None:
            result['Network'] = self.network.to_map()

        if self.work_space_id is not None:
            result['WorkSpaceId'] = self.work_space_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Network') is not None:
            temp_model = main_models.CreateGroupRequestNetwork()
            self.network = temp_model.from_map(m.get('Network'))

        if m.get('WorkSpaceId') is not None:
            self.work_space_id = m.get('WorkSpaceId')

        return self

class CreateGroupRequestNetwork(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The dedicated gateway ID.
        self.gateway_id = gateway_id
        # The security group ID.
        self.security_group_id = security_group_id
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

