# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVpcFirewallZoneRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        environment: str = None,
        lang: str = None,
        member_uid: str = None,
        region_no: str = None,
        source_ip: str = None,
        transit_router_id: str = None,
    ):
        self.cen_id = cen_id
        self.environment = environment
        self.lang = lang
        self.member_uid = member_uid
        self.region_no = region_no
        self.source_ip = source_ip
        self.transit_router_id = transit_router_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.environment is not None:
            result['Environment'] = self.environment

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('Environment') is not None:
            self.environment = m.get('Environment')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

