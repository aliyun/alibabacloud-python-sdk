# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterVipRequest(DaraModel):
    def __init__(
        self,
        connect_string: str = None,
        dbcluster_id: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
    ):
        # The endpoint of the cluster.
        self.connect_string = connect_string
        # The cluster ID.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the information about all AnalyticDB for MySQL Data Lakehouse Edition clusters within a region, including cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The VPC ID.
        # 
        # > 
        # 
        # *   The new **VPC** must reside in the same region as the cluster.
        # 
        # This parameter is required.
        self.vpcid = vpcid
        # The vSwitch ID.
        # 
        # > 
        # 
        # *   The new vSwitch must reside in the same zone as the cluster.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connect_string is not None:
            result['ConnectString'] = self.connect_string

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.vpcid is not None:
            result['VPCId'] = self.vpcid

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectString') is not None:
            self.connect_string = m.get('ConnectString')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

