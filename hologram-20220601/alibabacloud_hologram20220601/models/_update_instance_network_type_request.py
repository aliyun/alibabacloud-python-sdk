# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateInstanceNetworkTypeRequest(DaraModel):
    def __init__(
        self,
        any_tunnel_to_single_tunnel: str = None,
        network_types: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        vpc_owner_id: str = None,
        vpc_region_id: str = None,
    ):
        # Specifies whether to change the network type from AnyTunnel to SingleTunnel. This parameter is invalid for new instances. For new instances, this parameter is set to null by default.
        # 
        # Valid values:
        # 
        # *   others/null: The network type is not changed from AnyTunnel to SingleTunnel.
        # *   true: The network type is changed from AnyTunnel to SingleTunnel.
        self.any_tunnel_to_single_tunnel = any_tunnel_to_single_tunnel
        # A list of network types that you want to enable. The network types are randomly ordered in the list. For example, the Internet, Intranet, and VPCSingleTunnel network types are enabled. If you want to disable the Internet type, set this parameter to Intranet,VPCSingleTunnel.
        # 
        # Valid values:
        # 
        # *   VPCSingleTunnel: virtual private cloud (VPC).
        # *   Intranet: internal network.
        # *   VPCAnyTunnel: compatibility requirements. This value is not supported by new instances.
        # *   Internet: Internet.
        self.network_types = network_types
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The ID of the Alibaba Cloud account to which the VPC belongs.
        self.vpc_owner_id = vpc_owner_id
        # The region in which the VPC resides.
        self.vpc_region_id = vpc_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.any_tunnel_to_single_tunnel is not None:
            result['anyTunnelToSingleTunnel'] = self.any_tunnel_to_single_tunnel

        if self.network_types is not None:
            result['networkTypes'] = self.network_types

        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        if self.vpc_owner_id is not None:
            result['vpcOwnerId'] = self.vpc_owner_id

        if self.vpc_region_id is not None:
            result['vpcRegionId'] = self.vpc_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('anyTunnelToSingleTunnel') is not None:
            self.any_tunnel_to_single_tunnel = m.get('anyTunnelToSingleTunnel')

        if m.get('networkTypes') is not None:
            self.network_types = m.get('networkTypes')

        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        if m.get('vpcOwnerId') is not None:
            self.vpc_owner_id = m.get('vpcOwnerId')

        if m.get('vpcRegionId') is not None:
            self.vpc_region_id = m.get('vpcRegionId')

        return self

