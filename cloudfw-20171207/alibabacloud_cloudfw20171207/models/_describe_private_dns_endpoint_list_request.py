# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePrivateDnsEndpointListRequest(DaraModel):
    def __init__(
        self,
        access_instance_id: str = None,
        access_instance_name: str = None,
        firewall_type: str = None,
        member_uid: int = None,
        page_no: int = None,
        page_size: int = None,
        region_no: str = None,
        status: str = None,
        vpc_id: str = None,
    ):
        self.access_instance_id = access_instance_id
        self.access_instance_name = access_instance_name
        self.firewall_type = firewall_type
        self.member_uid = member_uid
        self.page_no = page_no
        self.page_size = page_size
        self.region_no = region_no
        self.status = status
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_instance_id is not None:
            result['AccessInstanceId'] = self.access_instance_id

        if self.access_instance_name is not None:
            result['AccessInstanceName'] = self.access_instance_name

        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.status is not None:
            result['Status'] = self.status

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessInstanceId') is not None:
            self.access_instance_id = m.get('AccessInstanceId')

        if m.get('AccessInstanceName') is not None:
            self.access_instance_name = m.get('AccessInstanceName')

        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

