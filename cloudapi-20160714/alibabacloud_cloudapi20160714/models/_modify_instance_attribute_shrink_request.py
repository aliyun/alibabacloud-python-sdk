# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceAttributeShrinkRequest(DaraModel):
    def __init__(
        self,
        delete_vpc_ip_block: str = None,
        egress_ipv_6enable: str = None,
        https_policy: str = None,
        ipv6enabled: str = None,
        instance_id: str = None,
        instance_name: str = None,
        intranet_segments: str = None,
        maintain_end_time: str = None,
        maintain_start_time: str = None,
        to_connect_vpc_ip_block_shrink: str = None,
        token: str = None,
        vpc_slb_intranet_enable: str = None,
    ):
        # If delete VPC Ip block.
        self.delete_vpc_ip_block = delete_vpc_ip_block
        # If enable outbound IPv6 Traffic.
        self.egress_ipv_6enable = egress_ipv_6enable
        # The HTTPS policy.
        self.https_policy = https_policy
        # If enable inbound IPv6 Traffic.
        self.ipv6enabled = ipv6enabled
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Instance Name
        self.instance_name = instance_name
        # Custom private CIDR block.
        self.intranet_segments = intranet_segments
        # Maintainable end time.
        self.maintain_end_time = maintain_end_time
        # Maintainable start time.
        self.maintain_start_time = maintain_start_time
        # The information about the CIDR block that API Gateway can use to access the virtual private cloud (VPC) of the backend service.
        self.to_connect_vpc_ip_block_shrink = to_connect_vpc_ip_block_shrink
        # The token of the request.
        self.token = token
        # Specifies whether to enable the self-calling domain name.
        self.vpc_slb_intranet_enable = vpc_slb_intranet_enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_vpc_ip_block is not None:
            result['DeleteVpcIpBlock'] = self.delete_vpc_ip_block

        if self.egress_ipv_6enable is not None:
            result['EgressIpv6Enable'] = self.egress_ipv_6enable

        if self.https_policy is not None:
            result['HttpsPolicy'] = self.https_policy

        if self.ipv6enabled is not None:
            result['IPV6Enabled'] = self.ipv6enabled

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.intranet_segments is not None:
            result['IntranetSegments'] = self.intranet_segments

        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time

        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time

        if self.to_connect_vpc_ip_block_shrink is not None:
            result['ToConnectVpcIpBlock'] = self.to_connect_vpc_ip_block_shrink

        if self.token is not None:
            result['Token'] = self.token

        if self.vpc_slb_intranet_enable is not None:
            result['VpcSlbIntranetEnable'] = self.vpc_slb_intranet_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteVpcIpBlock') is not None:
            self.delete_vpc_ip_block = m.get('DeleteVpcIpBlock')

        if m.get('EgressIpv6Enable') is not None:
            self.egress_ipv_6enable = m.get('EgressIpv6Enable')

        if m.get('HttpsPolicy') is not None:
            self.https_policy = m.get('HttpsPolicy')

        if m.get('IPV6Enabled') is not None:
            self.ipv6enabled = m.get('IPV6Enabled')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('IntranetSegments') is not None:
            self.intranet_segments = m.get('IntranetSegments')

        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')

        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')

        if m.get('ToConnectVpcIpBlock') is not None:
            self.to_connect_vpc_ip_block_shrink = m.get('ToConnectVpcIpBlock')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('VpcSlbIntranetEnable') is not None:
            self.vpc_slb_intranet_enable = m.get('VpcSlbIntranetEnable')

        return self

