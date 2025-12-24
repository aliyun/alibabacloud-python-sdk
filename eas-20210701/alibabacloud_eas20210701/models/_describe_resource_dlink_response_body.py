# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeResourceDLinkResponseBody(DaraModel):
    def __init__(
        self,
        aux_vswitch_list: List[str] = None,
        destination_cidrs: str = None,
        request_id: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The IDs of the secondary vSwitches that are directly connected.
        self.aux_vswitch_list = aux_vswitch_list
        # The CIDR blocks of the clients that you want to connect to. After this parameter is specified, the CIDR blocks are added to the back-to-origin route of the server. Either this parameter or the VSwitchIdList parameter can be used to determine CIDR blocks.
        self.destination_cidrs = destination_cidrs
        # The request ID.
        self.request_id = request_id
        # The ID of the security group that is directly connected.
        self.security_group_id = security_group_id
        # The ID of the primary vSwitch that is directly connected.
        self.v_switch_id = v_switch_id
        # The ID of the VPC that is directly connected.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aux_vswitch_list is not None:
            result['AuxVSwitchList'] = self.aux_vswitch_list

        if self.destination_cidrs is not None:
            result['DestinationCIDRs'] = self.destination_cidrs

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuxVSwitchList') is not None:
            self.aux_vswitch_list = m.get('AuxVSwitchList')

        if m.get('DestinationCIDRs') is not None:
            self.destination_cidrs = m.get('DestinationCIDRs')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

