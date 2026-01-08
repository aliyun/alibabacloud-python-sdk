# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVpcFirewallPrecheckRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        lang: str = None,
        member_uid: str = None,
        network_instance_type: str = None,
        region: str = None,
        transit_router_id: str = None,
        vpc_id: str = None,
    ):
        self.cen_id = cen_id
        self.lang = lang
        self.member_uid = member_uid
        self.network_instance_type = network_instance_type
        self.region = region
        self.transit_router_id = transit_router_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.network_instance_type is not None:
            result['NetworkInstanceType'] = self.network_instance_type

        if self.region is not None:
            result['Region'] = self.region

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('NetworkInstanceType') is not None:
            self.network_instance_type = m.get('NetworkInstanceType')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

