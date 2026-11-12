# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableDBClusterDynamoDBRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
    ):
        # The cluster ID.
        # > You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query all clusters in the target region, including cluster IDs. Usage notes: Status prerequisite: The DBClusterStatus of the cluster must be Running. After you call EnableDBClusterDynamoDB, the cluster enters the ConfigSwitching transitional state. You must poll DescribeDBClusterAttribute and wait for the cluster to recover. Usage notes: You must first call EnableDBClusterDynamoDB to enable the DynamoDB compatibility mode. Only PostgreSQL clusters are supported.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        return self

