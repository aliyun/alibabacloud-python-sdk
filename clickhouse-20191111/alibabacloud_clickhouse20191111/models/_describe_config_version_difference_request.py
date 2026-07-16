# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeConfigVersionDifferenceRequest(DaraModel):
    def __init__(
        self,
        change_id: str = None,
        dbcluster_id: str = None,
    ):
        # The ID of the change record. Call the [DescribeConfigHistory](https://help.aliyun.com/document_detail/452209.html) operation to query the IDs of change records.
        # 
        # This parameter is required.
        self.change_id = change_id
        # The cluster ID. Call the [DescribeDBClusters](https://help.aliyun.com/document_detail/170879.html) operation to query the IDs of all clusters in the destination region.
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
        if self.change_id is not None:
            result['ChangeId'] = self.change_id

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeId') is not None:
            self.change_id = m.get('ChangeId')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        return self

