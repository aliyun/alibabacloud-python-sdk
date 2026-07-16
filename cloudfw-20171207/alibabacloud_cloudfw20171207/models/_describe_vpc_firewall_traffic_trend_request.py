# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVpcFirewallTrafficTrendRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        lang: str = None,
        peer_vpc_id: str = None,
        private_ip: str = None,
        start_time: str = None,
        vpc_id: str = None,
    ):
        # The end time. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The language of the request and response. Valid values:
        # - **zh** (default): Chinese
        # - **en**: English
        self.lang = lang
        # The instance ID of the peer VPC instance.
        self.peer_vpc_id = peer_vpc_id
        # The private IP address.
        self.private_ip = private_ip
        # The start time. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The instance ID of the VPC-connected instance.
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
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.peer_vpc_id is not None:
            result['PeerVpcId'] = self.peer_vpc_id

        if self.private_ip is not None:
            result['PrivateIP'] = self.private_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PeerVpcId') is not None:
            self.peer_vpc_id = m.get('PeerVpcId')

        if m.get('PrivateIP') is not None:
            self.private_ip = m.get('PrivateIP')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

