# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAckClusterConnectorsRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        connector_name: str = None,
        lang: str = None,
        member_uid: str = None,
        page_no: str = None,
        page_size: str = None,
        region_no: str = None,
        vpc_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.connector_name = connector_name
        self.lang = lang
        self.member_uid = member_uid
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.region_no = region_no
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.connector_name is not None:
            result['ConnectorName'] = self.connector_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ConnectorName') is not None:
            self.connector_name = m.get('ConnectorName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

