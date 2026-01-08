# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAckClustersRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_spec: str = None,
        connector_status: str = None,
        member_uid: str = None,
        page_no: str = None,
        page_size: str = None,
        region_no: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_spec = cluster_spec
        self.connector_status = connector_status
        self.member_uid = member_uid
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec

        if self.connector_status is not None:
            result['ConnectorStatus'] = self.connector_status

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterSpec') is not None:
            self.cluster_spec = m.get('ClusterSpec')

        if m.get('ConnectorStatus') is not None:
            self.connector_status = m.get('ConnectorStatus')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        return self

