# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSQAConfigResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        group_name: str = None,
        request_id: str = None,
        sqastatus: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Warehouse Edition (V3.0) cluster.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the IDs of all AnalyticDB for MySQL Data Warehouse Edition (V3.0) clusters within a region.
        self.dbcluster_id = dbcluster_id
        # The name of the resource group.
        self.group_name = group_name
        # The request ID.
        self.request_id = request_id
        # Indicates whether short query acceleration (SQA) is enabled.
        self.sqastatus = sqastatus

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sqastatus is not None:
            result['SQAStatus'] = self.sqastatus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SQAStatus') is not None:
            self.sqastatus = m.get('SQAStatus')

        return self

