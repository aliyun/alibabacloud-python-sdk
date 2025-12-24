# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateResourceDLinkRequest(DaraModel):
    def __init__(
        self,
        destination_cidrs: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        v_switch_id_list: List[str] = None,
    ):
        # The CIDR blocks of the clients that you want to connect to. After this parameter is specified, the CIDR blocks are added to the back-to-origin route of the server. Either this parameter or the VSwitchIdList parameter can be used to determine CIDR blocks.
        self.destination_cidrs = destination_cidrs
        # The ID of the security group to which the Elastic Compute Service (ECS) instance belongs.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # The ID of the peer primary vSwitch. After this parameter is specified, an elastic network interface (ENI) is created in the VSwitch.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The vSwitches of the clients that you want to connect to. After this parameter is specified, the CIDR blocks of these vSwitches are added to the back-to-origin route of the server.
        self.v_switch_id_list = v_switch_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidrs is not None:
            result['DestinationCIDRs'] = self.destination_cidrs

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_id_list is not None:
            result['VSwitchIdList'] = self.v_switch_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCIDRs') is not None:
            self.destination_cidrs = m.get('DestinationCIDRs')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchIdList') is not None:
            self.v_switch_id_list = m.get('VSwitchIdList')

        return self

